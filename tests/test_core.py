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
