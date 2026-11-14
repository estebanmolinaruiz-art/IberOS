from iberos.semantic_ekiar_challenge_02 import audit

def test_known_additional_examples_no_blind_claim():
    a=audit()
    assert a["additional_published_cases"]==3
    assert a["training_cases"]==4
    assert a["new_blind_predictions_confirmed"]==0

def test_positive_complete_name_only():
    r=audit()["predictions"]
    assert r[0]["id"]=="MLH_F_11_28"
    assert r[0]["decision"]=="CONTEXTUAL_ASSOCIATION_ONLY"
    assert "iltubokon" in r[0]["gloss"]

def test_fragmentary_balkar_is_not_certified_role():
    r=audit()["predictions"][1]
    assert r["formula_like"]
    assert not r["full_person_name_certified"]
    assert r["decision"]=="ABSTAIN"

def test_ekia_mi_is_not_falsely_labelled_ekiar():
    r=audit()["predictions"][2]
    assert r["uncertain_related_variant"]
    assert r["decision"]=="ABSTAIN"
    assert not r["formula_like"]

def test_negative_control_abstains():
    r=audit()["predictions"][3]
    assert r["decision"]=="ABSTAIN"
    assert r["gloss"] is None

def test_no_auto_role_splitting():
    a=audit()
    assert a["contextual_interpretations"]==1
    assert a["abstentions"]==3
    assert a["independent_external_roles_confirmed"]==0
    assert not a["claim_of_new_decipherment"]
    assert not a["full3406_accessed"]
    assert not a["official_metrics_modified"]
