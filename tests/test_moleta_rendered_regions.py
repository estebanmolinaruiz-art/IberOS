"""Coarse photo/drawing panel crops are reproducible but do not validate individual glyphs."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def test_moleta_rendered_regions_are_bounded_and_scientifically_pending():
    data=json.loads((ROOT/"data/review/moleta_rendered_regions_v1.json").read_text(encoding="utf-8"))
    assert data["object_id"]=="IBR-PLM-0011"
    assert len(data["regions"])==2
    for r in data["regions"]:
        w,h=r["rendered_page_dimensions"]
        x0,y0,x1,y1=r["bounds_px"]
        assert 0<=x0<x1<=w and 0<=y0<y1<=h
        assert [x1-x0,y1-y0]==r["crop_dimensions_px"]
        assert r["per_sign_alignment"] is False
    assert data["sign_roi_count"]==0
    assert data["independently_verified_sign_count"]==0
    assert not data["published_image_rights_verified"]
    assert not data["semantic_translation_validated"]
