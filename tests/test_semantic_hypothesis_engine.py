import pytest
from iberos.semantic_hypothesis_engine import suggest_semantic_domains

def test_reviewed_rok_suggests_domain_but_never_translation():
    r=suggest_semantic_domains("IBR-PLM-0002",[{"form":"ROK","reading_source":"reviewed editorial source","reading_reviewed":True}])
    assert len(r["suggestions"])==1
    assert "direction unknown" in r["suggestions"][0]["possible_domain"]
    assert r["possible_full_translation"] is None
    assert r["translation_validated"] is False

def test_unreviewed_segment_produces_no_guess():
    r=suggest_semantic_domains("IBR-PLM-0002",[{"form":"SALIR","reading_source":"editorial draft","reading_reviewed":False}])
    assert r["suggestions"]==[]

def test_bi_needs_external_quantitative_anchor():
    s={"form":"BI","reading_source":"editorial source","reading_reviewed":True}
    r=suggest_semantic_domains("IBR-PLM-0002",[s])
    assert "no numeral" in r["suggestions"][0]["possible_domain"]
    assert r["suggestions"][0]["meaning_validated"] is False

def test_unknown_reading_source_rejected():
    with pytest.raises(ValueError):
        suggest_semantic_domains("IBR-PLM-0002",[{"form":"KUTUR","reading_reviewed":True}])
