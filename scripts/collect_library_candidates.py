#!/usr/bin/env python3
"""Collect candidate bibliography metadata; never publish as scientific evidence."""
import argparse
import json
import pathlib
import re
import urllib.parse
import urllib.request

BASE = pathlib.Path(__file__).resolve().parents[1] / "site" / "data"
TERMS = ["Iberian epigraphy", "Palaeohispanic inscriptions", "Iberian script", "Iberian language inscriptions", "Palaeohispanic epigraphy", "Iberian paleography", "Iberian lead tablets", "Pech Maho inscriptions"]
def norm(s):
    return re.sub(r"[^a-z0-9]+", "", str(s).casefold())
def collect(limit):
    seen = set()
    items = []
    per_term = max(1, (limit + len(TERMS) - 1) // len(TERMS))
    for term in TERMS:
        if len(items) >= limit:
            break
        offset = 0
        while offset < per_term and len(items) < limit:
            page_size = min(100, per_term - offset)
            url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": term, "rows": page_size, "offset": offset, "select": "DOI,title,author,published,URL,publisher"})
            request = urllib.request.Request(url, headers={"User-Agent": "IberOS-Library/1.1 (research metadata; contact via GitHub project)"})
            try:
                with urllib.request.urlopen(request, timeout=25) as response:
                    results = json.load(response).get("message", {}).get("items", [])
            except Exception as exc:
                print(f"Source unavailable for {term}, offset {offset}: {exc}")
                break
            if not results:
                break
            offset += len(results)
            for item in results:
                title = (item.get("title") or [""])[0]
                doi = item.get("DOI", "").strip().lower()
                link = item.get("URL", "")
                key = doi or norm(title)
                if not title or not link or not doi.startswith("10.") or key in seen:
                    continue
                seen.add(key)
                # Crossref search uses fuzzy relevance. Surface items as unapproved metadata only.
                items.append({"title": title, "doi": doi, "url": link,
                    "authors": "; ".join(((a.get("given", "") + " " + a.get("family", "")).strip() for a in item.get("author", [])))[:500],
                    "publisher": item.get("publisher", ""), "discovery_term": term,
                    "discovery_method": "crossref_candidate_search", "metadata_relevance_verified": False,
                    "status": "PENDING_EDITORIAL_REVIEW", "core_evidence_approved": False,
                    "rights": "Metadata link only; original publisher retains content rights"})
                if len(items) >= limit:
                    break
    return items

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--output", type=pathlib.Path, default=BASE / "library_candidates_v1.json")
    args = parser.parse_args()
    if not 1 <= args.limit <= 1000:
        parser.error("limit must be from 1 to 1000")
    records = collect(args.limit)
    if args.output.exists():
        previous = json.loads(args.output.read_text(encoding="utf-8"))
        existing = previous.get("items", [])
        used = {x.get("doi", "").lower() or norm(x.get("title", "")) for x in existing}
        for item in records:
            key = (item.get("doi") or "").lower() or norm(item["title"])
            if key not in used:
                existing.append(item)
                used.add(key)
        records = existing[:args.limit]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"schema": "IberOS-Library-Candidates/1.0", "review_required": True,
                                      "items": records}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(records)} candidates queued for review; zero approved for Core")

if __name__ == "__main__":
    main()
