from iberos.prediction_compare import compare_prediction
import pytest

P={"id":"P-1","source_url":"https://example.org/iberos-lock","fixed_on":"2026-09-01","preregistered":True}
F={"id":"F-1","source_url":"https://doi.org/10.1234/demo","published_on":"2026-10-01"}

def test_independent_agreement_still_not_prospective_pass():
    report=compare_prediction(P,F,{"verdict":"SUPPORTS","independence":True,"contamination_free":True,"evidence_note":"Independent comparison to be audited"})
    assert report["comparison_class"] == "EXTERNAL_CONVERGENCE"
    assert report["predates_publication"] is True
    assert report["strict_prospective_pass"] is False
    assert report["automatic_core_promotion"] is False

def test_independent_contradiction_is_not_silenced():
    report=compare_prediction(P,F,{"verdict":"CONTRADICTS","independence":True,"contamination_free":True,"evidence_note":"Different outcome"})
    assert report["comparison_class"] == "FAIL"

def test_unverified_independence_is_indeterminate():
    report=compare_prediction(P,F,{"verdict":"SUPPORTS","independence":False,"contamination_free":True,"evidence_note":"Source may be dependent"})
    assert report["comparison_class"] == "INDETERMINATE"

def test_undated_prediction_rejected():
    with pytest.raises(ValueError):
        compare_prediction({**P,"fixed_on":""},F,{"verdict":"UNCLEAR","evidence_note":"Unknown"})
