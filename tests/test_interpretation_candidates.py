import pytest
from iberos.interpretation_candidates import compare_interpretations

R={"transcription":"DOCUMENTED READING","source":"Editorial example source"}
P={"id":"H1","possible_translation":"[possible meaning]","sources":["Bibliographic reference"],"supporting_observations":["A formal parallel"],"objections":["No independent semantic anchor"]}

def test_interpretation_is_never_certified():
    result=compare_interpretations("IBR-PLM-0002",R,[P])
    assert result["candidates"][0]["epistemic_layer"]=="HYPOTHESIS"
    assert result["candidates"][0]["estimated_probability"] is None
    assert result["translation_validated"] is False
    assert result["reading_verified_independently"] is False

def test_multiple_alternatives_and_duplicate_rejected():
    result=compare_interpretations("IBR-PLM-0002",R,[P,{**P,"id":"H2","possible_translation":"[alternative]","objections":[]}])
    assert len(result["candidates"])==2
    with pytest.raises(ValueError):
        compare_interpretations("IBR-PLM-0002",R,[P,P])

def test_missing_documented_reading_or_sources_rejected():
    with pytest.raises(ValueError):
        compare_interpretations("IBR-PLM-0002",{"transcription":"TEST"},[P])
    with pytest.raises(ValueError):
        compare_interpretations("IBR-PLM-0002",R,[{**P,"sources":[]}])
