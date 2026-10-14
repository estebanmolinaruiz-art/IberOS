"""Portable, offline-friendly scientific audit manifest for IberOS mobile clients.

This is a data contract, not an Android/iOS application.
"""
from __future__ import annotations
from .core import AUTHORITY
from .object_rule_audit import audit_object_rules

SCHEMA = "IberOS-Mobile-CORE/1.0"

def mobile_object_payload(object_id: str, observations: list[dict] | None = None) -> dict:
    from .rule_execution import execute_rules
    audit = audit_object_rules(object_id)
    findings = []
    for obs in observations or []:
        if not isinstance(obs, dict) or obs.get("object_id") != object_id:
            raise ValueError("Every observation must explicitly match the object_id")
        findings.append(execute_rules(obs))
    return {
        "schema": SCHEMA, "object_id": object_id,
        "authority": dict(AUTHORITY),
        "modules": audit["modules"],
        "candidate_rules": audit["rules"],
        "evaluated_rules": findings,
        "evaluation_policy": "ONLY_EXPLICIT_SOURCED_OBSERVATIONS",
        "scientific_state": "UNVERIFIED",
        "automatic_core_promotion": False,
        "translation_validated": False,
    }
