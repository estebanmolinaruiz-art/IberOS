"""METROLOGY-MODELS-01: published-weight model sensitivity, not a translation.

All masses are literature-derived; no museum measurement independently
checked. Full3406, its splits and official metrics are not accessed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

O_MARKED_G = 41.29
WEIGHTS = (
    ("TOS_PELAT_10_POINTS", 418.0, 10),
    ("PUIG_CASTELLAR", 423.78, None),
    ("L_ALCUDIA", 424.0, None),
)


def compare(unit_mass_g: float = O_MARKED_G) -> dict:
    """Compare two explicit multiplication models using the SAME anchor."""
    if unit_mass_g <= 0:
        raise ValueError("INVALID_ANCHOR_MASS")
    models = []
    for multiplier, name in ((10, "DECIMAL_A_O"), (12, "DUODECIMAL_A_O")):
        expected = unit_mass_g * multiplier
        predictions = [
            {
                "object": obj,
                "published_mass_g": mass,
                "marks_reported": marks,
                "predicted_g": round(expected, 4),
                "signed_residual_g": round(mass - expected, 4),
                "absolute_error_percent": round(100 * abs(mass - expected) / expected, 3),
                "ratio_to_published_o": round(mass / unit_mass_g, 4),
                "marks_match_multiplier": (marks == multiplier if marks is not None else None),
            }
            for obj, mass, marks in WEIGHTS
        ]
        models.append({
            "model": name,
            "multiplier": multiplier,
            "predicted_a_g": round(expected, 4),
            "published_weights": predictions,
            "mean_absolute_residual_g": round(
                sum(abs(item["signed_residual_g"]) for item in predictions) / len(predictions), 4
            ),
        })
    return {
        "experiment": "METROLOGY_MODELS_01",
        "status": "RETROSPECTIVE_NONBLIND_SELECTED_LITERATURE",
        "unit_o_marked_g": unit_mass_g,
        "unit_o_object": "Puig de la Misericordia CS.02.01",
        "models": models,
        "reported_493g_weight_included": False,
        "reported_493g_weight_reason": "Ferrer i Jane 2026 reports a 1930 publication typographical error; check correction in primary archives",
        "semantic_gold": False,
        "numeric_bi_two_validated": False,
        "supports_abar_ten_validated": False,
        "archaeological_identity_independently_verified": False,
        "institutional_mass_measurements_verified": False,
        "sampling_independent": False,
        "hold_used_for_scoring": False,
        "frozen_full3406_modified": False,
        "official_metrics_changed": False,
        "next_gate": "Institutional inventory, measured masses and error margins, authentic mark photos and comparison with non-selected weights",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Descriptive comparison of published Iberian weight models")
    parser.add_argument("--o-mass", type=float, default=O_MARKED_G)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args(argv)
    output = json.dumps(compare(args.o_mass), ensure_ascii=False, indent=2) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
