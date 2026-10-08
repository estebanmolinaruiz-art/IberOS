from pathlib import Path

from iberos import (
    engine_status,
    evaluate_bi_context,
    family_objects,
    get_object,
    load_registry,
    rhotic_search_key,
    rok_semantic_guard,
    validate_result,
    validate_rhotic_usage,
    classify_validation_event,
    independence_key,
    independence_audit,
    resolve_split,
    split_integrity_audit,
    registry_independence_audit,
    independent_evidence_summary,
    evidence_promotion_review,
    family_gate_policy,
    evaluate_family_gate,
    family_gate_matrix,
    family_scientific_snapshot,
    family_dashboard,
    family_bottlenecks,
    evaluate_rok_recipient_candidate,
    rok_recipient_candidate_matrix,
    evaluate_ka_direction_candidate,
    ka_direction_candidate_matrix,
    evaluate_salir_prospective_candidate,
    salir_prospective_candidate_matrix,
    evaluate_kutur_prospective_candidate,
    kutur_prospective_candidate_matrix,
    evaluate_baides_batir_role_candidate,
    baides_batir_role_matrix,
    numeral_exact_value_gate,
    numeral_789_dashboard,
    evaluate_dedi_candidate,
    dedi_orthogonal_matrix,
    evaluate_dedi_predictive_gate,
)


def test_registry_has_curated_objects():
    rows = load_registry()
    assert len(rows) == 38


def test_tivissa_present():
    row = get_object("IBR-PLM-0002")
    assert row is not None
    assert "Tivissa" in row["Nombre_objeto"]


def test_family_lookup():
    rows = family_objects("EGIAR_EKIAR")
    assert any(r["OBJECT_ID"] == "IBR-CER-0001" for r in rows)


def test_example_validates():
    ok, errors = validate_result(Path("data/examples/tivissa.json"))
    assert ok, errors


def test_authority_chain_is_frozen():
    s = engine_status()
    assert s["authority"]["semantic_release"] == "C594"
    assert s["authority"]["prospective_lock"] == "C474"
    assert s["authority"]["technical_floor"] == "C539"
    assert s["authority"]["rok_network"] == "C541"
    assert s["official_metrics"]["ICS_global"] == 70.8
    assert s["official_metrics"]["BAIDES_BATIR"] == 75


def test_bi_guard_requires_quantitative_context():
    assert evaluate_bi_context()["decision"] == "UNRESOLVED"
    q = evaluate_bi_context(independently_quantitative=True)
    assert q["decision"] == "NUMERAL_CONTEXT_SUPPORTED"
    assert q["numeric_value"] == 2
    v = evaluate_bi_context(independently_quantitative=True, verbal_complex=True)
    assert v["decision"] == "NON_NUMERAL_DEFAULT"
    assert v["numeric_value"] is None


def test_rhotic_neutralization_is_search_only():
    assert rhotic_search_key("R1-O-KA") == "R-O-KA"
    assert validate_rhotic_usage(purpose="SEARCH", neutralized=True)["allowed"] is True
    assert validate_rhotic_usage(purpose="LEAK_GROUP", neutralized=True)["allowed"] is False
    assert validate_rhotic_usage(purpose="INDEPENDENCE", neutralized=True)["allowed"] is False


def test_rok_literal_direction_remains_open():
    assert rok_semantic_guard()["status"] == "VALIDATED_FUNCTIONAL_DOMAIN"
    assert rok_semantic_guard("give")["status"] == "PROBABLE_OPEN"
    assert rok_semantic_guard("receive")["status"] == "PROBABLE_OPEN"
    assert rok_semantic_guard("pay")["status"] == "UNSUPPORTED_LITERAL"



