#!/usr/bin/env python3
"""Read-only quality audit of the preliminary VALIDATION-01 physical-object master.
No automatic admission to HOLD and no inferred physical independence.
"""
import csv, json, re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MASTER=ROOT/"data/review/validation01_master_physical_objects_v1.csv"
def audit(rows):
    issues=[]
    seen_master=set();seen_object=set()
    for n,r in enumerate(rows,2):
        mid=r.get("master_id","").strip()
        oid=r.get("object_id","").strip()
        if not mid or mid in seen_master:issues.append({"row":n,"code":"MISSING_OR_DUPLICATE_MASTER_ID"})
        if not oid or oid in seen_object:issues.append({"row":n,"code":"MISSING_OR_DUPLICATE_OBJECT_ID"})
        seen_master.add(mid);seen_object.add(oid)
        url=r.get("source_url","").strip()
        if not url: issues.append({"row":n,"code":"SOURCE_URL_MISSING","object_id":oid})
        elif "..." in url or not re.match(r"^https?://[^/ ]+",url):
            issues.append({"row":n,"code":"SOURCE_URL_UNUSABLE_OR_TRUNCATED","object_id":oid})
        if r.get("physical_group","").strip() in ("","UNRESOLVED"):
            issues.append({"row":n,"code":"PHYSICAL_IDENTITY_UNRESOLVED","object_id":oid})
        if r.get("HOLD_eligible","").strip().upper()=="YES":
            requirements=("object_provenance_verified","full_sign_reading_verified","source_images_verified")
            if any(r.get(key,"").strip().upper()!="YES" for key in requirements) or not r.get("independent_reader","").strip():
                issues.append({"row":n,"code":"UNSUBSTANTIATED_HOLD_ADMISSION","object_id":oid})
    codes=Counter(i["code"] for i in issues)
    return {"records":len(rows),"hold_eligible":sum(r.get("HOLD_eligible","").upper()=="YES" for r in rows),
       "physical_independence_verified":0 if not rows else sum(r.get("object_provenance_verified","").upper()=="YES" and r.get("physical_group","") not in ("","UNRESOLVED") for r in rows),
       "issue_counts":dict(sorted(codes.items())),"issues":issues,
       "status":"AUDIT_REQUIRED" if issues else "STRUCTURAL_CHECKS_PASS",
       "note":"Passing structural checks never establishes novel physical objects or scientific validation."}
def load(path=MASTER):
    with open(path,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
if __name__=="__main__":
    print(json.dumps(audit(load()),ensure_ascii=False,indent=2))
