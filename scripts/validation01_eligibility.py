#!/usr/bin/env python3
"""VALIDATION-01 preregistered eligibility audit. Never claims linguistic success."""
import argparse
import json
from collections import Counter
from pathlib import Path

TEXT_FIELDS = ("verified_transcription", "validated_transcription", "sign_sequence")
INDEPENDENCE_FIELDS = ("physical_id", "phys_id", "leak_group")
PROSPECTIVE_FIELDS = ("prospective_locked", "lock_date", "prediction_created_at")


def audit(records):
    counts = Counter()
    issues = []
    eligible = []
    for i, obj in enumerate(records, 1):
        counts["objects"] += 1
        oid = obj.get("object_id") or f"line-{i}"
        inclusion = obj.get("iberos_inclusion")
        counts[f"inclusion:{inclusion or 'MISSING'}"] += 1
        if inclusion != "INCLUDE":
            continue
        counts["included"] += 1
        missing = []
        if not any(str(obj.get(key, "")).strip() for key in TEXT_FIELDS):
            missing.append("verified_sign_transcription")
        if not (str(obj.get("source", "")).strip()):
            missing.append("traceable_source")
        if not any(str(obj.get(key, "")).strip() for key in INDEPENDENCE_FIELDS):
            missing.append("resolved_physical_or_leak_identity")
        if not all(str(obj.get(key, "")).strip() for key in PROSPECTIVE_FIELDS):
            missing.append("prospective_precommit_and_lock")
        # An observed gold label for a predefined task is essential to score predictions.
        if not str(obj.get("gold_task_label", "")).strip():
            missing.append("independent_gold_task_label")
        if missing:
            issues.append({"object_id": oid, "missing": missing})
        else:
            eligible.append(oid)
    return {
        "protocol": "IberOS-VALIDATION-01",
        "phase": "eligibility_only",
        "counts": dict(sorted(counts.items())),
        "prospective_scoring_eligible": len(eligible),
        "eligible_object_ids": eligible,
        "blocked_records": issues,
        "linguistic_superiority": "NOT_EVALUATED",
        "semantic_discovery": "NOT_DEMONSTRATED",
        "gate": "READY_FOR_SCORING" if eligible else "BLOCKED_NO_ELIGIBLE_PROSPECTIVE_HOLDOUT",
        "caution": "No linguistic prediction has been scored; absence of data is not a failed linguistic hypothesis."
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/curated/iberos_curated_objects_v1.jsonl")
    parser.add_argument("--output", default="-")
    args = parser.parse_args()
    records = [json.loads(line) for line in Path(args.input).read_text(encoding="utf-8").splitlines() if line.strip()]
    result = audit(records)
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output == "-":
        print(serialized, end="")
    else:
        Path(args.output).write_text(serialized, encoding="utf-8")


if __name__ == "__main__":
    main()
