from iberos.prospective_gate_audit import audit_prospective_gates

def test_frozen_rok_and_ka_still_open():
    report=audit_prospective_gates()
    gates={g["protocol"]:g for g in report["gates"]}
    assert gates["ROK-RECIPIENT-02"]["gate_state"]=="OPEN"
    assert gates["KA-DIRECTION-PROSPECTIVE-01"]["gate_state"]=="OPEN"
    assert all(not g["passing_candidates"] for g in gates.values())
    assert report["automatic_core_promotion"] is False
    assert report["new_external_evidence_checked"] is False

def test_missing_external_anchors_not_omitted():
    gates={g["protocol"]:g for g in audit_prospective_gates()["gates"]}
    rok={r["reference"]:r for r in gates["ROK-RECIPIENT-02"]["candidates"]}
    assert "recipient_role_fixed_externally" in rok["F.9.7"]["missing_requirements"]
    ka={r["reference"]:r for r in gates["KA-DIRECTION-PROSPECTIVE-01"]["candidates"]}
    assert "flow_fixed_before_linguistic_analysis" in ka["BASTIDA-I"]["missing_requirements"]
