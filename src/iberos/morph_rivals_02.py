"""MORPH-RIVALS-02: cluster-aware terminal-position checks on TRAIN/VAL only.

Retrospective diagnostics. HOLD contents are never scored or read for motifs.
No semantic interpretations or prospective performance are inferred.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import json
import re
from pathlib import Path
from typing import Any

MOTIFS = {"BI_N": ("BI", "N"), "BA_N": ("BA", "N"),
          "A_N": ("A", "N"), "BI_R1": ("BI", "R1")}
SPLITS = ("TRAIN", "VAL")
BOUNDARY = re.compile(r"[¦:;∏│]")


def segments(text: str) -> list[list[str]]:
    return [[x for x in part.strip().upper().split("-") if x]
            for part in BOUNDARY.split(text) if part.strip()]


def analyze(records: list[dict[str, Any]]) -> dict[str, Any]:
    seen: set[str] = set()
    groups_by_split: dict[str, set[str]] = {k: set() for k in SPLITS}
    counts: dict[str, dict[str, dict[str, Any]]] = {
        s: {m: {"occurrences": 0, "terminal_occurrences": 0,
                 "records": set(), "groups": set(), "terminal_groups": set()}
            for m in MOTIFS} for s in SPLITS
    }
    errors = []
    skipped = {"HOLD": 0, "EXCLUDED": 0}
    for i, row in enumerate(records):
        if not isinstance(row, dict):
            errors.append(f"NON_OBJECT:{i}")
            continue
        split = row.get("split_v3_4_9")
        if split in skipped:
            skipped[split] += 1
            continue  # Do not access signature of HOLD or EXCLUDED.
        if split not in SPLITS:
            errors.append(f"INVALID_SPLIT:{i}")
            continue
        uid, dep = row.get("uid"), row.get("dependency_key_v3_4_9")
        if not isinstance(uid, str) or not uid or uid in seen:
            errors.append(f"DUPLICATE_OR_MISSING_UID:{i}")
            continue
        if not isinstance(dep, str) or not dep:
            errors.append(f"MISSING_GROUP:{i}")
            continue
        if not isinstance(row.get("signature"), str):
            errors.append(f"BAD_SIGNATURE:{i}")
            continue
        seen.add(uid)
        groups_by_split[split].add(dep)
        for seg in segments(row["signature"]):
            for pos in range(len(seg) - 1):
                pair = tuple(seg[pos:pos+2])
                for name, motif in MOTIFS.items():
                    if pair != motif:
                        continue
                    v = counts[split][name]
                    v["occurrences"] += 1
                    v["records"].add(uid)
                    v["groups"].add(dep)
                    if pos == len(seg) - 2:
                        v["terminal_occurrences"] += 1
                        v["terminal_groups"].add(dep)
    if errors:
        return {"experiment": "MORPH_RIVALS_02", "valid": False,
                "issues": errors[:30], "hold_scored": False}
    if groups_by_split["TRAIN"] & groups_by_split["VAL"]:
        return {"experiment": "MORPH_RIVALS_02", "valid": False,
                "issues": ["TRAIN_VAL_DEPENDENCY_OVERLAP"], "hold_scored": False}
    metrics = {}
    for split in SPLITS:
        metrics[split] = {}
        for name, v in counts[split].items():
            n = v["occurrences"]
            g = len(v["groups"])
            terminal_groups = len(v["terminal_groups"])
            metrics[split][name] = {
                "occurrences": n,
                "terminal_occurrences": v["terminal_occurrences"],
                "terminal_occurrence_fraction": round(v["terminal_occurrences"] / n, 6) if n else None,
                "uid_records": len(v["records"]),
                "dependency_groups": g,
                "dependency_groups_with_terminal_occurrence": terminal_groups,
                "terminal_group_fraction": round(terminal_groups / g, 6) if g else None,
            }
    return {
        "experiment": "MORPH_RIVALS_02", "valid": True,
        "comparison_status": "RETROSPECTIVE_POST_HOC_LEGACY_DATA",
        "original_record_count": len(records),
        "excluded_from_analysis": skipped,
        "hold_scored": False, "hold_records_inspected_for_signature": 0,
        "metrics": metrics,
        "observations": {
            split: {
                "BI_N_vs_BA_N_terminal_delta": round(
                    metrics[split]["BI_N"]["terminal_occurrence_fraction"]
                    - metrics[split]["BA_N"]["terminal_occurrence_fraction"], 6)
                if (metrics[split]["BI_N"]["terminal_occurrence_fraction"] is not None
                    and metrics[split]["BA_N"]["terminal_occurrence_fraction"] is not None)
                else None,
                "cluster_independence_p_value": None,
            } for split in SPLITS
        },
        "rival_interpretations": {
            "H_POSITIONAL_SUFFIX": "BI-N enriched at terminal positions vs BA-N; no predicted advantage observed in old snapshot.",
            "H_CONTEXTUAL_NON_SUFFIX": "BI-N position differs by context or appears internally; not equivalent to no grammar.",
            "H_NUMERIC_BI_N": "BI-N numeral or quantity marker; NOT TESTED: no independent numeric gold.",
        },
        "future_test_gate": "New externally sourced and pre-registered inscriptions never seen in FULL3406, split by physical object; independent sign readings and context gold.",
        "semantic_gold": 0, "linguistic_translation_validated": False,
        "legacy_splits_modified": False, "official_metrics_changed": False,
    }


def analyze_file(path: Path) -> dict[str, Any]:
    from .legacy_bridge import audit_file as audit_legacy
    checked = audit_legacy(path)
    if not checked["integrity"]["valid"]:
        raise ValueError("FULL3406_INTEGRITY_FAILED")
    document = json.loads(path.read_bytes())
    return analyze(document["records"])


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Retrospective clustered motif comparison; HOLD is sealed")
    p.add_argument("snapshot", type=Path)
    p.add_argument("--json", type=Path)
    args = p.parse_args(argv)
    report = analyze_file(args.snapshot)
    output = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.json:
        if args.snapshot.resolve() == args.json.resolve():
            raise ValueError("REFUSE_OVERWRITE_ORIGINAL")
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0 if report["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
