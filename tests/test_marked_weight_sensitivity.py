"""SCI-MET-04 fixtures use only cited real objects, never synthetic gold."""
import copy
import json
from pathlib import Path
import pytest
from iberos.marked_weight_sensitivity import evaluate

DATA=Path(__file__).resolve().parents[1]/"data/review/sci_met04_bastida_dot_mark_cases_v1.json"

def source():
    return json.loads(DATA.read_text(encoding="utf-8"))

def test_two_reported_dots_conflict_but_hypothetical_third_dot_would_fit():
    r=evaluate(source())
    assert 20.6<r["calibration_quantum_g"]<20.7
    a,b=r["alternative_mark_count_scenarios"]
    assert a["assumed_mark_count"]==2
    assert a["absolute_relative_error_pct"]>50
    assert not a["within_descriptive_10pct_band"]
    assert b["assumed_mark_count"]==3
    assert b["absolute_relative_error_pct"]<3
    assert b["within_descriptive_10pct_band"]
    assert b["assumption_photographically_verified"] is False
    assert r["number_of_marks_verified_from_original_image"] is False
    assert r["blind_test"] is False
    assert r["confirmed_iberian_sign_values"]==0
    assert r["confirmed_translations"]==0

def test_mass_or_edition_identity_cannot_be_silently_changed():
    d=source()
    d["preidentified_contradiction"]["reported_dot_count"]=3
    with pytest.raises(ValueError,match="Two-vs-three"):
        evaluate(d)
    d=source()
    d["calibration_objects"][1]["id"]="another object"
    with pytest.raises(ValueError,match="identities"):
        evaluate(d)
    d=source()
    d["preidentified_contradiction"]["visual_image_adjudicated"]=True
    with pytest.raises(ValueError,match="unverified"):
        evaluate(d)
