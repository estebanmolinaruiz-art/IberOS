"""Regression controls for staged IberOS editorial readings."""
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
READINGS=ROOT/"data/review/editorial_readings_pending_v1.jsonl"
REPORT=ROOT/"site/data/all_fiches_report_comparison_v1.json"

def test_pending_readings_do_not_trigger_semantic_rules():
    rows=[json.loads(s) for s in READINGS.read_text(encoding="utf-8").splitlines() if s.strip()]
    assert {r["object_id"] for r in rows}=={"IBR-LAP-0005","IBR-MUS-0001","IBR-PLM-0007"}
    assert all(r["review_status"]=="PENDING_GRAPHIC_REVIEW" and r["review_reference"] for r in rows)
    assert all(not s["reading_reviewed"] and s["reading_source"] for r in rows for s in r["segments"])
    subprocess.run([sys.executable,str(ROOT/"scripts/compare_all_fiches_reports.py"),
                    "--reviewed-readings",str(READINGS)],cwd=ROOT,check=True)
    report=json.loads(REPORT.read_text(encoding="utf-8"))
    assert report["count"]==38 and report["cited_count"]==38
    assert report["core_executed_count"]==0 and report["scientifically_validated_translations"]==0
    for row in report["records"]:
        assert not row["independently_verified_sign_transcription"]
        assert row["core_execution"]=="BLOCKED_MISSING_APPROVED_READING"
        assert not row["semantic_domain_suggestions"]
        assert not row["translation_validated"]
