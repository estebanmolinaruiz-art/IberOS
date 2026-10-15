import pytest
from iberos.library_ingest import triage_library_records

def test_multiple_editions_never_create_independent_objects():
    a={"title":"Edition A","source_url":"https://example.org/a","physical_object_id":"IBR-PLM-0002"}
    b={"title":"Edition B","source_url":"https://example.org/b","physical_object_id":"IBR-PLM-0002"}
    result=triage_library_records([a,b,a])
    assert result["document_count"]==2
    assert all(x["linked_curated_object_id"]=="IBR-PLM-0002" for x in result["records"])
    assert result["new_independent_scientific_objects"]==0
    assert all(not x["ready_for_core_execution"] for x in result["records"])

def test_unknown_physical_identity_requires_review():
    result=triage_library_records([{"title":"New inscription","source_url":"https://example.org/new","independence_evidence":"Excavation note"}])
    assert result["records"][0]["route"]=="UNMATCHED_OBJECT_REVIEW"
    assert result["records"][0]["physical_independence_declared"] is True
    assert result["records"][0]["physical_independence_verified"] is False

def test_unsafe_link_rejected():
    with pytest.raises(ValueError):
        triage_library_records([{"title":"Invalid","source_url":"javascript:alert(1)"}])
