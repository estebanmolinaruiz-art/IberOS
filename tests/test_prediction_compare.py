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

def test_hash_locked_prediction_is_still_not_validated():
    from hashlib import sha256
    text="ROK direction predicts an independently identified recipient"
    pred={**P,"statement":text,"statement_sha256":sha256(text.encode()).hexdigest(),
          "timestamp_evidence_url":"https://example.org/lock"}
    report=compare_prediction(pred,F,{"verdict":"SUPPORTS","independence":True,
        "contamination_free":True,"evidence_note":"Candidate external match"})
    assert report["prediction_hash_matches_text"] is True
    assert report["documentary_priority_candidate"] is True
    assert report["timestamp_evidence_checked_independently"] is False
    assert report["strict_prospective_pass"] is False

def test_tampered_prediction_hash_rejected_as_priority_evidence():
    pred={**P,"statement":"changed","statement_sha256":"0"*64,
          "timestamp_evidence_url":"https://example.org/lock"}
    report=compare_prediction(pred,F,{"verdict":"SUPPORTS","independence":True,
        "contamination_free":True,"evidence_note":"Hash not equal"})
    assert report["prediction_hash_matches_text"] is False
    assert report["documentary_priority_candidate"] is False

def test_http_source_is_rejected():
    with pytest.raises(ValueError):
        compare_prediction({**P,"source_url":"http://example.org/p"},
            F,{"verdict":"UNCLEAR","evidence_note":"Source invalid"})
