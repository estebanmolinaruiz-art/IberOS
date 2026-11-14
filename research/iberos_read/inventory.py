#!/usr/bin/env python3
"""IBEROS-READ-02: reproducible local inventory / readiness gate.

Run from repository root; never claims a sign has been read from an image.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

EXTS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".svg"}


def inventory(root):
    root = Path(root)
    assets = sorted(
        p for p in root.rglob("*")
        if p.is_file() and p.suffix.lower() in EXTS and ".git" not in p.parts
    )
    registry = root / "site/data/epigraphic-visual-registry-v1.json"
    manifest = root / "data/review/iberos_visual_matcher_manifest_v08.csv"
    records = json.loads(registry.read_text(encoding="utf-8"))["records"]
    with manifest.open(encoding="utf-8-sig", newline="") as f:
        samples = list(csv.DictReader(f))
    status = {}
    for r in records:
        status[r["status"]] = status.get(r["status"], 0) + 1
    candidates = []
    for r in records:
        candidates.append({
            "object_id": r["object_id"],
            "status": r["status"],
            "figure_locator": r.get("figure_locator"),
            "source_url": r.get("source_url"),
            "source_figure_url": r.get("source_figure_url"),
            "image_url": r.get("image_url"),
            "rights_verified": bool(r.get("rights_verified")),
            "glyphs_reviewed": sum(bool(g.get("reviewed")) for g in r.get("glyphs", [])),
            "recognition_state": "BLOCKED_NO_REVIEWED_LOCAL_PHOTO_AND_SIGN_CROPS",
        })
    return {
        "protocol": "IBEROS-READ-02",
        "audit_scope": "LOCAL_REPOSITORY_ONLY",
        "total_graphic_assets": len(assets),
        "extensions": {e: sum(p.suffix.lower() == e for p in assets) for e in sorted(EXTS)},
        "assets": [{"path": str(p.relative_to(root)).replace("\\", "/"),
                    "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in assets],
        "epigraphic_registry_objects": len(records),
        "epigraphic_statuses": status,
        "registry_direct_image_urls": sum(bool(r.get("image_url")) for r in records),
        "registry_rights_verified": sum(bool(r.get("rights_verified")) for r in records),
        "registry_reviewed_glyphs": sum(sum(bool(g.get("reviewed")) for g in r.get("glyphs", [])) for r in records),
        "reviewed_matcher_samples": sum(r.get("evidence_status") == "REVIEWED_SIGN" for r in samples),
        "independent_real_photo_accuracy": None,
        "scientifically_validated": False,
        "objects": candidates,
        "note": "Website covers, illustrations and renders are NOT archaeological source photographs. External figures are only references until verified and available for processing.",
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=Path("."))
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    report = inventory(a.root)
    data = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if a.output:
        a.output.write_text(data, encoding="utf-8")
    else:
        print(data, end="")


if __name__ == "__main__":
    main()
