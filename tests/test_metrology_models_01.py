"""Checks that published numerical-model contrast is not semantic proof."""
import pytest
from iberos.metrology_models_01 import compare


def test_decimal_and_duodecimal_use_identical_anchor():
    r = compare()
    a, b = r["models"]
    assert r["unit_o_marked_g"] == 41.29
    assert a["predicted_a_g"] == 412.9
    assert b["predicted_a_g"] == 495.48
    assert a["mean_absolute_residual_g"] < b["mean_absolute_residual_g"]


def test_1930_typographical_weight_excluded():
    r = compare()
    assert r["reported_493g_weight_included"] is False
    assert "BASTIDA_493G" not in str(r["models"])


def test_no_bi_or_abar_semantics_promotion():
    r = compare()
    assert not r["semantic_gold"]
    assert not r["numeric_bi_two_validated"]
    assert not r["supports_abar_ten_validated"]
    assert not r["sampling_independent"]
    assert not r["hold_used_for_scoring"]
    assert not r["official_metrics_changed"]


def test_object_marks_not_invented():
    r = compare()
    a, b = r["models"]
    assert a["published_weights"][0]["marks_match_multiplier"]
    assert not b["published_weights"][0]["marks_match_multiplier"]
    assert all(x["marks_match_multiplier"] is None for x in a["published_weights"][1:])


def test_positive_mass_required():
    with pytest.raises(ValueError, match="INVALID_ANCHOR"):
        compare(0.0)
