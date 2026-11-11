from iberos.metrology_sensitivity_05 import sensitivity


def test_all_weights_retained():
    r = sensitivity()
    assert r["objects"] == 37 and r["assemblages"] == 5
    assert all(x["within"] + x["outside"] == 37 for x in r["tolerance_sensitivity_at_2_1g"])
    assert all(x["within"] + x["outside"] == 37 for x in r["unit_sensitivity_at_5percent"])


def test_tolerance_grid_exact():
    assert [x["within"] for x in sensitivity()["tolerance_sensitivity_at_2_1g"]] == [6,10,16,22,29,32,33,35]


def test_unit_grid_exact():
    assert [x["within"] for x in sensitivity()["unit_sensitivity_at_5percent"]] == [23,24,22,17,11]


def test_no_semantic_proof_or_history_access():
    r = sensitivity()
    assert r["reference_within_5percent"] == 22
    assert r["best_grid_unit_is_not_estimated_unit"]
    assert r["post_hoc_grid_not_independent_validation"]
    assert not r["translation_or_numeric_gold_confirmed"]
    assert not r["full3406_accessed"]
    assert not r["official_metrics_modified"]