def test_validation_event_gate_never_auto_promotes_core():
    p = classify_validation_event(
        gate_passed=True,
        prospective=True,
        preregistered=True,
        independent=True,
        contamination_free=True,
    )
    assert p["classification"] == "STRICT_PROSPECTIVE_PASS"
    assert p["automatic_core_promotion"] is False

    e = classify_validation_event(
        gate_passed=True,
        external_source=True,
        independent=True,
        contamination_free=True,
    )
    assert e["classification"] == "EXTERNAL_CONVERGENCE"

    r = classify_validation_event(
        gate_passed=True,
        independent=True,
        contamination_free=True,
    )
    assert r["classification"] == "RETROSPECTIVE_REPLICATION"

    f = classify_validation_event(gate_passed=False)
    assert f["classification"] == "FAIL"

    u = classify_validation_event(gate_passed=None)
    assert u["classification"] == "INDETERMINATE"



def test_phys_id_dominates_documentary_independence():
    records = [
        {"ENTRY_ID": "casino-A", "OBJECT_ID": "OBJ-A", "PHYS_ID": "CASINOS-LEAD", "split": "TRAIN"},
        {"ENTRY_ID": "casino-B", "OBJECT_ID": "OBJ-B", "PHYS_ID": "CASINOS-LEAD", "split": "HOLD"},
    ]
    assert independence_key(records[0]) == "PHYS:CASINOS-LEAD"
    audit = independence_audit(records)
    assert audit["input_records"] == 2
    assert audit["independent_units"] == 1
    assert audit["collapsed_record_count"] == 1

    split = split_integrity_audit(records)
    assert split["conflict_count"] == 1
    assert split["conflicts"][0]["resolved_split"] == "HOLD"


def test_leak_group_collapses_editions_but_generic_dependency_label_does_not():
    same_object = [
        {"ENTRY_ID": "edition-1", "OBJECT_ID": "OBJ-1", "LEAK_GROUP": "LG-X"},
        {"ENTRY_ID": "edition-2", "OBJECT_ID": "OBJ-2", "LEAK_GROUP": "LG-X"},
    ]
    assert independence_audit(same_object)["independent_units"] == 1

    generic = [
        {"OBJECT_ID": "CTL-1", "Dependency_Group": "DEPENDENT_COPY"},
        {"OBJECT_ID": "CTL-2", "Dependency_Group": "DEPENDENT_COPY"},
    ]
    assert independence_audit(generic)["independent_units"] == 2


def test_specific_dependency_group_can_define_shared_unit():
    records = [
        {"OBJECT_ID": "A", "Dependency_Group": "SAME_OBJECT_SET"},
        {"OBJECT_ID": "B", "Dependency_Group": "SAME_OBJECT_SET"},
    ]
    assert independence_audit(records)["independent_units"] == 1


def test_split_precedence_is_hold_over_val_over_train():
    assert resolve_split(["TRAIN", "VAL"])["resolved_split"] == "VAL"
    assert resolve_split(["TRAIN", "HOLD", "VAL"])["resolved_split"] == "HOLD"


def test_curated_registry_has_no_accidental_mass_collapse():
    audit = registry_independence_audit()
    assert audit["input_records"] == 38
    assert audit["independent_units"] >= 35



def test_evidence_counts_by_independent_unit_not_rows():
    records = [
        {"ENTRY_ID": "A1", "PHYS_ID": "P1", "level": "E4", "evidence_class": "CONTEXT"},
        {"ENTRY_ID": "A2", "PHYS_ID": "P1", "level": "E5", "evidence_class": "CONTEXT"},
        {"ENTRY_ID": "B1", "PHYS_ID": "P2", "level": "E4", "evidence_class": "METROLOGY"},
    ]
    s = independent_evidence_summary(records)
    assert s["raw_records"] == 3
    assert s["independent_units"] == 2
    assert s["independent_level_counts"]["E5"] == 1
    assert s["independent_level_counts"]["E4"] == 1


