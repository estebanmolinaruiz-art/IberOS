"""FULL3406-BRIDGE-01: offline, read-only integration of frozen legacy data.
The historical JSON is user-supplied and is NOT distributed with the package.
No automatic identity mapping, semantic promotion, or retraining.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
from typing import Any
from .core import OFFICIAL_METRICS, load_registry

EXPECTED_SHA256 = "3cf66a5e9abbec2a8a356be3432d507da0d967d3310ffdeb3dc22878055d13a4"
EXPECTED_COUNTS = {"TRAIN": 2378, "VAL": 346, "HOLD": 623, "EXCLUDED": 59}
EXPECTED_RECORDS = 3406
EXPECTED_GROUPS = 1799
KEY_FIELD = "dependency_key_v3_4_9"
SPLIT_FIELD = "split_v3_4_9"


def audit_records(records: list[dict[str, Any]], *, expected_count: int = EXPECTED_RECORDS,
                  expected_groups: int = EXPECTED_GROUPS,
                  expected_splits: dict[str, int] | None = None) -> dict[str, Any]:
    """Use original dependency identities; EXCLUDED intentionally lacks an active key."""
    expected_splits = EXPECTED_COUNTS if expected_splits is None else expected_splits
    problems: list[str] = []
    seen: set[str] = set()
    duplicate_uids: list[str] = []
    splits: Counter[str] = Counter()
    groups: dict[str, set[str]] = defaultdict(set)
    missing_keys = excluded_with_key = 0
    for i, row in enumerate(records):
        if not isinstance(row, dict):
            problems.append(f"NOT_OBJECT_AT_INDEX:{i}")
            continue
        uid = row.get("uid")
        if not isinstance(uid, str) or not uid:
            problems.append(f"MISSING_UID_AT_INDEX:{i}")
        elif uid in seen:
            duplicate_uids.append(uid)
        else:
            seen.add(uid)
        split = row.get(SPLIT_FIELD)
        if split not in EXPECTED_COUNTS:
            problems.append(f"UNKNOWN_SPLIT_AT_INDEX:{i}")
            continue
        splits[split] += 1
        key = row.get(KEY_FIELD)
        if split == "EXCLUDED":
            if key:
                excluded_with_key += 1
        elif not isinstance(key, str) or not key:
            missing_keys += 1
        else:
            groups[key].add(split)
    if len(records) != expected_count:
        problems.append("WRONG_RECORD_COUNT")
    if duplicate_uids:
        problems.append("DUPLICATED_UID")
    if len(groups) != expected_groups:
        problems.append("WRONG_DEPENDENCY_GROUP_COUNT")
    if dict(splits) != dict(expected_splits):
        problems.append("WRONG_SPLIT_COUNTS")
    if missing_keys:
        problems.append("MISSING_ACTIVE_DEPENDENCY_KEYS")
    if excluded_with_key:
        problems.append("EXCLUDED_HAS_ACTIVE_DEPENDENCY_KEY")
    leakage = sorted(k for k, group_splits in groups.items() if len(group_splits) > 1)
    if leakage:
        problems.append("DEPENDENCY_SPLIT_LEAKAGE")
    return {
        "valid": not problems, "problems": problems,
        "record_count": len(records), "unique_uids": len(seen),
        "duplicated_uids": duplicate_uids[:10],
        "dependency_groups": len(groups), "split_counts": dict(splits),
        "active_missing_dependency_keys": missing_keys,
        "excluded_with_dependency_key": excluded_with_key,
        "leakage_group_count": len(leakage), "leakage_groups_sample": leakage[:10],
    }


def literal_matches(records: list[dict[str, Any]], needle: str) -> list[dict[str, str]]:
    """Only literal uid/catalog_id matches; absence never certifies independence."""
    matches = []
    for row in records:
        if any(needle.casefold() in str(row.get(k, "")).casefold()
               for k in ("uid", "catalog_id")):
            matches.append({
                "uid": row["uid"], "catalog_id": str(row.get("catalog_id", "")),
                "split": row[SPLIT_FIELD],
                "dependency_key": str(row.get(KEY_FIELD) or ""),
            })
    return matches


def audit_file(path: str | Path, *, expected_sha256: str = EXPECTED_SHA256) -> dict[str, Any]:
    """Verify exact historical binary fingerprint before parsing its contents."""
    raw = Path(path).read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != expected_sha256:
        raise ValueError("SHA256_MISMATCH: never substitute another FULL3406")
    doc = json.loads(raw)
    if not isinstance(doc, dict) or not isinstance(doc.get("records"), list):
        raise ValueError("MISSING_OR_INVALID_RECORDS")
    records = doc["records"]
    integrity = audit_records(records)
    declared = doc.get("stats_v3_4_9", {})
    stats_match = (
        declared.get("records_total") == integrity["record_count"]
        and declared.get("dependency_units") == integrity["dependency_groups"]
        and declared.get("record_split_counts") == integrity["split_counts"]
    )
    if not stats_match:
        integrity["valid"] = False
        integrity["problems"].append("STORED_STATS_DISAGREE")
    return {
        "experiment": "FULL3406_BRIDGE_01",
        "legacy_snapshot": "LEAK-SAFE v3.4.9 / FULL3406",
        "input_sha256": sha, "integrity": integrity,
        "stored_stats_consistent": stats_match,
        "curated_registry_objects": len(load_registry()),
        "legacy_curated_mapping": "NOT_CERTIFIED; separate identity systems",
        "xabia_cirne_literal_matches": literal_matches(records, "Cirne"),
        "la_mesa_literal_name_matches": literal_matches(records, "Mesa"),
        "alcolea_literal_name_matches": literal_matches(records, "Alcolea"),
        "la_mesa_independence_certified": False,
        "semantic_gold_available": 0, "grammar_accuracy": None,
        "training_or_prediction_executed": False,
        "original_snapshot_modified": False,
        "official_metrics_changed": False,
        "official_metrics": dict(OFFICIAL_METRICS),
        "next_gate": "Manual MLH/BDH and physical-object concordance; no HOLD promotion",
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Read-only frozen FULL3406 integrity audit")
    p.add_argument("snapshot", type=Path)
    p.add_argument("--json", type=Path)
    a = p.parse_args(argv)
    report = audit_file(a.snapshot)
    out = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if a.json:
        if a.snapshot.resolve() == a.json.resolve():
            p.error("Refusing to overwrite original snapshot")
        a.json.parent.mkdir(parents=True, exist_ok=True)
        a.json.write_text(out, encoding="utf-8")
    else:
        print(out, end="")
    return 0 if report["integrity"]["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
