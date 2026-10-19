"""Do not treat editorial readings or unaligned crops as blind glyph adjudications."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_blind_moleta_glyph_assessment_requires_two_independent_reviews():
    d=json.loads((ROOT/"data/review/moleta_blind_glyph_assessment_v1.json").read_text(encoding="utf-8"))
    a=json.loads((ROOT/"data/review/moleta_graphic_ambiguities_v1.json").read_text(encoding="utf-8"))
    assert [x["region_id"] for x in d["records"]]==[x["region"] for x in a["records"]]
    assert len(d["records"])==d["unresolved"]==5
    for row in d["records"]:
        assert row["photo_pixel_roi"] is None and row["drawing_pixel_roi"] is None
        assert not row["landmark_registration_verified"]
        assert row["observer_a"]["reviewer"] is None and row["observer_b"]["reviewer"] is None
        assert row["observer_a"]["observed_strokes"]==row["observer_b"]["observed_strokes"]==[]
        assert not row["editorial_comparison_unlocked"]
        assert row["adjudication"]=="PENDING_INDEPENDENT_OBSERVATIONS"
        assert not row["core_promotion_allowed"]
    assert d["independently_verified"]==0 and not d["semantic_validation"]
