from iberos.rok_case_audit import audit_rok_cases

def test_rok_gate_stays_open():
    r = audit_rok_cases()
    assert r["gate_state"] == "OPEN"
    assert r["passing_candidates"] == []
    assert r["automatic_core_promotion"] is False

def test_orleyl_witnesses_are_separate():
    r = audit_rok_cases()
    records = {x["reference"]: x for x in r["cases"]}
    assert "F.9.5" in records and "F.9.7" in records
    assert records["F.9.5"]["state"] == "OPEN"
    assert records["F.9.7"]["state"] == "OPEN"
    assert "recipient_role_fixed_externally" in records["F.9.5"]["missing_requirements"]
