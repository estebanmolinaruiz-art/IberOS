#!/usr/bin/env python3
"""DISCOVER-23: dependency-group decontamination and cross-family hypothesis falsification."""
import csv,json,hashlib,collections,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"research/core_association/discover23_results"
OUT.mkdir(exist_ok=True)
src=ROOT/"research/core_association/discover22_results/editorial_units.csv"
# Recompute upstream reproducibly from checked-in sources if no artifact present
if not src.exists():
    import subprocess,sys
    subprocess.run([sys.executable,str(ROOT/"research/core_association/discover22_corpus.py")],check=True,capture_output=True)
with src.open(encoding="utf8",newline="") as f:rows=list(csv.DictReader(f))
def family(x):
    if x.startswith("ORLEYL_"):return "ORLEYL"
    return x
by=collections.defaultdict(set)
for row in rows:by[row["unit"]].add(row["object_id"])
def lev(a,b):
    dp=list(range(len(b)+1))
    for i,c in enumerate(a,1):
        nd=[i]+[0]*len(b)
        for j,d in enumerate(b,1):
            nd[j]=min(nd[j-1]+1,dp[j]+1,dp[j-1]+(c!=d))
        dp=nd
    return dp[-1]
exact=[]
for u,ids in sorted(by.items()):
    if len(ids)<2:continue
    fams={family(i) for i in ids}
    exact.append({"unit":u,"objects":sorted(ids),"families":sorted(fams),
                  "independent_families":len(fams),"can_validate_cross_family":len(fams)>=2})
edits=[]
keys=sorted(u for u in by if len(u)>=5)
for i,a in enumerate(keys):
    for b in keys[i+1:]:
        if abs(len(a)-len(b))>1:continue
        if lev(a,b)!=1:continue
        ida=by[a];idb=by[b]
        if not any(x!=y for x in ida for y in idb):continue
        fam_a={family(x) for x in ida};fam_b={family(x) for x in idb}
        edits.append({"a":a,"b":b,"families_a":sorted(fam_a),"families_b":sorted(fam_b),
                      "cross_family":bool(any(x!=y for x in fam_a for y in fam_b))})
cross_exact=[x for x in exact if x["can_validate_cross_family"]]
cross_edit=[x for x in edits if x["cross_family"]]
units_by_family=collections.defaultdict(set)
for row in rows:units_by_family[family(row["object_id"])].add(row["unit"])
report={"protocol":"DISCOVER-23","status":"EXPLORATORY_NEGATIVE_RESULT",
        "n_editorial_rows":len(rows),"n_physical_ids":len({x["object_id"] for x in rows}),
        "n_dependency_families":len(units_by_family),
        "family_unit_counts":{k:len(v) for k,v in sorted(units_by_family.items())},
        "exact_cross_object":len(exact),"exact_cross_family":len(cross_exact),
        "one_edit_cross_object":len(edits),"one_edit_cross_family":len(cross_edit),
        "exact_candidates":exact,"one_edit_candidates":edits,
        "interpretation":"No valid independent cross-family confirmation of any candidate in the sampled transcriptions; not a falsification of the linguistic theories.",
        "limitations":["All Orleyl objects count as ONE leakage family even when different physical pieces.",
                       "Other named objects may have unresolved dependency links; conservative only for Orleyl.",
                       "Strings are editorial readings, not photographic OCR.",
                       "This is a screening gate and not a statistical p-value or calibrated classifier."]}
(OUT/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8")
with (OUT/"family_manifest.csv").open("w",encoding="utf8",newline="") as f:
 w=csv.writer(f);w.writerow(["dependency_family","n_distinct_units","n_rows"])
 for family_id,units in sorted(units_by_family.items()):
  w.writerow([family_id,len(units),sum(family(x["object_id"])==family_id for x in rows)])
print(json.dumps({k:v for k,v in report.items() if k not in ("exact_candidates","one_edit_candidates","limitations")},ensure_ascii=False))
if cross_exact or cross_edit:
 print("CROSS FAMILY CANDIDATES",cross_exact,cross_edit)
