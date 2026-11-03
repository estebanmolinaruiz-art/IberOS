"""SERRETA-SENS-01: formal editorial-reading sensitivity, not translation.

The three alternatives are editorial witnesses (D1), not independent readings
from the physical object. This experiment must not promote CORE metrics.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
from pathlib import Path
from typing import Any

from .core import ENGINE_PROTOCOL_VERSION, OFFICIAL_METRICS, independence_audit

EXPERIMENT_ID = "SERRETA-SENS-01"
PHYS_ID = "LA-SERRETA-I-INV-1016"
OPTIONS = {
    "B2": ("dai", "darr"),
    "B3": ("gadenin", "gadedin"),
    "B4": ("bidudenin", "bidudedin"),
}
# Source: Velaza (2011), transcribed in Ngomo Fernández (2021), p. 59.
# Only the three disputed elements vary. Line boundaries are retained.
FIXED_LINES = (
    ("iunstir", "śalirg", "basiŕtiŕ", "sabaŕi"),
    ("birinaŕ", "guŕś", "boiśtingiśdid"),
    ("seśgeŕśduŕan",),
    ("seŕaikala", "naltinge", "ildu"),
    ("niŕaenai", "bekoŕ", "sebagediŕan"),
)


def scenarios() -> list[dict[str, str]]:
    """Keep Drive's published numbering: B2 toggles fastest, then B3, B4."""
    cases = []
    for n in range(8):
        cases.append({
            "scenario": f"SER-SENS-{n + 1:02d}",
            "B2": OPTIONS["B2"][n & 1],
            "B3": OPTIONS["B3"][(n >> 1) & 1],
            "B4": OPTIONS["B4"][(n >> 2) & 1],
        })
    return cases


def tokens_for(case: dict[str, str]) -> list[list[str]]:
    """Preserve lines and transliteration; do not neutralize vibrants."""
    return [
        list(FIXED_LINES[0]),
        [case["B2"], *FIXED_LINES[1]],
        [*FIXED_LINES[2], "sesdiŕ" + case["B3"]],
        [FIXED_LINES[3][0], FIXED_LINES[3][1], case["B4"], FIXED_LINES[3][2]],
        list(FIXED_LINES[4]),
    ]


def run() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for case in scenarios():
        lines = tokens_for(case)
        tokens = list(itertools.chain.from_iterable(lines))
        rows.append({
            **case,
            "line_count": len(lines),
            "segment_count": len(tokens),
            "dedin_count": sum(token.endswith("dedin") for token in tokens),
            "denin_count": sum(token.endswith("denin") for token in tokens),
            "iunstir_present": "iunstir" in tokens,
            "naltinge_present": "naltinge" in tokens,
            "evidence_level": "D1",
            "scientific_promotion": False,
        })

    all_sets = [set(itertools.chain.from_iterable(tokens_for(case))) for case in scenarios()]
    common = sorted(set.intersection(*all_sets))
    # All variants derive from a single inscribed physical object.
    identity_rows = [
        {"ENTRY_ID": row["scenario"], "PHYS_ID": PHYS_ID}
        for row in rows
    ]
    independence = independence_audit(identity_rows)
    assert independence["independent_units"] == 1
    return {
        "experiment_id": EXPERIMENT_ID,
        "experiment_type": "retrospective_editorial_formal_sensitivity",
        "engine_guard_version": ENGINE_PROTOCOL_VERSION,
        "original_core_semantic_engine_executed": False,
        "official_metrics_changed": False,
        "official_metrics": dict(OFFICIAL_METRICS),
        "source_level": "D1",
        "semantic_validation": "NOT_PERFORMED",
        "scientific_promotion": False,
        "scenario_count": len(rows),
        "independent_physical_objects": independence["independent_units"],
        "stable_segment_count": len(common),
        "stable_segments": common,
        "variable_positions": ["B2", "B3", "B4"],
        "rows": rows,
        "notes": [
            "This computes exact editorial token counts, not grammatical validity or translation.",
            "The two published readings are not independent epigraphic observations.",
            "Preserve ŕ/r and ś/s distinctions; never use neutralization for identity.",
            "Scenario numbers match the existing IberOS Drive register.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="IberOS Serreta D1 formal sensitivity (8 cases)")
    parser.add_argument("--json", type=Path, help="Write reproducible JSON results")
    parser.add_argument("--csv", type=Path, help="Write scenario metrics CSV")
    args = parser.parse_args(argv)
    result = run()
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", encoding="utf-8", newline="") as file:
            fields = list(result["rows"][0])
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(result["rows"])
    if not args.json and not args.csv:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
