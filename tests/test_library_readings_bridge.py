import pytest
from iberos.library_readings_bridge import analyze_library_readings

BASE={"reading_id":"test-reading-1","object_id":"IBR-PLM-0002",
      "segments":[{"form":"ROK","reading_source":"Documentary edition","reading_reviewed":True}]}

def test_pending_does_not_suggest():
    result=analyze_library_readings([BASE])
    assert result["reports"][0]["suggestions"]==[]
    assert result["reports"][0]["review_gate_passed"] is False

def test_approved_reading_proposes_hypothesis_not_translation():
    rec={**BASE,"review_status":"APPROVED_READING","review_reference":"Explicit editorial decision"}
    result=analyze_library_readings([rec])
    row=result["reports"][0]
    assert len(row["suggestions"])==1
    assert row["suggestions"][0]["meaning_validated"] is False
    assert row["translation_validated"] is False

def test_unknown_object_and_duplicate_reading_rejected():
    with pytest.raises(ValueError):
        analyze_library_readings([BASE,BASE])
    with pytest.raises(ValueError):
        analyze_library_readings([{**BASE,"object_id":"NOT_CURATED"}])
