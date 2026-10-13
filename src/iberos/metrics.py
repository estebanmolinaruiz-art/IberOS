"""Explicit provenance and comparability labels for frozen IberOS metrics.

The catalog documents existing scores; it does not recalculate or promote them.
"""
from __future__ import annotations

from .core import AUTHORITY, OFFICIAL_METRICS

METRIC_DEFINITIONS = {
    "CORE": ("scientific_release_rubric", 45, "27/45", "frozen rubric score"),
    "CORE_plus_INFER": ("scientific_release_rubric_plus_inference", 45, "28/45", "frozen rubric score"),
    "ICS_global": ("historical_ics", None, None, "historical indicator; calculation not recovered"),
    "INFER_progress": ("inference_workflow", None, None, "internal inference-progress indicator; denominator not recovered"),
    "ROK": ("family_release_state", None, None, "family-specific frozen indicator"),
    "KA_KE": ("family_release_state", None, None, "family-specific frozen indicator"),
    "SALIR": ("family_release_state", None, None, "family-specific frozen indicator"),
    "KUTUR": ("family_release_state", None, None, "family-specific frozen indicator"),
    "BAIDES_BATIR": ("family_release_state", None, None, "family-specific frozen indicator"),
    "D_E_I": ("family_release_state", None, None, "family-specific frozen indicator"),
}


def metric_registry() -> dict:
    """Return lossless metric values with definitions and limits."""
    if set(METRIC_DEFINITIONS) != set(OFFICIAL_METRICS):
        raise ValueError("Metric definitions and frozen indicators are out of sync")
    return {
        "protocol": "IBEROS-METRICS-COMPARABILITY-01",
        "authority": dict(AUTHORITY),
        "metrics": {
            name: {
                "value": value,
                "scope": METRIC_DEFINITIONS[name][0],
                "denominator": METRIC_DEFINITIONS[name][1],
                "numerator_denominator": METRIC_DEFINITIONS[name][2],
                "interpretation": METRIC_DEFINITIONS[name][3],
                "historical_formula_verified": False,
                "language_decipherment_percentage": False,
            }
            for name, value in OFFICIAL_METRICS.items()
        },
        "historical_pre_github_baseline": "NOT_VERIFIED",
        "single_global_completion_percentage": None,
        "scientific_state": "FROZEN",
        "automatic_core_promotion": False,
    }


def compare_metric_values(left_name: str, right_name: str) -> dict:
    """Refuse misleading percentage comparisons across distinct rubrics."""
    registry = metric_registry()["metrics"]
    if left_name not in registry or right_name not in registry:
        raise ValueError("Unknown metric identifier")
    left, right = registry[left_name], registry[right_name]
    comparable = (
        left_name == right_name
        and left["denominator"] is not None
        and right["denominator"] == left["denominator"]
    )
    return {
        "left": left_name,
        "right": right_name,
        "comparable_as_same_rubric": comparable,
        "status": "SAME_FROZEN_RUBRIC" if comparable else "NOT_COMPARABLE_WITHOUT_HISTORICAL_METHOD",
        "automatic_core_promotion": False,
    }
