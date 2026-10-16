#!/usr/bin/env python3
"""Process externally reviewed library readings into a non-promoting report."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from iberos.library_readings_bridge import analyze_library_readings

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--input",required=True)
    parser.add_argument("--output",default="site/data/library_reading_analysis_v1.json")
    args=parser.parse_args()
    rows=[]
    for number,line in enumerate(Path(args.input).read_text(encoding="utf-8-sig").splitlines(),1):
        if line.strip():
            item=json.loads(line)
            if not isinstance(item,dict):
                raise ValueError(f"Line {number}: expected JSON object")
            rows.append(item)
    report=analyze_library_readings(rows)
    dest=Path(args.output)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(f"Reading records: {report['reading_count']}; scientific translations promoted: 0")

if __name__=="__main__":
    main()
