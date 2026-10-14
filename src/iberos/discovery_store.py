"""Persistent, review-only research discovery ledger.

Pure standard-library JSONL store; ingestion cannot change scientific CORE.
"""
from __future__ import annotations
import json
from pathlib import Path
from .discovery import review_discoveries

ALLOWED_MODULES = frozenset({"GEO", "PALEO", "MORPH", "LEXSEM", "TRACE", "INFER"})

def classify_discovery(item: dict) -> dict:
    """Produce non-semantic review routing from *explicit* source metadata only."""
    tags = item.get("modules", [])
    if not isinstance(tags, list) or any(t not in ALLOWED_MODULES for t in tags):
        raise ValueError("modules must be a list of recognized modules")
    return {"modules_to_review": sorted(set(tags)) or ["TRACE"],
            "review_status": "AWAITING_HUMAN_REVIEW",
            "hypothesis_status": "NOT_TESTED",
            "automatic_core_promotion": False}

def append_discoveries(path: str | Path, records: list[dict]) -> dict:
    """Atomically deduplicate and persist an inbox, failing closed on corruption."""
    path = Path(path)
    existing = []
    if path.exists():
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Invalid JSONL at line {n}") from exc
            if not isinstance(record, dict) or not isinstance(record.get("id"), str):
                raise ValueError(f"Invalid ledger record at line {n}")
            existing.append(record)
    known = {x["id"] for x in existing}
    incoming = review_discoveries(records)["items"]
    fresh = []
    for original, candidate in zip(records, incoming):
        # Dedup within each batch is handled by review_discoveries; look up
        # source record by normalized title and URL for explicit review tags.
        match = next((r for r in records if
                      str(r.get("title", "")).strip().casefold() == candidate["title"].casefold()
                      and str(r.get("url", "")).strip().casefold() == candidate["url"].casefold()), {})
        if candidate["id"] in known:
            continue
        candidate.update(classify_discovery(match))
        known.add(candidate["id"])
        fresh.append(candidate)
    if fresh:
        path.parent.mkdir(parents=True, exist_ok=True)
        data = existing + fresh
        tmp = path.with_name(path.name + ".tmp")
        tmp.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in data), encoding="utf-8")
        tmp.replace(path)
    return {"new": len(fresh), "total": len(existing) + len(fresh),
            "scientific_state": "UNVERIFIED_INBOX", "automatic_core_promotion": False}
