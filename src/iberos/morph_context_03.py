"""MORPH-CONTEXT-03: dependency-aware graphemic neighbors and support labels.

Retrospective historical examination. HOLD is not scored or read for motif
signatures. Editorial support labels are never normalized into archaeological
claims and no observed adjacency is a translation.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
from .legacy_bridge import audit_file as check_original

SPLITS = ("TRAIN", "VAL")
MOTIFS = {"BI_N": ("BI", "N"), "BA_N": ("BA", "N"),
          "A_N": ("A", "N"), "BI_R1": ("BI", "R1")}
BOUNDARY = re.compile(r"[¦:;∏│]")


def read_segments(signature: str) -> list[list[str]]:
    return [[token for token in seg.strip().upper().split("-") if token]
            for seg in BOUNDARY.split(signature) if seg.strip()]


def _rank_counts(counter: Counter, n: int = 12) -> list[dict]:
    return [{"token": token, "count": count} for token, count in counter.most_common(n)]


def analyze(records: list[dict]) -> dict:
    seen = set()
    dependency_split = {}
    observations: dict[str, dict[str, list[dict]]] = {
        split: {name: [] for name in MOTIFS} for split in SPLITS
    }
    skips = {"HOLD": 0, "EXCLUDED": 0}
    errors = []
    for i, row in enumerate(records):
        if not isinstance(row, dict):
            errors.append(f"NON_OBJECT:{i}")
            continue
        split = row.get("split_v3_4_9")
        if split in skips:
            skips[split] += 1
            continue  # Do not access these signatures at all.
        if split not in SPLITS:
            errors.append(f"BAD_SPLIT:{i}")
            continue
        uid, dep = row.get("uid"), row.get("dependency_key_v3_4_9")
        if not isinstance(uid, str) or not uid or uid in seen:
            errors.append(f"BAD_UID:{i}")
            continue
        seen.add(uid)
        if not isinstance(dep, str) or not dep:
            errors.append(f"BAD_DEPENDENCY:{i}")
            continue
        if dep in dependency_split and dependency_split[dep] != split:
            errors.append(f"TRAIN_VAL_GROUP_LEAK:{dep}")
            continue
        dependency_split[dep] = split
        sig = row.get("signature")
        if not isinstance(sig, str):
            errors.append(f"BAD_SIGNATURE:{i}")
            continue
        support = row.get("support")
        support = support.strip() if isinstance(support, str) and support.strip() else "<UNKNOWN>"
        for seg in read_segments(sig):
            for at in range(len(seg) - 1):
                pair = tuple(seg[at:at + 2])
                for name, wanted in MOTIFS.items():
                    if pair != wanted:
                        continue
                    observations[split][name].append({
                        "uid": uid, "dep": dep, "support": support,
                        "prior": seg[at - 1] if at else "<START>",
                        "next": seg[at + 2] if at + 2 < len(seg) else "<END>",
                        "terminal": at + 2 == len(seg),
                        "initial": at == 0,
                    })
    if errors:
        return {"experiment": "MORPH_CONTEXT_03", "valid": False,
                "issues": errors[:30], "hold_scored": False}
    results = {}
    for split in SPLITS:
        results[split] = {}
        for name, events in observations[split].items():
            dgroups = {x["dep"] for x in events}
            support = Counter(x["support"] for x in events)
            group_occ = Counter(x["dep"] for x in events)
            results[split][name] = {
                "occurrences": len(events),
                "uid_records": len({x["uid"] for x in events}),
                "dependency_groups": len(dgroups),
                "initial_occurrences": sum(x["initial"] for x in events),
                "terminal_occurrences": sum(x["terminal"] for x in events),
                "groups_with_terminal": len({x["dep"] for x in events if x["terminal"]}),
                "groups_with_missing_support": len({
                    x["dep"] for x in events if x["support"] == "<UNKNOWN>"
                }),
                "max_occurrences_in_one_dependency_group": max(group_occ.values(), default=0),
                "preceding_signs": _rank_counts(Counter(x["prior"] for x in events)),
                "following_signs": _rank_counts(Counter(x["next"] for x in events)),
                "editorial_support_labels": _rank_counts(support),
            }
    return {
        "experiment": "MORPH_CONTEXT_03", "valid": True,
        "data_mode": "RETROSPECTIVE_DESCRIPTIVE_NOT_INDEPENDENT_VALIDATION",
        "original_record_count": len(records), "excluded_from_motif_analysis": skips,
        "hold_scored": False, "hold_signatures_inspected": 0,
        "results": results,
        "independent_context_gold": False,
        "numeric_gold_available": False,
        "translation_validated": False,
        "official_metrics_changed": False,
        "frozen_partitions_modified": False,
        "limitations": [
            "Neighbor symbols are graphemic adjacency, not grammar or semantic roles",
            "Support values are raw editorial labels; missing does not mean unknown archaeological support",
            "Dependencies group repeated editions, not necessarily physical identity",
            "No new blinded sample, no p-values, no hypothesis promotion",
        ],
        "next_gate": "Pre-register numerical-context labels from independent artifact evidence; avoid previously seen HOLD and historical texts",
    }


def analyze_file(path: Path) -> dict:
    base = check_original(path)
    if not base["integrity"]["valid"]:
        raise ValueError("FULL3406_INTEGRITY_FAILED")
    return analyze(json.loads(path.read_bytes())["records"])


def main(argv=None):
    p = argparse.ArgumentParser(description="IberOS frozen corpus contextual morphology analysis")
    p.add_argument("snapshot", type=Path)
    p.add_argument("--json", type=Path)
    args = p.parse_args(argv)
    result = analyze_file(args.snapshot)
    output = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.json:
        if args.json.resolve() == args.snapshot.resolve():
            raise ValueError("CANNOT_OVERWRITE_FROZEN_SNAPSHOT")
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0 if result["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
