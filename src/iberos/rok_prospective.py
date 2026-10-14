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
    # Union all identifiers, including transitive physical / leak / dependency
    # bridges. One connected component is at most one documentary witness.
    from .core import GENERIC_DEPENDENCY_LABELS
    parents = list(range(len(observations)))
    def root(i: int) -> int:
        while parents[i] != i:
            parents[i] = parents[parents[i]]
            i = parents[i]
        return i
    def join(a: int, b: int) -> None:
        a, b = root(a), root(b)
        if a != b:
            parents[max(a, b)] = min(a, b)
    seen: dict[str, int] = {}
    usable = []
    for i, row in enumerate(observations):
        if not isinstance(row, dict) or not isinstance(row.get("physical_id"), str):
            continue
        phys = row["physical_id"].strip()
        if not phys:
            continue
        usable.append(i)
        keys = ["PHYS:" + phys]
        for name in ("LEAK_GROUP", "Dependency_Group", "TEXT_DEPENDENCY_GROUP"):
            value = row.get(name)
            if not isinstance(value, str) or not value.strip():
                continue
            value = value.strip()
            if name == "Dependency_Group" and value.upper() in GENERIC_DEPENDENCY_LABELS:
                continue
            keys.append(name + ":" + value)
        for key in keys:
            if key in seen:
                join(i, seen[key])
            else:
                seen[key] = i
    # Context is recorded for archaeological review, not used to merge objects.
    shared_contexts: dict[str, list[int]] = {}
    for i, row in enumerate(observations):
        if not isinstance(row, dict):
            continue
        context = row.get("archaeological_context")
        if isinstance(context, str) and context.strip():
            shared_contexts.setdefault(context.strip(), []).append(i)
    shared_contexts = {key: ids for key, ids in shared_contexts.items()
                       if len(ids) > 1}
    components: dict[int, list[int]] = {}
    for i in usable:
        components.setdefault(root(i), []).append(i)
    duplicates = [members for members in components.values() if len(members) > 1]
    for members in duplicates:
        errors.append("cross-edition dependency (transitive documentary dependency): observations " +
                      ", ".join(str(i) for i in members))
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
            "documentary_components": [members for _, members in sorted(components.items())],
            "documentary_unit_count": len(components),
            "shared_archaeological_contexts": shared_contexts,
            "context_independence_review_required": bool(shared_contexts),
            "official_rok_recipient_gate": "OPEN",
            "scientific_state": "UNVERIFIED",
            "automatic_core_promotion": False}
