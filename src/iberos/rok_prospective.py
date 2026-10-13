"""Pre-registered discrimination protocol for ROK interpretations.

This is a research audit, not a semantic validator and not the official
ROK-RECIPIENT-02 release gate.
"""
from __future__ import annotations
from typing import Any

PROTOCOL = "ROK-SEGMENTATION-PROSPECTIVE-01"
HYPOTHESES = {
    "H1": "NP+TE segmentation with an externally anchored participant role",
    "H2": "TE is part of TEROKAN; no independent NP role follows from TE",
    "H3": "ROK distribution is a genre formula rather than a fixed transfer role",
}
REQUIRED = ("witness_id", "physical_id", "source", "passage", "lock_id",
            "lock_hash", "prediction_id", "prediction", "segmentation",
            "external_role", "external_role_source", "independent_context",
            "held_out", "reading_secure", "genre", "control_type")


def assess_rok_prospective(observations: Any) -> dict[str, Any]:
    """Check preregistration and classify evidence without adjudicating meaning."""
    errors: list[str] = []
    if not isinstance(observations, list) or not observations:
        errors.append("nonempty observations list required")
        observations = []
    seen_physical: set[str] = set()
    summaries = []
    for i, row in enumerate(observations):
        prefix = f"observations[{i}]"
        if not isinstance(row, dict):
            errors.append(f"{prefix}: object required")
            continue
        missing = [key for key in REQUIRED
                   if key not in row or row[key] is None
                   or isinstance(row[key], str) and not row[key].strip()]
        if missing:
            errors.append(f"{prefix}: missing {', '.join(missing)}")
            continue
        if row["prediction"] not in HYPOTHESES:
            errors.append(f"{prefix}: unknown hypothesis")
        if row["segmentation"] not in ("NP_TE_ROK", "NP_TEROKAN", "UNRESOLVED"):
            errors.append(f"{prefix}: unrecognized segmentation")
        if row["external_role"] not in ("RECIPIENT", "GIVER", "OTHER", "UNRESOLVED"):
            errors.append(f"{prefix}: unrecognized external role")
        if row["control_type"] not in ("TARGET", "NON_ROK", "NEGATIVE"):
            errors.append(f"{prefix}: invalid control type")
        for key in ("independent_context", "held_out", "reading_secure"):
            if type(row[key]) is not bool:
                errors.append(f"{prefix}: {key} must be boolean")
        phys = str(row["physical_id"]).strip()
        if phys in seen_physical:
            errors.append(f"{prefix}: duplicate physical witness")
        seen_physical.add(phys)
        if row["control_type"] == "TARGET" and row["external_role"] == "UNRESOLVED":
            errors.append(f"{prefix}: target has no externally anchored role")
        if not row["independent_context"] or not row["held_out"] or not row["reading_secure"]:
            errors.append(f"{prefix}: prospective safeguards incomplete")
        summaries.append({"witness_id": row["witness_id"],
                          "physical_id": phys,
                          "prediction": row["prediction"],
                          "segmentation": row["segmentation"],
                          "control_type": row["control_type"]})
    has_target = any(x["control_type"] == "TARGET" for x in summaries)
    has_control = any(x["control_type"] != "TARGET" for x in summaries)
    if not has_target:
        errors.append("at least one target witness required")
    if not has_control:
        errors.append("at least one non-target control required")
    return {"protocol": PROTOCOL,
            "hypotheses": dict(HYPOTHESES),
            "status": "BLOCKED" if errors else "READY_FOR_INDEPENDENT_REVIEW",
            "errors": errors, "witnesses": summaries,
            "official_rok_recipient_gate": "OPEN",
            "scientific_state": "UNVERIFIED",
            "automatic_core_promotion": False}
