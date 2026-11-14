"""Audit Mas de Moreno published impression descriptions without inventing inventory IDs.

2009 figure references are source figure panels, not official archaeological IDs.
Six aggregate-derived 2015 reconciliation slots are NOT individually identified
stamps and are deliberately excluded from analytical sample size.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data/review/mas_moreno_impression_inventory_v1.json"
SCHEMA = "IberOS-MASMORENO-IMPRESSIONS/1.0"
ALLOWED_STATES = {
    "INDIVIDUAL_DESCRIPTION_NOT_OFFICIAL_INVENTORY",
    "AGGREGATE_RECONCILIATION_SLOT_NOT_INDIVIDUAL_OBJECT",
}


def audit_impressions(document: dict) -> dict:
    if not isinstance(document, dict) or document.get("schema") != SCHEMA:
        raise ValueError("Incorrect inventory schema")
    if document.get("cost_eur") != 0:
        raise ValueError("Costs are forbidden")
    records = document.get("records")
    if not isinstance(records, list) or len(records) != 15:
        raise ValueError("Expected 15 historical impression rows")
    ids = [r.get("local_record_id") for r in records]
    if len(set(ids)) != len(ids) or not all(isinstance(x, str) and x for x in ids):
        raise ValueError("Duplicate or absent local ID")
    if any(r.get("official_inventory_id") is not None for r in records):
        raise ValueError("Official archaeological IDs not independently established")
    if any(r.get("photo_independently_read") is not False for r in records):
        raise ValueError("No blind photographic re-reading available")
    if any(r.get("stamp_matrix_id") is not None for r in records):
        raise ValueError("Stamp dies cannot be assigned by editorial spelling")
    if any(r.get("identity_status") not in ALLOWED_STATES for r in records):
        raise ValueError("Unknown identity state")
    documented = [r for r in records if r["identity_status"] ==
                  "INDIVIDUAL_DESCRIPTION_NOT_OFFICIAL_INVENTORY"]
    anonymous = [r for r in records if r["identity_status"] ==
                 "AGGREGATE_RECONCILIATION_SLOT_NOT_INDIVIDUAL_OBJECT"]
    if len(documented) != 9 or len(anonymous) != 6:
        raise ValueError("2009 and 2015 cohorts cannot be conflated")
    if any(not r["counts_as_individual_description"] for r in documented):
        raise ValueError("2009 case not actually described")
    if any(r["counts_as_individual_description"] or r.get("family") is not None
           or r.get("figure_panel") is not None for r in anonymous):
        raise ValueError("Unidentified 2015 slot presented as an identified artefact")
    counts = Counter((r["script"], r["object_support"]) for r in records)
    # Gorgues 2009 describes the script of kaku as possibly Iberian or Celtiberian.
    if counts.pop(("IBERIAN_OR_CELTIBERIAN", "LOOM_WEIGHT"), 0) != 1:
        raise ValueError("Uncertainty over kaku script must be retained")
    # The thesis calls 13 of the 15 Iberian; that category is an aggregate,
    # not independent confirmation of the script of every 2009 impression.
    expected = {
        ("IBERIAN", "STORAGE_JAR_RIM"): 6,
        ("IBERIAN", "LOOM_WEIGHT"): 4,
        ("IBERIAN", "COMMON_WARE"): 1,
        ("LATIN", "STORAGE_JAR_RIM"): 1,
        ("LATIN", "AMPHORA"): 1,
        ("UNDETERMINED_PALEOHISPANIC", "STORAGE_JAR_RIM"): 1,
    }
    if dict(counts) != expected:
        raise ValueError("Mismatch in object support counts")
    # O(?) and kaku are provisionally placed among 2015 '13 Iberian'
    # based on the published aggregate; no individual script proof inferred.
    totals = document["published_2015_totals"]
    if totals["total"] != 15 or sum(sum(x.values()) for k, x in totals.items()
                                     if isinstance(x, dict)) != 15:
        raise ValueError("Incorrect published historical total")
    expected_support = {
        "STORAGE_JAR_RIM": 8, "LOOM_WEIGHT": 5,
        "COMMON_WARE": 1, "AMPHORA": 1,
    }
    actual_support = dict(Counter(r["object_support"] for r in records))
    if actual_support != expected_support:
        raise ValueError("Published material support classes do not reconcile")
    gorgues_figs = [r["figure_panel"] for r in documented if r["figure_panel"]]
    if len(set(gorgues_figs)) != len(gorgues_figs):
        raise ValueError("Duplicate figure panel; verify two physical objects")
    if any(r["family"] == "ORTINKO" for r in documented):
        raise ValueError("2009 O(?) reading cannot be silently promoted to Ortinko")
    if any(r["context_phase"] == "P3_CONFIRMED" for r in documented):
        raise ValueError("Overconfident archaeological phase")
    if any(r["discovery_source"] == "SACILOTTO_UNTIL_2015_AGGREGATE" for r in documented):
        raise ValueError("Anonymous impression counted as individually described")
    if document.get("validated_physical_inventory_count") != 0 or document.get("semantic_gold_count") != 0:
        raise ValueError("Scientific validation unsupported")
    return {
        "schema": "IberOS-MASMORENO-IMPRESSIONS-AUDIT/1.0",
        "reconciled_historical_impressions": len(records),
        "individual_2009_descriptions": len(documented),
        "anonymous_reconciliation_slots": len(anonymous),
        "2009_figure_panels": len(gorgues_figs),
        "object_support_totals": actual_support,
        "original_inventory_numbers_verified": 0,
        "individual_stamp_matrices_adjudicated": 0,
        "double_blind_photo_readings": 0,
        "semantic_role_gold_independent": 0,
        "new_semantic_hold": 0,
        "translation_validated": False,
        "automatic_core_promotion": False,
        "notice": "Six anonymous slots are arithmetic reconciliation only. No validated official 15-object register exists here.",
    }


def main() -> None:
    print(json.dumps(audit_impressions(json.loads(DATA.read_text(encoding="utf-8"))),
                     indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
