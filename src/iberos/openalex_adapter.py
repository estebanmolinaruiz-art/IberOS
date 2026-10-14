"""Opt-in OpenAlex scholarly metadata discovery; never semantic learning.

Network access occurs only when fetch_openalex() is explicitly run.
"""
from __future__ import annotations
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from .discovery_store import append_discoveries

API = "https://api.openalex.org/works"
QUERY = "Iberian inscriptions epigraphy"

def normalize_openalex_works(payload: dict) -> list[dict]:
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        raise ValueError("Invalid OpenAlex response")
    result = []
    for work in payload["results"]:
        if not isinstance(work, dict):
            continue
        title = work.get("display_name")
        doi = work.get("doi")
        landing = work.get("primary_location") or {}
        url = doi or (landing.get("landing_page_url") if isinstance(landing, dict) else None)
        if not isinstance(title, str) or not isinstance(url, str) or not url.startswith("https://"):
            continue
        result.append({
            "title": title, "url": url,
            "published_at": work.get("publication_date"),
            "source_name": "OpenAlex",
            "claimed_findings": "",
            "modules": ["TRACE", "PALEO"],
        })
    return result

def fetch_openalex(query: str = QUERY, per_page: int = 20, timeout: int = 12) -> list[dict]:
    """Fetch public article metadata only; abstracts and claims are not inferred."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Query required")
    if not 1 <= per_page <= 100:
        raise ValueError("per_page must be 1..100")
    params = urlencode({"search": query, "per-page": per_page})
    request = Request(API + "?" + params, headers={"User-Agent":"IberOS-Research-Discovery/1.0 (https://github.com/estebanmolinaruiz-art/IberOS)","Accept":"application/json"})
    with urlopen(request, timeout=timeout) as response:
        payload = json.load(response)
    return normalize_openalex_works(payload)

def sync_openalex(path: str, query: str = QUERY, per_page: int = 20) -> dict:
    records = fetch_openalex(query=query, per_page=per_page)
    status = append_discoveries(path, records)
    return {"fetched_candidates":len(records), **status, "source":"OpenAlex",
            "manual_source_review_required": True}
