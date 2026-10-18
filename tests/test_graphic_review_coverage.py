"""Graphic evidence coverage is explicit and never semantic approval."""
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from export_graphic_review_coverage import generate

def test_corpus_graphic_coverage_all_38_objects():
    report=generate()
    assert report["object_count"]==38
    assert len(report["records"])==38
    assert report["objects_with_structured_graphic_observations"]==3
    assert report["graphic_observation_count"]==9
    assert sum(x["graphic_observation_count"] for x in report["records"])==9
    assert all(x["independently_verified_sign_count"]==0 for x in report["records"])
    assert all(not x["translation_validated"] and not x["core_semantic_approval"] for x in report["records"])
    assert sum(x["graphic_review_status"]=="NO_STRUCTURED_GRAPHIC_OBSERVATIONS" for x in report["records"])==35
