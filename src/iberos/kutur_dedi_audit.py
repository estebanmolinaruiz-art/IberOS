"""Non-promoting KUTUR prospective and D(E/I) formal-validation audit."""
from __future__ import annotations
from .core import AUTHORITY, kutur_prospective_candidate_matrix, dedi_combined_gate

def audit_kutur_dedi() -> dict:
    kutur = kutur_prospective_candidate_matrix()
    # No epigraphic records or preregistration are manufactured here.
    dedi = dedi_combined_gate([])
    return {
        "schema": "IberOS-KUTUR-DEDI-Audit/1.0",
        "authority": dict(AUTHORITY),
        "kutur": {
            "protocol": kutur["protocol"], "gate_state": kutur["gate_state"],
            "candidates": kutur["rows"], "passing_candidates": kutur["passing_candidates"],
            "next_required_evidence": kutur["next_required_evidence"],
            "fail_or_degrade_trigger": kutur["fail_or_degrade_trigger"],
        },
        "dedi": {
            "protocol": dedi["protocol"], "state": dedi["state"],
            "predictive_state": dedi["predictive_state"],
            "documentary_state": dedi["documentary_state"],
            "scientific_state": dedi["scientific_state"],
            "new_observations_supplied": 0,
        },
        "new_external_evidence_checked": False,
        "automatic_core_promotion": False,
    }
