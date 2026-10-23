#!/usr/bin/env python3
"""CORE corpus provenance audit: report defects without promoting scientific claims."""
import argparse,csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def assess(rows):
    findings=[];seen={}
    for n,r in enumerate(rows,2):
        oid=r.get("object_id","").strip()
        url=r.get("source_url","").strip()
        reason=[]
        if not oid:reason.append("MISSING_ID")
        if oid in seen:reason.append("DUPLICATE_ID")
        seen[oid]=n
        if not url:reason.append("NO_SOURCE")
        elif "..." in url or not url.startswith(("https://","http://")):reason.append("SOURCE_NEEDS_REPAIR")
        if r.get("physical_group","").strip() in ("","UNRESOLVED"):reason.append("PHYSICAL_GROUP_UNVERIFIED")
        if r.get("full_sign_reading_verified","").upper()!="YES":reason.append("NO_VERIFIED_SIGN_READING")
        if r.get("HOLD_eligible","").upper()=="YES" and reason:reason.append("UNSAFE_HOLD_CANDIDATE")
        if reason:findings.append({"object_id":oid,"row":n,"issues":reason})
    counts=Counter(issue for f in findings for issue in f["issues"])
    return {"records":len(rows),"issue_counts":dict(sorted(counts.items())),"findings":findings,
      "translation_validation":"NOT_EVALUATED",
      "note":"No source URL, object identity or editorial reading alone proves an Iberian translation."}
def load(p):
    with open(p,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--input",default=str(ROOT/"data/review/validation01_master_physical_objects_v1.csv"))
    parser.add_argument("--output")
    args=parser.parse_args()
    result=assess(load(args.input))
    content=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.output:Path(args.output).write_text(content,encoding="utf-8")
    else:print(content,end="")
