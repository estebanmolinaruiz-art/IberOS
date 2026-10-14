from iberos.rule_catalog import rule_catalog
from iberos.core import ACTIVE_PROTOCOLS, FAMILY_GATE_POLICIES, OFFICIAL_METRICS


def test_rule_catalog_has_unique_code_linked_entries():
    catalog = rule_catalog()
    ids = [entry["id"] for entry in catalog["entries"]]
    assert len(ids) == len(set(ids))
    assert catalog["counts"]["active_guards"] == len(ACTIVE_PROTOCOLS)
    assert catalog["counts"]["family_gates"] == len(FAMILY_GATE_POLICIES) + 1
    assert catalog["counts"]["documented_entries"] == len(ids)


def test_rule_catalog_never_promotes_semantics():
    catalog = rule_catalog()
    assert catalog["automatic_core_promotion"] is False
    assert catalog["counts"]["verified_translation_rules"] == 0
    assert all(entry["semantic_translation_verified"] is False for entry in catalog["entries"])


def test_catalog_does_not_change_frozen_metrics():
    assert OFFICIAL_METRICS["CORE"] == "27/45 = 60.0%"
    assert OFFICIAL_METRICS["CORE_plus_INFER"] == "28/45 = 62.2%"
