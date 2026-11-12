from iberos.metrology_discrimination_03 import compare

def test_nominal_weight_aliasing():
    x=compare()
    assert x["nominal_overlap"]["42g_is_20_times_2_1g"]
    assert x["nominal_overlap"]["420g_is_200_times_2_1g"]
    assert not x["mass_only_42_420_discriminates_models"]

def test_alternative_residuals_are_explicit():
    data={x["label"]:x for x in compare()["examples"]}
    assert data["NOMINAL_SMALL"]["nearest_integer_multiple"]==20
    assert data["NOMINAL_LARGE"]["nearest_integer_multiple"]==200
    assert data["TOS_PELAT"]["nearest_integer_multiple"]==199
    assert data["TOS_PELAT"]["signed_residual_g"] == 0.1

def test_no_semantic_accuracy_inferred():
    x=compare()
    assert not x["semantic_gold_validated"]
    assert x["translations_validated"] == 0
    assert not x["scientific_metrics_changed"]
    assert not x["full3406_accessed"]
    assert all(not row["establishes_iberian_sign_meaning"] for row in x["examples"])

def test_no_fictitious_museum_measurement():
    x=compare()
    assert x["museum_status"] == "PROMISE_TO_PROVIDE_INFORMATION_NO_TECHNICAL_DATA_YET"
    assert len(x["must_have_to_unblock"]) == 6
