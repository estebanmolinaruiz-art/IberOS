from iberos.metrology_admission_07 import audit
import pytest


def test_empty_inventory_is_not_successful_blind_validation():
    r=audit([])
    assert r["eligible_new_blind"]==0 and r["total"]==0


def test_published_decimal_is_not_instrumental_uncertainty():
    r=audit([{"object_id":"PUIG_2309","mass_g":41.29,"reading":"o"}])
    x=r["results"][0]
    assert not x["eligible_for_new_blind_test"]
    assert "INVALID_OR_MISSING_UNCERTAINTY_G" in x["evidence_issues"]
    assert x["decision"]=="ABSTAIN_PENDING_EVIDENCE"


def test_missing_independent_readings_blocks():
    r=audit([{"object_id":"TOS_PELAT","mass_g":418.0,"resolution_g":0.01,
              "uncertainty_g":0.1,"independent_mark_readings":[{"reading":"10 points"}]}])
    assert not r["results"][0]["independent_mark_reading_verified"]


def complete():
    return {"object_id":"SYNTHETIC_ONLY","institution":"Test Museum",
      "inventory_id":"TEST-1","physical_object_identity":"unique physical identifier",
      "context_reference":"archival context","image_reference":"photo ID",
      "image_rights":"institutional permission","reading_reference":"independent sheet",
      "mass_g":42.0,"resolution_g":0.01,"uncertainty_g":0.04,
      "instrument_id":"balance-1","calibration_reference":"record-1",
      "measurement_date":"2026-11-11","conservation_assessment":"intact",
      "independent_mark_readings":[
        {"reading":"o","reader_id":"blind-A","reading_date":"2026-11-11","blind_to_weight_and_model":True},
        {"reading":"o","reader_id":"blind-B","reading_date":"2026-11-11","blind_to_weight_and_model":True}],
      "historical_aliases_checked":True,
      "independent_object_from_full3406":True,
      "predictions_registered_before_reading":True,
      "not_previously_published_or_seen":True,
      "negative_controls_registered":True}


def test_synthetic_complete_record_is_eligible_not_translation():
    r=audit([complete()])
    assert r["eligible_new_blind"]==1
    assert r["results"][0]["automatic_semantic_translation"] is None
    assert not r["scientific_metrics_changed"]


def test_published_object_must_not_be_called_new_even_with_full_metadata():
    a=complete()
    a["not_previously_published_or_seen"]=False
    assert not audit([a])["results"][0]["eligible_for_new_blind_test"]


def test_independent_disagreement_blocks():
    a=complete()
    a["independent_mark_readings"][1]["reading"]="n"
    x=audit([a])["results"][0]
    assert "DISAGREEMENT_BETWEEN_BLIND_READINGS" in x["evidence_issues"]
    assert not x["eligible_for_new_blind_test"]


def test_corrupted_positive_values_fails():
    a=complete()
    for bad in (float("nan"),0,-2,True):
        a["uncertainty_g"]=bad
        assert not audit([a])["results"][0]["mass_primary_verified"]


def test_duplicate_id_fails_closed():
    with pytest.raises(ValueError, match="DUPLICATE"):
        audit([complete(),complete()])
