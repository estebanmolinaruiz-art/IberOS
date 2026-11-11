"""METROLOGY-ADMISSION-07: fail-closed primary evidence and prospective eligibility.

No FULL3406 access, no fresh physical measurements. Data qualification is
separate from eligibility for a *new, blind* Iberian linguistic evaluation.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

REQUIRED_TEXT = ("object_id", "institution", "inventory_id", "physical_object_identity",
                 "context_reference", "image_reference", "image_rights", "reading_reference")
REQUIRED_METROLOGY = ("mass_g", "resolution_g", "uncertainty_g",
                      "instrument_id", "calibration_reference",
                      "measurement_date", "conservation_assessment")
REQUIRED_READING = ("reading", "reader_id", "reading_date", "blind_to_weight_and_model")
REQUIRED_PROSPECTIVE = ("historical_aliases_checked", "independent_object_from_full3406",
                        "predictions_registered_before_reading", "not_previously_published_or_seen",
                        "negative_controls_registered")


def _missing_text(record: dict, field: str) -> bool:
    return not isinstance(record.get(field), str) or not record[field].strip()


def _positive_finite(value: Any) -> bool:
    return isinstance(value, (float, int)) and not isinstance(value, bool) and math.isfinite(value) and value > 0


def assess(record: dict) -> dict:
    """Declare *why* an object cannot be used, rather than assign a made-up value."""
    issues = []
    for field in REQUIRED_TEXT:
        if _missing_text(record, field):
            issues.append("MISSING_" + field.upper())
    for field in ("mass_g", "resolution_g", "uncertainty_g"):
        if not _positive_finite(record.get(field)):
            issues.append("INVALID_OR_MISSING_" + field.upper())
    if _positive_finite(record.get("mass_g")) and _positive_finite(record.get("uncertainty_g")):
        if record["uncertainty_g"] >= record["mass_g"]:
            issues.append("UNCERTAINTY_NOT_SMALLER_THAN_MASS")
    for field in REQUIRED_METROLOGY:
        if field not in ("mass_g", "resolution_g", "uncertainty_g") and _missing_text(record, field):
            issues.append("MISSING_" + field.upper())
    readers = record.get("independent_mark_readings")
    if not isinstance(readers, list) or len(readers) < 2:
        issues.append("TWO_INDEPENDENT_READINGS_REQUIRED")
    else:
        distinct = set()
        for i, reading in enumerate(readers):
            if not isinstance(reading, dict):
                issues.append(f"BAD_READING_{i}")
                continue
            for field in REQUIRED_READING:
                if field == "blind_to_weight_and_model":
                    if reading.get(field) is not True:
                        issues.append(f"NOT_BLIND_READING_{i}")
                elif _missing_text(reading, field):
                    issues.append(f"MISSING_READING_{i}_{field.upper()}")
            if isinstance(reading.get("reader_id"), str):
                distinct.add(reading["reader_id"].strip())
        if len(distinct) < 2:
            issues.append("READERS_NOT_DISTINCT")
        readings = [r.get("reading") for r in readers if isinstance(r, dict)]
        if len(readings) >= 2 and len({x for x in readings if isinstance(x, str)}) > 1:
            # Preserve disagreement as uncertainty, never auto-reconcile.
            issues.append("DISAGREEMENT_BETWEEN_BLIND_READINGS")
    mass_ready = not any(
        e.startswith(("INVALID_OR_MISSING_", "UNCERTAINTY_", "MISSING_INSTRUMENT",
                      "MISSING_CALIBRATION", "MISSING_MEASUREMENT", "MISSING_CONSERVATION"))
        for e in issues
    )
    mark_ready = not any(
        e.startswith(("TWO_INDEPENDENT", "BAD_READING", "NOT_BLIND",
                      "MISSING_READING", "READERS_NOT_DISTINCT",
                      "DISAGREEMENT_BETWEEN"))
        for e in issues
    ) and not _missing_text(record, "image_reference") and not _missing_text(record, "reading_reference")
    documentation_complete = not issues
    prospective_issues = [
        "MISSING_OR_FALSE_" + field.upper()
        for field in REQUIRED_PROSPECTIVE if record.get(field) is not True
    ]
    can_be_blind_test = documentation_complete and not prospective_issues
    return {
        "object_id": record.get("object_id"),
        "mass_primary_verified": mass_ready,
        "independent_mark_reading_verified": mark_ready,
        "documentation_complete": documentation_complete,
        "eligible_for_new_blind_test": can_be_blind_test,
        "decision": "ELIGIBLE_FOR_PREREGISTERED_TEST" if can_be_blind_test
                    else "ABSTAIN_PENDING_EVIDENCE",
        "evidence_issues": issues,
        "prospective_issues": prospective_issues,
        "automatic_semantic_translation": None,
    }


def audit(records: list[dict]) -> dict:
    if not isinstance(records, list):
        raise ValueError("EXPECTED_LIST")
    results = []
    ids = set()
    for i, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"NON_OBJECT_{i}")
        ident = record.get("object_id")
        if ident in ids and isinstance(ident, str):
            raise ValueError("DUPLICATE_OBJECT_ID")
        if isinstance(ident, str):
            ids.add(ident)
        results.append(assess(record))
    return {
        "experiment": "METROLOGY_ADMISSION_07",
        "schema": "independent_primary_physical_and_visual_evidence",
        "total": len(results),
        "qualified_mass": sum(x["mass_primary_verified"] for x in results),
        "qualified_mark": sum(x["independent_mark_reading_verified"] for x in results),
        "eligible_new_blind": sum(x["eligible_for_new_blind_test"] for x in results),
        "results": results,
        "scientific_metrics_changed": False,
        "full3406_read_or_modified": False,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args(argv)
    input_path = args.input_json.resolve()
    if args.json and args.json.resolve() == input_path:
        raise ValueError("CANNOT_OVERWRITE_INPUT")
    records = json.loads(input_path.read_text(encoding="utf-8"))
    output = json.dumps(audit(records), indent=2, ensure_ascii=False) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
