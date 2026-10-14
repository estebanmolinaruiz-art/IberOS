import pytest
from iberos.multimodule import research_pipeline, MODULES
from iberos.discovery import review_discoveries


def test_pipeline_integrates_six_modules_with_scientific_lock():
    report = research_pipeline("IBR-PLM-0002")
    assert set(report["modules"]) == set(MODULES)
    assert report["automatic_core_promotion"] is False
    assert report["modules"]["INFER"]["candidate_meaning"] is None
    assert report["modules"]["GEO"]["result"]["object_coordinates_verified"] is False


def test_unknown_object_is_rejected():
    with pytest.raises(ValueError):
        research_pipeline("NOT_A_CURATED_OBJECT")


def test_incoming_discoveries_deduplicated_and_quarantined():
    row = {"title": "New Iberian inscription", "url": "https://example.org/paper"}
    result = review_discoveries([row, row])
    assert result["count"] == 1
    assert result["items"][0]["status"] == "UNVERIFIED_INBOX"
    assert result["items"][0]["eligible_for_core"] is False


def test_discovery_requires_traceable_source():
    with pytest.raises(ValueError):
        review_discoveries([{"title": "Uncited claim", "url": ""}])
