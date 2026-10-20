import json
from pathlib import Path

def test_illeta_three_texts_keep_uncertainties_and_source_face_conflict_open():
    p=Path(__file__).resolve().parents[1]/"data/review/core_6p03_illeta_sign_uncertainty_2026_10_20.json"
    d=json.loads(p.read_text(encoding="utf-8"))
    assert d["physical_witness_count"]==1
    assert len(d["text_units"])==3
    assert d["metadata_conflict"]["status"]=="RESOLVED_BY_PRIMARY_FIGURE_WITH_ABSTRACT_DISCREPANCY"
    assert "cara A" in d["metadata_conflict"]["primary_edition_description"]
    assert d["text_units"][2]["editorial_face"].startswith("A (2024 fig.6")
    assert sum(len(t["uncertainties"]) for t in d["text_units"])>=6
    assert not d["review_flags"]["photographic_independent_signs_verified"]
    assert not d["review_flags"]["automatic_core_promotion"]
