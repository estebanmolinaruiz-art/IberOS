"""METROLOGY-HYBRID-02. Transparent 10/12 vs uniform 10/10 or 12/12.

Literature-based, deliberately non-blind diagnostic; no physical museum
measurements certified, no claims about decipherment, no FULL3406 access.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

O_ANCHORS_G = {
    "PUIG_MISERICORDIA_O_SIGN": 41.29,
    "COVALTA_IV": 42.20,
    "CIGARRALEJO_VII": 41.46,
}
A_WEIGHTS_G = {
    "TOS_PELAT_10_POINTS": 418.00,
    "PUIG_CASTELLAR": 423.78,
    "L_ALCUDIA": 424.00,
}
KI_REFERENCE_G = 3.43  # Literature-level ARS heavy drachma example; not a new weighed object.
CANDIDATES = (
    ("HYBRID_10_12", 10, 12),
    ("UNIFORM_10_10", 10, 10),
    ("UNIFORM_12_12", 12, 12),
    ("MIXED_12_10", 12, 10),
)


def evaluate(o_g: float = 41.29, ki_g: float = KI_REFERENCE_G) -> dict:
    if not 0 < o_g < 1000 or not 0 < ki_g < 1000:
        raise ValueError("INVALID_POSITIVE_MASS")
    rows = []
    for name, a_factor, ki_divisor in CANDIDATES:
        a_pred = o_g * a_factor
        ki_pred = o_g / ki_divisor
        a_errors = [
            {
                "object": key,
                "published_mass_g": mass,
                "predicted_mass_g": round(a_pred, 6),
                "signed_residual_g": round(mass - a_pred, 6),
                "absolute_percentage_error": round(100 * abs(mass - a_pred) / mass, 5),
            } for key, mass in A_WEIGHTS_G.items()
        ]
        ki_error = 100 * abs(ki_g - ki_pred) / ki_g
        a_mape = sum(item["absolute_percentage_error"] for item in a_errors) / len(a_errors)
        rows.append({
            "model": name,
            "a_to_o_factor": a_factor,
            "o_to_ki_divisor": ki_divisor,
            "predicted_a_g": round(a_pred, 6),
            "predicted_ki_g": round(ki_pred, 6),
            "a_weight_errors": a_errors,
            "a_mape_percent": round(a_mape, 5),
            "ki_absolute_percentage_error": round(ki_error, 5),
            # Equal-domain descriptive mean: one a-domain average and one ki observation.
            # NOT a likelihood, evidence strength or pre-registered accuracy metric.
            "two_domain_descriptive_mean_percent": round((a_mape + ki_error) / 2, 5),
        })
    sensitivity = []
    for anchor, mass in O_ANCHORS_G.items():
        predictions = evaluate_anchor(mass, ki_g)
        sensitivity.append({"anchor": anchor, "mass_g": mass,
                            "best_descriptive_model": predictions[0]["model"],
                            "models_ordered": predictions})
    return {
        "experiment": "METROLOGY_HYBRID_02",
        "status": "RETROSPECTIVE_LITERATURE_COMPARISON_NOT_BLIND",
        "o_anchor_g": o_g,
        "ki_reference_g": ki_g,
        "o_anchor_candidates_g": O_ANCHORS_G,
        "selected_a_weights_g": A_WEIGHTS_G,
        "models": rows,
        "anchor_sensitivity": sensitivity,
        "historical_493_g_excluded": True,
        "institutional_remeasurement_confirmed": False,
        "independent_sampling": False,
        "independent_numeric_gold": False,
        "bi_equals_two_confirmed": False,
        "abar_equals_ten_confirmed": False,
        "translations_validated": 0,
        "hold_or_full3406_accessed": False,
        "official_metrics_changed": False,
        "limitations": [
            "The 3.43 g ki value is an illustrative published coin metric, not an audited representative sample.",
            "The selected a weights are taken from literature arguing for these metrological models.",
            "No uncertainty propagation for wear, instrument, ancient mint/weight variation or provenance.",
            "Units a/o/ki and their relation are hypotheses, not independently established semantic gold.",
            "Comparison is a diagnostic fit, not probability, significance or proof of linguistic meaning.",
        ],
    }


def evaluate_anchor(o_g: float, ki_g: float) -> list[dict]:
    result = []
    for name, a_factor, ki_divisor in CANDIDATES:
        predicted_a = o_g * a_factor
        predicted_ki = o_g / ki_divisor
        a_mape = sum(100 * abs(mass - predicted_a) / mass
                     for mass in A_WEIGHTS_G.values()) / len(A_WEIGHTS_G)
        ki_ape = 100 * abs(ki_g - predicted_ki) / ki_g
        result.append({"model": name, "a_mape_percent": round(a_mape, 4),
                       "ki_ape_percent": round(ki_ape, 4),
                       "two_domain_descriptive_mean_percent": round((a_mape + ki_ape) / 2, 4)})
    return sorted(result, key=lambda item: item["two_domain_descriptive_mean_percent"])


def main(argv=None):
    parser = argparse.ArgumentParser(description="Historical a/o/ki hybrid versus uniform model sensitivities")
    parser.add_argument("--o-mass", type=float, default=41.29)
    parser.add_argument("--ki-mass", type=float, default=KI_REFERENCE_G)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args(argv)
    result = evaluate(o_g=args.o_mass, ki_g=args.ki_mass)
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
