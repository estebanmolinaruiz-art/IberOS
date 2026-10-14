"""Auditable comparisons of external findings with *dated* IberOS predictions.

Textual agreement is never inferred automatically. The reviewer must supply
an explicit comparison and independent documentary evidence.
"""
from __future__ import annotations
from datetime import date

VERDICTS = frozenset({"SUPPORTS", "CONTRADICTS", "UNCLEAR"})
LABELS = frozenset({"STRICT_PROSPECTIVE_PASS", "EXTERNAL_CONVERGENCE",
                    "RETROSPECTIVE_REPLICATION", "FAIL", "INDETERMINATE"})

def _date(value: str) -> date:
    if not isinstance(value, str):
        raise ValueError("Date must be ISO YYYY-MM-DD")
    return date.fromisoformat(value)

def compare_prediction(prediction: dict, finding: dict, assessment: dict) -> dict:
    """Check chronology and provenance, returning non-promoting candidate status."""
    pid, fid = prediction.get("id"), finding.get("id")
    if not pid or not fid or not prediction.get("source_url") or not finding.get("source_url"):
        raise ValueError("Both records require id and source_url")
    pd, fd = _date(prediction.get("fixed_on")), _date(finding.get("published_on"))
    verdict = assessment.get("verdict")
    if verdict not in VERDICTS:
        raise ValueError("Explicit SUPPPORTS/CONTRADICTS/UNCLEAR assessment required")
    if not assessment.get("evidence_note"):
        raise ValueError("Evidence comparison note is required")
    prior = pd < fd
    independent = assessment.get("independence") is True
    clean = assessment.get("contamination_free") is True
    preregistered = prediction.get("preregistered") is True
    # Dates alone do not prove preregistration, independence, or a successful
    # test. Even complete self-attested metadata is pending external review.
    if verdict == "CONTRADICTS" and independent and clean:
        label = "FAIL"
    elif verdict == "SUPPORTS" and independent and clean:
        label = "EXTERNAL_CONVERGENCE" if prior else "RETROSPECTIVE_REPLICATION"
    else:
        label = "INDETERMINATE"
    return {
        "prediction_id": pid, "finding_id": fid,
        "predates_publication": prior,
        "chronology_is_proof_of_priority": False,
        "preregistered_declared": preregistered,
        "independent_declared": independent,
        "contamination_free_declared": clean,
        "reviewer_verdict": verdict,
        "comparison_class": label,
        "strict_prospective_pass": False,
        "scientific_state": "AWAITING_INDEPENDENT_REVIEW",
        "reviewer_note": assessment["evidence_note"],
        "automatic_core_promotion": False,
    }
