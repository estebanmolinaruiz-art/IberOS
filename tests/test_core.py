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
