"""Scientific guardrails for WORK-01/02/03; examples are not semantic gold."""
import copy
import json
from pathlib import Path

import pytest

from iberos.prediction_translation_work import build_docket

PILOT = (Path(__file__).resolve().parents[1] /
         "data/review/prediction_translation_pilot_v1.json")


def sample():
    return json.loads(PILOT.read_text(encoding="utf-8"))


def test_three_competing_possible_translations_not_truth():
    out = build_docket(sample())
    assert out["historical_cases"] == 1
    assert out["independent_physical_objects_represented"] == 1
    assert out["rival_hypotheses"] == 3
    assert out["semantically_evaluated_predictions"] == 0
    assert out["translation_accuracy"] is None
    assert out["preregistration_verified"] is False
    assert out["translation_validated"] is False
    assert out["automatic_core_promotion"] is False
    assert all(
        rival["evaluation_state"] == "NOT_EVALUATED"
        and rival["epistemic_layer"] == "HYPOTHESIS"
        and rival["semantic_gold"] is None
        and rival["estimated_probability"] is None
        and rival["prediction_lock_state"] == "NOT_PROSPECTIVELY_LOCKED"
        for case in out["cases"] for rival in case["hypotheses"]
    )


def test_hashes_are_stable_content_identifiers_only():
    first, second = build_docket(sample()), build_docket(sample())
    a = [x["statement_sha256"] for x in first["cases"][0]["hypotheses"]]
    b = [x["statement_sha256"] for x in second["cases"][0]["hypotheses"]]
    assert a == b and len(set(a)) == 3 and all(len(h) == 64 for h in a)
    assert first["preregistration_verified"] is False


@pytest.mark.parametrize("field,value", [
    ("evaluation_role", "HOLD"),
    ("evaluation_role", "VAL"),
    ("independent_semantic_gold", True),
    ("independent_semantic_gold", None),
    ("translation_validated", True),
    ("reading_level", "UNKNOWN"),
    ("reading_source_url", "http://example.com/reading"),
])
def test_unverified_or_contaminating_inputs_fail_closed(field, value):
    doc = sample()
    doc["cases"][0][field] = value
    with pytest.raises(ValueError):
        build_docket(doc)


def test_reject_duplicate_hypotheses_and_undefined_predications():
    doc = sample()
    doc["cases"][0]["hypotheses"][1]["hypothesis_id"] = "H-MAKER"
    with pytest.raises(ValueError):
        build_docket(doc)
    doc = sample()
    doc["cases"][0]["hypotheses"][1]["falsifiable_prediction"] = ""
    with pytest.raises(ValueError):
        build_docket(doc)


def test_no_double_count_of_same_physical_object():
    doc = sample()
    duplicate = copy.deepcopy(doc["cases"][0])
    duplicate["case_id"] = "SCI-PRED-01-SECOND_EDITORIAL_WITNESS"
    doc["cases"].append(duplicate)
    out = build_docket(doc)
    assert out["historical_cases"] == 2
    assert out["independent_physical_objects_represented"] == 1


def test_integration_keeps_external_gold_zero():
    from scripts.run_prediction_translation_works import audit
    out = audit(sample())
    assert out["scientific_verdict"] == "NOT_EVALUATED"
    assert out["translation_validated"] is False
    assert out["existing_controls"]["hold01_semantic_gold_available"] == 0
    assert out["existing_controls"]["serreta_semantic_validation"] == "NOT_PERFORMED"
    assert len(out["works"]) == 3
