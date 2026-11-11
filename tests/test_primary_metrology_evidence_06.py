from iberos.primary_metrology_evidence_06 import SPECIMENS, audit, Specimen
import pytest


def test_published_mass_not_instrument_uncertainty():
    data=audit()
    assert data["published_mass_count"]==2
    assert data["instrumental_uncertainty_verified"]==0
    assert all(x["measurement_uncertainty_g"] is None for x in data["items"])
    assert all(not x["verified_metrology"] for x in data["items"])


def test_photo_and_author_autopsy_not_independent_gold():
    data=audit()
    assert data["independent_mark_readings"]==0
    assert all(not x["eligible_for_blind_semantic_test"] for x in data["items"])
    assert all(x["reading_credibility"]=="AUTHOR_PUBLICATION_ONLY" for x in data["items"])


def test_historical_inventory_and_reweigh_not_conflated():
    data=audit()
    a,b=data["items"]
    assert a["museum_inventory"].startswith("2309 ")
    assert a["published_mass_g"]==41.29
    assert b["published_mass_g"]==423.78
    assert b["museum_inventory"] is None
    assert "Iron ring" in b["conservation_note"]


def test_no_full3406_or_metrics():
    data=audit()
    assert not data["historical_full3406_accessed"]
    assert not data["metrics_modified"]
    assert data["test_samples_qualified"]==0


def test_bad_uncertainty_fails():
    from dataclasses import replace
    with pytest.raises(ValueError,match="INVALID_UNCERTAINTY"):
        audit((replace(SPECIMENS[0], measurement_uncertainty_g=-0.01),))
