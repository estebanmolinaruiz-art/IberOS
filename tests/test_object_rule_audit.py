from iberos.object_rule_audit import audit_object_rules
from iberos.rule_catalog import rule_catalog
import pytest

def test_object_audit_preserves_indeterminate_scientific_status():
    result=audit_object_rules("IBR-PLM-0002")
    assert len(result["rules"])==rule_catalog()["counts"]["documented_entries"]
    assert all(r["rule_passed"] is None for r in result["rules"])
    assert all(r["semantic_translation_verified"] is False for r in result["rules"])
    assert result["automatic_core_promotion"] is False
    assert set(result["modules"])=={"GEO","PALEO","MORPH","LEXSEM","TRACE","INFER"}

def test_bad_object_rejected():
    with pytest.raises(ValueError):
        audit_object_rules("NOT_IN_CORPUS")
