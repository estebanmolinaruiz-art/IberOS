import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("masteraudit",ROOT/"scripts/validation01_master_audit.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def test_current_master_does_not_claim_independence():
    r=m.audit(m.load())
    assert r["records"]==22
    assert r["hold_eligible"]==0
    assert r["physical_independence_verified"]==0
def test_truncated_url_and_missing_source_detected():
    rows=[{"master_id":"M1","object_id":"O1","source_url":"https://example.org/foo...","physical_group":"UNRESOLVED","HOLD_eligible":"NO"},
          {"master_id":"M2","object_id":"O2","source_url":"","physical_group":"UNRESOLVED","HOLD_eligible":"NO"}]
    r=m.audit(rows)
    assert r["issue_counts"]["SOURCE_URL_UNUSABLE_OR_TRUNCATED"]==1
    assert r["issue_counts"]["SOURCE_URL_MISSING"]==1
def test_unsafe_hold_admission_blocked():
    r=m.audit([{"master_id":"M","object_id":"O","source_url":"https://example.org","physical_group":"P","HOLD_eligible":"YES"}])
    assert r["issue_counts"]["UNSUBSTANTIATED_HOLD_ADMISSION"]==1
def test_duplicate_ids_detected():
    row={"master_id":"M","object_id":"O","source_url":"https://example.org","physical_group":"P","HOLD_eligible":"NO"}
    r=m.audit([row,row])
    assert r["issue_counts"]["MISSING_OR_DUPLICATE_MASTER_ID"]==1
    assert r["issue_counts"]["MISSING_OR_DUPLICATE_OBJECT_ID"]==1
