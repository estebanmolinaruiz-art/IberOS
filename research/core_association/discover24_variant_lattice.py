#!/usr/bin/env python3
"""DISCOVER-24: variant-lattice and epistemic sensitivity, not suffix counts."""
from pathlib import Path
import json,re,csv,hashlib,collections
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"research/core_association/discover24_results"
OUT.mkdir(exist_ok=True)
p=ROOT/"data/review/editorial_readings_pending_v1.jsonl"
objects=[json.loads(x) for x in p.read_text(encoding="utf8").splitlines() if x.strip()]
c=next(x for x in objects if x["object_id"]=="IBR-PLM-0007")
d=c["editorial_edition_transcription"]
assert set(d)>=set(["dual","nondual"])
def tokens(x):
    # Exact punctuation and final editorial continuation retained outside linguistic token alignment
    return [q.strip() for q in re.split(r"\s*\.\s*",x) if q.strip()]
records=[]
variants=[]
for side in ["A","B"]:
    a,b=d["dual"][side],d["nondual"][side]
    assert len(a)==len(b)
    for ix,(x,y) in enumerate(zip(a,b),1):
        ta,tb=tokens(x),tokens(y)
        assert len(ta)==len(tb), f"must never silently align unequal units: {side}:{ix}"
        for pos,(u,v) in enumerate(zip(ta,tb),1):
            unit={"side":side,"line":ix,"position":pos,"dual":u,"nondual":v,
                  "reading_stable":u==v,"editorial_only":True,
                  "is_continuation":"(])" in u or "(])" in v,
                  "numerical_roman":bool(re.fullmatch(r"I+",u)) and u==v}
            records.append(unit)
            if u!=v:
                variants.append(unit)
def edits(a,b):
    # dynamic programming with full source character preservation
    n,m=len(a),len(b); dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):dp[i][0]=i
    for j in range(m+1):dp[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+(a[i-1]!=b[j-1]))
    return dp[n][m]
for v in variants:v["codepoint_edit_distance"]=edits(v["dual"],v["nondual"])
# Define prediction statements only if all edition alternatives agree, not semantic correctness.
numeric=[]
for side in ["A","B"]:
    for i,line in enumerate(d["dual"][side],1):
        tok=tokens(line)
        for j,u in enumerate(tok):
            if re.fullmatch(r"I+",u):
                previous=tok[j-1] if j else None
                alternative=tokens(d["nondual"][side][i-1])
                assert alternative[j]==u
                # Units preceding Roman numerals considered editorial characters, not validated labels.
                numeric.append({"side":side,"line":i,"count_strokes_as_edited":len(u),
                                "preceding_dual":previous,
                                "preceding_nondual":alternative[j-1] if j else None,
                                "stable_preceding_label":previous==alternative[j-1] if j else False,
                                "visual_number_verified":False})
# Label invariance: even if reading shifts, shared conventional class pattern may remain.
mapping=[]
for v in variants:
    mapping.append({"side":v["side"],"line":v["line"],"position":v["position"],
                    "dual":v["dual"],"nondual":v["nondual"],
                    "distance":v["codepoint_edit_distance"]})
report={
  "protocol":"DISCOVER-24", "source":str(p.relative_to(ROOT)),
  "source_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),
  "reference":c["review_reference"], "status":"EXPLORATORY_EDITORIAL_SENSITIVITY",
  "total_position_units":len(records),"invariant_position_units":sum(x["reading_stable"] for x in records),
  "changed_position_units":len(variants),
  "changed_units":mapping,"roman_numeric_mentions":numeric,
  "all_numeric_counts_stable_between_editions":all(x["stable_preceding_label"] for x in numeric),
  "hypotheses":[
    {"id":"H24-A","claim":"Roman stroke counts remain identical across editorial readings","test":"look for numeric glyphs in independent photos and verify stroke counts","status":"EDITORIAL_INVARIANT_NOT_VISUAL"},
    {"id":"H24-B","claim":"Dual/nondual alternatives may be local allographs of a coherent graphical class","test":"blind glyph review predicts matched g/k and d/t alternations","status":"UNVERIFIED"},
    {"id":"H24-C","claim":"Whether a symbol is a lexical unit cannot be decided from unchanging Roman numeral context","test":"external known quantities and distinct textual contexts","status":"UNDECIDABLE"}],
  "limitations":["One physical object; editorial alternatives are not independent inscriptions.",
                 "Roman I repeated is edited notation here, not visually counted original strokes.",
                 "No translated words nor tested logograms.",
                 "Content normalized by source, which reports potential lacunae and reading doubts."]
}
(OUT/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8")
with (OUT/"variant_lattice.csv").open("w",encoding="utf8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
with (OUT/"numeral_invariants.csv").open("w",encoding="utf8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(numeric[0]));w.writeheader();w.writerows(numeric)
print(json.dumps({"units":len(records),"stable":report["invariant_position_units"],"changed":len(variants),
                  "changes":mapping,"numbers":numeric},ensure_ascii=False))
