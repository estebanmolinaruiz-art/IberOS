"""Read-only independent-evidence gap report for frozen ROK and KA gates."""
from __future__ import annotations
from .core import (
    AUTHORITY, rok_recipient_candidate_matrix, ka_direction_candidate_matrix,
)

def audit_prospective_gates() -> dict:
    ro = rok_recipient_candidate_matrix()
    ka = ka_direction_candidate_matrix()
    gates = []
    for matrix in (ro, ka):
        rows = [
            {"reference": row["reference"], "state": row["state"],
             "missing_requirements": list(row["missing_requirements"]),
             "criteria": dict(row["criteria"])}
            for row in matrix["rows"]
        ]
        gates.append({
            "protocol": matrix["protocol"],
            "gate_state": matrix["gate_state"],
            "passing_candidates": list(matrix["passing_candidates"]),
            "candidates": rows,
            "next_required_evidence": matrix["next_required_evidence"],
        })
    return {
        "schema": "IberOS-Prospective-Gate-Audit/1.0",
        "authority": dict(AUTHORITY), "gates": gates,
        "new_external_evidence_checked": False,
        "automatic_core_promotion": False,
    }
