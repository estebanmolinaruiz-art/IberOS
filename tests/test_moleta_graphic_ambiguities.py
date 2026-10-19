"""Editorial glyph alternatives must not become independent graphic evidence."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def test_moleta_ambiguous_signs_are_source_backed_and_unresolved():
    data=json.loads((ROOT/"data/review/moleta_graphic_ambiguities_v1.json").read_text(encoding="utf-8"))
    assert data["object_id"]=="IBR-PLM-0011"
    assert [(x["figure"],x["page"]) for x in data["figures"]]==[(4,215),(5,216)]
    assert data["inspection_status"]=="SOURCE_TEXT_CHECKED_FIGURES_NOT_VISUALLY_RETRIEVED"
    assert len(data["records"])==5
    assert len({x["region"] for x in data["records"]})==5
    assert all(len(x["alternative_readings"])>=2 and not x["resolved"] for x in data["records"])
    assert data["independent_glyph_count"]==0
    assert not data["semantic_validation"] and not data["core_semantic_approval"]
