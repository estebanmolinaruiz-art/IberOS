"""FULL3406-EXT-02: evidence-preserving external Iberika/BDH bridge.

External I-codes are **not** FULL3406 UID and are not interchangeable with
MLH/BDH reference systems. Only explicit published crosswalk rows are used.
This module is read-only and cannot certify physical identity or semantics.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from .catalog_crosswalk import concordance
from .legacy_bridge import audit_file

EXTERNAL_CODE = re.compile(r"^I\d{5}$")
EDITED_CODE = re.compile(r"^[a-gk]\.\d{1,2}\.\d{1,3}(?:\s+[a-z])?$", re.I)
LINK_STATUSES = {"VERIFIED", "FULL_GROUP_VERIFIED", "PARTIAL_GROUP", "MULTI_ENTRY_REVIEW"}


def _parts(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def build_external_bridge(registry: list[dict[str, str]],
                          external_links: list[dict[str, str]],
                          historical_records: list[dict[str, Any]]) -> dict[str, Any]:
    curated_ids = {row["OBJECT_ID"] for row in registry}
    if len(curated_ids) != len(registry):
        raise ValueError("DUPLICATE_CURATED_OBJECT_ID")
    if len({r["uid"] for r in historical_records}) != len(historical_records):
        raise ValueError("DUPLICATE_FULL3406_UID")
    mlh = concordance(registry, historical_records)
    by_object = {case["object_id"]: case for case in mlh["cases"]}
    seen_external: dict[str, str] = {}
    seen_object: set[str] = set()
    rows = []
    invalid = []
    for idx, link in enumerate(external_links, start=2):
        object_id = link.get("OBJECT_ID", "").strip()
        upstream_ids = _parts(link.get("UPSTREAM_IDS", ""))
        labels = _parts(link.get("Upstream_Labels", ""))
        status = link.get("Link_Status", "").strip()
        source_url = link.get("Source_URL", "").strip()
        evidence_errors = []
        if object_id not in curated_ids:
            evidence_errors.append("OBJECT_NOT_CURATED")
        if object_id in seen_object:
            evidence_errors.append("DUPLICATE_OBJECT_LINK_ROW")
        seen_object.add(object_id)
        if status not in LINK_STATUSES:
            evidence_errors.append("UNKNOWN_LINK_STATUS")
        if not source_url.startswith("https://cathalaunia.org/Iberika/"):
            evidence_errors.append("UPSTREAM_SOURCE_NOT_CANONICAL")
        for upstream_id in upstream_ids:
            if not EXTERNAL_CODE.fullmatch(upstream_id):
                evidence_errors.append("INVALID_UPSTREAM_ID")
            if upstream_id in seen_external and seen_external[upstream_id] != object_id:
                evidence_errors.append("UPSTREAM_ID_SHARED_BY_DIFFERENT_OBJECTS")
            seen_external[upstream_id] = object_id
        if len(upstream_ids) != int(link.get("Verified_ID_Count", "-1")):
            evidence_errors.append("DECLARED_EXTERNAL_ID_COUNT_MISMATCH")
        # Only bibliographic codes in an explicit label may be searched in
        # historical catalog_id. Generic labels such as 'cara a' are ignored.
        candidates = {}
        for label in labels:
            if not EDITED_CODE.fullmatch(label):
                continue
            rx = re.compile(r"(?<![A-Za-z0-9.])" + re.escape(label)
                            + r"(?![A-Za-z0-9.])", re.I)
            for record in historical_records:
                catalog = str(record.get("catalog_id", ""))
                if rx.search(catalog):
                    candidates.setdefault(record["uid"], {
                        "uid": record["uid"],
                        "historical_split": record["split_v3_4_9"],
                        "historical_catalog_id": catalog,
                        "external_editorial_label": label,
                        "documentary_only": True,
                    })
        prev = by_object.get(object_id, {})
        if evidence_errors:
            invalid.extend({"row": idx, "object_id": object_id, "error": e}
                           for e in sorted(set(evidence_errors)))
        rows.append({
            "object_id": object_id,
            "reference_system": "IBERIKA_EXTERNAL_I_CODE",
            "upstream_ids": upstream_ids,
            "verified_external_id_count": len(upstream_ids),
            "upstream_editorial_labels": labels,
            "source_url": source_url,
            "source_link_status": status,
            "source_confidence": link.get("Confidence", ""),
            "historical_label_candidate_uids": sorted(candidates),
            "historical_label_candidate_count": len(candidates),
            "historical_label_split_values": sorted(
                {v["historical_split"] for v in candidates.values()}),
            "historical_mlh_candidate_uids": sorted(e["uid"] for e in prev.get("entries", [])),
            "historical_mlh_candidate_count": prev.get("matching_entries", 0),
            "identity_crosswalk_certified": False,
            "physical_independence_certified": False,
            "grammatical_gold_available": False,
            "evidence_errors": sorted(set(evidence_errors)),
            "label_candidates": sorted(candidates.values(), key=lambda r:r["uid"]),
            "risk": ("PARTIAL_SOURCE_GROUP" if status in {"PARTIAL_GROUP","MULTI_ENTRY_REVIEW"}
                     else "GROUP_REQUIRES_OBJECT_LEVEL_REVIEW"),
        })
    return {
        "experiment": "FULL3406_EXTERNAL_CROSSWALK_02",
        "curated_objects": len(registry),
        "objects_with_upstream_links": len(rows),
        "distinct_external_I_codes": len(seen_external),
        "source_link_status_counts": dict(Counter(row["source_link_status"] for row in rows)),
        "objects_with_historical_editorial_label_candidates": sum(
            bool(row["historical_label_candidate_uids"]) for row in rows),
        "distinct_historical_label_uids": len({
            uid for row in rows for uid in row["historical_label_candidate_uids"]}),
        "invalid": invalid,
        "valid": not invalid,
        "records": rows,
        "full3406_modified": False,
        "official_metrics_changed": False,
        "semantic_accuracy": None,
        "promotion_permitted": False,
        "important_limit": "External I-code IDs are not FULL3406 UIDs; editorial coincidences do not establish physical-object equality.",
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Read-only FULL3406 external crosswalk")
    p.add_argument("snapshot", type=Path)
    p.add_argument("curated_registry_csv", type=Path)
    p.add_argument("external_link_csv", type=Path)
    p.add_argument("--json", type=Path)
    args = p.parse_args(argv)
    if not audit_file(args.snapshot)["integrity"]["valid"]:
        raise ValueError("FULL3406_INTEGRITY_FAIL")
    original = json.loads(args.snapshot.read_bytes())["records"]
    with args.curated_registry_csv.open(encoding="utf-8-sig", newline="") as f:
        curated = list(csv.DictReader(f))
    with args.external_link_csv.open(encoding="utf-8-sig", newline="") as f:
        links = list(csv.DictReader(f))
    report = build_external_bridge(curated, links, original)
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.json:
        if args.json.resolve() in {args.snapshot.resolve(),args.curated_registry_csv.resolve(),
                                   args.external_link_csv.resolve()}:
            raise ValueError("REFUSING_TO_OVERWRITE_INPUT")
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0 if report["valid"] else 2

if __name__ == "__main__":
    raise SystemExit(main())
