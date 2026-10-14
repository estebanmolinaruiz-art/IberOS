"""Strict input gate for published CORE evaluations; never infer observations from tags."""
from __future__ import annotations
from .core import get_object
from .rule_execution import execute_rules

def evaluate_reviewed_observations(records: list[dict]) -> dict[str, list[dict]]:
    """Run only explicitly sourced, reviewer-approved observations per known object.

    Approval here authorizes technical execution, not scientific confirmation.
    """
    if not isinstance(records, list):
        raise ValueError("Expected list of observation records")
    result: dict[str, list[dict]] = {}
    seen: set[str] = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Observation must be a dictionary")
        oid, evidence_id = record.get("object_id"), record.get("evidence_id")
        if not isinstance(oid, str) or get_object(oid) is None:
            raise ValueError("Unknown observation object_id")
        if not isinstance(evidence_id, str) or not evidence_id.strip() or evidence_id in seen:
            raise ValueError("A unique evidence_id is mandatory")
        seen.add(evidence_id)
        if record.get("review_status") != "APPROVED_FOR_TECHNICAL_EVALUATION":
            continue
        if not isinstance(record.get("source_reference"), str) or not record["source_reference"].strip():
            raise ValueError("Approved observations require documentary source_reference")
        if not isinstance(record.get("rules"), list) or not record["rules"]:
            raise ValueError("Approved observations require explicit rules")
        report = execute_rules(record)
        report["evidence_id"] = evidence_id
        report["review_status"] = "APPROVED_FOR_TECHNICAL_EVALUATION"
        report["scientific_state"] = "UNVERIFIED"
        result.setdefault(oid, []).append(report)
    return result
