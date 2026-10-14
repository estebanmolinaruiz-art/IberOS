from iberos.bi_salir_audit import audit_bi_salir

def test_salir_prospective_gate_stays_open():
    r=audit_bi_salir()
    assert r["salir_gate_state"]=="OPEN"
    assert all(x["state"]=="OPEN" for x in r["salir_candidates"])
    assert r["automatic_core_promotion"] is False
    assert r["new_external_evidence_checked"] is False

def test_bi_discrimination_and_conflict_are_visible():
    r=audit_bi_salir()
    contexts={x["context"]:x for x in r["bi_context_tests"]}
    assert contexts["NO_EXTERNAL_ANCHOR"]["result"]["numeric_value"] is None
    assert contexts["INDEPENDENT_QUANTITATIVE_CONTEXT"]["result"]["numeric_value"]==2
    assert contexts["VERBAL_COMPLEX"]["result"]["numeric_value"] is None
    assert contexts["CONFLICTING_FLAGS"]["result"]["decision"]=="NON_NUMERAL_DEFAULT"
    assert r["bi_conflicting_flags_require_external_resolution"] is True
    assert all(x["attested_inscription_evidence"] is False for x in contexts.values())
