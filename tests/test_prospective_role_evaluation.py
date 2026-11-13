"""SCI-PRED-03 scoring is deterministic, falsifiable and NEVER a semantic pass.

Entire fixture is synthetic. No real inscription, external reviewer or gold.
"""
import copy
import json

import pytest

from iberos.prospective_role_lock import PROTOCOL_PATH, seal
from iberos.prospective_role_evaluation import compare_trial, evaluate_cohort


def protocol():
    return json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))


def synthetic_pair(i=1, marker="x-te", maker_is_a=True, gold_date="2026-12-01"):
    blind_id = f"SYNTHETIC-{i}"
    physical_id = f"SYNTHETIC-OBJECT-{i}"
    c = {
        "blind_id": blind_id, "physical_id": physical_id,
        "reading_source_url": "https://example.org/synthetic/no-archaeology",
        "context_type": "BUILDING", "reading_level": "D3",
        "script": "IBERIAN", "independence_status": "EXTERNALLY_ATTESTED",
        "participants": [
            {"person_id": "A", "name_form": marker,
             "name_status": "INDEPENDENTLY_IDENTIFIED"},
            {"person_id": "B", "name_form": "y",
             "name_status": "INDEPENDENTLY_IDENTIFIED"},
        ],
    }
    roles = {"A": "PRODUCER", "B": "COMMISSIONER"} if maker_is_a else {
        "A": "COMMISSIONER", "B": "PRODUCER",
    }
    g = {
        "blind_id": blind_id, "physical_id": physical_id,
        "documentary_lineage_id": f"SYNTHETIC-PUNCH-LINEAGE-{i}",
        "external_gold_source_url": "https://example.org/synthetic/gold",
        "lock_commit_url": "https://github.com/example/fiction/commit/abc",
        "unblind_evidence_url": "https://example.org/synthetic/unblinded",
        "prediction_committed_on": "2026-11-15",
        "unblinded_on": "2026-12-02",
        "external_gold_first_public_on": gold_date,
        "independent_role_reviewers": [
            {"reviewer_id": "synthetic-one", "roles": roles},
            {"reviewer_id": "synthetic-two", "roles": copy.deepcopy(roles)},
        ],
    }
    return {"sealed": seal(c, protocol()), "gold": g}


def test_zero_case_is_explicitly_inconclusive():
    r = evaluate_cohort([], protocol())
    assert r["total_attempted_physical_objects"] == 0
    assert r["accuracy_on_all_eligible"] is None
    assert r["experimental_state"] == "INSUFFICIENT_N"
    assert r["scientific_pass"] is False


def test_contradictory_case_is_counted_not_discarded():
    p = synthetic_pair(maker_is_a=False)
    r = compare_trial(p["sealed"], p["gold"], protocol())
    assert r["outcome"] == "DECLARED_H_MAKER_MISMATCH"
    assert r["h_maker_correct_against_declared_gold"] is False
    assert r["h_commissioner_correct_against_declared_gold"] is True
    assert r["scientific_confirmation"] is False


def test_blind_disagreement_is_not_a_hit():
    p = synthetic_pair()
    p["gold"]["independent_role_reviewers"][1]["roles"] = {
        "A": "COMMISSIONER", "B": "PRODUCER",
    }
    r = evaluate_cohort([p], protocol())
    assert r["reviewer_disagreements"] == 1
    assert r["role_predictions_made"] == 0
    assert r["h_maker_correct_against_declared_gold"] == 0


def test_absention_is_recorded_in_coverage():
    p = synthetic_pair(marker="x")
    r = evaluate_cohort([p], protocol())
    assert r["abstentions"] == 1
    assert r["coverage"] == 0
    assert r["accuracy_on_all_eligible"] == 0


def test_twenty_synthetic_matches_only_threshold_candidate_not_truth():
    pp = [synthetic_pair(i=i + 1, maker_is_a=i < 16) for i in range(20)]
    r = evaluate_cohort(pp, protocol(), locked_train_baseline_accuracy=0.5)
    assert r["total_attempted_physical_objects"] == 20
    assert r["h_maker_correct_against_declared_gold"] == 16
    assert r["h_maker_incorrect_against_declared_gold"] == 4
    assert r["accuracy_on_all_eligible"] == 0.8
    assert r["coverage"] == 1
    assert r["experimental_state"] == "THRESHOLD_CANDIDATE_PENDING_EXTERNAL_AUDIT"
    assert not r["scientific_pass"]
    assert not r["translation_validated"]
    assert r["statistical_inference"] == "NOT_PERFORMED"


def test_known_public_gold_before_lock_cannot_count_as_prospective():
    pp = [synthetic_pair(i=i + 1, gold_date="2026-01-01") for i in range(20)]
    r = evaluate_cohort(pp, protocol(), locked_train_baseline_accuracy=0.5)
    assert r["newly_released_gold_after_lock"] == 0
    assert r["experimental_state"] == "RETROSPECTIVE_GOLD_RELEASE_NOT_STRICT_PROSPECTIVE"


def test_baseline_must_be_prelocked_to_check_threshold():
    pp = [synthetic_pair(i=i + 1) for i in range(20)]
    r = evaluate_cohort(pp, protocol())
    assert r["experimental_state"] == "BASELINE_NOT_LOCKED"
    with pytest.raises(ValueError):
        evaluate_cohort(pp, protocol(), locked_train_baseline_accuracy=True)


def test_reuse_of_same_physical_or_punch_lineage_fails():
    p1, p2 = synthetic_pair(1), synthetic_pair(2)
    p2["gold"]["documentary_lineage_id"] = p1["gold"]["documentary_lineage_id"]
    with pytest.raises(ValueError, match="lineage"):
        evaluate_cohort([p1, p2], protocol())
    p2 = synthetic_pair(2)
    p2["gold"]["physical_id"] = p1["gold"]["physical_id"]
    with pytest.raises(ValueError, match="identity"):
        evaluate_cohort([p1, p2], protocol())


def test_sealed_hash_tamper_and_protocol_mismatch_fail():
    p = synthetic_pair()
    p["sealed"]["statement"]["marked_person_id"] = "B"
    with pytest.raises(ValueError, match="hash"):
        compare_trial(p["sealed"], p["gold"], protocol())
    p = synthetic_pair()
    altered = protocol()
    altered["state"] = "CHANGED"
    with pytest.raises(ValueError, match="original locked protocol"):
        compare_trial(p["sealed"], p["gold"], altered)


def test_date_priority_and_reviewer_ids_are_mandatory():
    p = synthetic_pair()
    p["gold"]["unblinded_on"] = "2026-11-15"
    with pytest.raises(ValueError, match="unblind"):
        compare_trial(p["sealed"], p["gold"], protocol())
    p = synthetic_pair()
    p["gold"]["independent_role_reviewers"][1]["reviewer_id"] = "synthetic-one"
    with pytest.raises(ValueError, match="distinct"):
        compare_trial(p["sealed"], p["gold"], protocol())
