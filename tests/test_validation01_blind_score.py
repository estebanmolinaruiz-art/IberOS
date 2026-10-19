import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("v01",ROOT/"scripts/validation01_blind_score.py")
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
def test_empty_real_manifest_blocked():
    import csv
    with (ROOT/"data/review/validation01_holdout_v1.csv").open() as f:rows=list(csv.DictReader(f))
    assert module.audit(rows)["gate"]=="BLOCKED"
def test_no_independence_leak():
    r={"object_id":"a","physical_group":"p1","split":"TRAIN"}
    s={**r,"split":"HOLD"}
    result=module.audit([r,s],minimum=1)
    assert result["gate"]=="BLOCKED"
    assert any(x[1]=="LEAKAGE_BETWEEN_SPLITS" for x in result["problems"])
def test_uncommitted_predicted_label_rejected():
    r={"object_id":"a","physical_group":"p1","split":"HOLD","source_url":"https://example.org",
       "reading_reviewed":"YES","prediction_locked_at":"2026-10-19T08:00:00Z",
       "gold_reviewed_at":"2026-10-19T09:00:00Z","gold_label":"1",
       "iberos_prediction":"1","baseline_prediction":"0",
       "gold_independent_reviewer":"independent"}
    assert module.audit([r],minimum=1)["gate"]=="BLOCKED"
