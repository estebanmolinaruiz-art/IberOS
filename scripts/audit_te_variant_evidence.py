#!/usr/bin/env python3
"""Check 15 TE catalog variants without asserting visual verification."""
import csv,json,sys
from pathlib import Path
EXPECTED={"te"+str(i) for i in range(1,17)}-{"te7"}
def audit(rows):
    issues=[];variants=set();codes=set()
    for i,r in enumerate(rows,2):
        label=r["source_variant_label"];code=r["unicode_decimal"]
        if label in variants or code in codes:issues.append([i,"DUPLICATE_VARIANT_OR_CODE"])
        variants.add(label);codes.add(code)
        if r["source_value_candidate"]!="te":issues.append([i,"NOT_TE_LABEL"])
        if r["activation_status"]!="BLOCKED":issues.append([i,"PREMATURE_ACTIVATION"])
        if r["visual_review_status"]=="NOT_INSPECTED" and (r["reviewer"] or r["independent_reviewer"]):
            issues.append([i,"REVIEWER_WITHOUT_INSPECTION"])
        if r["activation_status"]=="VERIFIED" and not (r["original_image_url"] and r["image_sha256"] and r["independent_reviewer"]):
            issues.append([i,"UNVERIFIABLE_ACTIVATION"])
    if len(rows)!=15:issues.append([0,"EXPECTED_15_VARIANTS"])
    # Not all intermediate variant numbers need to exist. Compare to documented exact catalog labels separately.
    return {"records":len(rows),"labels":sorted(variants),"problems":issues,
      "status":"PASS_STAGING" if not issues else "BLOCKED","verified_glyphs":0,
      "validation01":"NOT_EVALUATED"}
if __name__=="__main__":
    p=Path(sys.argv[1] if len(sys.argv)>1 else "data/review/te_variant_evidence_15_v1.csv")
    with p.open(encoding="utf-8",newline="") as f:report=audit(list(csv.DictReader(f)))
    print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(bool(report["problems"]))
