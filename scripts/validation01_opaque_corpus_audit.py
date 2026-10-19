#!/usr/bin/env python3
"""Audit staged third-party Iberian inscriptions. Never interpret custom-font bytes as signs."""
import argparse,csv,json,re
from collections import Counter
from pathlib import Path
REQUIRED={"source_id","editorial_id","support","source_url","source_encoded_excerpt","encoding","reading_status","te_status","prospective_eligible"}
def audit(rows):
    issues=[];ids=set();refs=set()
    for i,r in enumerate(rows,2):
        missing=sorted(k for k in REQUIRED if not (r.get(k) or "").strip())
        if missing:issues.append({"row":i,"error":"MISSING","fields":missing});continue
        if r["source_id"] in ids:issues.append({"row":i,"error":"DUPLICATE_SOURCE_ID"})
        ids.add(r["source_id"])
        if not re.fullmatch(r"https://cathalaunia\.org/Iberika/I[0-9]{5}",r["source_url"]):
            issues.append({"row":i,"error":"SOURCE_NOT_MATCHED"})
        if r["encoding"]=="CUSTOM_FONT_OPAQUE":
            if r["reading_status"]!="NOT_DECODED" or r["te_status"]!="UNKNOWN" or r["prospective_eligible"]!="NO":
                issues.append({"row":i,"error":"OPAQUE_TEXT_FALSE_PROMOTION"})
    return {"records_staged":len(rows),"unique_source_ids":len(ids),"status":"PASS" if not issues else "BLOCKED","problems":issues,
            "decoded_atomic_inscriptions":0,"reviewed_te_positive":0,"reviewed_te_negative":0,"holdout_cases":0,
            "note":"A staged coded-font excerpt is NOT a decoded editorial transcription."}
def main():
    p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("--output");a=p.parse_args()
    with open(a.input,encoding="utf-8-sig",newline="") as f:out=audit(list(csv.DictReader(f)))
    s=json.dumps(out,ensure_ascii=False,indent=2)+"\n"
    if a.output:Path(a.output).write_text(s,encoding="utf8")
    else:print(s,end="")
    raise SystemExit(0 if out["status"]=="PASS" else 1)
if __name__=="__main__":main()
