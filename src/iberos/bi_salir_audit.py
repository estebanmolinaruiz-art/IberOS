"""Read-only BI/BIN context discriminator and prospective SALIR gap report."""
from __future__ import annotations
from .core import AUTHORITY, evaluate_bi_context, salir_prospective_candidate_matrix

def audit_bi_salir() -> dict:
    matrix = salir_prospective_candidate_matrix()
    contexts = [
        {"context":"NO_EXTERNAL_ANCHOR","input":{"independently_quantitative":False,"verbal_complex":False}},
        {"context":"INDEPENDENT_QUANTITATIVE_CONTEXT","input":{"independently_quantitative":True,"verbal_complex":False}},
        {"context":"VERBAL_COMPLEX","input":{"independently_quantitative":False,"verbal_complex":True}},
        {"context":"CONFLICTING_FLAGS","input":{"independently_quantitative":True,"verbal_complex":True}},
    ]
    for row in contexts:
        row["result"] = evaluate_bi_context(**row["input"])
        row["attested_inscription_evidence"] = False
    return {"schema":"IberOS-BI-SALIR-Audit/1.0",
            "authority":dict(AUTHORITY),
            "bi_protocol":"BI-DISAMBIG-01",
            "bi_context_tests":contexts,
            "bi_conflicting_flags_require_external_resolution":True,
            "salir_protocol":matrix["protocol"],
            "salir_gate_state":matrix["gate_state"],
            "salir_candidates":matrix["rows"],
            "salir_next_required_evidence":matrix["next_required_evidence"],
            "salir_fail_or_degrade_trigger":matrix["fail_or_degrade_trigger"],
            "new_external_evidence_checked":False,
            "automatic_core_promotion":False}