def test_promotion_review_is_blocked_by_duplicate_object():
    duplicated = [
        {"ENTRY_ID": "A1", "PHYS_ID": "P1", "level": "E5", "evidence_class": "METROLOGY"},
        {"ENTRY_ID": "A2", "PHYS_ID": "P1", "level": "E5", "evidence_class": "METROLOGY"},
    ]
    gate = evidence_promotion_review(
        duplicated,
        target_level="E5",
        minimum_independent_units=2,
    )
    assert gate["qualifying_independent_units"] == 1
    assert gate["review_eligible"] is False
    assert gate["automatic_core_promotion"] is False


def test_promotion_review_can_require_orthogonal_evidence_classes():
    records = [
        {"OBJECT_ID": "O1", "level": "E5", "evidence_class": "METROLOGY"},
        {"OBJECT_ID": "O2", "level": "E5", "evidence_class": "NUMISMATIC"},
    ]
    gate = evidence_promotion_review(
        records,
        target_level="E5",
        minimum_independent_units=2,
        required_evidence_classes=["METROLOGY", "NUMISMATIC"],
    )
    assert gate["review_eligible"] is True
    assert gate["automatic_core_promotion"] is False

    blocked = evidence_promotion_review(
        records,
        target_level="E5",
        minimum_independent_units=2,
        required_evidence_classes=["METROLOGY", "BILINGUAL"],
    )
    assert blocked["review_eligible"] is False
    assert blocked["missing_evidence_classes"] == ["BILINGUAL"]



def test_family_policy_aliases_and_authority():
    assert family_gate_policy("ŔOK")["family"] == "ROK"
    assert family_gate_policy("KA")["family"] == "KA_KE_KU"
    assert family_gate_policy("BAIDES")["family"] == "BAIDES_BATIR"
    assert family_gate_policy("METROLOGY")["family"] == "NUM_METRO"
    assert family_gate_policy("SALIR")["authority"]["semantic_release"] == "C594"


def test_salir_functional_gate_requires_orthogonal_classes_across_independent_units():
    records = [
        {"OBJECT_ID": "S1", "level": "E4", "evidence_class": "QUANTITATIVE"},
        {"OBJECT_ID": "S2", "level": "E4", "evidence_class": "ECONOMIC"},
    ]
    gate = evaluate_family_gate("SALIR", records, scope="functional")
    assert gate["state"] == "REVIEW_ELIGIBLE"
    assert gate["automatic_core_promotion"] is False


def test_rok_exact_gate_stays_blocked_without_prospective_pass():
    records = [
        {"OBJECT_ID": "R1", "level": "E5", "evidence_class": "STRUCTURAL"},
        {"OBJECT_ID": "R2", "level": "E5", "evidence_class": "ROLE_FIXED"},
        {"OBJECT_ID": "R3", "level": "E5", "evidence_class": "ORTHOGONAL"},
    ]
    blocked = evaluate_family_gate("ROK", records, scope="exact")
    assert blocked["state"] == "BLOCKED"
    assert blocked["prospective_gate"] == "ROK-RECIPIENT-02"

    passed = evaluate_family_gate(
        "ROK",
        records,
        scope="exact",
        strict_prospective_pass=True,
    )
    assert passed["state"] == "REVIEW_ELIGIBLE"
    assert passed["automatic_core_promotion"] is False


def test_num_metro_exact_values_need_independent_quantitative_and_orthogonal_support():
    one_object = [
        {"ENTRY_ID": "A", "PHYS_ID": "P1", "level": "E5", "evidence_class": "QUANTITATIVE"},
        {"ENTRY_ID": "B", "PHYS_ID": "P1", "level": "E5", "evidence_class": "ORTHOGONAL"},
    ]
    gate = evaluate_family_gate(
        "NUM_METRO",
        one_object,
        scope="exact",
        strict_prospective_pass=True,
    )
    assert gate["state"] == "OPEN"
    assert gate["review"]["qualifying_independent_units"] == 1


