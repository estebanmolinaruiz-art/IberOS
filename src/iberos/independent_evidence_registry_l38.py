"""IberOS L38: conservative audit of independent epigraphic evidence.

Checks completeness, not truth. Confirmation is *never* awarded from
editorial metadata or caller-provided claims. Python 3.10+, stdlib only.
"""
from __future__ import annotations
import csv
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = (
    "object_id", "catalog_id", "transcription", "candidate_family",
    "edition_url", "edition_reference", "image_url", "image_access",
    "independent_image_reading_id", "archaeological_context_source",
    "chronology_source", "reviewer_id", "review_date", "audit_decision", "notes",
)
DECISIONS = frozenset({"PENDING", "REJECTED", "UNRESOLVED"})

def _https_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc) and not parsed.username

def audit(record: dict) -> dict:
    issues = [f"MISSING_FIELD:{field}" for field in REQUIRED if field not in record]
    if issues:
        return {"object_id": record.get("object_id"), "state": "BLOCKED",
                "issues": issues, "family_confirmed": False}
    if not record["object_id"].strip() or not record["transcription"].strip():
        issues.append("OBJECT_ID_OR_TRANSCRIPTION_EMPTY")
    if record["edition_url"] and not _https_url(record["edition_url"]):
        issues.append("INVALID_EDITION_URL")
    if not record["edition_url"] or not record["edition_reference"]:
        issues.append("EDITION_NOT_TRACEABLE")
    if not record["image_url"] or not _https_url(record["image_url"]):
        issues.append("ORIGINAL_IMAGE_NOT_LINKED")
    if record["image_access"] != "DIRECT_PRIMARY_IMAGE_VERIFIED":
        issues.append("PRIMARY_IMAGE_NOT_INSPECTED_INDEPENDENTLY")
    if not record["independent_image_reading_id"]:
        issues.append("NO_INDEPENDENT_IMAGE_READING")
    if not record["archaeological_context_source"]:
        issues.append("CONTEXT_NOT_INDEPENDENTLY_DOCUMENTED")
    if not record["chronology_source"]:
        issues.append("CHRONOLOGY_NOT_INDEPENDENTLY_DOCUMENTED")
    if not record["reviewer_id"] or not record["review_date"]:
        issues.append("INDEPENDENT_REVIEW_NOT_RECORDED")
    if record["audit_decision"] not in DECISIONS:
        issues.append("SELF_DECLARED_CONFIRMATION_NOT_ACCEPTED")
    state = "REJECTED" if record["audit_decision"] == "REJECTED" else "BLOCKED"
    if not issues and state == "BLOCKED":
        issues.append("EXTERNAL_ADJUDICATION_REQUIRED")
    return {
        "object_id": record["object_id"],
        "catalog_id": record["catalog_id"],
        "candidate_family": record["candidate_family"], "state": state,
        "issues": issues, "family_confirmed": False,
        "numeric_value_verified": False, "new_translation_validated": False,
    }

def evaluate_csv(path: str | Path) -> dict:
    with Path(path).open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    ids = [row.get("object_id") for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("DUPLICATE_OBJECT_ID")
    return {
        "experiment": "IBEROS_L38_EVIDENCE_GATE", "count": len(rows),
        "confirmed": 0, "objects": [audit(row) for row in rows],
        "metrics_changed": False,
        "note": "Provenance completeness audit, not independent paleographic verification.",
    }
