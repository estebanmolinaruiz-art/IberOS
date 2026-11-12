"""SCI-PRED-03: compare sealed predictions with *later disclosed* external role labels.

Retrospective/boundary-control evaluator. External dates, reviewer independence
and gold authenticity require independent human/source verification. No input
can make this module certify a translation or promote CORE automatically.
"""
from __future__ import annotations

from datetime import date
from math import ceil
from urllib.parse import urlsplit

from .prospective_role_lock import _sha

ROLES = frozenset({"PRODUCER", "COMMISSIONER"})
SEALED_SCHEMA = "IberOS-SCI-PRED-02-Sealed-Prediction/1.0"


def _nonempty(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _url(value) -> bool:
    if not _nonempty(value):
        return False
    p = urlsplit(value)
    return p.scheme == "https" and bool(p.netloc) and not p.username and not p.password


def _day(value: str) -> date:
    if not _nonempty(value):
        raise ValueError("Missing dated evidence")
    return date.fromisoformat(value)


def compare_trial(sealed: dict, gold: dict, protocol: dict) -> dict:
    """Score a declared, blinded two-person role judgment without proving it.

    Both independent human role assessments are visible only to this function,
    NEVER to prospective_role_lock.seal. Metadata-only source assertions do not
    prove gold independence, chronology, actual sign reading, or translation.
    """
    if not isinstance(sealed, dict) or sealed.get("schema") != SEALED_SCHEMA:
        raise ValueError("A sealed prediction is required")
    if not isinstance(gold, dict) or not isinstance(protocol, dict):
        raise ValueError("Gold and protocol must be objects")
    statement = sealed.get("statement")
    if not isinstance(statement, dict) or sealed.get("statement_sha256") != _sha(statement):
        raise ValueError("Sealed prediction hash mismatch")
    if statement.get("protocol_sha256") != _sha(protocol):
        raise ValueError("Not the original locked protocol")
    if protocol.get("protocol") != "SCI-PRED-02/1.0":
        raise ValueError("Protocol version mismatch")
    blind_id, phys_id = statement.get("blind_id"), statement.get("physical_id")
    people = statement.get("participant_ids")
    if not all(_nonempty(x) for x in (blind_id, phys_id)):
        raise ValueError("Sealed identity is incomplete")
    if not isinstance(people, list) or len(people) != 2 or len(set(people)) != 2:
        raise ValueError("Exactly two sealed person identities are required")
    if gold.get("blind_id") != blind_id or gold.get("physical_id") != phys_id:
        raise ValueError("Gold identity does not match sealed object")
    stamp_family = gold.get("documentary_lineage_id")
    if not _nonempty(stamp_family):
        raise ValueError("Missing independently auditable documentary lineage")
    for field in ("external_gold_source_url", "lock_commit_url",
                  "unblind_evidence_url"):
        if not _url(gold.get(field)):
            raise ValueError(f"HTTPS {field} required")
    lock_date = _day(gold.get("prediction_committed_on"))
    unblind_date = _day(gold.get("unblinded_on"))
    gold_release_date = _day(gold.get("external_gold_first_public_on"))
    if lock_date >= unblind_date:
        raise ValueError("Cannot unblind on/before prediction commitment")
    reviewers = gold.get("independent_role_reviewers")
    if not isinstance(reviewers, list) or len(reviewers) != 2:
        raise ValueError("Require two independently documented role reviews")
    reviewer_ids, reviewer_labels = set(), []
    for review in reviewers:
        if not isinstance(review, dict):
            raise ValueError("Malformed role review")
        rid = review.get("reviewer_id")
        roles = review.get("roles")
        if not _nonempty(rid) or rid in reviewer_ids:
            raise ValueError("Two distinct named reviewer IDs required")
        reviewer_ids.add(rid)
        if not isinstance(roles, dict) or set(roles) != set(people):
            raise ValueError("Role labels must cover exactly the two sealed people")
        if set(roles.values()) != ROLES:
            raise ValueError("Role labels must distinguish producer and commissioner")
        reviewer_labels.append(roles)
    consensus = reviewer_labels[0] == reviewer_labels[1]
    target = statement.get("marked_person_id")
    if target is not None and target not in people:
        raise ValueError("Predicted target not a sealed participant")
    if target is None:
        if statement.get("h_maker_prediction") is not None:
            raise ValueError("Abstention cannot contain a guessed maker")
        outcome = "ABSTAIN"
        maker_correct = None
        commissioner_correct = None
    elif not consensus:
        outcome = "REVIEWER_DISAGREEMENT"
        maker_correct = None
        commissioner_correct = None
    else:
        maker = statement.get("h_maker_prediction")
        commissioner = statement.get("h_commissioner_prediction")
        if (maker != {"person_id": target, "role": "PRODUCER"}
                or commissioner != {"person_id": target, "role": "COMMISSIONER"}):
            raise ValueError("Locked rival predictions were altered")
        maker_correct = reviewer_labels[0][target] == "PRODUCER"
        commissioner_correct = reviewer_labels[0][target] == "COMMISSIONER"
        outcome = "DECLARED_H_MAKER_MATCH" if maker_correct else "DECLARED_H_MAKER_MISMATCH"
    return {
        "blind_id": blind_id,
        "physical_id": phys_id,
        "documentary_lineage_id": stamp_family,
        "reviewer_consensus_declared": consensus,
        "outcome": outcome,
        "h_maker_correct_against_declared_gold": maker_correct,
        "h_commissioner_correct_against_declared_gold": commissioner_correct,
        "strictly_new_gold_release_after_lock": gold_release_date > lock_date,
        "chronology_metadata_internally_consistent": True,
        "gold_external_authenticity_verified_by_software": False,
        "reviewer_independence_verified_by_software": False,
        "sealed_timestamp_verified_by_software": False,
        "scientific_confirmation": False,
    }


def evaluate_cohort(pairs: list[dict], protocol: dict, *,
                    locked_train_baseline_accuracy: float | None = None) -> dict:
    """No success claims from fewer than 20 physically and editorially independent objects."""
    if not isinstance(pairs, list) or len(pairs) > 20:
        raise ValueError("Expected first 0-20 consecutive evaluation objects")
    if locked_train_baseline_accuracy is not None:
        if (type(locked_train_baseline_accuracy) is not float
                or not 0 <= locked_train_baseline_accuracy <= 1):
            raise ValueError("TRAIN baseline must be a frozen float in [0,1]")
    trials = [compare_trial(x["sealed"], x["gold"], protocol) for x in pairs]
    physical_ids = [x["physical_id"] for x in trials]
    lineages = [x["documentary_lineage_id"] for x in trials]
    if len(set(physical_ids)) != len(physical_ids):
        raise ValueError("Duplicate physical object: not independent trials")
    if len(set(lineages)) != len(lineages):
        raise ValueError("Duplicate editorial/stamp lineage: not independent trials")
    attempted = len(trials)
    maker_correct = sum(x["h_maker_correct_against_declared_gold"] is True for x in trials)
    maker_incorrect = sum(x["h_maker_correct_against_declared_gold"] is False for x in trials)
    disagreements = sum(x["outcome"] == "REVIEWER_DISAGREEMENT" for x in trials)
    abstentions = sum(x["outcome"] == "ABSTAIN" for x in trials)
    covered = maker_correct + maker_incorrect
    new_gold_trials = sum(x["strictly_new_gold_release_after_lock"] for x in trials)
    performance = (maker_correct / attempted) if attempted else None
    coverage = (covered / attempted) if attempted else None
    threshold_n = 20
    accuracy_threshold = 0.8
    margin_threshold = 0.15
    candidate = (
        attempted >= threshold_n
        and disagreements == 0 and abstentions == 0
        and new_gold_trials == attempted
        and maker_correct >= ceil(accuracy_threshold * attempted)
        and locked_train_baseline_accuracy is not None
        and performance - locked_train_baseline_accuracy >= margin_threshold - 1e-10
    )
    if attempted < threshold_n:
        state = "INSUFFICIENT_N"
    elif new_gold_trials != attempted:
        state = "RETROSPECTIVE_GOLD_RELEASE_NOT_STRICT_PROSPECTIVE"
    elif locked_train_baseline_accuracy is None:
        state = "BASELINE_NOT_LOCKED"
    elif disagreements:
        state = "REVIEW_DISAGREEMENT_REQUIRES_RESOLUTION"
    elif candidate:
        state = "THRESHOLD_CANDIDATE_PENDING_EXTERNAL_AUDIT"
    else:
        state = "THRESHOLD_NOT_MET"
    return {
        "schema": "IberOS-SCI-PRED-03-Declared-Gold-Evaluation/1.0",
        "experimental_state": state,
        "total_attempted_physical_objects": attempted,
        "independent_documentary_lineages_declared": len(lineages),
        "role_predictions_made": covered,
        "h_maker_correct_against_declared_gold": maker_correct,
        "h_maker_incorrect_against_declared_gold": maker_incorrect,
        "abstentions": abstentions,
        "reviewer_disagreements": disagreements,
        "newly_released_gold_after_lock": new_gold_trials,
        "coverage": coverage,
        "accuracy_on_all_eligible": performance,
        "accuracy_on_predicted_only": maker_correct / covered if covered else None,
        "locked_train_baseline_accuracy": locked_train_baseline_accuracy,
        "baseline_margin_on_all_eligible": (performance - locked_train_baseline_accuracy)
            if performance is not None and locked_train_baseline_accuracy is not None else None,
        "trials": trials,
        "statistical_inference": "NOT_PERFORMED",
        "external_provenance_verified_by_software": False,
        "scientific_pass": False,
        "translation_validated": False,
        "automatic_core_promotion": False,
        "notice": (
            "Outcomes are against *declared* human labels only. A reviewer must "
            "independently verify sources, date priority, sign readings, sealed "
            "commit and the absence of exposure/leakage before any scientific claim."
        ),
    }
