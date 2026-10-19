#!/usr/bin/env python3
"""Strict TE sign-token audit on sourced, reviewer-approved editorial token sequences.

Input is NOT arbitrary Latin text: 'te' syllabogram must already be atomically marked.
"""
import argparse,csv,json,re
from collections import Counter
from pathlib import Path
TOKENS=set("a e i o u l m n r ŕ s ś ḿ ba be bi bo bu ta te ti to tu ka ke ki ko ku".split())
FIELDS=["object_id","physical_group","source_url","edition_locator","signary","sign_tokens","reading_status","full_line_reviewed","independent_reviewer","cohort"]
def inspect(rows):
    results=[];errors=[]
    for number,r in enumerate(rows,2):
        if not any((v or "").strip() for v in r.values()):continue
        missing=[k for k in FIELDS if not (r.get(k) or "").strip()]
        if missing:errors.append({"line":number,"error":"MISSING_FIELDS","fields":missing});continue
        if not r["source_url"].startswith("https://"):errors.append({"line":number,"error":"SOURCE_URL_INVALID"});continue
        if r["cohort"] not in ("DEVELOPMENT","RETROSPECTIVE_SCREENING"):
            errors.append({"line":number,"error":"NO_HOLDOUT_IMPORT"});continue
        if r["reading_status"] not in ("REVIEWED","AMBIGUOUS","UNREVIEWED"):
            errors.append({"line":number,"error":"INVALID_READING_STATUS"});continue
        units=r["sign_tokens"].split()
        if not units:
            errors.append({"line":number,"error":"MALFORMED_TOKEN_STREAM"});continue
        unknown=[u for u in units if u not in TOKENS and u not in ("?","[lacuna]")]
        if unknown:errors.append({"line":number,"error":"UNRECOGNIZED_ATOMIC_SIGNS","values":unknown});continue
        if (r["reading_status"]!="REVIEWED" or r["full_line_reviewed"]!="YES"
            or "?" in units or "[lacuna]" in units):
            status="UNKNOWN"
        else:status="PRESENT" if "te" in units else "ABSENT_IN_REVIEWED_LINE"
        results.append({"object_id":r["object_id"],"physical_group":r["physical_group"],
                        "source_url":r["source_url"],"edition_locator":r["edition_locator"],
                        "te_status":status,"te_token_count":units.count("te") if status!="UNKNOWN" else None,
                        "cohort":r["cohort"],"evidence_type":"EDITORIAL_TRANSCRIPTION_NOT_INDEPENDENT_GLYPH_VERIFICATION"})
    return {"status":"ERROR" if errors else "RETROSPECTIVE_SCREENED","records":len(results),
            "counts":dict(Counter(r["te_status"] for r in results)),"errors":errors,"results":results,
            "prospective_holdout_scored":0,"linguistic_discovery":"NOT_EVALUATED"}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("csv_file");p.add_argument("--output");args=p.parse_args()
    with open(args.csv_file,encoding="utf-8-sig",newline="") as f:report=inspect(list(csv.DictReader(f)))
    out=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if args.output:Path(args.output).write_text(out,encoding="utf8")
    else:print(out,end="")
    raise SystemExit(bool(report["errors"]))
