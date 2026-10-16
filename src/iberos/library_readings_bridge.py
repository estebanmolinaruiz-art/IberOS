"""Reviewed reading intake: documentary gate before semantic-domain suggestions."""
from __future__ import annotations
from .core import get_object, AUTHORITY
from .semantic_hypothesis_engine import suggest_semantic_domains

def analyze_library_readings(records: list[dict]) -> dict:
    if not isinstance(records, list):
        raise ValueError("Expected list of reading records")
    reports=[]
    seen=set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Reading record must be an object")
        rid=record.get("reading_id")
        oid=record.get("object_id")
        if not isinstance(rid,str) or not rid.strip() or rid in seen:
            raise ValueError("Unique reading_id required")
        seen.add(rid)
        if not isinstance(oid,str) or get_object(oid) is None:
            raise ValueError("Known curated object_id required")
        segments=record.get("segments")
        if not isinstance(segments,list):
            raise ValueError("Explicit segments list required")
        approved=record.get("review_status")=="APPROVED_READING" and isinstance(record.get("review_reference"),str) and bool(record["review_reference"].strip())
        # Never promote user-declared segment review status unless record-level gate passes.
        gated=[{**s,"reading_reviewed":bool(approved and s.get("reading_reviewed") is True)}
               for s in segments if isinstance(s,dict)]
        if len(gated)!=len(segments):
            raise ValueError("Every segment must be an object")
        analysis=suggest_semantic_domains(oid,gated)
        reports.append({"reading_id":rid,"object_id":oid,"review_gate_passed":approved,
                        "review_reference":record.get("review_reference") if approved else None,
                        "suggestions":analysis["suggestions"],
                        "translation_validated":False,"automatic_core_promotion":False})
    return {"schema":"IberOS-Library-Reading-Analysis/1.0","authority":dict(AUTHORITY),
            "reading_count":len(reports),"reports":reports,
            "notice":"Reading approval is an editorial assertion requiring independent verification; semantic domains are hypotheses.",
            "automatic_core_promotion":False}