def test_family_matrix_does_not_auto_promote():
    evidence = {
        "SALIR": [
            {"OBJECT_ID": "S1", "level": "E4", "evidence_class": "QUANTITATIVE"},
            {"OBJECT_ID": "S2", "level": "E4", "evidence_class": "ECONOMIC"},
        ],
        "KUTUR": [
            {"OBJECT_ID": "K1", "level": "E4", "evidence_class": "FORMULARY"},
            {"OBJECT_ID": "K2", "level": "E4", "evidence_class": "STRUCTURAL"},
        ],
    }
    matrix = family_gate_matrix(evidence)
    assert matrix["automatic_core_promotion"] is False
    assert matrix["families"]["SALIR"]["state"] == "REVIEW_ELIGIBLE"
    assert matrix["families"]["KUTUR"]["state"] == "REVIEW_ELIGIBLE"



def test_dashboard_matches_frozen_release_metrics():
    d = family_dashboard()
    rows = {r["family"]: r for r in d["rows"]}
    assert rows["SALIR"]["state"] == "CORE"
    assert rows["SALIR"]["official_score"] == 75
    assert rows["ROK"]["official_score"] == 75
    assert rows["KA_KE_KU"]["physical_counts"]["KA_Q"] == "7/154"
    assert rows["KUTUR"]["physical_counts"]["objects"] == 9
    assert rows["BAIDES_BATIR"]["physical_counts"]["BAITES_objects"] == 9
    assert rows["NUM_METRO"]["state"] == "INFER"
    assert d["official_metrics"]["ICS_global"] == 70.8
    assert d["automatic_core_promotion"] is False


def test_snapshot_keeps_narrow_claims_blocked():
    rok = family_scientific_snapshot("ROK")
    assert "direction" in rok["blocked_statement"]
    salir = family_scientific_snapshot("SALIR")
    assert "money" in salir["blocked_statement"]
    num = family_scientific_snapshot("NUM_METRO")
    assert "TOR=9" in num["blocked_statement"]


def test_bottlenecks_start_with_release_priority():
    b = family_bottlenecks()
    assert [x["family"] for x in b[:4]] == ["ROK", "KA_KE_KU", "SALIR", "KUTUR"]
    assert b[0]["next_gate"] == "ROK-RECIPIENT-02"



def test_rok_recipient_matrix_keeps_semantic_gate_open():
    m = rok_recipient_candidate_matrix()
    assert m["gate_state"] == "OPEN"
    assert m["passing_candidates"] == []
    h = evaluate_rok_recipient_candidate("H.0.1")
    assert h["criteria"]["np_e_er_secure"] is True
    assert h["criteria"]["recipient_role_fixed_externally"] is False
    c = evaluate_rok_recipient_candidate("C.21.10")
    assert "recipient_role_fixed_externally" in c["missing_requirements"]
    assert c["automatic_core_promotion"] is False



def test_ka_direction_matrix_rejects_source_generated_validation():
    b = evaluate_ka_direction_candidate("BASTIDA-I")
    assert b["state"] == "OPEN"
    assert b["criteria"]["source_independent_of_hypothesis"] is False

    o = evaluate_ka_direction_candidate("ORLEYL-CS.21.08")
    assert o["criteria"]["new_independent_transaction"] is True
    assert o["criteria"]["flow_fixed_before_linguistic_analysis"] is False


def test_murcia_fragment_is_contextually_independent_but_linguistically_powerless():
    m = evaluate_ka_direction_candidate("MURCIA-2026-FRAGMENT")
    assert m["criteria"]["flow_fixed_before_linguistic_analysis"] is True
    assert m["criteria"]["ka_ku_opportunity"] is False
    assert m["state"] == "OPEN"


def test_ka_direction_gate_remains_open():
    matrix = ka_direction_candidate_matrix()
    assert matrix["gate_state"] == "OPEN"
    assert matrix["passing_candidates"] == []
    assert matrix["automatic_core_promotion"] is False



def test_salir_matrix_keeps_gate_open():
    matrix = salir_prospective_candidate_matrix()
    assert matrix["gate_state"] == "OPEN"
    assert matrix["passing_candidates"] == []
    assert matrix["automatic_core_promotion"] is False


