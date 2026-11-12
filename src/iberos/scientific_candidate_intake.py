"""SCI-PRED-04: curate *leads* into blinded candidate packets, never semantic gold.

This intake is deliberately prior to prediction and independent adjudication.
No new physical artefact or role can be certified from metadata alone.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

SCHEMA = "SCI-PRED-04/1"
ALLOWED_CONTEXTS = {"BUILDING", "MANUFACTURE"}
ALLOWED_EXPOSURE = {"KNOWN_TRAIN", "KNOWN_VALIDATION", "KNOWN_HOLD", "UNKNOWN", "NEW_DECLARED"}
FORBIDDEN_KEYS = {
    "gold", "gold_label", "gold_roles", "role", "roles", "true_role",
    "producer", "commissioner", "maker", "owner", "slave", "latin",
    "latin_translation", "translation", "possible_translation",
    "semantic_gold", "outcome", "correct", "prediction_outcome",
}
FIELDS = {"candidate_id", "physical_id", "documentary_lineage_id", "aliases",
          "reading_source_url", "image_reference_url", "image_sha256",
          "script", "context_type", "prior_exposure", "physical_audit_reference",
          "physical_auditor", "sign_reviews"}
REVIEW_FIELDS = {"reviewer_id", "independence_group", "source_image_sha256",
                 "method", "blind_to_editorial", "participants"}
PERSON_FIELDS = {"person_id", "name_form", "name_status"}


def _has_gold(data) -> bool:
    if isinstance(data, dict):
        return any(k.lower() in FORBIDDEN_KEYS or _has_gold(v)
                   for k, v in data.items())
    if isinstance(data, list):
        return any(_has_gold(x) for x in data)
    return False


def _present(x) -> bool:
    return isinstance(x, str) and bool(x.strip())


def _https(value) -> bool:
    if not _present(value):
        return False
    p = urlsplit(value)
    return (p.scheme == "https" and bool(p.netloc)
            and not p.username and not p.password)


def _hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False,
                     separators=(",", ":")).encode("utf-8")).hexdigest()


def _names(review: dict) -> list[dict] | None:
    people = review.get("participants")
    if not isinstance(people, list) or len(people) != 2:
        return None
    ids = set()
    for p in people:
        if not isinstance(p, dict) or set(p) != PERSON_FIELDS:
            return None
        if not all(_present(p[k]) for k in PERSON_FIELDS):
            return None
        if p["name_status"] != "INDEPENDENTLY_IDENTIFIED":
            return None
        if p["person_id"] in ids:
            return None
        ids.add(p["person_id"])
    return sorted(people, key=lambda p: p["person_id"])


def audit(document: dict) -> dict:
    if not isinstance(document, dict) or set(document) != {"schema", "candidates"}:
        raise ValueError("Expected exactly schema and candidates")
    if document["schema"] != SCHEMA:
        raise ValueError("Unknown candidate queue schema")
    records = document["candidates"]
    if not isinstance(records, list) or len(records) > 1000:
        raise ValueError("Expected at most 1000 candidate lead records")
    seen_id, seen_physical, seen_lineage, seen_aliases = set(), set(), set(), set()
    results = []
    for index, candidate in enumerate(records, 1):
        if not isinstance(candidate, dict) or set(candidate) - FIELDS:
            raise ValueError("Unexpected candidate fields")
        if _has_gold(candidate):
            raise ValueError("Gold-bearing information forbidden in blind intake")
        cid = candidate.get("candidate_id")
        if not _present(cid) or cid in seen_id:
            raise ValueError("Missing or duplicate candidate_id")
        seen_id.add(cid)
        issues = []
        physical = candidate.get("physical_id")
        lineage = candidate.get("documentary_lineage_id")
        if not _present(physical) or not _present(lineage):
            issues.append("PHYSICAL_AND_LINEAGE_IDENTITY_REQUIRED")
        else:
            if physical in seen_physical:
                issues.append("REPEATED_PHYSICAL_OBJECT")
            if lineage in seen_lineage:
                issues.append("REPEATED_PUNCH_OR_EDITORIAL_LINEAGE")
            seen_physical.add(physical)
            seen_lineage.add(lineage)
        exposure = candidate.get("prior_exposure")
        if exposure not in ALLOWED_EXPOSURE:
            issues.append("PRIOR_EXPOSURE_NOT_REVIEWED")
        elif exposure != "NEW_DECLARED":
            issues.append("RETROSPECTIVE_OR_EXPOSURE_UNRESOLVED")
        aliases = candidate.get("aliases")
        if (not isinstance(aliases, list) or not aliases
                or any(not _present(v) for v in aliases)
                or len(set(aliases)) != len(aliases)):
            issues.append("DOCUMENTARY_ALIASES_NOT_RECONCILED")
        else:
            for alias in aliases:
                normalized_alias = alias.strip().casefold()
                if normalized_alias in seen_aliases:
                    issues.append("REUSED_EDITORIAL_ALIAS")
                seen_aliases.add(normalized_alias)
        if candidate.get("script") != "IBERIAN":
            issues.append("SCRIPT_NOT_ADMITTED")
        if candidate.get("context_type") not in ALLOWED_CONTEXTS:
            issues.append("NO_PREDECLARED_ROLE_CONTEXT")
        for field in ("reading_source_url", "image_reference_url",
                      "physical_audit_reference"):
            if not _https(candidate.get(field)):
                issues.append("MISSING_VERIFIABLE_" + field.upper())
        if not _present(candidate.get("physical_auditor")):
            issues.append("PHYSICAL_IDENTITY_AUDITOR_REQUIRED")
        sha = candidate.get("image_sha256")
        if (not _present(sha) or len(sha) != 64
                or any(c not in "0123456789abcdefABCDEF" for c in sha)):
            issues.append("SOURCE_IMAGE_HASH_REQUIRED")
        reviews = candidate.get("sign_reviews")
        people = None
        if not isinstance(reviews, list) or len(reviews) != 2:
            issues.append("TWO_BLIND_SIGN_READINGS_REQUIRED")
        else:
            reviewer_ids, groups, reviewed = set(), set(), []
            for review in reviews:
                if not isinstance(review, dict) or set(review) != REVIEW_FIELDS:
                    issues.append("INVALID_SIGN_REVIEW_FORMAT")
                    continue
                rid, group = review.get("reviewer_id"), review.get("independence_group")
                names = _names(review)
                if not _present(rid) or not _present(group) or not names:
                    issues.append("IDENTIFIED_READERS_AND_TWO_PERSON_SPANS_REQUIRED")
                elif (review["method"] != "DIRECT_IMAGE"
                      or review["blind_to_editorial"] is not True
                      or review["source_image_sha256"] != sha):
                    issues.append("READINGS_NOT_BLIND_ON_IDENTICAL_IMAGE")
                else:
                    reviewed.append(names)
                    if rid in reviewer_ids or group in groups:
                        issues.append("REVIEWERS_NOT_INDEPENDENT")
                    reviewer_ids.add(rid)
                    groups.add(group)
            if len(reviewed) == 2:
                if reviewed[0] != reviewed[1]:
                    issues.append("SIGN_READINGS_OR_PERSON_SPANS_DISAGREE")
                elif len(reviewer_ids) == 2 and len(groups) == 2:
                    people = reviewed[0]
        if people is None:
            issues.append("NO_CONCORDANT_DOUBLE_READING")
        issues = list(dict.fromkeys(issues))
        if "RETROSPECTIVE_OR_EXPOSURE_UNRESOLVED" in issues:
            state = "EXCLUDED_FROM_PROSPECTIVE_HOLD"
        elif any(i.startswith("REPEATED_") or i == "REUSED_EDITORIAL_ALIAS" for i in issues):
            state = "DUPLICATE_DEPENDENCY_BLOCK"
        elif issues:
            state = "BLOCKED_EVIDENCE"
        else:
            state = "READY_FOR_EXTERNAL_ADMISSION_AUDIT"
        # A reviewer must verify the identity, blindness and novelty claims
        # OUTSIDE this module. A preview is not yet eligible for sealing.
        preview = None
        if not issues:
            preview = {
                "blind_id": cid, "physical_id": physical,
                "reading_source_url": candidate["reading_source_url"],
                "context_type": candidate["context_type"], "reading_level": "D3",
                "participants": people, "script": "IBERIAN",
                "independence_status": "REQUIRES_EXTERNAL_AUDIT",
            }
        results.append({
            "candidate_id": cid, "physical_id": physical,
            "documentary_lineage_id": lineage,
            "state": state, "issues": issues,
            "blind_packet_preview": preview,
            "automatic_sealing_permitted": False,
            "independent_admission_verified": False,
        })
    counts = dict(sorted(Counter(r["state"] for r in results).items()))
    return {
        "schema": "IberOS-SCI-PRED-04-Intake-Audit/1.0",
        "input_sha256": _hash(document),
        "total_leads": len(results), "counts": counts,
        "ready_for_external_admission_audit": counts.get("READY_FOR_EXTERNAL_ADMISSION_AUDIT", 0),
        "results": results,
        "gold_labels_consumed": False,
        "semantic_predictions_scored": 0,
        "translation_validated": False,
        "automatic_core_promotion": False,
        "notice": "Intake metadata are self-attested; only external human audit can admit a new physical HOLD. Never unblind gold before committing prediction.",
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--output", type=Path)
    a = p.parse_args(argv)
    doc = json.loads(a.input.read_text(encoding="utf-8"))
    report = audit(doc)
    payload = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if a.output:
        if a.output.resolve() == a.input.resolve():
            raise ValueError("Cannot overwrite original candidate queue")
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
