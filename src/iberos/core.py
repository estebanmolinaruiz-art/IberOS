from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None

PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parent.parent.parent

def _registry_path() -> Path:
    packaged = PACKAGE_ROOT / "data" / "iberos_objects_registry_v2.0.csv"
    if packaged.exists():
        return packaged
    candidate = REPO_ROOT / "data" / "curated" / "iberos_objects_registry_v2.0.csv"
    if candidate.exists():
        return candidate
    raise FileNotFoundError("IberOS registry not found.")


def load_registry() -> list[dict[str, str]]:
    path = _registry_path()
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def get_object(object_id: str) -> dict[str, str] | None:
    for row in load_registry():
        if row.get("OBJECT_ID") == object_id:
            return row
    return None

def family_objects(family: str) -> list[dict[str, str]]:
    family = family.upper()
    results = []
    for row in load_registry():
        families = {x.upper() for x in row.get("Familias_Tags", "").split(";") if x}
        if family in families:
            results.append(row)
    return results

def schema_path() -> Path:
    return PACKAGE_ROOT / "schema" / "iberos-result-v1.schema.json"

def validate_result(path_or_record: str | Path | dict[str, Any]):
    if isinstance(path_or_record, dict):
        record = path_or_record
    else:
        with Path(path_or_record).open(encoding="utf-8") as f:
            record = json.load(f)
    with schema_path().open(encoding="utf-8") as f:
        schema = json.load(f)
    if Draft202012Validator is None:
        return False, ["jsonschema is not installed"]
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(record), key=lambda e: list(e.path))
    return len(errors) == 0, [e.message for e in errors]
