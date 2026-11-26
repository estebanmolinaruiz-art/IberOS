#!/usr/bin/env python3
"""DISCOVER-01: zero-cost evidence readiness, object leakage and falsification gates.

Runs on existing IberOS data only. Makes NO semantic or photographic claims.
"""
import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def load(root):
    root = Path(root)
    assets = {
        "registry": root / "data/curated/iberos_objects_registry_v2.0.csv",
        "links": root / "data/curated/iberos_partial_entry_link_v2.4.csv",
        "visual": root / "site/data/epigraphic-visual-registry-v1.json",
        "alignment": root / "data/review/validation01_orleyl_17_visual_alignment_v1.csv",
        "matcher": root / "data/review/iberos_visual_matcher_manifest_v08.csv",
    }
    return assets, {k: (json.loads(p.read_text(encoding="utf-8"))
                       if k == "visual" else rows(p))
                    for k, p in assets.items()}


def assess(root):
    assets, sources = load(root)
    objects = sources["registry"]
    links = sources["links"]
    visual = sources["visual"]["records"]
    alignment = sources["alignment"]
    matcher = sources["matcher"]
    by_object = {x["OBJECT_ID"]: x for x in objects}
    link_ids = {x["OBJECT_ID"] for x in links}
    visual_ids = {x["object_id"] for x in visual}
    duplications = [x for x,n in Counter(x["OBJECT_ID"] for x in objects).items() if n > 1]
    candidates = []
    for item in objects:
        oid = item["OBJECT_ID"]
        source = item.get("Fuente","").strip()
        candidates.append({
            "object_id": oid,
            "object": item.get("Nombre_objeto",""),
            "site": item.get("Yacimiento",""),
            "support": item.get("Soporte",""),
            "corpus_role": item.get("IberOS_Inclusion",""),
            "has_source_url": source.startswith("https://") or source.startswith("http://"),
            "has_external_entry_link": oid in link_ids,
            "has_visual_documentary_record": oid in visual_ids,
            "has_verified_original_sign_crops": False,
            "has_independent_semantic_gold": False,
            "eligible_for_blind_semantic_benchmark": False,
            "required_next_evidence": "physical sign crops with independent glyph and contextual adjudication",
        })
    matcher_statuses = Counter(x.get("evidence_status","") for x in matcher)
    confirmed_images = [
        r for r in visual if r.get("exact_object_match_verified") is True
        and r.get("image_url") and r.get("glyphs")
        and any(g.get("reviewed") is True for g in r.get("glyphs", []))
    ]
    unverified = [r for r in alignment if r.get("coordinate_verification","").startswith("UNVERIFIED")]
    # The physically disjoint split is a *rule*, not an invented train/test partition.
    return {
        "protocol": "IBEROS-DISCOVER-01",
        "source_sha256": {k: hashlib.sha256(v.read_bytes()).hexdigest() for k,v in assets.items()},
        "curated_object_rows": len(objects),
        "unique_curated_objects": len(by_object),
        "duplicate_object_ids": duplications,
        "external_link_rows": len(links),
        "visual_registry_rows": len(visual),
        "verified_linked_sign_images": len(confirmed_images),
        "existing_visual_alignment_rows": len(alignment),
        "unverified_coordinate_rows": len(unverified),
        "visual_matcher_training_rows": len(matcher),
        "visual_matcher_evidence_statuses": dict(matcher_statuses),
        "ready_for_automatic_glyph_training": len(confirmed_images) > 0 and len(matcher) > 0,
        "ready_for_semantic_model_comparison": False,
        "model_comparison": {
            "phonetic": "BASELINE_DEFINED_NOT_TESTED",
            "logographic": "ALTERNATIVE_DEFINED_NOT_TESTED",
            "mixed": "ALTERNATIVE_DEFINED_NOT_TESTED",
            "nonlinguistic_marks": "NEGATIVE_CONTROL_DEFINED_NOT_TESTED",
            "holdout_accuracy": None,
            "semantic_gold_count": 0,
            "result": "ABSTAIN_NO_INDEPENDENT_SEMANTIC_GOLD",
        },
        "physical_split_policy": "PHYS_ID/LEAK_GROUP disjoint, same object and all faces always same split; same site sensitivity test",
        "negative_control_policy": "Do not score anepigraphic amphora marks as iberian graphemes; compare against shuffled context and positional controls",
        "guardrail": "No retrospective match or editorial-copy reading can be promoted to Core, translation or achievement",
        "object_evidence_queue": candidates,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=".")
    p.add_argument("--output")
    args = p.parse_args()
    obj = assess(args.root)
    report = json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
    else:
        print(report, end="")


if __name__ == "__main__":
    main()
