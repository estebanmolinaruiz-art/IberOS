"""Auditable comparisons of external findings with *dated* IberOS predictions.

Textual agreement is never inferred automatically. The reviewer must supply
an explicit comparison and independent documentary evidence.
"""
from __future__ import annotations
from datetime import date
from hashlib import sha256
from urllib.parse import urlparse

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
    for url in (prediction["source_url"], finding["source_url"]):
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            raise ValueError("Evidence sources must be HTTPS URLs")
    pd, fd = _date(prediction.get("fixed_on")), _date(finding.get("published_on"))
    verdict = assessment.get("verdict")
    if verdict not in VERDICTS:
        raise ValueError("Explicit SUPPORTS/CONTRADICTS/UNCLEAR assessment required")
    if not assessment.get("evidence_note"):
        raise ValueError("Evidence comparison note is required")
    prior = pd < fd
    independent = assessment.get("independence") is True
    clean = assessment.get("contamination_free") is True
    preregistered = prediction.get("preregistered") is True
    prediction_text = prediction.get("statement")
    prediction_hash = prediction.get("statement_sha256")
    hash_valid = (
        isinstance(prediction_text, str) and bool(prediction_text.strip())
        and isinstance(prediction_hash, str)
        and sha256(prediction_text.encode("utf-8")).hexdigest() == prediction_hash
    )
    time_lock_evidence = prediction.get("timestamp_evidence_url")
    priority_documented = (
        prior and preregistered and hash_valid
        and isinstance(time_lock_evidence, str)
        and urlparse(time_lock_evidence).scheme == "https"
        and bool(urlparse(time_lock_evidence).netloc)
    )
    # Metadata and hashes permit a reproducible audit, not proof that a
    # timestamp or comparison was independently verified.
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
        "prediction_hash_matches_text": hash_valid,
        "documentary_priority_candidate": priority_documented,
        "timestamp_evidence_checked_independently": False,
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
