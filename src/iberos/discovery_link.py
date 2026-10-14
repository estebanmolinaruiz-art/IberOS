"""Evidence-safe bibliographic linking; no fuzzy matches or automatic CORE updates."""
from __future__ import annotations
import re
from .core import load_registry

ID_PATTERN = re.compile(r"\bIBR-[A-Z0-9]+-\d{4}\b")

def proposed_object_links(records: list[dict]) -> list[dict]:
    """Only explicit known OBJECT_ID mentions may create a proposed link."""
    known = {row["OBJECT_ID"] for row in load_registry()}
    results = []
    for record in records:
        if not isinstance(record, dict) or not isinstance(record.get("id"), str):
            raise ValueError("Expected persistent discovery records with id")
        text = " ".join(str(record.get(k) or "") for k in
                        ("title", "claimed_findings", "object_identifiers"))
        mentions = sorted(set(ID_PATTERN.findall(text)))
        results.append({
            "discovery_id": record["id"],
            "candidate_object_ids": [x for x in mentions if x in known],
            "unmatched_id_mentions": [x for x in mentions if x not in known],
            "link_state": "PROPOSED_UNVERIFIED" if mentions else "NO_EXPLICIT_OBJECT_ID",
            "link_is_evidence": False,
            "automatic_core_promotion": False,
        })
    return results
