"""Local photo controls are not sign transcriptions or drawing registrations."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_moleta_local_photo_controls():
    x=json.loads((ROOT/"data/review/moleta_photo_control_windows_v1.json").read_text(encoding="utf-8"))
    assert len(x["windows"])==3
    w,h=x["photo_crop_dimensions_px"]
    for r in x["windows"]:
        x0,y0,x1,y1=r["rect_px"]
        assert 0<=x0<x1<=w and 0<=y0<y1<=h
        assert r["observable"] and r["risk"]
    assert not x["published_editorial_sign_mapping"]
    assert not x["photo_drawing_alignment_approved"]
    assert x["signs_independently_read"]==0
    assert not x["semantic_translation_validated"] and not x["reproduction_rights_verified"]
