from __future__ import annotations

import argparse
import json
from pathlib import Path

from iberos import (
    engine_status,
    load_registry,
    registry_independence_audit,
    rok_recipient_candidate_matrix,
    ka_direction_candidate_matrix,
    salir_prospective_candidate_matrix,
    kutur_prospective_candidate_matrix,
    baides_batir_role_matrix,
    numeral_789_dashboard,
    dedi_orthogonal_matrix,
    numeral_exact_value_gate,
)


def build_snapshot() -> dict:
    rows = load_registry()
    inclusion_counts = {}
    for row in rows:
        key = row.get("IberOS_Inclusion", "")
        inclusion_counts[key] = inclusion_counts.get(key, 0) + 1

    independence = registry_independence_audit()
    status = engine_status()
    rok = rok_recipient_candidate_matrix()
    ka = ka_direction_candidate_matrix()
    salir = salir_prospective_candidate_matrix()
    kutur = kutur_prospective_candidate_matrix()
    bb = baides_batir_role_matrix()
    nums = numeral_789_dashboard()
    dedi = dedi_orthogonal_matrix()
    sorse = numeral_exact_value_gate("SORSE")

    return {
        "benchmark_version": "1.0.1",
        "software_version": "1.0.1",
        "date": "2026-10-11",
        "scope": "curated_public_layer",
        "corpus": {
            "raw_objects": len(rows),
            "independent_units": independence["independent_units"],
            "collapsed_records": independence["collapsed_record_count"],
            "inclusion_counts": {
                "INCLUDE": inclusion_counts.get("INCLUDE", 0),
                "CONTROL_ONLY": inclusion_counts.get("CONTROL_ONLY", 0),
                "EXCLUDED_CONTROL": inclusion_counts.get("EXCLUDED_CONTROL", 0),
                "CONDITIONAL": inclusion_counts.get("CONDITIONAL", 0),
            },
        },
        "authority": status["authority"],
        "official_metrics": status["official_metrics"],
        "open_gates": {
            "ROK": {
                "state": rok["gate_state"],
                "passing_candidates": rok["passing_candidates"],
            },
            "KA_KE_KU": {
                "state": ka["gate_state"],
                "passing_candidates": ka["passing_candidates"],
            },
            "SALIR": {
                "state": salir["gate_state"],
                "passing_candidates": salir["passing_candidates"],
            },
            "KUTUR": {
                "state": kutur["gate_state"],
                "passing_candidates": kutur["passing_candidates"],
            },
            "BAIDES_BATIR_EXACT_ROLE": {
                "state": bb["exact_role_gate_state"],
                "exact_role_fixed_candidates": bb["exact_role_fixed_candidates"],
            },
            "NUM_789": {
                "closed_values": nums["closed_values"],
            },
            "D_E_I_EXACT_FEATURE": {
                "state": dedi["exact_feature_state"],
                "passing_candidates": dedi["passing_candidates"],
            },
        },
        "negative_and_adversarial_evidence": {
            "excluded_controls": inclusion_counts.get("EXCLUDED_CONTROL", 0),
            "sorse_c1_8_physical_anchor": (
                "FAIL" if "C.1.8" in sorse["known_blocker"] else "UNRESOLVED"
            ),
            "automatic_core_promotion": False,
        },
        "interpretation": {
            "not_a_decipherment_percentage": True,
            "official_metrics_are_release_indicators": True,
            "open_gates_are_preserved_as_open": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    snapshot = build_snapshot()
    text = json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
