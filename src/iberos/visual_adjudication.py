"""Scientific visual-collation intake for IberOS Core (PALEO / VALIDATION / CORPUS).

A queue entry is a question about a sign, not an inspected sign. Two blind
readers are a prerequisite for human adjudication, never automatic proof of a
glyph, morphological value, translation or ancient role.
"""
from __future__ import annotations

from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path
from math import isfinite
import json
import re
import unicodedata

from .shared_evidence import validate_evidence

SCHEMA = "IberOS-Core-Visual-Collation/1.0"
SOURCES = {
    "PAL": "data/review/palaeographic_alignment_priority_v1.json",
    "SERRETA": "site/data/serreta-variants-v1.json",
    "VILLARES": "site/data/villares-v-discrepancies-v1.json",
}
SOURCE_SCHEMAS = {
    "PAL": "IberOS-Palaeographic-Alignment/1.0",
    "SERRETA": "IberOS-Serreta-Editorial-Variants/1.0",
    "VILLARES": "IberOS-VillaresV-DiscrepancyMatrix/1.0",
}
HASH_PATTERN = re.compile(r"^[a-fA-F0-9]{64}$")


def editorial_delta(left: str, right: str) -> dict:
    """Compare Unicode editorial characters, emphatically NOT photographed signs."""
    if not isinstance(left, str) or not isinstance(right, str):
        raise ValueError("Two editorial strings are required")
    a = unicodedata.normalize("NFC", left)
    b = unicodedata.normalize("NFC", right)
    diff = SequenceMatcher(None, a, b, autojunk=False)
    edits = [
        {"op": tag, "a_start": i, "a_end": j, "b_start": k, "b_end": m,
         "before": a[i:j], "after": b[k:m]}
        for tag, i, j, k, m in diff.get_opcodes() if tag != "equal"
    ]
    return {"kind": "EDITORIAL_UNICODE_CODEPOINT_DIFFERENCE",
            "not_photographic_sign_count": True,
            "edits": edits, "edit_blocks": len(edits),
            "source_text_identical": not edits}


