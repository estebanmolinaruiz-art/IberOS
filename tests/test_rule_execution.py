import pytest
from iberos.rule_execution import execute_rules

def test_bi_unknown_context_blocks():
    r=execute_rules({"source_reference":"Example editorial source","rules":["BI-DISAMBIG-01"]})
    assert r["results"][0]["status"]=="BLOCKED"
    assert r["automatic_core_promotion"] is False

def test_bi_quantitative_requires_external_citation():
    base={"source_reference":"Example","rules":["BI-DISAMBIG-01"],
          "independently_quantitative":True,"verbal_complex":False}
    assert execute_rules(base)["results"][0]["status"]=="BLOCKED"
    res=execute_rules({**base,"quantitative_source_reference":"DOI/example"})
    assert res["results"][0]["rule_result"]["numeric_value"]==2
    assert res["scientific_state"]=="UNVERIFIED"

def test_rok_literal_stays_open():
    res=execute_rules({"source_reference":"Example","rules":["ROK-DIRECTION-GUARD-01"],"rok_literal":"give"})
    assert res["results"][0]["rule_result"]["status"]=="PROBABLE_OPEN"
    assert res["automatic_core_promotion"] is False

def test_unsupported_rule_fails():
    with pytest.raises(ValueError):
        execute_rules({"source_reference":"Example","rules":["UNREGISTERED"]})
