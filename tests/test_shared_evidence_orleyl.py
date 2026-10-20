"""Real-case smoke test: source-linked Orleyl evidence remains unvalidated."""
from pathlib import Path
import json
from iberos.shared_evidence import validate_evidence

ROOT=Path(__file__).resolve().parents[1]
def test_orleyl_real_source_survives_shared_contract():
    original=json.loads((ROOT/"data/review/orleyl_te_glyph_review_v1.json").read_text(encoding="utf-8"))
    candidate=original["figure25_line2_coordinate_grid_check_2026_10_20"]
    bbox=candidate["target_bbox_candidate_xyxy"]
    records=[
       {"evidence_id":"ORLEYL-EDITORIAL-1981","object_id":"ORLEYL-VIIB","source_reference":"Fletcher et al. 1981, p.110, VII-B line 2","layer":"EDITORIAL","state":"REVIEWED","pillars":["PALEO","CORPUS"]},
       {"evidence_id":"ORLEYL-FIG25-CANDIDATE","object_id":"ORLEYL-VIIB","source_reference":"Fletcher et al. 1981, fig.25, PDF p.111","layer":"GRAPHIC","state":"CANDIDATE","pillars":["PALEO","LAB"],"bbox_xyxy":bbox,"source_page":111,"dependent_on":["ORLEYL-EDITORIAL-1981"]},
       {"evidence_id":"ORLEYL-TE-HYPOTHESIS","object_id":"ORLEYL-VIIB","source_reference":"IberOS Orleyl comparison protocol, unvalidated","layer":"LINGUISTIC_HYPOTHESIS","state":"UNVERIFIED","pillars":["MORPH","VALIDATION"],"dependent_on":["ORLEYL-FIG25-CANDIDATE"]},
    ]
    result=validate_evidence(records)
    assert result["count"]==3
    assert result["records"][1]["bbox_xyxy"]==bbox
    assert result["records"][2]["dependent_on"]==["ORLEYL-FIG25-CANDIDATE"]
    assert result["automatic_core_promotion"] is False
    assert original["exact_glyph_coordinates_verified"] is False
    assert original["eligible_for_core_execution"] is False
