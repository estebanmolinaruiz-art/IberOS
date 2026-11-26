#!/usr/bin/env python3
"""IBEROS-ASSOC-02: join existing Write glyph labels and signary candidates.

This is a documentary association bridge, NOT OCR and NOT lexical translation.
Zero external dependencies. Never changes src/iberos/core.py or authority state.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

WRITE_VALUES = tuple("a e i o u l m n r ŕ s ba be bi bo bu ta te ti to tu ka ke ki ko ku".split())


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def from_write_page(path):
    page = Path(path).read_text(encoding="utf-8")
    match = re.search(r"const glyphFiles=\{(.*?)\};", page, flags=re.S)
    if match is None:
        raise ValueError("Write glyphFiles mapping not found")
    # Extract only the conventional value and SVG filename; no JavaScript execution.
    pairs = re.findall(r'(?:"([^"]+)"|([a-z]+)):"(NE Iberian [^"]+\.svg)"', match.group(1))
    glyphs = {quoted or bare: filename for quoted, bare, filename in pairs}
    if set(glyphs) != set(WRITE_VALUES):
        raise ValueError("Unexpected Write signary; manual review required: " + str(sorted(set(glyphs) ^ set(WRITE_VALUES))))
    return glyphs


def normalize_value(value):
    v = str(value).strip().lower()
    # Only case-normalization: NO automatic DA/TA, DO/TO, GI/KI, R/R1 or dual equivalence.
    return v


def build(root):
    root = Path(root)
    write_path = root / "site/write/index.html"
    signary_path = root / "data/review/cathalaunia_signary_review_queue_286_v2.csv"
    orleyl_path = root / "data/curated/rok_orleyl_editorial_alignment_1981.csv"
    glyphs = from_write_page(write_path)
    with signary_path.open(encoding="utf-8-sig", newline="") as handle:
        signary = list(csv.DictReader(handle))
    with orleyl_path.open(encoding="utf-8-sig", newline="") as handle:
        orleyl = list(csv.DictReader(handle))
    variants = []
    for rec in signary:
        original = rec["source_value_candidate"]
        normalized = normalize_value(original)
        direct = bool(original) and normalized in glyphs and rec["review_queue"] == "SIMPLE_SOURCE_LABEL"
        variants.append({
            "unicode_decimal": rec["unicode_decimal"],
            "source_variant_label": rec["source_variant_label"],
            "source_value_candidate": original,
            "write_value": normalized if direct else None,
            "write_svg_filename": glyphs[normalized] if direct else None,
            "review_queue": rec["review_queue"],
            "independent_review": rec["independent_review"],
            "usable_for_auto_reading": False,
            "status": "DOCUMENTARY_LABEL_JOIN_NOT_VISUALLY_VERIFIED" if direct else "REQUIRES_PALEOGRAPHIC_REVIEW",
            "source_url": rec["source_url"],
        })
    alignments = []
    for rec in orleyl:
        normalized = normalize_value(rec["editorial_token"])
        alignments.append({
            "witness": rec["witness"],
            "phys_key": rec["phys_key"],
            "line": rec["line"],
            "token_index": rec["token_index"],
            "editorial_token": rec["editorial_token"],
            "direct_write_value": normalized if normalized in glyphs else None,
            "source_page": rec["primary_page_pdf"],
            "image_page": rec["primary_image_pdf"],
            "original_editorial_status": rec["editorial_status"],
            "graphic_photo_verified": rec["graphic_photo_verified"],
            "status": "EDITORIAL_ONLY_NOT_INDEPENDENT_READING",
        })
    return {
        "protocol": "IBEROS-ASSOC-02",
        "source_sha256": {str(path.relative_to(root)): sha256(path)
            for path in (write_path, signary_path, orleyl_path)},
        "write_graphic_values": len(glyphs),
        "catalogue_candidate_rows": len(signary),
        "simple_source_labels": sum(x["review_queue"] == "SIMPLE_SOURCE_LABEL" for x in variants),
        "direct_documentary_joins": sum(x["write_value"] is not None for x in variants),
        "candidate_types": dict(Counter(x["review_queue"] for x in variants)),
        "orleyl_editorial_tokens": len(alignments),
        "orleyl_photographically_confirmed_tokens": sum(x["graphic_photo_verified"] == "true" for x in alignments),
        "visual_recognition_accuracy": None,
        "semantic_validation": "NOT_EVALUATED",
        "core_modified": False,
        "readiness": "DOCUMENTARY_BRIDGE_ONLY",
        "variants": variants,
        "orleyl_alignment": alignments,
        "warnings": [
            "No source-labelled variant is automatically a verified glyph crop.",
            "Latin/modern sign values are transliterations, not translated word meanings.",
            "Do not infer DA/TA, DO/TO, GI/KI, dual series or rhotic identities.",
            "The Orleyl table uses editorial readings only; not photographic OCR.",
            "PHYS_ID/LEAK_GROUP separation and prospective HOLD required for scientific validation.",
        ],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path("."))
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    data = json.dumps(build(a.root), ensure_ascii=False, indent=2) + "\n"
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(data, encoding="utf-8")
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
