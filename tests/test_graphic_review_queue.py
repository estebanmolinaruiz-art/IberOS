"""Graphic review queue must not infer inspected images or semantic approvals."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from build_graphic_review_queue import build_queue

def test_queue_has_35_uninspected_objects():
    data=build_queue()
    assert data["total_objects"]==38
    assert data["unreviewed_queue_count"]==35
    assert data["objects_with_existing_graphic_observations"]==3
    assert len({x["object_id"] for x in data["records"]})==35
    assert all(not x["image_access_checked"] and not x["image_rights_checked"] for x in data["records"])
    assert all(not x["graphic_reading_verified"] and not x["translation_validated"] for x in data["records"])
    assert all(x["priority_basis"]=="CATALOGUE_WORKFLOW_ONLY" for x in data["records"])
