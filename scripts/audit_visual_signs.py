#!/usr/bin/env python3
"""Export conservative sign-review readiness from existing IberOS Core sources.

Normal execution reports the evidence gaps. --require-adjudicated deliberately
fails until there is independently adjudicated sign evidence in a separate
approved registry. Never substitute editorial difference scores for a glyph.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from iberos.visual_adjudication import audit_repository


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--output", type=Path)
    p.add_argument("--require-adjudicated", action="store_true")
    args = p.parse_args(argv)
    result = audit_repository(args.root)
    body = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(body, encoding="utf-8")
    else:
        print(body, end="")
    if args.require_adjudicated and result["independently_verified_glyphs"] == 0:
        print("IberOS: independent sign validation remains blocked; editorial comparisons are not glyph autopsies.",
              file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
