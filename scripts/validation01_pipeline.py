#!/usr/bin/env python3
"""Single read-only validation01 pipeline; never fabricates gold or HOLD."""
import argparse,csv,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def module(name):
    p=ROOT/"scripts"/(name+".py")
    s=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def rows(path):
    with open(path,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def run(root=ROOT):
    root=Path(root)
    te=rows(root/"data/review/validation01_te_tokenized_review_v1.csv")
    hold=rows(root/"data/review/validation01_holdout_v1.csv")
    prereg=json.loads((root/"data/review/validation01_preregistration_v1.json").read_text(encoding="utf8"))
    readiness=module("validation01_readiness").evaluate(te,hold,prereg)
    token_audit=module("validation01_te_token_audit").inspect(te)
    score=module("validation01_blind_score").audit(hold)
    # Critical: no pilot examples and no prediction/gold artifacts generated automatically.
    return {"pipeline":"IBEROS_VALIDATION01","reading_audit":{"records":token_audit["records"],
            "errors":token_audit["errors"],"counts":token_audit["counts"]},
            "readiness":readiness,"hold_scoring_gate":score["gate"],
            "hold_scoring_problems":score.get("problems",[]),
            "development_mask_generator":"AVAILABLE_MANUAL_REVIEW_ONLY",
            "pipeline_gate":"BLOCKED" if readiness["gate"]=="BLOCKED" or score["gate"]=="BLOCKED" or token_audit["errors"] else "AUDIT_REQUIRED",
            "scientific_verdict":"NOT_EVALUATED",
            "note":"Workflow integration is not a scientific result; never promote HOLD automatically."}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--output");a=p.parse_args()
    report=run();body=json.dumps(report,ensure_ascii=False,indent=2)+"\n"
    if a.output:Path(a.output).write_text(body,encoding="utf8")
    print(body,end="")
