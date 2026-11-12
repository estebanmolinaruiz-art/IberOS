#!/usr/bin/env python3
"""Prepare the GitHub Pages build artifact for iberos-ia.com.

Only rewrite the generated site output, not historical repo documentation or
scientific source data. Run after the CORE export and integration audit, before
upload-pages-artifact. This does NOT configure GitHub Pages Settings or DNS.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

OLD_BASE = "https://estebanmolinaruiz-art.github.io/IberOS"
NEW_BASE = "https://iberos-ia.com"
TEXT_EXT = {".html", ".htm", ".xml", ".txt", ".css", ".js", ".mjs",
            ".json", ".webmanifest", ".svg", ".jsonld"}

def prepare_site(site: Path, *, check: bool = False) -> dict:
    if not (site / "index.html").is_file():
        raise FileNotFoundError(f"Site root not found: {site}/index.html")

    modified: list[str] = []
    old_refs = 0
    for path in sorted(site.rglob("*")):
        if not path.is_file() or path.is_symlink() or path.suffix.lower() not in TEXT_EXT:
            continue
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            raise ValueError(f"Expected UTF-8 web asset: {path}") from None
        matches = original.count(OLD_BASE)
        old_refs += matches
        if not matches:
            continue
        modified.append(path.relative_to(site).as_posix())
        if not check:
            path.write_text(original.replace(OLD_BASE, NEW_BASE), encoding="utf-8")

    if check and old_refs:
        raise AssertionError(f"Old public URL appears {old_refs} times in {modified[:15]}")
    if not check:
        # Validate the canonical website and crawler entry points in the build.
        homepage = (site / "index.html").read_text(encoding="utf-8")
        sitemap = (site / "sitemap.xml").read_text(encoding="utf-8")
        robots = (site / "robots.txt").read_text(encoding="utf-8")
        if f'href="{NEW_BASE}/"' not in homepage:
            raise AssertionError("Homepage canonical link for new domain not found")
        if f"<loc>{NEW_BASE}/</loc>" not in sitemap:
            raise AssertionError("Main page missing from new sitemap")
        if f"Sitemap: {NEW_BASE}/sitemap.xml" not in robots:
            raise AssertionError("robots.txt does not point to new sitemap")
    return {"mode": "check" if check else "rewrite",
            "changed_files": len(modified), "old_base_occurrences": old_refs,
            "sample_files": modified[:25]}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", type=Path, default=Path("site"))
    parser.add_argument("--check", action="store_true",
                        help="Fail if old GitHub Pages URL remains in the build artifact")
    args = parser.parse_args()
    print(json.dumps(prepare_site(args.site, check=args.check), ensure_ascii=False))

if __name__ == "__main__":
    main()
