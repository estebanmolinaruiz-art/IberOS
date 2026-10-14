"""External discovery intake: quarantine new research until manual verification."""
from __future__ import annotations
from datetime import datetime, timezone
from hashlib import sha256
from urllib.parse import urlparse

def review_discoveries(records: list[dict]) -> dict:
    if not isinstance(records, list):
        raise ValueError("Expected list of discovery records")
    out, seen = [], set()
    for item in records:
        if not isinstance(item, dict):
            raise ValueError("Discovery must be an object")
        title, url = str(item.get("title", "")).strip(), str(item.get("url", "")).strip()
        parsed = urlparse(url)
        if not title or parsed.scheme != "https" or not parsed.netloc:
            raise ValueError("Discovery needs a title and HTTPS source URL")
        identity = sha256((title.casefold()+"|"+url.casefold()).encode()).hexdigest()[:16]
        if identity in seen:
            continue
        seen.add(identity)
        out.append({
            "id": "DISC-"+identity, "title": title, "url": url,
            "published_at": item.get("published_at"),
            "source_name": item.get("source_name", ""),
            "claimed_findings": item.get("claimed_findings", ""),
            "status": "UNVERIFIED_INBOX",
            "source_reviewed": False, "independent_replication": False,
            "eligible_for_core": False, "automatic_core_promotion": False,
            "requires": ["source_authenticity", "bibliographic_verification",
                         "physical_witness_independence", "expert_epigraphic_review"],
        })
    return {"items": out, "count": len(out), "scientific_state": "UNVERIFIED",
            "automatic_core_promotion": False}
