"""Historical controls are fixed; tests NEVER claim decipherment."""
import json
import math
from pathlib import Path

import pytest

from iberos.ponderal_model_comparison import analyse

DATA = Path(__file__).resolve().parents[1]/"data/review/sci_met03_published_weights_v1.json"


def run():
    return analyse(json.loads(DATA.read_text(encoding="utf-8")))


def test_real_five_weights_and_equivalence_are_retrospective():
    result=run()
    v=result["villanueva"]
    assert len(v["observed_masses_g"]) == 5
    assert math.isclose(v["fitted_unit21_g"],21.349640287769788,abs_tol=1e-5)
    assert v["rms_g_21_fixed"] < v["rms_g_20_525_from_aras_fixed"]
    assert v["model_42_with_half_ratios_exactly_identical_to_21"]
    assert result["scientific_result"]=="UNDERDETERMINED_MARK_SEMANTICS"
    assert result["validated_translation_count"]==0
    assert result["independent_blind_semantic_success"] is False


def test_two_triangles_do_not_prove_two_ibero_o_signs():
    result=run()
    assert result["aras"]["one_41_05_unit_if_marks_non_quantitative"] == 41.05
    assert result["aras"]["two_20_525_units_if_each_mark_additive"] == 20.525
    assert result["aras"]["image_sign_collation_completed"] is False
    assert not any(x["additive_semantics_verified"] for x in result["published_comparative_mark_controls"])


def test_altering_primary_reference_fails_closed():
    data=json.loads(DATA.read_text(encoding="utf-8"))
    data["groups"][0]["published_ratios_21g"]=[1,2,3,5,9]
    with pytest.raises(ValueError, match="altered"):
        analyse(data)


def test_invalid_mass_fails_closed():
    data=json.loads(DATA.read_text(encoding="utf-8"))
    data["groups"][0]["mass_g"][0]=float("nan")
    with pytest.raises(ValueError,match="mass"):
        analyse(data)
