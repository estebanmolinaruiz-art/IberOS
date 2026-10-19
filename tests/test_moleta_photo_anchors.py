"""Cross-image broad anchors are not verified individual sign locations."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_moleta_broad_anchors_do_not_validate_signs():
    x=json.loads((ROOT/"data/review/moleta_photo_anchors_v1.json").read_text(encoding="utf-8"))
    assert x["status"]=="BROAD_VISUAL_ANCHORS_NOT_GLYPH_ROIS"
    for kind in ("photo","drawing"):
        w,h=x[kind+"_image_dimensions"]
        assert len(x[kind+"_regions"])==3
        for r in x[kind+"_regions"]:
            l,t,rr,b=r["rect"]
            assert 0<=l<rr<=w and 0<=t<b<=h
    assert not x["cross_image_landmarks_verified"]
    assert len(x["unresolved_editorial_regions"])==5
    assert all(r["photo_sign_rect"] is None and r["drawing_sign_rect"] is None for r in x["unresolved_editorial_regions"])
    assert x["signs_verified"]==0 and not x["core_allowed"]
