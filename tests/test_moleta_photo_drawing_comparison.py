"""The Moleta comparison is a pending evidence workflow, not five verified signs."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def test_moleta_comparison_matches_editorial_uncertainties_and_blocks_core():
    a=json.loads((ROOT/"data/review/moleta_graphic_ambiguities_v1.json").read_text(encoding="utf-8"))
    b=json.loads((ROOT/"data/review/moleta_photo_drawing_comparison_v1.json").read_text(encoding="utf-8"))
    assert a["object_id"]==b["object_id"]=="IBR-PLM-0011"
    assert b["photo"]["pdf_page_index_zero_based"]==12
    assert b["drawing"]["pdf_page_index_zero_based"]==13
    assert [x["region"] for x in a["records"]]==[x["region"] for x in b["rows"]]
    for x,y in zip(a["records"],b["rows"]):
        assert x["alternative_readings"]==y["candidate_readings"]
        assert y["photo_strokes_recorded"] is None
        assert y["drawing_strokes_recorded"] is None
        assert y["decision"]=="UNRESOLVED"
    assert b["inspection_status"]=="PHOTO_AND_DRAWING_LOCATED_NOT_VISUALLY_COMPARED"
    assert b["independently_verified_sign_count"]==0
    assert not b["semantic_translation_validated"] and not b["core_approval"]
