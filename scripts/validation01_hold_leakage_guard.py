#!/usr/bin/env python3
"""Prohibit previously known orleyl and screened objects in prospective HOLD."""
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def known_ids(screening,critical):
    ids={r.get("object_id","").strip().upper() for r in screening}
    # Physical object aliases, not single word numbers.
    ids.update({"ORLEYL-V","ORLEYL-VII","F.9.5","F.9.7","IBR-PLM-0006"})
    ids.update(r.get("object_id","").strip().upper() for r in critical)
    return {x for x in ids if x}
def evaluate(hold,screening,critical):
    known=known_ids(screening,critical)
    issues=[]
    for i,row in enumerate(hold,2):
        if row.get("split","").upper()!="HOLD":continue
        oid=row.get("object_id","").strip().upper()
        gid=row.get("physical_group","").strip().upper()
        if oid in known or gid in known or any(x in oid or x in gid for x in ("ORLEYL-VII","ORLEYL-V","ORLEY-VII","ORLEY-V")):
            issues.append({"row":i,"object_id":oid,"physical_group":gid,"issue":"KNOWN_DEVELOPMENT_OBJECT_IN_HOLD"})
    return {"gate":"BLOCKED" if issues else "PASS_KNOWN_OBJECT_SCREEN","known_development_ids":len(known),"issues":issues,
            "note":"Does not establish novelty of unknown objects; independent human provenance review still required."}
def load(path):
    with open(path,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
if __name__=="__main__":
    print(json.dumps(evaluate(load(ROOT/"data/review/validation01_holdout_v1.csv"),
      load(ROOT/"data/review/validation01_te_screening_2026-10-19.csv"),
      load(ROOT/"data/review/validation01_orleyl_critical_lines_v1.csv")),ensure_ascii=False,indent=2))
