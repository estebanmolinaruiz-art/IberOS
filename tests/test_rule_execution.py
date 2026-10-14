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

def test_paleo_rhotic_blocks_scientific_neutralization():
    data={"source_reference":"Editorial sign record","rules":["PALEO-RHOTIC-LOCK-01"],
          "rhotic_purpose":"INDEPENDENCE","rhotic_neutralized":True}
    report=execute_rules(data)["results"][0]
    assert report["status"]=="REJECTED_BY_GUARD"
    assert report["rule_result"]["allowed"] is False

def test_paleo_rhotic_allows_search_only():
    data={"source_reference":"Editorial sign record","rules":["PALEO-RHOTIC-LOCK-01"],
          "rhotic_purpose":"SEARCH","rhotic_neutralized":True}
    assert execute_rules(data)["results"][0]["rule_result"]["allowed"] is True

def test_ka_known_candidate_remains_open():
    data={"source_reference":"Published candidate matrix","rules":["KA-DIRECTION-PROSPECTIVE-01"],
          "ka_candidate_reference":"BASTIDA-I"}
    report=execute_rules(data)
    assert report["results"][0]["status"]=="OPEN_PENDING_INDEPENDENT_DIRECTION"
    assert report["results"][0]["rule_result"]["state"]=="OPEN"
    assert report["automatic_core_promotion"] is False

def test_ka_unregistered_candidate_is_blocked():
    data={"source_reference":"Unknown example","rules":["KA-DIRECTION-PROSPECTIVE-01"],
          "ka_candidate_reference":"INVALID"}
    assert execute_rules(data)["results"][0]["status"]=="BLOCKED"
