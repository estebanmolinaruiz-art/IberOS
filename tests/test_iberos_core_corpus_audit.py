import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("core_audit",ROOT/"scripts/iberos_core_corpus_audit.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_existing_corpus_not_promoted():
    r=m.assess(m.load(ROOT/"data/review/validation01_master_physical_objects_v1.csv"))
    assert r["records"]==22
    assert r["translation_validation"]=="NOT_EVALUATED"
    assert r["issue_counts"]["NO_VERIFIED_SIGN_READING"]==22
def test_negative_control_missing_source_not_success():
    r=m.assess([{"object_id":"NEG-1","source_url":"","physical_group":"UNRESOLVED","full_sign_reading_verified":"NO","HOLD_eligible":"NO"}])
    assert "NO_SOURCE" in r["findings"][0]["issues"]
    assert r["translation_validation"]=="NOT_EVALUATED"
def test_unsafe_hold_is_flagged():
    r=m.assess([{"object_id":"NEG-2","source_url":"","physical_group":"UNRESOLVED","full_sign_reading_verified":"NO","HOLD_eligible":"YES"}])
    assert "UNSAFE_HOLD_CANDIDATE" in r["findings"][0]["issues"]
