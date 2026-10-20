"""Export a reproducible 6P-03 corpus-to-evidence linking diagnostic."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from iberos.corpus_evidence_bridge import link_repository

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument("--out",type=Path)
    args=p.parse_args()
    result=json.dumps(link_repository(args.root),ensure_ascii=False,indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(result,encoding="utf-8")
    else:
        print(result,end="")
if __name__=="__main__":
    main()
