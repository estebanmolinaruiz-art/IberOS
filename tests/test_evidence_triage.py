from iberos.evidence_triage import build_evidence_triage

def test_triage_does_not_equate_tags_with_observations():
    result=build_evidence_triage()
    assert result["schema"]=="IberOS-Evidence-Triage/1.0"
    assert result["object_count"] == len(result["tasks"])
    assert result["object_count"] > 0
    assert len({x["object_id"] for x in result["tasks"]}) == result["object_count"]
    assert all(x["eligible_for_technical_execution"] is False for x in result["tasks"])
    assert all(x["automatic_core_promotion"] is False for x in result["tasks"])
    assert all(x["source_verified_for_rule"] is False for x in result["tasks"])

def test_tivissa_rok_review_not_auto_approved():
    result=build_evidence_triage()
    row=next(x for x in result["tasks"] if x["object_id"]=="IBR-PLM-0002")
    assert "ROK-DIRECTION-GUARD-01" in row["candidate_rule_ids"]
    assert row["review_status"]=="NEEDS_EXACT_PASSAGE_AND_INDEPENDENT_CHECK"
