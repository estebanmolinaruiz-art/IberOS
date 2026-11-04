"""Evidence-specific reconciliation for La Vispesa and Pech-Maho in frozen FULL3406.

Read-only: no reassignment of splits, no physical equivalence inference,
and no creation of grammatical gold labels.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

PECH_TEXT_UIDS = (
    "RAN21,p61.Pech-Maho B.7.38 (plom6)principal@R3657",
    "CE12, P15, 1.7 Pech Maho V B.7.38 AI@R4192",
)
PECH_EDITORIAL_NOTE_UID = (
    "***CE12, P15, 1 S'ha mantingut lectura inicial de tots els ploms, "
    "excepte B.7.38. Per revisar la que proposa autor, internet@R4467"
)
VISPESA_UIDS = ("d.12.1 a@R1701", "d.12.2@R1703")
FROZEN_KEY = "dependency_key_v3_4_9"
FROZEN_SPLIT = "split_v3_4_9"


def reconcile(records: list[dict[str, Any]]) -> dict[str, Any]:
    selected = [*PECH_TEXT_UIDS, PECH_EDITORIAL_NOTE_UID, *VISPESA_UIDS]
    matches: dict[str, list[dict[str, Any]]] = {uid: [] for uid in selected}
    for record in records:
        if record.get("uid") in matches:
            matches[record["uid"]].append(record)
    issues = [f"MISSING_OR_DUPLICATE_UID:{uid}" for uid, found in matches.items()
              if len(found) != 1]
    if issues:
        return {"experiment": "EPI_IDENTITY_RESOLUTION_01",
                "status": "FAIL_CLOSED", "issues": issues, "scientific_promotion": False}
    pech = [matches[uid][0] for uid in PECH_TEXT_UIDS]
    note = matches[PECH_EDITORIAL_NOTE_UID][0]
    vispesa = [matches[uid][0] for uid in VISPESA_UIDS]
    pkeys = {r.get(FROZEN_KEY) for r in [*pech, note]}
    vsplits = [r.get(FROZEN_SPLIT) for r in vispesa]
    if len(pkeys) != 1 or None in pkeys:
        issues.append("PECH_DEPENDENCY_NOT_SINGLE")
    if any(r.get(FROZEN_SPLIT) != "VAL" for r in [*pech, note]):
        issues.append("PECH_SPLIT_CHANGED")
    if not all(r.get("signature") for r in pech):
        issues.append("PECH_READING_MISSING")
    if note.get("signature") not in ("", None):
        issues.append("EDITORIAL_NOTE_IS_NOT_EMPTY")
    if vsplits != ["HOLD", "TRAIN"]:
        issues.append("VISPESA_SPLITS_CHANGED")
    if len({r.get(FROZEN_KEY) for r in vispesa}) != 2:
        issues.append("VISPESA_DEPENDENCY_KEY_CHANGED")
    return {
        "experiment": "EPI_IDENTITY_RESOLUTION_01",
        "status": "PASS_WITH_EPISTEMIC_LOCKS" if not issues else "FAIL_CLOSED",
        "issues": issues,
        "pech_maho": {
            "mlh": "B.7.38",
            "historical_entries": 3,
            "textual_reading_records": 2,
            "editorial_notes_excluded_from_text_analysis": 1,
            "physical_documents_proven": 1 if not issues else None,
            "independent_texts": 1 if not issues else None,
            "frozen_dependency_group_count": len(pkeys),
            "frozen_split": "VAL",
            "reading_uids": list(PECH_TEXT_UIDS),
            "non_text_uid": PECH_EDITORIAL_NOTE_UID,
            "status": "EDITORIAL_VARIANTS_OF_ONE_LEAD_OBJECT_NOT_INDEPENDENT",
            "gold_grammatical_labels": None,
        },
        "la_vispesa": {
            "mlh": ["D.12.1", "D.12.2"],
            "historical_uids": list(VISPESA_UIDS),
            "split_original": dict(zip(VISPESA_UIDS, vsplits)),
            "inscribed_stone_groups": 2,
            "same_monument": "DISPUTED_IN_LITERATURE",
            "prospective_group": "LA_VISPESA_CONSERVATIVE_SAME_MONUMENT_RISK",
            "prospective_holdout_eligible": False,
            "status": "DISTINCT_INSCRIBED_FRAGMENTS_UNRESOLVED_MONUMENTAL_DEPENDENCY",
            "note": "A shared evaluation exclusion is recommended WITHOUT rewriting frozen splits or dependency keys.",
        },
        "original_records_modified": False,
        "original_splits_modified": False,
        "semantic_gold_available": 0,
        "scientific_promotion": False,
    }


def audit_file(path: Path) -> dict[str, Any]:
    from .legacy_bridge import audit_file as legacy_check
    integrity = legacy_check(path)
    if not integrity["integrity"]["valid"]:
        raise ValueError("FULL3406_NOT_VERIFIED")
    document = json.loads(path.read_bytes())
    return reconcile(document["records"])


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Read-only evidence reconciliation for La Vispesa and Pech-Maho")
    p.add_argument("snapshot", type=Path)
    p.add_argument("--json", type=Path)
    a = p.parse_args(argv)
    result = audit_file(a.snapshot)
    out = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if a.json:
        if a.json.resolve() == a.snapshot.resolve():
            raise ValueError("REFUSING_TO_OVERWRITE_SNAPSHOT")
        a.json.parent.mkdir(parents=True, exist_ok=True)
        a.json.write_text(out, encoding="utf-8")
    else:
        print(out, end="")
    return 0 if result["status"] == "PASS_WITH_EPISTEMIC_LOCKS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
