"""METROLOGY-SENSITIVITY-05: tolerance/reference-unit robustness for 37 published weights."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from .metrology_assemblages_04 import audit

TOLERANCES_PERCENT = (1, 2, 3, 5, 7.5, 10, 15, 20)
UNIT_GRID_G = (2., 2.05, 2.1, 2.15, 2.2)


def sensitivity() -> dict:
    reference = audit(unit_g=2.1, tolerance_percent=5)
    n = reference["published_mass_count"]
    by_tolerance = []
    for tolerance in TOLERANCES_PERCENT:
        r = audit(unit_g=2.1, tolerance_percent=tolerance)
        by_tolerance.append({
            "tolerance_percent": tolerance,
            "within": r["count_within_tolerance"],
            "outside": n - r["count_within_tolerance"],
            "groups": {g["group"]: {"within": g["within_tolerance"],
                                      "total": g["n_objects"]} for g in r["groups"]},
        })
    by_unit = []
    for unit in UNIT_GRID_G:
        r = audit(unit_g=unit, tolerance_percent=5)
        by_unit.append({"unit_g": unit, "within": r["count_within_tolerance"],
                        "outside": n - r["count_within_tolerance"]})
    return {
        "experiment": "METROLOGY_SENSITIVITY_05",
        "source_experiment": "METROLOGY_ASSEMBLAGES_04",
        "assemblages": reference["assemblage_count"], "objects": n,
        "fixed_series_ratios": list(reference["published_series_ratios"]),
        "tolerance_sensitivity_at_2_1g": by_tolerance,
        "unit_sensitivity_at_5percent": by_unit,
        "reference_within_5percent": reference["count_within_tolerance"],
        "best_grid_unit_is_not_estimated_unit": True,
        "post_hoc_grid_not_independent_validation": True,
        "marks_and_denominations_available": False,
        "new_physical_measurements": 0,
        "full3406_accessed": False,
        "translation_or_numeric_gold_confirmed": False,
        "official_metrics_modified": False,
        "main_conclusion": "Counts depend on tolerance and assumed unit; numerical proximity is not epigraphic evidence.",
    }


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--json", type=Path)
    args = p.parse_args(argv)
    content = json.dumps(sensitivity(), ensure_ascii=False, indent=2) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(content, encoding="utf-8")
    else:
        print(content, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
