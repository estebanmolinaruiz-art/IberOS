"""Scientific fail-closed regression tests for historical read-only bridge."""
import pytest
from iberos.legacy_bridge import audit_records, audit_file, EXPECTED_SHA256
from iberos.core import OFFICIAL_METRICS


def toy():
    return [
        {"uid":"one", "dependency_key_v3_4_9":"dep-a","split_v3_4_9":"TRAIN"},
        {"uid":"two", "dependency_key_v3_4_9":"dep-a","split_v3_4_9":"TRAIN"},
        {"uid":"three", "dependency_key_v3_4_9":"dep-b","split_v3_4_9":"HOLD"},
        {"uid":"four","split_v3_4_9":"EXCLUDED"},
    ]


def check(rows):
    return audit_records(rows,expected_count=4,expected_groups=2,
        expected_splits={"TRAIN":2,"HOLD":1,"EXCLUDED":1})


def test_documentary_group_vs_uid():
    result=check(toy())
    assert result["valid"]
    assert result["dependency_groups"]==2
    assert result["record_count"]==4


def test_split_leakage_rejected():
    rows=toy()
    rows[1]["split_v3_4_9"]="HOLD"
    assert "DEPENDENCY_SPLIT_LEAKAGE" in check(rows)["problems"]


def test_duplicate_uid_rejected():
    rows=toy()
    rows[1]["uid"]="one"
    assert "DUPLICATED_UID" in check(rows)["problems"]


def test_missing_active_key_rejected():
    rows=toy()
    del rows[0]["dependency_key_v3_4_9"]
    assert "MISSING_ACTIVE_DEPENDENCY_KEYS" in check(rows)["problems"]


def test_excluded_records_have_no_key():
    rows=toy()
    assert check(rows)["excluded_with_dependency_key"]==0
    rows[3]["dependency_key_v3_4_9"]="false-key"
    assert "EXCLUDED_HAS_ACTIVE_DEPENDENCY_KEY" in check(rows)["problems"]


def test_digest_guard_prevents_substitution(tmp_path):
    fake=tmp_path/"FULL3406.json"
    fake.write_text('{"records":[]}',encoding="utf-8")
    with pytest.raises(ValueError,match="SHA256_MISMATCH"):
        audit_file(fake)


def test_no_official_metric_changes():
    assert len(EXPECTED_SHA256)==64
    assert OFFICIAL_METRICS["CORE"]=="27/45 = 60.0%"
