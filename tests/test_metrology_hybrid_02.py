from iberos.metrology_hybrid_02 import evaluate
import pytest

def test_hybrid_prediction_both_levels():
    row=evaluate()["models"][0]
    assert row["model"]=="HYBRID_10_12"
    assert row["predicted_a_g"]==412.9
    assert abs(row["predicted_ki_g"]-41.29/12)<1e-5

def test_uniform_models_are_controls():
    rows={r["model"]:r for r in evaluate()["models"]}
    assert rows["UNIFORM_10_10"]["predicted_ki_g"]==4.129
    assert rows["UNIFORM_12_12"]["predicted_a_g"]==495.48
    assert rows["HYBRID_10_12"]["two_domain_descriptive_mean_percent"] < rows["UNIFORM_10_10"]["two_domain_descriptive_mean_percent"]
    assert rows["HYBRID_10_12"]["two_domain_descriptive_mean_percent"] < rows["UNIFORM_12_12"]["two_domain_descriptive_mean_percent"]

def test_anchor_sensitivity():
    out=evaluate()
    assert len(out["anchor_sensitivity"])==3
    assert all(x["best_descriptive_model"]=="HYBRID_10_12" for x in out["anchor_sensitivity"])

def test_no_linguistic_promotion_or_hold():
    r=evaluate()
    assert not r["bi_equals_two_confirmed"]
    assert not r["abar_equals_ten_confirmed"]
    assert not r["independent_numeric_gold"]
    assert not r["hold_or_full3406_accessed"]
    assert not r["official_metrics_changed"]

def test_493g_excluded():
    r=evaluate()
    assert r["historical_493_g_excluded"]
    assert "BASTIDA_493G" not in r["selected_a_weights_g"]

def test_invalid_masses_rejected():
    with pytest.raises(ValueError):
        evaluate(0)
    with pytest.raises(ValueError):
        evaluate(41.29,0)
