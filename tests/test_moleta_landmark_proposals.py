"""Moleta silhouette landmarks are proposals, not sign registrations."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def test_landmarks_are_bounded_but_not_sign_alignments():
    d=json.loads((ROOT/"data/review/moleta_landmark_proposals_v1.json").read_text(encoding="utf-8"))
    assert d["registration_state"]=="PROPOSED_SILHOUETTE_ONLY_UNVERIFIED"
    assert len(d["landmarks"])==4
    assert len({r["label"] for r in d["landmarks"]})==4
    for r in d["landmarks"]:
        for key,size in (("photo",d["photo_crop_pixels"]),("drawing",d["drawing_crop_pixels"])):
            x,y=r[key]
            assert 0<=x<size[0] and 0<=y<size[1]
    assert d["fit_transform"] is None and d["fit_residual_px"] is None
    assert d["sign_correspondences_confirmed"]==0
    assert d["sign_level_rois"]==[]
    assert d["unresolved_signs"]==5 and d["independent_glyph_verification"]==0

def test_exploratory_affine_is_not_approved_for_glyph_registration():
    d=json.loads((ROOT/"data/review/moleta_landmark_proposals_v1.json").read_text(encoding="utf-8"))
    diagnostic=d["exploratory_affine_diagnostic"]
    assert len(diagnostic["residual_px_by_landmark"])==len(d["landmarks"])==4
    assert diagnostic["rmse_px"]>20
    assert diagnostic["maximum_residual_px"]>30
    assert "NOT approved" in diagnostic["interpretation"]
    assert d["fit_transform"] is None
    assert d["sign_correspondences_confirmed"]==0
