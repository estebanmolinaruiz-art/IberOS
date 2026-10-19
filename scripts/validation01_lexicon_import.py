#!/usr/bin/env python3
"""Import an existing Iberian sign/word table into a non-promoting evidence staging file.

Input CSV columns: record_id,object_id,source_url,reading,reading_type,physical_id,
                   dependency_group,signary,uncertainty
No content is interpreted or promoted to scientific truth.
"""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

REQUIRED = {"record_id", "object_id", "source_url", "reading", "reading_type"}
ALLOWED = {"observed", "editorial", "hypothesis"}

def audit(rows):
    accepted, rejected = [], []
    seen = set()
    for line, row in enumerate(rows, 2):
        problems = []
        for key in REQUIRED:
            if not (row.get(key) or "").strip():
                problems.append("missing_" + key)
        kind = (row.get("reading_type") or "").strip().lower()
        if kind not in ALLOWED:
            problems.append("invalid_reading_type")
        rid = (row.get("record_id") or "").strip()
        if rid in seen:
            problems.append("duplicate_record_id")
        seen.add(rid)
        if not (row.get("physical_id") or "").strip() and not (row.get("dependency_group") or "").strip():
            problems.append("unresolved_independence")
        if problems:
            rejected.append({"line": line, "record_id": rid, "reasons": sorted(problems)})
            continue
        accepted.append({
            "record_id": rid,
            "object_id": row["object_id"].strip(),
            "source_url": row["source_url"].strip(),
            "reading": row["reading"].strip(),
            "reading_type": kind,
            "physical_id": (row.get("physical_id") or "").strip(),
            "dependency_group": (row.get("dependency_group") or "").strip(),
            "signary": (row.get("signary") or "").strip(),
            "uncertainty": (row.get("uncertainty") or "").strip(),
            "scientific_state": "UNVERIFIED",
            "validation01_holdout_eligible": False
        })
    return accepted, rejected

def main():
    p = argparse.ArgumentParser()
    p.add_argument("source_csv")
    p.add_argument("--output", required=True)
    args = p.parse_args()
    with Path(args.source_csv).open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not REQUIRED.issubset(reader.fieldnames or []):
            p.error("Missing mandatory headers: " + ", ".join(sorted(REQUIRED - set(reader.fieldnames or []))))
        accepted, rejected = audit(reader)
    target = Path(args.output)
    if target.resolve() == Path(args.source_csv).resolve():
        p.error("Output cannot overwrite source")
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as out:
        for item in accepted:
            out.write(json.dumps(item, ensure_ascii=False) + "\n")
    print(json.dumps({
        "accepted": len(accepted),
        "rejected": len(rejected),
        "rejection_details": rejected,
        "holdout_promotions": 0,
        "evidence_type_counts": dict(Counter(r["reading_type"] for r in accepted))
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
