"""MORPH-STRATA-01: read-only retrospective graphemic motif frequencies.

No training, decoding, grammatical gold, prospective validation or semantics.
Distinct orthographic R/R1 variants are retained in all outputs.
"""
from __future__ import annotations
from collections import defaultdict
from hashlib import sha256
import argparse
import json
from pathlib import Path
import re

EXPECTED_SHA256 = "3cf66a5e9abbec2a8a356be3432d507da0d967d3310ffdeb3dc22878055d13a4"
SPLITS = ("TRAIN", "VAL", "HOLD")
MOTIFS = {
    "BA_I_TE_S": (("BA", "I", "TE", "S"),),
    "BA_TI_R": (("BA", "TI", "R"),),
    "BA_TI_R1": (("BA", "TI", "R1"),),
    "KU_TU_R": (("KU", "TU", "R"),),
    "KU_TU_R1": (("KU", "TU", "R1"),),
    "BI_N": (("BI", "N"),),
    "BI_ISOLATED": (("BI",),),
}
COMBINED = {
    "BATIR_ORTHOGRAPHIC_VARIANTS": ("BA_TI_R", "BA_TI_R1"),
    "KUTUR_ORTHOGRAPHIC_VARIANTS": ("KU_TU_R", "KU_TU_R1"),
}
BOUNDARIES = re.compile(r"[¦:;∏│]")


def token_segments(signature: str) -> list[list[str]]:
    """Do not join matches across editorial or explicit word boundaries."""
    return [[token for token in segment.split("-") if token]
            for segment in BOUNDARIES.split(signature.upper()) if segment.strip()]


def count_occurrences(tokens: list[str], motif: tuple[str, ...], *, isolated: bool = False) -> int:
    if isolated:
        return int(tokens == list(motif))
    n = len(motif)
    return sum(tuple(tokens[i:i + n]) == motif for i in range(len(tokens) - n + 1))


def audit_records(records: list[dict]) -> dict:
    observations: dict[str, dict[str, dict]] = defaultdict(dict)
    errors = []
    for i, record in enumerate(records):
        split = record.get("split_v3_4_9")
        if split == "EXCLUDED":
            continue
        if split not in SPLITS:
            errors.append(f"UNKNOWN_SPLIT:{i}")
            continue
        dep, uid = record.get("dependency_key_v3_4_9"), record.get("uid")
        if not isinstance(dep, str) or not dep or not isinstance(uid, str) or not uid:
            errors.append(f"MISSING_IDENTITY:{i}")
            continue
        signature = record.get("signature")
        if not isinstance(signature, str):
            errors.append(f"INVALID_SIGNATURE:{i}")
            continue
        segments = token_segments(signature)
        for motif_name, variants in MOTIFS.items():
            isolated = motif_name == "BI_ISOLATED"
            n = sum(count_occurrences(seg, variant, isolated=isolated)
                    for seg in segments for variant in variants)
            if n:
                if uid in observations[motif_name]:
                    errors.append(f"DUPLICATE_UID:{uid}")
                observations[motif_name][uid] = {"split": split, "dep": dep, "occ": n}
    if errors:
        return {"valid": False, "errors": errors[:30], "results": {}}
    for combined, sources in COMBINED.items():
        for source in sources:
            for uid, item in observations[source].items():
                if uid in observations[combined]:
                    observations[combined][uid]["occ"] += item["occ"]
                else:
                    observations[combined][uid] = dict(item)
    output = {}
    for name in [*MOTIFS, *COMBINED]:
        obs = observations[name]
        by_split = {}
        for split in SPLITS:
            selected = [item for item in obs.values() if item["split"] == split]
            by_split[split] = {
                "occurrences": sum(item["occ"] for item in selected),
                "uid_records": len(selected),
                "dependency_units": len({item["dep"] for item in selected}),
            }
        output[name] = {
            "total_occurrences": sum(item["occ"] for item in obs.values()),
            "total_uid_records": len(obs),
            "total_dependency_units": len({item["dep"] for item in obs.values()}),
            "splits": by_split,
        }
    return {
        "experiment": "MORPH_STRATA_01", "valid": True,
        "input_records": len(records), "results": output,
        "training_or_prediction_executed": False, "semantic_gold_available": 0,
        "grammatical_accuracy": None, "independence_certified": False,
        "retrospective_exploratory": True, "frozen_splits_modified": False,
        "original_records_modified": False,
        "disclaimer": ("Graphemic substring counts only, not segmentation or meaning. "
                       "BA-I-TE-S is not automatically BAIDES; BI-N is not necessarily numeral two. "
                       "R/R1 are preserved. Patterns cannot cross editorial boundaries."),
    }


def audit_file(path: Path) -> dict:
    raw = path.read_bytes()
    if sha256(raw).hexdigest() != EXPECTED_SHA256:
        raise ValueError("FULL3406_SHA256_MISMATCH")
    document = json.loads(raw)
    if not isinstance(document, dict) or not isinstance(document.get("records"), list):
        raise ValueError("FULL3406_RECORDS_MISSING")
    return audit_records(document["records"])


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Retrospective FULL3406 graphemic motif diagnostics")
    parser.add_argument("full3406", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args(argv)
    result = audit_file(args.full3406)
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.json:
        if args.json.resolve() == args.full3406.resolve():
            parser.error("Refusing to overwrite frozen corpus")
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0 if result["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
