#!/usr/bin/env python3
"""VALIDATION-01: blind, leak-safe scoring; not a test of translation truth."""
import argparse,csv,json,hashlib,random
from collections import Counter
from pathlib import Path

FIELDS=("object_id","physical_group","split","source_url","reading_reviewed","prediction_locked_at",
        "gold_reviewed_at","gold_label","iberos_prediction","baseline_prediction")
LABELS={"0","1"}
def audit(rows,minimum=20):
    problems=[];seen={};hold=[]
    for i,r in enumerate(rows,2):
        if not any(str(v).strip() for v in r.values() if v is not None): continue
        split=r.get("split","").upper()
        if split not in {"TRAIN","VAL","HOLD"}:problems.append([i,"INVALID_SPLIT"]);continue
        id=r.get("physical_group","").strip()
        if not id:problems.append([i,"MISSING_PHYSICAL_ID"]);continue
        if id in seen and seen[id]!=split:problems.append([i,"LEAKAGE_BETWEEN_SPLITS"])
        seen[id]=split
        if split!="HOLD":continue
        hold.append(r)
        for k in FIELDS:
            if not r.get(k,"").strip():problems.append([i,"MISSING_"+k])
        for k in ("gold_label","iberos_prediction","baseline_prediction"):
            if r.get(k,"") not in LABELS:problems.append([i,"INVALID_"+k])
        if r.get("reading_reviewed")!="YES":problems.append([i,"UNREVIEWED_READING"])
        if r.get("prediction_locked_at","")>=r.get("gold_reviewed_at",""):problems.append([i,"NOT_PROSPECTIVELY_LOCKED"])
        if r.get("predictions_frozen_sha256","")=="":
            problems.append([i,"NO_PREDICTION_COMMITMENT"])
        if not r.get("gold_independent_reviewer","").strip():
            problems.append([i,"NO_INDEPENDENT_GOLD_REVIEW"])
    if len({r.get("physical_group","") for r in hold})<minimum:
        problems.append([0,"INSUFFICIENT_INDEPENDENT_HOLDOUT"])
    if problems:return {"gate":"BLOCKED","hold_rows":len(hold),"problems":problems,"superiority":"NOT_EVALUATED"}
    def metric(key):
        correct=sum(r[key]==r["gold_label"] for r in hold)
        p=[r for r in hold if r["gold_label"]=="1"]
        n=[r for r in hold if r["gold_label"]=="0"]
        sensitivity=sum(r[key]=="1" for r in p)/len(p) if p else None
        specificity=sum(r[key]=="0" for r in n)/len(n) if n else None
        return {"accuracy":correct/len(hold),"balanced_accuracy":(sensitivity+specificity)/2 if sensitivity is not None and specificity is not None else None}
    ib=metric("iberos_prediction");base=metric("baseline_prediction")
    return {"gate":"DESCRIPTIVE_SCORING_ONLY","hold_rows":len(hold),"iberos":ib,"baseline":base,
            "delta_accuracy":ib["accuracy"]-base["accuracy"],"superiority":"NOT_CONFIRMED",
            "note":"No hypothesis claim without preregistered independent replication, uncertainty intervals, and baseline training audit."}

def main():
    a=argparse.ArgumentParser();a.add_argument("csv_file");a.add_argument("--minimum",type=int,default=20);a.add_argument("--output");v=a.parse_args()
    with open(v.csv_file,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
    result=audit(rows,v.minimum)
    text=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if v.output:Path(v.output).write_text(text,encoding="utf-8")
    else:print(text,end="")
if __name__=="__main__":main()