def _read(root: Path, label: str) -> dict:
    payload = json.loads((root / SOURCES[label]).read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or payload.get("schema") != SOURCE_SCHEMAS[label]:
        raise ValueError(f"Unexpected or missing source schema: {label}")
    return payload


def build_queue(root: Path) -> list[dict]:
    """Unify existing review targets without creating duplicate physical objects."""
    root = Path(root)
    pal, ser, vil = (_read(root, label) for label in ("PAL", "SERRETA", "VILLARES"))
    if pal.get("rows") is None or ser.get("variants") is None or vil.get("rows") is None:
        raise ValueError("Missing review arrays")
    if ser.get("object_id") != "IBR-PLM-0009" or vil.get("object_id") != "IBR-PLM-0005":
        raise ValueError("Physical object mismatch between review sources")
    out = []
    for entry in pal["rows"]:
        if not isinstance(entry, dict) or not entry.get("review_id") or not entry.get("object_id"):
            raise ValueError("Invalid PALAEO review row")
        out.append({
            "review_id": entry["review_id"], "object_id": entry["object_id"],
            "source_family": "PAL", "face_line": None,
            "target": entry.get("editorial_segment", ""),
            "candidate_editorial_strings": [entry.get("editorial_segment", "")],
            "source_reference": entry.get("source_url") or entry.get("attribution", ""),
            "figure_locator": entry.get("source_location"),
            "image_bbox": entry.get("source_facsimile_coordinates"),
            "visual_verified": False, "priority": "EXISTING",
        })
    for i, entry in enumerate(ser["variants"], 1):
        if not isinstance(entry, dict) or not isinstance(entry.get("historical"), list) or len(entry["historical"]) != 2:
            raise ValueError("Serreta variants require two editorial alternatives")
        face_line = entry.get("line")
        out.append({
            "review_id": f"SER-VAR-{i:02d}", "object_id": ser["object_id"],
            "source_family": "SERRETA", "face_line": face_line,
            "target": entry.get("modern", ""),
            "candidate_editorial_strings": list(entry["historical"]),
            "source_reference": "https://www.alcoi.org/es/areas/cultura/museo/publicaciones/recerques/recerques_0001.html",
            "figure_locator": "Fletcher y Silgo 1992, p. 10 fotografías A/B; localización exacta del signo pendiente",
            "image_bbox": None, "visual_verified": False, "priority": "HIGH" if face_line == "B1" else "NORMAL",
        })
    for entry in vil["rows"]:
        if not isinstance(entry, dict) or not entry.get("id"):
            raise ValueError("Invalid Villares review row")
        if entry.get("glyph_photo_verified") is not False:
            raise ValueError("Villares source claims photographic review without signed evidence")
        out.append({
            "review_id": entry["id"], "object_id": vil["object_id"],
            "source_family": "VILLARES", "face_line": f"{entry['face']}{entry['line']}",
            "target": entry.get("category", ""),
            "candidate_editorial_strings": [entry["museum_excerpt"], entry["edition_2024_excerpt"]],
            "source_reference": vil["edition_source"],
            "figure_locator": "Ferrer i Jané 2024, fotografías fig. 1 p. 312 / dibujos fig. 2 p. 313",
            "image_bbox": None, "visual_verified": False,
            "priority": "HIGH" if entry.get("review_priority") == "ALTA" else "NORMAL",
        })
    ids = [entry["review_id"] for entry in out]
    if len(ids) != len(set(ids)):
        raise ValueError("Review target IDs must be globally unique")
    if any(not entry["source_reference"] or not entry["object_id"] for entry in out):
        raise ValueError("Every target must cite a source and physical object")
    return out


def assess_blind_collation(submission: dict) -> dict:
    """Gate TWO independently obtained image readings; never issue scientific approval.

    All required checks must pass to reach READY_FOR_HUMAN_ADJUDICATION.
    An adjudicator must separately decide on the source and sign outside Core.
    """
    if not isinstance(submission, dict):
        raise ValueError("Collation submission must be a dictionary")
    if submission.get("scientifically_validated") is True or submission.get("automatic_core_promotion") is True:
        raise ValueError("A submission cannot promote itself to verified evidence")
    problems = []
    for field in ("review_id", "object_id", "source_page", "figure_locator", "source_image_url"):
        if not isinstance(submission.get(field), str) or not submission[field].strip():
            problems.append("MISSING_" + field.upper())
    sha = submission.get("source_image_sha256")
    if not isinstance(sha, str) or not HASH_PATTERN.fullmatch(sha):
        problems.append("IMAGE_HASH_REQUIRED")
    bbox = submission.get("bbox_xyxy")
    if (not isinstance(bbox, list) or len(bbox) != 4
            or any(type(v) not in (int, float) or not isfinite(v) for v in bbox)
            or (all(type(v) in (int, float) and isfinite(v) for v in bbox)
                and (not all(0 <= v <= 1 for v in bbox)
                     or bbox[0] >= bbox[2] or bbox[1] >= bbox[3]))):
        problems.append("VERIFIED_NORMALIZED_BBOX_REQUIRED")
    if submission.get("object_match_reviewed") is not True:
        problems.append("OBJECT_MATCH_NOT_REVIEWED")
    readers = submission.get("readers", [])
    if not isinstance(readers, list):
        problems.append("INVALID_READER_LIST")
        readers = []
    if len(readers) < 2:
        problems.append("TWO_BLIND_READERS_REQUIRED")
    valid_readers = []
    for reading in readers:
        if not isinstance(reading, dict):
            problems.append("INVALID_READER_RECORD")
            continue
        if not all(isinstance(reading.get(k), str) and reading[k].strip()
                   for k in ("reviewer_id", "independence_group", "reading")):
            problems.append("REVIEWER_IDENTITY_OR_READING_MISSING")
            continue
        if reading.get("method") != "DIRECT_IMAGE" or reading.get("blind_to_editorial") is not True:
            problems.append("NONBLIND_OR_DERIVED_EDITORIAL_READING")
            continue
        if not isinstance(sha, str) or reading.get("source_image_sha256") != sha:
            problems.append("READER_IMAGE_MISMATCH")
            continue
        valid_readers.append(reading)
    if len(valid_readers) >= 2:
        reviewer_ids = [x["reviewer_id"] for x in valid_readers]
        groups = [x["independence_group"] for x in valid_readers]
        if len(set(reviewer_ids)) < len(reviewer_ids) or len(set(groups)) < len(groups):
            problems.append("NONINDEPENDENT_REVIEWERS")
        if len({unicodedata.normalize("NFC", x["reading"]) for x in valid_readers}) > 1:
            problems.append("READINGS_DISAGREE")
    elif len(readers) >= 2:
        problems.append("TWO_ELIGIBLE_READERS_REQUIRED")
    problems = list(dict.fromkeys(problems))
    return {
        "review_id": submission.get("review_id"),
        "status": "BLOCKED" if problems else "READY_FOR_HUMAN_ADJUDICATION",
        "blockers": problems,
        "independent_readings_received": len(valid_readers),
        "scientifically_validated": False,
        "automatic_core_promotion": False,
        "semantic_translation_confirmed": False,
    }


def audit_repository(root: Path) -> dict:
    cases = build_queue(root)
    source_counts = dict(sorted(Counter(x["source_family"] for x in cases).items()))
    objects = sorted({x["object_id"] for x in cases})
    editorial_deltas = {}
    for case in cases:
        a = case["candidate_editorial_strings"]
        if len(a) == 2:
            editorial_deltas[case["review_id"]] = editorial_delta(a[0], a[1])
    evidence = validate_evidence([
        {"evidence_id": "VISUAL-" + x["review_id"], "object_id": x["object_id"],
         "source_reference": x["source_reference"], "layer": "GRAPHIC",
         "state": "UNVERIFIED", "pillars": ["PALEO", "VALIDATION"],
         "sign_label": x["target"]}
        for x in cases
    ])
    return {
        "schema": SCHEMA, "review_units": len(cases), "physical_objects": len(objects),
        "object_ids": objects, "by_source": source_counts,
        "editorial_pairs_compared": len(editorial_deltas),
        "editorial_pairs_different": sum(not x["source_text_identical"] for x in editorial_deltas.values()),
        "independently_verified_glyphs": 0,
        "independent_blind_readings": 0,
        "ready_for_human_adjudication": 0,
        "scientific_verdict": "NOT_EVALUATED",
        "automatic_core_promotion": False,
        "evidence_contract": {"count": evidence["count"], "layers": ["GRAPHIC"],
                              "state": "UNVERIFIED"},
        "priorities": [{"review_id": x["review_id"], "object_id": x["object_id"],
                        "face_line": x["face_line"], "source_family": x["source_family"],
                        "editorial_strings": x["candidate_editorial_strings"],
                        "editorial_delta": editorial_deltas.get(x["review_id"]),
                        "figure_locator": x["figure_locator"],
                        "status": "IMAGE_AND_BLIND_REVIEW_PENDING"}
                       for x in cases if x["priority"] == "HIGH"],
        "note": ("Review units are editorial comparison targets, not distinct inscriptions "
                 "or individually verified signs. Text differences cannot prove glyph "
                 "identity, ancient semantics or translation. Reader consensus only "
                 "permits external human adjudication."),
    }
