import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("v01_adversarial",ROOT/"scripts/validation01_blind_score.py")
v01=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v01)

def row(group="g1"):
    return {
        "object_id":group,"physical_group":group,"split":"HOLD",
        "source_url":"https://example.org/object/"+group,"reading_reviewed":"YES",
        "prediction_locked_at":"2026-10-19T08:00:00Z",
        "gold_reviewed_at":"2026-10-19T09:00:00Z",
        "gold_label":"1","iberos_prediction":"1","baseline_prediction":"0",
        "predictions_frozen_sha256":"a"*64,
        "gold_independent_reviewer":"independent"
    }

def test_distinct_groups_can_reach_descriptive_only():
    result=v01.audit([row("g1"),row("g2")],minimum=2)
    assert result["gate"]=="DESCRIPTIVE_SCORING_ONLY"
    assert result["superiority"]=="NOT_CONFIRMED"

def test_duplicate_hold_group_rejected_even_with_enough_distinct_groups():
    result=v01.audit([row("g1"),row("g1"),row("g2")],minimum=2)
    assert result["gate"]=="BLOCKED"
    assert any(problem[1]=="DUPLICATE_PHYSICAL_GROUP_IN_SPLIT" for problem in result["problems"])

def test_invalid_non_iso_date_rejected():
    r=row()
    r["prediction_locked_at"]="yesterday"
    result=v01.audit([r],minimum=1)
    assert result["gate"]=="BLOCKED"
    assert any(problem[1]=="INVALID_LOCK_OR_GOLD_TIMESTAMP" for problem in result["problems"])

def test_invalid_commitment_format_rejected():
    r=row()
    r["predictions_frozen_sha256"]="not-a-real-sha"
    result=v01.audit([r],minimum=1)
    assert result["gate"]=="BLOCKED"
    assert any(problem[1]=="NO_PREDICTION_COMMITMENT" for problem in result["problems"])

def test_aware_timestamp_order_not_lexicographic():
    r=row()
    r["prediction_locked_at"]="2026-10-19T11:00:00+02:00"
    r["gold_reviewed_at"]="2026-10-19T08:30:00Z"
    result=v01.audit([r],minimum=1)
    assert result["gate"]=="BLOCKED"
    assert any(problem[1]=="NOT_PROSPECTIVELY_LOCKED" for problem in result["problems"])
