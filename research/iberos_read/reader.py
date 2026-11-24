#!/usr/bin/env python3
"""IBEROS-READ-01: reproducible visual sign-matching baseline; NOT decipherment.

Input: real inscription image, manually defined pixel bounding boxes, local PNG
reference crops labelled with WRITE sign values. Does not use editorial readings.
Requires free packages: opencv-python and numpy.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

WRITE_SIGNS = tuple("a e i o u l m n r ŕ s ba be bi bo bu ta te ti to tu ka ke ki ko ku".split())


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cv():
    try:
        import cv2
        import numpy as np
    except ImportError as exc:
        raise SystemExit("Install free dependencies: pip install opencv-python numpy") from exc
    return cv2, np


def normalized_mask(image, side=64):
    """Otsu binarization, tight ink bounds and scale-preserving centering."""
    cv2, np = cv()
    if image is None or image.size == 0:
        raise ValueError("Missing or empty sign crop")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # Prefer the minority colour as ink. Reject essentially blank crops.
    if np.count_nonzero(binary) > binary.size / 2:
        binary = cv2.bitwise_not(binary)
    ys, xs = np.nonzero(binary)
    if len(xs) < 3:
        raise ValueError("Insufficient visible ink")
    tight = binary[ys.min():ys.max()+1, xs.min():xs.max()+1]
    h, w = tight.shape
    scale = (side - 12) / max(h, w)
    resized = cv2.resize(tight, (max(1, round(w*scale)), max(1, round(h*scale))),
                         interpolation=cv2.INTER_NEAREST)
    canvas = np.zeros((side, side), dtype=np.uint8)
    y = (side - resized.shape[0]) // 2
    x = (side - resized.shape[1]) // 2
    canvas[y:y+resized.shape[0], x:x+resized.shape[1]] = resized
    return canvas


def load_templates(directory):
    cv2, np = cv()
    directory = Path(directory)
    templates = []
    for path in sorted(directory.glob("*.png")):
        sign = path.stem.split("__", 1)[0]
        if sign not in WRITE_SIGNS:
            continue
        image = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
        if image is None:
            continue
        try:
            mask = normalized_mask(image)
        except ValueError:
            continue
        templates.append((sign, path.name, mask, digest(path)))
    if not templates:
        raise ValueError("No usable local PNG templates; expected ba__variant.png etc.")
    return templates


def classify_crop(crop, templates, min_score=0.72, min_margin=0.08):
    cv2, np = cv()
    try:
        mask = normalized_mask(crop)
    except ValueError:
        return {"status": "ABSTAIN", "reason": "NO_VISIBLE_INK", "candidates": []}
    rankings = []
    for sign, filename, ref, sha in templates:
        # Explicit fixed-pixel baseline; no learned model or semantic inference.
        diff = np.mean(np.abs(mask.astype(np.float32) - ref.astype(np.float32))) / 255
        score = float(round(1 - diff, 6))
        rankings.append({"sign": sign, "score": score, "template": filename,
                         "template_sha256": sha})
    best_per_sign = {}
    for result in rankings:
        name = result["sign"]
        if name not in best_per_sign or result["score"] > best_per_sign[name]["score"]:
            best_per_sign[name] = result
    ranked = sorted(best_per_sign.values(), key=lambda v: (-v["score"], v["sign"]))
    best = ranked[0]
    margin = best["score"] - ranked[1]["score"] if len(ranked) > 1 else 1.0
    status = "CANDIDATE" if best["score"] >= min_score and margin >= min_margin else "ABSTAIN"
    return {"status": status, "prediction": best["sign"] if status == "CANDIDATE" else None,
            "margin": round(margin, 6), "candidates": ranked[:3]}


def run(image_path, boxes_path, templates_dir, min_score=0.72, min_margin=0.08):
    cv2, np = cv()
    image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Cannot load image")
    boxes = json.loads(Path(boxes_path).read_text(encoding="utf-8"))
    if not isinstance(boxes, list):
        raise ValueError("Boxes must be a JSON array")
    templates = load_templates(templates_dir)
    height, width = image.shape[:2]
    results = []
    for i, rect in enumerate(boxes):
        x, y, w, h = (rect[k] for k in ("x", "y", "w", "h"))
        if any(type(v) is not int for v in (x, y, w, h)) or x < 0 or y < 0 or w <= 0 or h <= 0 or x+w > width or y+h > height:
            raise ValueError(f"Invalid bounding box {i}")
        prediction = classify_crop(image[y:y+h, x:x+w], templates, min_score, min_margin)
        results.append({"index": i, "box": rect, **prediction})
    return {
        "protocol": "IBEROS-READ-01", "classification": "EXPERIMENTAL_VISUAL_BASELINE",
        "image_sha256": digest(image_path), "boxes_sha256": digest(boxes_path),
        "template_count": len(templates), "sign_classes": len(set(t[0] for t in templates)),
        "thresholds": {"min_score": min_score, "min_margin": min_margin},
        "readings": results, "estimated_translation": None,
        "scientifically_validated": False,
        "limitations": ["Manual sign bounding boxes", "Local PNG templates required",
                        "Pixel matching is sensitive to damage and sign variants",
                        "Not tested on independent archaeological inscriptions",
                        "No semantic inference or historical translation"],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--image", required=True, type=Path)
    ap.add_argument("--boxes", required=True, type=Path, help='JSON: [{"x":0,"y":0,"w":30,"h":40}]')
    ap.add_argument("--templates", required=True, type=Path)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--min-score", type=float, default=0.72)
    ap.add_argument("--min-margin", type=float, default=0.08)
    a = ap.parse_args()
    if not 0 <= a.min_score <= 1 or not 0 <= a.min_margin <= 1:
        ap.error("Thresholds must be in [0, 1]")
    report = run(a.image, a.boxes, a.templates, a.min_score, a.min_margin)
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if a.output:
        a.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
