#!/usr/bin/env python3
"""Export one standalone offline JSON data bundle; does not compile an app."""
from __future__ import annotations
import json
import argparse
from pathlib import Path
from iberos.core import load_registry, AUTHORITY
from iberos.mobile_sync import mobile_object_payload

def build_bundle() -> dict:
    objects = {x["OBJECT_ID"]: mobile_object_payload(x["OBJECT_ID"]) for x in load_registry()}
    return {"schema":"IberOS-Mobile-Bundle/1.0",
            "authority": dict(AUTHORITY), "object_count": len(objects),
            "objects": objects,
            "notice":"Offline research metadata; no confirmed automated decipherment."}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",default="site/data/mobile_core_bundle_v1.json")
    args=parser.parse_args()
    target=Path(args.out)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(build_bundle(),ensure_ascii=False,sort_keys=True,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
