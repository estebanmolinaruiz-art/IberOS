from iberos.semantic_recipient_property_04 import audit, predict

def test_known_letter_example_predicts_recipient_but_not_gold():
    r=audit()
    assert r["calibration_cases"]==3
    assert r["positive_published_cases"]==2
    assert r["new_blind_cases"]==0
    assert not r["property_vs_recipient_lexically_disambiguated"]

def test_reused_illeta_plomb_abstains():
    r=audit()["reported_cases"][2]
    assert r["decision"]=="ABSTAIN_RECIPIENT_VS_PROPERTY"
    assert r["reading"]=="ka+belauŕ / nai"
    assert not r["role_independently_certified"]

def test_genitive_nai_alone_is_not_recipient():
    r=predict(dict(id="SYN",folded_or_rolled=True,property_marker_nai=True,
                   short_external_label=True,long_internal_message=False,
                   independent_text_reuse=False))
    assert r["decision"]=="ABSTAIN_INSUFFICIENT_PHYSICAL_CONTEXT"

def test_negative_control_ordinary_unfolded_mark():
    r=predict(dict(id="SYN",folded_or_rolled=False,short_external_label=True,
                   long_internal_message=True,independent_text_reuse=False))
    assert r["decision"].startswith("ABSTAIN")

def test_full3406_untouched_and_no_decipherment():
    r=audit()
    assert not r["official_metrics_modified"]
    assert not r["full3406_accessed"]
    assert r["external_two_role_gold"]==0
