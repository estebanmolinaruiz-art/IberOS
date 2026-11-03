"""ADVERSARIAL-01 regression and mutation-resistant scientific guard tests."""
from dataclasses import replace

import pytest

from iberos.core import OFFICIAL_METRICS
from iberos.adversarial_01 import (
    CASES, ORLEYL_CONTEXT, controlled_decision, naive_suffix_guess, run,
)


def test_five_unique_cases_with_corrected_external_ids():
    assert [c.case_id for c in CASES] == [
        "ADV-01", "ADV-02", "ADV-03", "ADV-04", "ADV-05",
    ]
    assert len({c.phys_id for c in CASES}) == 5
    assert "F.20.3" in CASES[3].inscription
    assert "E.1.308" in CASES[2].inscription
    assert all(c.source_grade == "D1" for c in CASES)


def test_shared_context_not_mistaken_for_same_physical_object():
    result = run()
    assert CASES[0].phys_id != CASES[1].phys_id
    assert CASES[0].leak_group == CASES[1].leak_group == ORLEYL_CONTEXT
    assert result["physically_distinct_objects"] == 5
    assert result["contextual_groups"] == 4


@pytest.mark.parametrize("case", CASES, ids=lambda c: c.case_id)
def test_suffix_similarity_does_not_promote_a_grammar(case):
    candidate = controlled_decision(case)
    assert candidate["grammatical_decision"] == "ABSTAIN"
    assert candidate["automatic_semantic_promotion"] is False
    assert "NO_INDEPENDENT_SEMANTIC_GROUND_TRUTH" in candidate["reasons"]


def test_azaila_personal_name_hypothesis_stays_unconfirmed():
    c = CASES[2]
    assert naive_suffix_guess(c.transcription) == "SHARED_TIN_FAMILY"
    result = controlled_decision(c)
    assert "ONOMASTIC_ALTERNATIVE" in result["reasons"]
    assert result["grammatical_decision"] == "ABSTAIN"


def test_incomplete_pico_stays_incomplete_even_if_suffix_matches():
    c = CASES[3]
    assert c.is_partial
    assert "POSSIBLY_INCOMPLETE_SEQUENCE" in controlled_decision(c)["reasons"]


def test_unresolved_readings_remain_open_under_mutation():
    for i in (1, 4):
        c = CASES[i]
        alternative = replace(c, transcription=("biteroketine" if i == 1 else "bidudedin"))
        result = controlled_decision(alternative)
        assert result["grammatical_decision"] == "ABSTAIN"
        assert "UNRESOLVED_VARIANT_OR_SEGMENTATION" in result["reasons"]


def test_no_accuracy_without_gold_and_no_official_metric_changes():
    result = run()
    assert result["cases"] == 5
    assert result["semantic_gold_labels"] == 0
    assert result["naive_suffix_matches"] == 5
    assert result["abstentions"] == 5
    assert result["not_a_trained_classifier"] is True
    assert result["scientific_promotion"] is False
    assert result["official_metrics_changed"] is False
    assert result["official_metrics"] == OFFICIAL_METRICS
