"""METROLOGY-DISCRIMINATION-03: explicitly challenge mass-only interpretations.

The 2.1-g alternative reproduces nominal 42-g and 420-g masses, so those
anchors alone CANNOT distinguish competing schemes or validate sign values.
No access to FULL3406, no training or new museum evidence assumed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

BASELINE_G = 2.1
LITERATURE_EXAMPLES_G = {
    "NOMINAL_SMALL": 42.0,
    "NOMINAL_LARGE": 420.0,
    "PUIG_MISERICORDIA": 41.29,
    "TOS_PELAT": 418.0,
}


def compare() -> dict:
    results = []
    for label, mass in LITERATURE_EXAMPLES_G.items():
        nearest = round(mass / BASELINE_G)
        residual = mass - nearest * BASELINE_G
        results.append({
            "label": label,
            "published_or_nominal_mass_g": mass,
            "alternative_base_mass_g": BASELINE_G,
            "nearest_integer_multiple": nearest,
            "nearest_multiple_g": round(nearest * BASELINE_G, 5),
            "signed_residual_g": round(residual, 5),
            "relative_absolute_residual_percent": round(100 * abs(residual) / mass, 4),
            "establishes_iberian_sign_meaning": False,
        })
    return {
        "experiment": "METROLOGY_DISCRIMINATION_03",
        "analysis_type": "RETROSPECTIVE_ADVERSARIAL_CHECK",
        "source_alternative": "Iberian ponderal series discussed in Fletcher-Silgo 1995 and Villanueva de la Jara study 2018",
        "source_url": "https://www.researchgate.net/publication/331529729_Un_conjunto_de_ponderales_ibericos_procedente_de_Villanueva_de_la_Jara_Cuenca",
        "nominal_overlap": {"42g_is_20_times_2_1g": True,
                            "420g_is_200_times_2_1g": True},
        "mass_only_42_420_discriminates_models": False,
        "examples": results,
        "must_have_to_unblock": [
            "Complete inventory of weights chosen without reference to model fit",
            "Original mark photos with scale and independent sign readings",
            "Institutional masses, precision and conservation state",
            "Provenance, dating, support, object-level deduplication",
            "Predeclared predictions on genuinely new objects and negative controls",
            "Explicit analysis of alternative 2.1-g system alongside a/o/ki",
        ],
        "museum_status": "PROMISE_TO_PROVIDE_INFORMATION_NO_TECHNICAL_DATA_YET",
        "museum_response_date": "2026-11-05",
        "full3406_accessed": False,
        "historical_splits_modified": False,
        "semantic_gold_validated": False,
        "translations_validated": 0,
        "scientific_metrics_changed": False,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Document mass-only model non-identifiability")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args(argv)
    output = json.dumps(compare(), indent=2, ensure_ascii=False) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
