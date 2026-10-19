#!/usr/bin/env python3
"""VALIDATION-01-TE-MASK pilot: prepare DEVELOPMENT-only masked-sign examples.
Do not use on HOLD; an independent custodian must prepare, seal and release HOLD.
"""
import argparse,csv,hashlib,json
SIGNS=set("a e i o u l m n r ŕ s ś ḿ ba be bi bo bu ta te ti to tu ka ke ki ko ku".split())
def make(rows,salt):
    if not salt:raise ValueError("Non-empty salt required")
    seen=set();items=[];issues=[]
    for i,r in enumerate(rows,2):
        if r.get("cohort")!="DEVELOPMENT":issues.append([i,"NOT_DEVELOPMENT"]);continue
        if r.get("reading_status")!="REVIEWED" or r.get("full_line_reviewed")!="YES" or not r.get("independent_reviewer","").strip():
            issues.append([i,"UNREVIEWED_LINE"]);continue
        group=r.get("physical_group","").strip()
        if not group or group in seen:issues.append([i,"MISSING_OR_REPEATED_PHYSICAL_GROUP"]);continue
        tokens=r.get("sign_tokens","").split()
        if len(tokens)<3 or any(t not in SIGNS for t in tokens):
            issues.append([i,"INVALID_ATOMIC_TOKENS"]);continue
        seen.add(group)
        choice=int(hashlib.sha256((salt+"\0"+group).encode()).hexdigest(),16)%len(tokens)
        gold="1" if tokens[choice]=="te" else "0"
        masked=tokens[:];masked[choice]="[MASK]"
        items.append({"object_id":r["object_id"],"physical_group":group,
          "masked_tokens":" ".join(masked),"masked_index":choice,
          "source_url":r["source_url"],"edition_locator":r["edition_locator"],
          "development_gold_label":gold,"cohort":"DEVELOPMENT",
          "status":"PILOT_ONLY_NOT_BLIND_HOLD"})
    return {"examples":items,"issues":issues,"hold_examples":0,"validation":"NOT_EVALUATED"}
def read(path):
    with open(path,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("output");p.add_argument("--salt",required=True)
    a=p.parse_args();result=make(read(a.input),a.salt)
    cols=["object_id","physical_group","masked_tokens","masked_index","source_url","edition_locator","development_gold_label","cohort","status"]
    with open(a.output,"w",encoding="utf8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(result["examples"])
    print(json.dumps({"development_examples":len(result["examples"]),"issues":result["issues"],
                      "hold_examples":0,"validation":"NOT_EVALUATED"},ensure_ascii=False))
