from iberos.kutur_dedi_audit import audit_kutur_dedi

def test_kutur_remains_open_without_external_evidence():
    result = audit_kutur_dedi()
    assert result["kutur"]["gate_state"] == "OPEN"
    assert result["kutur"]["passing_candidates"] == []
    assert result["new_external_evidence_checked"] is False
    assert result["automatic_core_promotion"] is False

def test_dedi_empty_inputs_do_not_promote():
    result = audit_kutur_dedi()
    assert result["dedi"]["state"] == "BLOCKED"
    assert result["dedi"]["new_observations_supplied"] == 0
    assert result["dedi"]["scientific_state"] == "UNVERIFIED"

def test_kutur_has_explicit_falsifier_and_independence_requirement():
    result = audit_kutur_dedi()
    assert result["kutur"]["fail_or_degrade_trigger"]
    assert "independently" in result["kutur"]["next_required_evidence"]
