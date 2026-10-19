"""Moleta enhancement is repeatable but may not auto-validate a damaged glyph."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def test_moleta_enhancement_keeps_original_provenance_and_uncertainty():
    x=json.loads((ROOT/"data/review/moleta_enhancement_experiment_v1.json").read_text(encoding="utf-8"))
    assert x["object_id"]=="IBR-PLM-0011"
    assert x["photo_embedded_pixels"]==[2125,2124]
    assert x["drawing_embedded_pixels"]==[711,956]
    assert len(x["source_photo_embedded_sha256"])==64
    assert len(x["source_drawing_embedded_sha256"])==64
    assert len(x["processing"])==5
    assert len(x["unresolved_regions"])==5
    assert x["sign_level_roi_confirmed"]==x["resolved_sign_count"]==0
    assert x["semantic_validation"] is False
    assert x["core_promotion"] is False
    assert x["rights_to_republish"] is False
