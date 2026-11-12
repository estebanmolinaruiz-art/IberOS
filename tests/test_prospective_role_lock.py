"""SCI-PRED-02 negative and positive software-only tests (no archaeological gold)."""
import copy
import json
from pathlib import Path
import pytest
from iberos.prospective_role_lock import PROTOCOL_PATH, seal


def protocol():
    return json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))


def synthetic_case():
    return {
        "blind_id": "SYNTHETIC-NOT-A-REAL-INSCRIPTION",
        "physical_id": "SYNTHETIC-PHYS-1",
        "reading_source_url": "https://example.org/synthetic",
        "context_type": "BUILDING",
        "reading_level": "D3",
        "script": "IBERIAN",
        "independence_status": "EXTERNALLY_ATTESTED",
        "participants": [
            {"person_id": "A", "name_form": "x-te",
             "name_status": "INDEPENDENTLY_IDENTIFIED"},
            {"person_id": "B", "name_form": "y",
             "name_status": "INDEPENDENTLY_IDENTIFIED"},
        ],
    }


def test_synthetic_maker_vs_commissioner_locked_distinctly():
    result = seal(synthetic_case(), protocol())
    s = result["statement"]
    assert s["marked_person_id"] == "A"
    assert s["h_maker_prediction"] == {"person_id": "A", "role": "PRODUCER"}
    assert s["h_commissioner_prediction"] == {"person_id": "A", "role": "COMMISSIONER"}
    assert s["h_null_prediction"] == "ABSTAIN"
    assert result["translation_validated"] is False
    assert result["gold_independently_verified"] is False
    assert result["semantic_gold_provided_to_predictor"] is False
    assert seal(synthetic_case(), protocol()) == result


def test_absent_or_ambiguous_te_abstains():
    c = synthetic_case()
    c["participants"][0]["name_form"] = "x"
    assert seal(c, protocol())["statement"]["marked_person_id"] is None
    c["participants"][0]["name_form"] = "x-te"
    c["participants"][1]["name_form"] = "y-te"
    assert seal(c, protocol())["statement"]["marked_person_id"] is None


@pytest.mark.parametrize("field,bad", [
    ("reading_level", "D1"),
    ("reading_level", "UNKNOWN"),
    ("script", "CELTIBERIAN"),
    ("independence_status", "SELF_DECLARED"),
    ("context_type", "UNKNOWN"),
    ("reading_source_url", "http://invalid.test/item"),
])
def test_fail_closed_for_ineligible_cases(field, bad):
    c = synthetic_case()
    c[field] = bad
    with pytest.raises(ValueError):
        seal(c, protocol())


@pytest.mark.parametrize("gold_key", ["gold", "role", "translation", "true_role",
                                       "latin", "outcome", "context_gold"])
def test_reject_gold_label_even_if_correct(gold_key):
    c = synthetic_case()
    c[gold_key] = "PRODUCER"
    with pytest.raises(ValueError):
        seal(c, protocol())
    c = synthetic_case()
    c["participants"][0][gold_key] = "PRODUCER"
    with pytest.raises(ValueError):
        seal(c, protocol())


def test_role_predictions_do_not_authorize_scientific_promotion():
    c = synthetic_case()
    c["participants"][1]["name_status"] = "EDITORIAL_UNVERIFIED"
    with pytest.raises(ValueError):
        seal(c, protocol())
    c = synthetic_case()
    c["participants"][1]["person_id"] = "A"
    with pytest.raises(ValueError):
        seal(c, protocol())
    c = synthetic_case()
    c["participants"].append(copy.deepcopy(c["participants"][1]))
    with pytest.raises(ValueError):
        seal(c, protocol())
