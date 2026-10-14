#!/usr/bin/env python3
"""Explicit OpenAlex metadata intake. No scientific promotion or auto-commit."""
import argparse
import json
from iberos.openalex_adapter import sync_openalex

def main():
    parser=argparse.ArgumentParser(description="Fetch scholarly candidates into unverified local JSONL")
    parser.add_argument("--out",default="data/inbox/openalex_candidates.jsonl")
    parser.add_argument("--query",default="Iberian inscriptions epigraphy")
    parser.add_argument("--limit",type=int,default=20)
    args=parser.parse_args()
    print(json.dumps(sync_openalex(args.out,args.query,args.limit),ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
