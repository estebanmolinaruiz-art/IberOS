"""HOLD-01: leakage-safe retrospective blind packet for IberOS.

Creates a sealed evaluation manifest from external published objects. Does not
pretend that grammatical gold labels exist or claim prospective discovery.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .core import OFFICIAL_METRICS, load_registry


@dataclass(frozen=True)
class HoldCandidate:
    key: str
    name: str
    source: str
    phys_id: str
    leak_group: str
    evidential_grade: str
    role: str
    grammatical_gold: str | None = None


CANDIDATES = (
    HoldCandidate(
        "HOLD-01-B", "La Mesa Alcolea del Rio lead", "https://doi.org/10.36707/palaeohispanica.v0i17.136",
        "LA-MESA-2017-LEAD", "LA-MESA-2017", "D1", "external_script_transfer",
    ),
)


CIRNE_CORPUS_EXCLUSION = {
    "id": "HOLD-01-A",
    "name": "Fundacio CIRNE Xabia lead",
    "reason": "ALREADY_IN_FOLCH_2024_CORPUS_ROW_4354",
    "source_spreadsheet": "19ct13SfIqjaUCFzJaROmwGdTIf92vSqvoHoNAAk8bs4",
    "tabs": ["text", "cadenes"],
    "row": 4354,
}

KNOWN_PRIOR = (
    ("IBR-MUS-0001", "Caminreal mosaic MLH E.7.1 = K.5.3"),
    ("IBR-MUS-0002", "Andelo mosaic K.28.1"),
)


def _mask_key(text: str) -> str:
    return hashlib.sha256(("HOLD-01-v1|" + text).encode("utf-8")).hexdigest()[:16]


def run() -> dict[str, Any]:
    registry = load_registry()
    registry_ids = {r["OBJECT_ID"] for r in registry}
    known_exclusions = [
        {"id": item_id, "name": name, "reason": "ALREADY_IN_CURATED_REGISTRY"}
        for item_id, name in KNOWN_PRIOR if item_id in registry_ids
    ]
    assert len(known_exclusions) == 2, "Curated baseline changed; review split"
    known_exclusions.append(dict(CIRNE_CORPUS_EXCLUSION))
    # The live registry does not yet contain explicit concordances for every
    # external item. Thus absence here is NOT proof of non-contamination.
    hold = [
        {
            "blind_id": _mask_key(c.key),
            "grammatical_prediction": None,
            "source_grade": c.evidential_grade,
            "gold_available": c.grammatical_gold is not None,
        }
        for c in CANDIDATES
    ]
    assert len({r["blind_id"] for r in hold}) == len(hold)
    assert len({c.phys_id for c in CANDIDATES}) == len(CANDIDATES)
    assert len({c.leak_group for c in CANDIDATES}) == len(CANDIDATES)
    return {
        "experiment": "HOLD-01",
        "kind": "retrospective_masked_evaluation_preparation",
        "external_candidates": len(hold),
        "preexisting_exclusions": known_exclusions,
        "blinded_packet": hold,
        "semantic_gold_available": 0,
        "score_grammar_accuracy": None,
        "model_predictions_executed": False,
        "candidate_concordance_status": "LA_MESA_PENDING_LEGACY_3406_AUDIT",
        "independence_certified": False,
        "holdout_locked_for_prospective_claim": False,
        "release_promotion": False,
        "official_metrics_changed": False,
        "official_metrics": dict(OFFICIAL_METRICS),
        "note": "CIRNE Xabia is excluded: Folch 2024 corpus text and cadenes row 4354. La Mesa remains uncertified; no semantic score.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="IberOS HOLD-01 blinded packet")
    parser.add_argument("--json", type=Path)
    args = parser.parse_args(argv)
    content = json.dumps(run(), indent=2, ensure_ascii=False) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(content, encoding="utf-8")
    else:
        print(content, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