def test_pech_maho_salir_is_convergent_not_prospective():
    p = evaluate_salir_prospective_candidate("PECH-MAHO-2025")
    assert p["criteria"]["salir_secure"] is True
    assert p["criteria"]["post_lock_or_genuinely_unused"] is False
    assert p["criteria"]["economic_context_fixed_independently"] is False


def test_murcia_has_context_but_no_salir():
    m = evaluate_salir_prospective_candidate("MURCIA-2026-FRAGMENT")
    assert m["criteria"]["economic_context_fixed_independently"] is True
    assert m["criteria"]["salir_secure"] is False
    assert m["state"] == "OPEN"



def test_kutur_matrix_keeps_gate_open():
    matrix = kutur_prospective_candidate_matrix()
    assert matrix["gate_state"] == "OPEN"
    assert matrix["passing_candidates"] == []
    assert matrix["automatic_core_promotion"] is False


def test_cerdanya_kutur_is_semantically_strong_but_prelock():
    c = evaluate_kutur_prospective_candidate("CERDANYA-KUTUN-KUTUR")
    assert c["criteria"]["kutu_family_secure"] is True
    assert c["criteria"]["writing_formulary_context_fixed_independently"] is True
    assert c["criteria"]["post_lock_or_genuinely_unused"] is False
    assert c["state"] == "OPEN"


def test_el_vilar_kutan_does_not_force_ritual_literal():
    e = evaluate_kutur_prospective_candidate("EL-VILAR-KUTAN-2022")
    assert e["criteria"]["kutu_family_secure"] is True
    assert e["criteria"]["writing_formulary_context_fixed_independently"] is False



def test_baides_batir_functional_opposition_core_exact_labels_open():
    m = baides_batir_role_matrix()
    assert m["functional_opposition_state"] == "CORE_PRESERVED"
    assert m["exact_role_gate_state"] == "OPEN"
    assert m["exact_role_fixed_candidates"] == []
    assert m["automatic_core_promotion"] is False


def test_castellruf_supports_internal_role_contrast_without_fixing_title():
    c = evaluate_baides_batir_role_candidate("CASTELLRUF-2025")
    assert c["functional_support"]["role_contrast_internal"] is True
    assert c["functional_support"]["supports_baides_validator"] is True
    assert c["functional_support"]["supports_batir_principal"] is True
    assert c["exact_institutional_label_fixed"] is False


def test_palamos_is_adversarial_against_unique_beneficiary():
    p = evaluate_baides_batir_role_candidate("PALAMOS-C.4.1")
    assert p["classification"] == "ADVERSARIAL_CONSTRAINT"
    assert p["exact_institutional_label_fixed"] is False



def test_numeral_789_exact_values_remain_unclosed():
    d = numeral_789_dashboard()
    assert d["closed_values"] == []
    rows = {r["lexeme"]: r for r in d["rows"]}
    assert rows["SISBI"]["candidate_value"] == 7
    assert rows["SORSE"]["candidate_value"] == 8
    assert rows["TOR"]["candidate_value"] == 9
    assert rows["SORSE"]["physical_anchor_count"] == 0
    assert rows["TOR"]["state"] == "BEST_CURRENT_VALUE_NOT_CLOSED"


def test_sorse_c18_failure_is_preserved():
    s = numeral_exact_value_gate("SORSE")
    assert "C.1.8" in s["known_blocker"]
    assert s["automatic_core_promotion"] is False


def test_tor_requires_specific_value_discriminator():
    t = numeral_exact_value_gate("TOR")
    assert t["next_gate"] == "TOR-COMP-PHYS-01"
    assert "9" in t["pass_rule"]



def test_dedi_matrix_preserves_formal_core_but_exact_feature_open():
    m = dedi_orthogonal_matrix()
    assert m["formal_state"] == "CORE_MORPHOLOGICAL_COMPLEX"
    assert m["official_score"] == 50
    assert m["exact_feature_state"] == "OPEN"
    assert m["passing_candidates"] == []
    assert m["automatic_core_promotion"] is False


