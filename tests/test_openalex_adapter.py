from iberos.openalex_adapter import normalize_openalex_works, sync_openalex
import iberos.openalex_adapter as adapter
import json

def test_openalex_mapping_uses_only_bibliographic_metadata():
    payload={"results":[{"display_name":"An Iberian inscription","doi":"https://doi.org/10.1234/example","publication_date":"2026-01-02"},{"display_name":"No link"}]}
    out=normalize_openalex_works(payload)
    assert len(out)==1
    assert out[0]["claimed_findings"]==""
    assert out[0]["modules"]==["TRACE","PALEO"]

def test_sync_persists_review_only(monkeypatch,tmp_path):
    monkeypatch.setattr(adapter,"fetch_openalex",lambda **kwargs:[{"title":"New epigraphic paper","url":"https://doi.org/10.1234/test","modules":["TRACE"]}])
    path=tmp_path/"discoveries.jsonl"
    a=sync_openalex(str(path))
    b=sync_openalex(str(path))
    assert a["new"]==1 and b["new"]==0
    record=json.loads(path.read_text().splitlines()[0])
    assert record["eligible_for_core"] is False
    assert record["automatic_core_promotion"] is False

def test_invalid_response_rejected():
    import pytest
    with pytest.raises(ValueError):
        normalize_openalex_works({"results":{}})
