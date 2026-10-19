"""Cited figures and editorial alternatives must remain distinct from independently verified signs."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def test_moleta_illeta_figures_and_editorial_uncertainty():
    data=json.loads((ROOT/"data/review/graphic_evidence_batch_01_v1.json").read_text(encoding="utf-8"))
    by_id={r["object_id"]:r for r in data["records"]}
    moleta=by_id["IBR-PLM-0011"]
    illeta=by_id["IBR-PLM-0012"]
    assert moleta["figure_reference_located"] and moleta["printed_page"]==215
    assert 216 in moleta["additional_printed_pages"]
    assert illeta["figure_reference_located"] and illeta["printed_page"]==256
    assert {259,260}.issubset(set(illeta["additional_printed_pages"]))
    assert illeta["editorial_reading"]=="ildurkon"
    assert "ildurbon" in illeta["alternative_readings"]
    assert moleta["visual_evidence_status"]=="NOT_INSPECTED"
    assert illeta["visual_evidence_status"]=="PUBLISHED_PHOTOS_AND_DRAWING_VISUALLY_INSPECTED_NOT_SIGN_VERIFIED"
    assert "Fig.8" in illeta["visual_comparison_note"]
    for item in (moleta,illeta):
        assert item["sign_by_sign_verified"] is False
        assert item["eligible_for_core"] is False
    assert data["signs_independently_verified"]==0
