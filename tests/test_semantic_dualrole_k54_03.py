from iberos.semantic_dualrole_k54_03 import audit, RIVALS

def test_two_physical_supports_but_one_formula_type():
    x=audit()
    assert x["published_physical_objects"]==2
    assert x["independent_formula_types"]==1
    assert all(obj["paired_stamps"] for obj in x["objects"])

def test_latin_roles_distinct():
    x=audit()
    assert x["latin_role_count"]==2
    assert {r["externally_attested_role"] for r in x["latin_externally_supported_roles"]}=={
        "servus_of_Lucius_Atilius","master_in_genitive"}

def test_iberian_role_alignment_not_assumed_gold():
    x=audit()
    assert x["hard_gold_iberian_roles"]==0
    assert not x["abiner_means_servus_confirmed"]
    assert not x["iberian_roles_external_confirmed"]
    assert not x["roles_from_iberian_independently_scored"]

def test_retains_abiner_ambiguous_and_null():
    models={x["model"] for x in RIVALS}
    assert models=={"H1_ABINER_SERVUS","H2_ABINER_PERSONAL_NAME",
                    "H3_PRAGMATIC_NOT_LITERAL_EQUIVALENCE"}

def test_same_texts_are_not_two_independent_successes():
    x=audit()
    assert x["historical_bilingual_training_reuse"]
    assert not x["genuine_new_blind_result"]
    assert not x["new_decipherment_confirmed"]

def test_integration_non_mutating():
    x=audit()
    assert not x["full3406_accessed"]
    assert not x["official_metrics_modified"]

def test_external_isonensis_name_context_is_a_rival_control():
    x=audit()
    evidence=x["independent_onomastic_parallel"]
    assert evidence["latin_text"]=="Fulvius Abiner(icus)"
    assert evidence["attests_abiner_as_personal_name_in_latin_context"]
    assert evidence["is_same_physical_object_as_k54"] is False
    assert evidence["proves_iberian_abiner_means_personal_name"] is False
    assert x["external_context_suggests_abiner_personal_name"] is True
    assert not x["lexical_disambiguation_complete"]
