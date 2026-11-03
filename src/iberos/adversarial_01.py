"""ADVERSARIAL-01: five editorial controls, not a grammatical classifier.

Positive controls here assert documentary constraints, NOT Iberian meanings.
Suffix-only predictions are intentionally refused without independent labels.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .core import OFFICIAL_METRICS, independence_audit

EXPERIMENT = "ADVERSARIAL-01"
ORLEYL_CONTEXT = "ORLEYL_SEPULTURA_II"


@dataclass(frozen=True)
class Case:
    case_id: str
    inscription: str
    transcription: str
    phys_id: str
    leak_group: str
    source_grade: str
    context: str
    is_partial: bool = False
    variant_unresolved: bool = False


CASES = (
    Case("ADV-01", "Orleyl V F.9.5", "biteroketetine", "ORLEYL-V-F9.5",
         ORLEYL_CONTEXT, "D1", "formula_candidate"),
    Case("ADV-02", "Orleyl VII F.9.7", "basbiteroketine",
         "ORLEYL-VII-F9.7", ORLEYL_CONTEXT, "D1", "related_formula_candidate",
         variant_unresolved=True),
    Case("ADV-03", "Azaila TE.02.308=E.1.308=AZ.330", "baśtaŕtine",
         "AZAILA-AMPHORA-TE02.308", "AZAILA-AMPHORA-TE02.308", "D1",
         "possible_personal_name"),
    Case("ADV-04", "Pico de los Ajos III F.20.3", "bitarsteti",
         "PICO-AJOS-III-F20.3", "PICO-AJOS-III-F20.3", "D1",
         "incomplete_comparandum", is_partial=True),
    Case("ADV-05", "La Serreta I A.04.01", "bidudenin",
         "LA-SERRETA-I-INV-1016", "LA-SERRETA-I-INV-1016", "D1",
         "disputed_reading", variant_unresolved=True),
)


def naive_suffix_guess(token: str) -> str | None:
    """Deliberately weak baseline that ignores context; used to expose error."""
    return "SHARED_TIN_FAMILY" if token.endswith(("tine", "tetine", "teti", "denin", "dedin")) else None


def controlled_decision(case: Case) -> dict[str, Any]:
    """Do not learn gold meanings from the same examples used to set guards."""
    reasons = ["D1_EDITORIAL_ONLY", "NO_INDEPENDENT_SEMANTIC_GROUND_TRUTH"]
    if case.is_partial:
        reasons.append("POSSIBLY_INCOMPLETE_SEQUENCE")
    if case.variant_unresolved:
        reasons.append("UNRESOLVED_VARIANT_OR_SEGMENTATION")
    if case.leak_group == ORLEYL_CONTEXT:
        reasons.append("SHARED_ARCHAEOLOGICAL_CONTEXT")
    if case.context == "possible_personal_name":
        reasons.append("ONOMASTIC_ALTERNATIVE")
    return {
        "case_id": case.case_id,
        "naive_suffix_guess": naive_suffix_guess(case.transcription),
        "grammatical_decision": "ABSTAIN",
        "candidate_context": case.context,
        "reasons": reasons,
        "automatic_semantic_promotion": False,
    }


def run() -> dict[str, Any]:
    rows = [controlled_decision(c) for c in CASES]
    # Actual physical identities remain distinct; contextual leakage is audited
    # separately, since CORE independence_key privileges PHYS_ID over LEAK_GROUP.
    physical = independence_audit([
        {"ENTRY_ID": c.case_id, "PHYS_ID": c.phys_id} for c in CASES
    ])
    contextual = independence_audit([
        {"ENTRY_ID": c.case_id, "LEAK_GROUP": c.leak_group} for c in CASES
    ])
    assert physical["independent_units"] == 5
    assert contextual["independent_units"] == 4
    return {
        "experiment_id": EXPERIMENT,
        "test_kind": "adversarial_non_promotional_guard",
        "not_a_trained_classifier": True,
        "cases": len(CASES),
        "physically_distinct_objects": physical["independent_units"],
        "contextual_groups": contextual["independent_units"],
        "semantic_gold_labels": 0,
        "naive_suffix_matches": sum(r["naive_suffix_guess"] is not None for r in rows),
        "abstentions": sum(r["grammatical_decision"] == "ABSTAIN" for r in rows),
        "scientific_promotion": False,
        "official_metrics_changed": False,
        "official_metrics": dict(OFFICIAL_METRICS),
        "rows": rows,
        "notes": [
            "All readings are D1 editorial witnesses, not D2/D3 verification.",
            "Azaila's onomastic interpretation is an alternative hypothesis, not a gold label.",
            "Orleyl V and VII share an archaeological context but have different physical IDs.",
            "The baseline suffix guess demonstrates overgeneralization, not model accuracy.",
            "No classifier accuracy, grammatical inference or translation is reported.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="IberOS five-case non-promotional adversarial check")
    p.add_argument("--json", type=Path, help="Write JSON report (otherwise print)")
    args = p.parse_args(argv)
    result = json.dumps(run(), ensure_ascii=False, indent=2) + "\n"
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(result, encoding="utf-8")
    else:
        print(result, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
