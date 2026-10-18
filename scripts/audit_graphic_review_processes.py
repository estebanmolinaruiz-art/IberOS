#!/usr/bin/env python3
"""Ten independent, reproducible documentary controls for graphic evidence."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "data/review"

def audit():
    files = [REVIEW / "casinos_graphic_uncertainties_v1.json",
             REVIEW / "sagunto_caminreal_graphic_uncertainties_v1.json"]
    datasets = [json.loads(path.read_text(encoding="utf-8")) for path in files]
    rows = [r for d in datasets for r in d["records"]]
    checks = {
        "P01_datasets_declared_counts": all(len(d["records"]) == d["record_count"] for d in datasets),
        "P02_unique_evidence_ids": len({r["evidence_id"] for r in rows}) == len(rows),
        "P03_stable_object_and_region_ids": all(r.get("object_id") and r.get("region") and r.get("location") for r in rows),
        "P04_alternatives_are_explicit": all(r.get("editorial_alternatives") for r in rows),
        "P05_inspection_status_explicit": all(r.get("visual_inspection") for r in rows),
        "P06_damage_or_limit_explicit": all(r.get("damage") for r in rows),
        "P07_independent_review_not_claimed": all(r["independent_reviewer"] is None and not r["sign_by_sign_verified"] for r in rows),
        "P08_image_reuse_not_assumed": all(r.get("public_image_reuse_authorized") is False for r in rows if r["object_id"] != "IBR-PLM-0007"),
        "P09_no_semantic_promotion": all(not r["core_execution_allowed"] and not r["meaning_validated"] for r in rows) and all(not d["automatic_core_promotion"] and not d["translation_validated"] for d in datasets),
        "P10_corpus_coverage": len(rows) == 9 and {r["object_id"] for r in rows} == {"IBR-PLM-0007", "IBR-LAP-0005", "IBR-MUS-0001"},
    }
    return {"schema": "IberOS-Graphic-Checks/1.0", "checked_records": len(rows),
            "checked_objects": 3, "checks": checks, "passed": sum(checks.values()),
            "total": len(checks), "scientific_translations_validated": 0}

if __name__ == "__main__":
    result = audit()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["passed"] != result["total"]:
        raise SystemExit(1)
