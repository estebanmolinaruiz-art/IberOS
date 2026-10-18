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
