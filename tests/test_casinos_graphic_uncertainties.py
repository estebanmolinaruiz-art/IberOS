"""Casinos image-review evidence must never auto-promote editorial variants."""
import json
from pathlib import Path

DATA=Path(__file__).resolve().parents[1]/"data/review/casinos_graphic_uncertainties_v1.json"

def test_casinos_uncertainties_are_explicitly_gated():
    report=json.loads(DATA.read_text(encoding="utf-8"))
    rows=report["records"]
    assert len(rows)==report["record_count"]==5
    assert {x["region"] for x in rows}=={"A1","A3","B1","B2","B3"}
    assert len({x["evidence_id"] for x in rows})==5
    assert all(x["source"] and x["editorial_alternatives"] and x["damage"] for x in rows)
    assert all(x["visual_inspection"]=="REPRODUCTION_INSPECTED" for x in rows)
    assert all(x["review_status"]=="PENDING_GRAPHIC_REVIEW" and not x["sign_by_sign_verified"] for x in rows)
    assert all(x["independent_reviewer"] is None and not x["core_execution_allowed"] and not x["meaning_validated"] for x in rows)
    assert not report["automatic_core_promotion"] and not report["translation_validated"]

def test_all_fiches_report_includes_five_unapproved_graphic_regions():
    import subprocess, sys
    root=Path(__file__).resolve().parents[1]
    subprocess.run([sys.executable,str(root/"scripts/compare_all_fiches_reports.py"),"--reviewed-readings",str(root/"data/review/editorial_readings_pending_v1.jsonl")],cwd=root,check=True)
    report=json.loads((root/"site/data/all_fiches_report_comparison_v1.json").read_text(encoding="utf-8"))
    assert report["graphic_uncertainty_count"]==9
    casinos=next(x for x in report["records"] if x["object_id"]=="IBR-PLM-0007")
    assert casinos["graphic_uncertainty_count"]==5
    assert {x["region"] for x in casinos["graphic_uncertainties"]}=={"A1","A3","B1","B2","B3"}
    assert all(not x["sign_by_sign_verified"] for x in casinos["graphic_uncertainties"])
    assert all(len(x["requirements_before_core"])==4 for x in casinos["graphic_uncertainties"])
    assert set(report["objects_with_graphic_uncertainty"])=={"IBR-PLM-0007","IBR-LAP-0005","IBR-MUS-0001"}
    assert casinos["core_execution"]=="BLOCKED_MISSING_APPROVED_READING"
    assert report["core_executed_count"]==0

def test_sagunto_caminreal_uncertainties_are_blocked():
    x=json.loads((DATA.parent/"sagunto_caminreal_graphic_uncertainties_v1.json").read_text(encoding="utf-8"))
    assert x["record_count"]==4
    assert {r["object_id"] for r in x["records"]}=={"IBR-LAP-0005","IBR-MUS-0001"}
    assert all(not r["sign_by_sign_verified"] and not r["core_execution_allowed"] for r in x["records"])
