#!/usr/bin/env python3
"""Create auditable *unannotated* Fletcher source panels; never assert glyph IDs.

Usage:
 python scripts/orleyl_prepare_source_panels.py --pdf Fletcher1981.pdf --out /tmp/orleyl-panels
Requires PyMuPDF (pip install pymupdf). Source PDF is not redistributed.
"""
import argparse
import hashlib
import json
from pathlib import Path

PAGES = {
    "orleyl_v_figure22": 65,
    "orleyl_viib_figure25": 111,
    "orleyl_v_photo_plate17": 153,
    "orleyl_viib_photo_plate22": 158,
}

def source_hash(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

def source_manifest(pdf, page_count, scale, panels):
    return {
        "schema": "IberOS-Orleyl-Source-Panels/1",
        "pdf_sha256": source_hash(pdf),
        "source_pdf_name": Path(pdf).name,
        "source_pdf_page_count": page_count,
        "render_scale": scale,
        "orientation": "AS_RENDERED_FROM_SOURCE_PDF_NOT_VERIFIED",
        "glyph_positions_verified": False,
        "panels": panels,
        "note": "Page numbers are one-based PDF pages, not printed pages. No crop or sign position is validated.",
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--scale", type=float, default=2.0)
    args = parser.parse_args()
    if args.scale <= 0 or args.scale > 6:
        parser.error("--scale must be >0 and <=6")
    if not args.pdf.is_file() or args.pdf.read_bytes()[:4] != b"%PDF":
        parser.error("The input must be an existing PDF")
    try:
        import fitz
    except ImportError as exc:
        parser.error("PyMuPDF is required: pip install pymupdf")
    args.out.mkdir(parents=True, exist_ok=True)
    panels = []
    with fitz.open(args.pdf) as doc:
        if len(doc) < max(PAGES.values()):
            parser.error("PDF does not have the expected 158 pages; verify source edition")
        for name, pdf_page in PAGES.items():
            page = doc[pdf_page - 1]
            pix = page.get_pixmap(matrix=fitz.Matrix(args.scale, args.scale), alpha=False)
            filename = name + ".png"
            pix.save(str(args.out / filename))
            panels.append({
                "name": name, "pdf_page": pdf_page, "file": filename,
                "dimensions_px": [pix.width, pix.height],
                "rotation_applied_degrees": 0, "editorial_target_only": True,
                "graphic_glyph_verification": "PENDING"
            })
        record = source_manifest(args.pdf, len(doc), args.scale, panels)
    (args.out / "source_manifest.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(str(args.out / "source_manifest.json"))

if __name__ == "__main__":
    main()
