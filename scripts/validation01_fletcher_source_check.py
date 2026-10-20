#!/usr/bin/env python3
"""Check Fletcher source-referenced TE contrast, not palaeographic or blinded validation."""
import csv,sys,json
from pathlib import Path
def check(rows):
    data={r["object_id"]:r for r in rows}
    if set(data)!={"ORLEYL-V","ORLEYL-VII"}:return {"gate":"BLOCKED","error":"EXPECTED_TWO_KNOWN_DEVELOPMENT_OBJECTS"}
    v=data["ORLEYL-V"]["target_editorial_tokens"].lower().split("-")
    vii=data["ORLEYL-VII"]["target_editorial_tokens"].lower().split("-")
    if vii[:2]!=["ba","s"]:return {"gate":"BLOCKED","error":"VII_BAS_EDITORIAL_PREFIX_NOT_TRACKED"}
    a,b=v,vii[2:]
    matches=[i for i in range(len(a)) if a[:i]+a[i+1:]==b]
    if matches!=[5] or a[5]!="te":
        return {"gate":"BLOCKED","error":"EXPECTED_SINGLE_EXTRA_ATOMIC_TE_AFTER_KE"}
    if any(r["split"]!="DEVELOPMENT" or r["evidence_level"]!="PRIMARY_EDITORIAL_LINE" or r["visual_glyphs_verified"]!="0" for r in rows):
        return {"gate":"BLOCKED","error":"UNSUPPORTED_PROMOTION_OR_HOLD"}
    return {"gate":"PASS_EDITORIAL_ONLY","extra_sign":"te","index_zero_based":5,
            "source_pdf_pages":[67,110],"visual_glyphs_verified":0,
            "hold_predictions_evaluated":0,"scientific_verdict":"NOT_EVALUATED"}
if __name__=="__main__":
    p=Path(sys.argv[1] if len(sys.argv)>1 else "data/review/validation01_fletcher_critical_passages_source_checked.csv")
    with p.open(encoding="utf8",newline="") as f:r=check(list(csv.DictReader(f)))
    print(json.dumps(r,ensure_ascii=False,indent=2))
    raise SystemExit(r["gate"]!="PASS_EDITORIAL_ONLY")