def test_np_de_egiar_is_constraint_not_exact_solution():
    d = evaluate_dedi_candidate("NP-DE-EGIAR")
    assert d["criteria"]["external_variable_fixed"] is True
    assert d["criteria"]["di_branch_present"] is False
    assert d["state"] == "OPEN"


def test_pech_maho_is_formal_pair_without_external_discriminator():
    p = evaluate_dedi_candidate("PECH-MAHO-B.7.38")
    assert p["criteria"]["matched_de_di_pair"] is True
    assert p["criteria"]["external_variable_fixed"] is False
    assert p["state"] == "OPEN"


def test_rejected_shortcuts_are_encoded():
    m = dedi_orthogonal_matrix()
    assert "DE=AGENT_DI=OBJECT" in m["rejected_shortcuts"]
    assert "E_I_BY_AN" in m["rejected_shortcuts"]



def test_dedi_missing_control_is_not_observed():
    c = evaluate_dedi_candidate("NP-DI-EGIAR")
    assert c["criteria"]["observed"] is False
    assert c["criteria"]["di_branch_present"] is False
    assert c["root_relation"] == "NOT_OBSERVED"


def test_dedi_castellet_is_structural_not_identical_root():
    c = evaluate_dedi_candidate("CASTELLET-F.13.75")
    assert c["root_relation"] == "STRUCTURAL_PARALLEL_ONLY"
    assert c["criteria"]["identical_root_verified"] is False
    assert c["state"] == "OPEN"


def test_dedi_prediction_blocks_unsupported_formal_pair():
    rows = [
        {"PHYS_ID": "A", "external_variable": "actor", "observed_branch": "E"},
        {"PHYS_ID": "B", "external_variable": "patient", "observed_branch": "I"},
    ]
    g = evaluate_dedi_predictive_gate(
        rows, preregistered_rule={"actor": "E", "patient": "I"}
    )
    assert g["state"] == "BLOCKED"
    assert "external_source_documented" in g["rows"][0]["missing_requirements"]


def test_dedi_prediction_rejects_duplicate_phys_id():
    common = {
        "external_source_id": "test-only", "external_fixed_before_reading": True,
        "source_independent_of_hypothesis": True,
        "held_out_before_prediction": True,
        "root_identity_verified": True, "segmentation_verified": True,
    }
    rows = [
        {**common, "PHYS_ID": "A", "external_variable": "actor", "observed_branch": "E"},
        {**common, "PHYS_ID": "A", "external_variable": "patient", "observed_branch": "I"},
    ]
    g = evaluate_dedi_predictive_gate(
        rows, preregistered_rule={"actor": "E", "patient": "I"}
    )
    assert g["state"] == "BLOCKED"
    assert "independent_physical_unit" in g["rows"][1]["missing_requirements"]


def test_dedi_prediction_synthetic_positive_is_review_only():
    common = {
        "external_source_id": "synthetic-test-only",
        "external_fixed_before_reading": True,
        "source_independent_of_hypothesis": True,
        "held_out_before_prediction": True,
        "root_identity_verified": True, "segmentation_verified": True,
    }
    rows = [
        {**common, "PHYS_ID": "SYN-1", "external_variable": "actor", "observed_branch": "E"},
        {**common, "PHYS_ID": "SYN-2", "external_variable": "patient", "observed_branch": "I"},
    ]
    g = evaluate_dedi_predictive_gate(
        rows, preregistered_rule={"actor": "E", "patient": "I"}
    )
    assert g["state"] == "REVIEW_ELIGIBLE"
    assert g["automatic_core_promotion"] is False


def test_dedi_prediction_requires_both_branches_and_valid_rule():
    g = evaluate_dedi_predictive_gate(
        [{"PHYS_ID": "A", "observed_branch": "E", "external_variable": "actor"}],
        preregistered_rule={"actor": "E"},
    )
    assert g["state"] == "BLOCKED"
    assert g["preregistered_rule_valid"] is False
