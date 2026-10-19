#!/usr/bin/env python3
"""Audit candidates against the previously captured 286-entry source inventory.
Source-label concordance is NOT glyph-by-glyph palaeographic verification.
"""
import argparse,csv,json
from collections import Counter
def audit(source,candidates):
    source_by_code={r["unicode_decimal"]:r for r in source}
    seen=set();problems=[];stats=Counter()
    for r in candidates:
        code=r["unicode_decimal"];stats[r["review_queue"]]+=1
        if code in seen:problems.append((code,"DUPLICATE"));continue
        seen.add(code)
        original=source_by_code.get(code)
        if not original:problems.append((code,"NOT_IN_SOURCE"));continue
        if r["source_variant_label"]!=original["source_variant_label"]:
            problems.append((code,"SOURCE_LABEL_MISMATCH"))
        if r["usable_for_auto_reading"]!="NO" or r["independent_review"]!="PENDING":
            problems.append((code,"UNSUPPORTED_REVIEW_PROMOTION"))
        if r["review_queue"]!="SIMPLE_SOURCE_LABEL" and r["source_value_candidate"]:
            problems.append((code,"NON_SIMPLE_AUTOCANDIDATE"))
    if set(source_by_code)!=seen:problems.append(("*","INVENTORY_INCOMPLETE"))
    return {"source_records":len(source_by_code),"candidate_records":len(candidates),
            "source_label_checks":len(seen),"classes":dict(sorted(stats.items())),
            "problems":problems,"status":"PASS_SOURCE_METADATA" if not problems else "BLOCKED",
            "glyphs_visually_verified":0,"auto_reading_activated":0,
            "validation01":"NOT_EVALUATED"}
def read(path):
    with open(path,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("source");p.add_argument("candidates");p.add_argument("--output");a=p.parse_args()
    report=audit(read(a.source),read(a.candidates))
    result=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if a.output:
        from pathlib import Path
        Path(a.output).write_text(result,encoding="utf8")
    else:print(result,end="")
    raise SystemExit(report["status"]!="PASS_SOURCE_METADATA")
