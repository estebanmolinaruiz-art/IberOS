"""Review-only bridge from expanded public library records to scientific CORE.

Physical independence must be explicitly evidenced; never count editions as objects.
"""
from __future__ import annotations
from hashlib import sha256
from urllib.parse import urlparse
from .core import load_registry, AUTHORITY

def triage_library_records(records: list[dict]) -> dict:
    if not isinstance(records, list):
        raise ValueError("Expected list of library records")
    curated = {r["OBJECT_ID"] for r in load_registry()}
    seen = set()
    items = []
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Library record must be an object")
        source = record.get("source_url")
        title = record.get("title")
        if not isinstance(title, str) or not title.strip() or not isinstance(source, str):
            raise ValueError("Title and source URL required")
        parsed = urlparse(source)
        if parsed.scheme != "https" or not parsed.netloc:
            raise ValueError("Source URL must be HTTPS")
        doc_key = sha256((title.strip().casefold()+"|"+source.strip().casefold()).encode()).hexdigest()[:20]
        if doc_key in seen:
            continue
        seen.add(doc_key)
        physical_id = record.get("physical_object_id")
        linked = physical_id if isinstance(physical_id, str) and physical_id in curated else None
        claim = record.get("independence_evidence")
        has_claim = isinstance(claim, str) and bool(claim.strip())
        items.append({
            "document_id": "LIB-"+doc_key, "title":title.strip(), "source_url":source,
            "linked_curated_object_id":linked,
            "claimed_physical_object_id":physical_id if isinstance(physical_id,str) else None,
            "route": "DOCUMENTARY_EDITION_OF_CURATED_OBJECT" if linked else "UNMATCHED_OBJECT_REVIEW",
            "physical_independence_declared":has_claim,
            "physical_independence_verified":False,
            "reading_verified":False,
            "ready_for_core_execution":False,
            "counts_as_new_independent_object":False,
            "review_status":"PENDING_PHYSICAL_IDENTITY_AND_READING_REVIEW",
            "automatic_core_promotion":False,
        })
    return {"schema":"IberOS-Library-Inbox/1.0", "authority":dict(AUTHORITY),
            "document_count":len(items), "records":items,
            "new_independent_scientific_objects":0,
            "automatic_core_promotion":False}
