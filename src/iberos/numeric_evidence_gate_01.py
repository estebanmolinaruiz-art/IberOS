"""NUMERIC-EVIDENCE-GATE-01: reject already-known quantitative examples as new blind tests.
Only historical catalog IDs and split labels are accessed; no HOLD signatures.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

FULL3406_SHA256 = "3cf66a5e9abbec2a8a356be3432d507da0d967d3310ffdeb3dc22878055d13a4"
SOURCES = [
    {
        "id": "CASINOS_PALHISP_2014", "year": 2014,
        "doi": "10.36707/palaeohispanica.v0i14.54",
        "url": "https://ifc-ojs.es/index.php/palaeohispanica/es/article/view/54",
        "locator_regex": r"\bCasinos\b",
        "documented_context": "a-o-ki metrological expressions on both sides",
        "hypothesis": "bi/bin proposed as numeral 2; precise value not independently confirmed",
        "numeric_value_confirmed": False, "semantic_gold": False,
        "archaeological_provenance": "reported Casinos area; exact archaeological site unknown",
    },
    {
        "id": "IBERIAN_NUMERAL_SYSTEM_2009", "year": 2009,
        "doi": "10.36707/palaeohispanica.v0i9.239",
        "url": "https://ifc-ojs.es/index.php/palaeohispanica/es/article/view/239",
        "locator_regex": None,
        "documented_context": "review of numeric combinations and coin-value marks",
        "hypothesis": "lexical numeral interpretation under discussion",
        "numeric_value_confirmed": False, "semantic_gold": False,
    },
]


def gate(records: list[dict], sources: list[dict] | None = None) -> dict:
    sources = SOURCES if sources is None else sources
    seen: set[str] = set()
    issues: list[str] = []
    for i, row in enumerate(records):
        uid = row.get("uid")
        if not isinstance(uid, str) or not uid or uid in seen:
            issues.append(f"DUPLICATE_OR_BAD_UID:{i}")
        seen.add(uid)
    outcomes = []
    for source in sources:
        expr = source.get("locator_regex")
        if expr:
            rx = re.compile(expr, re.I)
            hits = [{
                "uid": row.get("uid"),
                "catalog_id": row.get("catalog_id"),
                "historical_split": row.get("split_v3_4_9"),
            } for row in records if rx.search(str(row.get("catalog_id") or ""))]
            status = ("HISTORICAL_CORPUS_OVERLAP_BLOCKED" if hits
                      else "ABSENCE_BY_NAME_ONLY_NOT_NEWNESS_PROOF")
        else:
            hits = []
            status = "REVIEW_ARTICLE_NOT_A_NEW_SPECIMEN"
        outcomes.append({
            **{k: v for k, v in source.items() if k != "locator_regex"},
            "historical_catalog_hits": hits,
            "historical_catalog_hit_count": len(hits),
            "status": status, "eligible_for_new_blind_evaluation": False,
        })
    return {
        "experiment": "NUMERIC_EVIDENCE_GATE_01",
        "valid": not issues, "issues": issues[:20],
        "historical_record_count": len(records),
        "sources": outcomes,
        "hold_signatures_read": False,
        "training_or_scoring_executed": False,
        "numeric_semantics_validated": False,
        "original_splits_modified": False,
        "official_metrics_changed": False,
        "next_gate": "Independent new physical object + evidence + blind quantitative labels + prespecified evaluation",
    }


def audit_file(path: Path) -> dict:
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != FULL3406_SHA256:
        raise ValueError("FULL3406_SHA256_MISMATCH")
    source = json.loads(raw)
    if not isinstance(source, dict) or not isinstance(source.get("records"), list):
        raise ValueError("INVALID_FULL3406_DOCUMENT")
    return gate(source["records"])


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Read-only external numeric evidence leakage gate")
    p.add_argument("snapshot", type=Path)
    p.add_argument("--json", type=Path)
    a = p.parse_args(argv)
    result = audit_file(a.snapshot)
    output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if a.json:
        if a.json.resolve() == a.snapshot.resolve():
            raise ValueError("REFUSE_OVERWRITE_FROZEN_INPUT")
        a.json.parent.mkdir(parents=True, exist_ok=True)
        a.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0 if result["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
