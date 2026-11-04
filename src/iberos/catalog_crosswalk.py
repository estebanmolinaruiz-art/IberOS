"""Read-only MLH editorial concordance for frozen FULL3406. Never infer grammar."""
from __future__ import annotations
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

MLH = re.compile(r"(?<![A-Za-z0-9.])([A-GK]\.\d{1,2}\.\d{1,3})(?![0-9])", re.I)

def reference_codes(reference: str) -> list[str]:
    if re.match(r"^\s*(?:BDH|Hesperia)\b", reference, re.I):
        return []
    first = re.split(r"\s*[·/]\s*(?:Hesperia|BDH|GI\.|NA\.|MNAT|ELRH)\b",
                     reference, maxsplit=1, flags=re.I)[0]
    first = re.sub(r"\bMLH\s+", "", first, flags=re.I)
    out = []
    for m in MLH.finditer(first):
        code = m.group(1).lower()
        if code not in out:
            out.append(code)
        ext = re.match(r"-(\d{1,3})(?![0-9])", first[m.end():])
        if ext:
            alias = code.rsplit(".", 1)[0] + "." + ext.group(1)
            if alias not in out:
                out.append(alias)
    return out

def concordance(registry: list[dict], records: list[dict]) -> dict:
    results = []
    for obj in registry:
        source = obj.get("Referencia epigráfica", "")
        codes = reference_codes(source)
        hits = {}
        for code in codes:
            rx = re.compile(r"(?<![A-Za-z0-9.])" + re.escape(code) + r"(?![0-9])", re.I)
            initial = re.compile(r"^\s*" + re.escape(code) + r"(?![0-9])", re.I)
            for r in records:
                label = str(r.get("catalog_id", ""))
                if rx.search(label):
                    hits.setdefault(r["uid"], {
                        "uid": r["uid"], "catalog_id": label,
                        "split": r["split_v3_4_9"],
                        "dependency_key": r.get("dependency_key_v3_4_9"),
                        "reference_class": ("DIRECT_EDITORIAL_ID" if initial.match(label)
                                            else "EMBEDDED_REFERENCE_REVIEW"),
                    })
        entries = sorted(hits.values(), key=lambda item: item["uid"])
        splits = sorted({item["split"] for item in entries})
        status = ("NO_EXPLICIT_MLH_REFERENCE" if not codes
                  else "NO_TEXTUAL_MATCH" if not entries
                  else "MULTISPLIT_EDITORIAL_REFERENCE_REVIEW" if len(splits) > 1
                  else "EDITORIAL_REVIEW_REQUIRED" if any(
                      e["reference_class"] == "EMBEDDED_REFERENCE_REVIEW" for e in entries)
                  else "EDITORIAL_ID_MATCH_NEEDS_PHYSICAL_CROSSCHECK")
        results.append({
            "object_id": obj["OBJECT_ID"], "reference": source, "mlh_codes": codes,
            "status": status, "matching_entries": len(entries),
            "historical_splits": splits, "physical_identity_verified": False,
            "independence_certified": False, "entries": entries,
        })
    return {
        "experiment": "FULL3406_MLH_CROSSWALK_01",
        "registry_objects": len(results),
        "objects_with_any_candidate": sum(bool(r["entries"]) for r in results),
        "matched_uid_count": len({e["uid"] for r in results for e in r["entries"]}),
        "multisplit_reference_objects": [
            r["object_id"] for r in results if len(r["historical_splits"]) > 1],
        "status_counts": dict(Counter(r["status"] for r in results)),
        "cases": results, "original_splits_modified": False,
        "scientific_promotion": False,
        "note": "Editorial MLH matches only; physical identity and grammatical gold unverified.",
    }

def main(argv=None) -> int:
    from .legacy_bridge import audit_file, EXPECTED_SHA256
    p = argparse.ArgumentParser(description="IberOS frozen MLH crosswalk")
    p.add_argument("snapshot", type=Path)
    p.add_argument("curated_csv", type=Path)
    p.add_argument("--json", type=Path)
    a = p.parse_args(argv)
    if not audit_file(a.snapshot)["integrity"]["valid"]:
        raise ValueError("FULL3406_INTEGRITY_FAILED")
    records = json.loads(a.snapshot.read_bytes())["records"]
    with a.curated_csv.open(encoding="utf-8-sig", newline="") as file:
        curated = list(csv.DictReader(file))
    report = concordance(curated, records)
    report["full3406_sha256"] = EXPECTED_SHA256
    output = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if a.json:
        if a.json.resolve() in {a.snapshot.resolve(), a.curated_csv.resolve()}:
            raise ValueError("REFUSING_TO_OVERWRITE_INPUT")
        a.json.parent.mkdir(parents=True, exist_ok=True)
        a.json.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
