"""Exploratory image panels must not imply matched sign positions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_moleta_exploratory_regions_are_bounded_and_unvalidated():
    x=json.loads((ROOT/"data/review/moleta_exploratory_regions_v1.json").read_text(encoding="utf-8"))
    assert x["object_id"]=="IBR-PLM-0011"
    assert len(x["regions"])==3
    for a in x["regions"]:
        for key,shape in (("photo_rect",x["rendered_photo_size"]),("drawing_rect",x["rendered_drawing_size"])):
            l,t,r,b=a[key]
            assert 0<=l<r<=shape[0] and 0<=t<b<=shape[1]
    assert x["sign_rois_mapped"]==x["graphic_decisions_made"]==0
    assert x["unresolved_glyph_regions"]==5
    assert not x["published_image_licence_verified"]
    assert not x["semantic_translation_validated"] and not x["core_promotion_allowed"]
