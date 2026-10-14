"""Read-only ROK recipient network report."""
from .core import ROK_RECIPIENT_CANDIDATES, evaluate_rok_recipient_candidate, rok_recipient_candidate_matrix, AUTHORITY

def audit_rok_cases():
    references = sorted(ROK_RECIPIENT_CANDIDATES)
    rows = [evaluate_rok_recipient_candidate(ref) for ref in references]
    matrix = rok_recipient_candidate_matrix()
    return {
        "schema": "IberOS-ROK-Audit/1.0",
        "authority": dict(AUTHORITY),
        "cases": rows,
        "gate_state": matrix["gate_state"],
        "passing_candidates": matrix["passing_candidates"],
        "automatic_core_promotion": False,
    }
