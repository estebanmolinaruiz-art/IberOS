#!/usr/bin/env python3
"""VALIDATION-01 readiness gate: demand real independent evidence, not code-only success."""
import argparse,csv,json
from collections import Counter
from pathlib import Path

def load(path):
    with open(path,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def evaluate(te_rows,hold_rows,protocol):
    audited=[r for r in te_rows if r.get("reading_status")=="REVIEWED" and
             r.get("full_line_reviewed")=="YES" and r.get("independent_reviewer","").strip()
             and r.get("physical_group","").strip() and r.get("sign_tokens","").strip()
             and r.get("source_url","").strip()]
    hold=[r for r in hold_rows if r.get("split","").upper()=="HOLD"]
    unique_hold={r.get("physical_group","").strip() for r in hold if r.get("physical_group","").strip()}
    required=("target_definition","prediction_rule_frozen","baseline_rule_frozen",
              "split_plan_frozen","freeze_commit","blind_gold_protocol")
    missing=[key for key in required if not protocol.get(key) or
             str(protocol[key]).strip() in ("","PENDING","TBD","NO","UNSET")]
    blockers=[]
    if not audited:blockers.append("NO_INDEPENDENT_ATOMIC_SIGN_LINE_REVIEW")
    if not hold:blockers.append("NO_HOLD_RECORDS")
    if len(unique_hold)<20:blockers.append("UNDER_20_INDEPENDENT_HOLD_PHYSICAL_GROUPS")
    if missing:blockers.append("PREREGISTRATION_INCOMPLETE")
    # An existing gold label cannot be a data-dependent substitute for a declared prediction task.
    if any(r.get("te_status") in ("1","0") and r.get("reading_status")!="REVIEWED" for r in te_rows):
        blockers.append("UNREVIEWED_TE_CLASSIFICATION")
    return {"protocol":"VALIDATION-01","gate":"BLOCKED" if blockers else "CANDIDATE_FOR_BLIND_AUDIT",
      "reviewed_atomic_lines":len(audited),"hold_rows":len(hold),
      "unique_hold_groups":len(unique_hold),"preregistration_missing":missing,
      "blockers":blockers,"result":"NOT_EVALUATED",
      "note":"Passing readiness never constitutes a positive linguistic validation."}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--te",default="data/review/validation01_te_tokenized_review_v1.csv")
    p.add_argument("--hold",default="data/review/validation01_holdout_v1.csv")
    p.add_argument("--protocol",default="data/review/validation01_preregistration_v1.json")
    a=p.parse_args()
    result=evaluate(load(a.te),load(a.hold),json.loads(Path(a.protocol).read_text(encoding="utf8")))
    print(json.dumps(result,ensure_ascii=False,indent=2))
