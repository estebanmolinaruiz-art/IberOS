"""Graphical evidence intake cannot silently turn bibliography into sign validation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_graphic_evidence_first_batch_is_consistent_and_unverified():
    source=json.loads((ROOT/"data/review/graphic_intake_batch_01_v1.json").read_text(encoding="utf-8"))
    data=json.loads((ROOT/"data/review/graphic_evidence_batch_01_v1.json").read_text(encoding="utf-8"))
    assert data["record_count"]==len(data["records"])==10
    assert [x["object_id"] for x in source["records"]]==[x["object_id"] for x in data["records"]]
    assert len({x["review_id"] for x in data["records"]})==10
    for x in data["records"]:
        assert x["source_url"].startswith("https://")
        assert x["specific_figure"] is None and x["printed_page"] is None
        assert x["face"] is None and x["line"] is None and x["sign_index"] is None
        assert x["visual_evidence_status"]=="NOT_INSPECTED"
        assert x["image_reuse_rights"]=="NOT_VERIFIED"
        assert x["sign_by_sign_verified"] is False
        assert x["eligible_for_core"] is False and x["semantic_translation_validated"] is False
    assert data["signs_independently_verified"]==data["semantic_translations_validated"]==0
