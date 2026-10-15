#!/usr/bin/env python3
"""Turn exported library metadata JSONL into a review-only CORE intake inbox."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from iberos.library_ingest import triage_library_records

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input", required=True,help="Library source records in JSONL")
    ap.add_argument("--output",default="site/data/library_core_inbox_v1.json")
    args=ap.parse_args()
    records=[]
    for number,line in enumerate(Path(args.input).read_text(encoding="utf-8-sig").splitlines(),1):
        if not line.strip():
            continue
        value=json.loads(line)
        if not isinstance(value,dict):
            raise ValueError(f"Line {number}: expected JSON object")
        records.append(value)
    report=triage_library_records(records)
    target=Path(args.output)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(f"Documentation records in review: {report['document_count']}; new validated independent objects: 0")

if __name__=="__main__":
    main()
