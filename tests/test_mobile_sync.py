import pytest
from iberos.mobile_sync import mobile_object_payload

def test_mobile_payload_matches_web_audit_and_is_not_translation():
    from iberos.object_rule_audit import audit_object_rules
    p = mobile_object_payload("IBR-PLM-0002")
    a = audit_object_rules("IBR-PLM-0002")
    assert p["modules"] == a["modules"]
    assert p["candidate_rules"] == a["rules"]
    assert p["evaluated_rules"] == []
    assert p["automatic_core_promotion"] is False
    assert p["translation_validated"] is False

def test_explicit_sourced_rules_execute_only_for_matching_object():
    p = mobile_object_payload("IBR-PLM-0002", [{
        "object_id": "IBR-PLM-0002", "source_reference": "Test editorial record",
        "rules": ["BI-DISAMBIG-01"]}])
    assert p["evaluated_rules"][0]["results"][0]["status"] == "BLOCKED"

def test_cross_object_observation_is_refused():
    with pytest.raises(ValueError):
        mobile_object_payload("IBR-PLM-0002", [{
            "object_id":"IBR-PLM-0003","source_reference":"Bad association",
            "rules":["BI-DISAMBIG-01"]}])
