#!/usr/bin/env python3
"""DISCOVER-22: corpus-wide coverage, with strict source-type and leakage gates."""
import csv, json, re, hashlib, random
from pathlib import Path
from collections import Counter, defaultdict

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"research"/"core_association"/"discover22_results"
OUT.mkdir(exist_ok=True)
def readcsv(p): 
    with (ROOT/p).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def readjsonl(p):
    return [json.loads(x) for x in (ROOT/p).read_text(encoding="utf8").splitlines() if x.strip()]
def dump(p,obj): (OUT/p).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding="utf8")
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()

inventory=readjsonl("data/curated/iberos_curated_objects_v1.jsonl")
readings=readjsonl("data/review/editorial_readings_pending_v1.jsonl")
parallel=readcsv("research/protocols/ORLEYL-EDITORIAL-PARALLELS-2026-10-18.csv")
opaque=readcsv("data/review/validation01_external_opaque_readings_batch01.csv")
slots=readcsv("data/curated/rok_orleyl_editorial_alignment_1981.csv")
sources=["data/curated/iberos_curated_objects_v1.jsonl","data/review/editorial_readings_pending_v1.jsonl","research/protocols/ORLEYL-EDITORIAL-PARALLELS-2026-10-18.csv","data/review/validation01_external_opaque_readings_batch01.csv","data/curated/rok_orleyl_editorial_alignment_1981.csv"]
manifest=[{"source":p,"sha256":sha(p),"records":len((inventory if p==sources[0] else readings if p==sources[1] else parallel if p==sources[2] else opaque if p==sources[3] else slots))} for p in sources]

# Keep editorial readings as strings, never silently turn letters into confirmed glyphs.
docs=[]
for r in readings:
    eid=r["object_id"]
    t=r.get("editorial_transcription",{})
    if "iberian" in t:
        strings=[t["iberian"]]
        status="EDITORIAL_ONLY_NO_GRAPHIC_REVIEW"
    elif "dual" in t:
        # One reading per physically identical object, not two pseudo-independent objects.
        strings=t["nondual"]["A"]+t["nondual"]["B"]
        status="EDITORIAL_NONDUAL_CHOICE_ALTERNATIVE_EXISTS"
    else:
        continue
    docs.append({"object_id":eid,"strings":strings,"status":status,"source":"editorial_readings_pending_v1"})
for r in parallel:
    # editorial parallels: preserve each Orleyl object as a separate physical group
    for objkey,segkey in [("object","editorial_reading"),("comparison_object","comparison_editorial_reading")]:
        name=r.get(objkey,"")
        seg=r.get(segkey,"")
        if name and seg: docs.append({"object_id":"ORLEYL_"+name.replace("Orleyl ","").replace("-","_"),"strings":[seg],"status":"EDITORIAL_PARALLEL_NOT_HOLDOUT","source":"ORLEYL-EDITORIAL-PARALLELS"})
# Exact written units between punctuation: strict normalized groups, not syllabic glyphs.
# Exclude ambiguous/partial/groups containing digits or brackets, avoid treating editorial alternatives as independent.
def units(text):
    # deliberately do not split a transliteration into hypothetical syllabic signs
    raw=re.split(r"[·.\s]+",text.strip())
    return [x.casefold() for x in raw if len(x)>1 and re.fullmatch(r"[a-záàéèíïóòúüńñŕśš]+",x,re.I)]
records=[]
for d in docs:
    for s in d["strings"]:
        for g in units(s):
            records.append({"object_id":d["object_id"],"unit":g,"source":d["source"],"status":d["status"]})
# Object family is key: repeated same string in multiple editions does not count as independent validation.
byunit=defaultdict(set)
for r in records:byunit[r["unit"]].add(r["object_id"])
independent=[{"unit":u,"objects":sorted(ids),"n_objects":len(ids)} for u,ids in byunit.items() if len(ids)>=2]
independent.sort(key=lambda r:(-r["n_objects"],r["unit"]))

# separately inspect documented physical sign tokens, no cross-encoding assumption
orleyl=defaultdict(list)
for r in slots:
    if r["sequence_role"]=="comparandum" and r["token_index"].isdigit() and int(r["token_index"])>0:
        orleyl[r["phys_key"]].append((int(r["token_index"]),r["editorial_token"]))
orleyl={k:[x[1] for x in sorted(v)] for k,v in orleyl.items()}
def bigrams(seq):return {"-".join(seq[i:i+2]) for i in range(len(seq)-1)}
shared=sorted(set.intersection(*(bigrams(v) for v in orleyl.values()))) if len(orleyl)>1 else []
# Repeated full-unit patterns across object IDs only, not sign strings; no semantics inferred.
counter=Counter(x["unit"] for x in records)
bad=[r for r in opaque if r.get("reading_status")!="READING_VERIFIED"]
coverage={
 "registry_objects":len(inventory),
 "editorial_reading_entries":len(readings),
 "editorial_object_records":len(docs),
 "unique_editorial_object_ids":len(set(d["object_id"] for d in docs)),
 "clean_editorial_groups_extracted":len(records),
 "unique_editorial_groups":len(byunit),
 "cross_object_exact_groups":len(independent),
 "opaque_unusable_records":len(bad),
 "orleyl_comparandum_objects":len(orleyl),
 "orleyl_shared_2token":shared,
 "notes":["No OCR values obtained by this experiment.","Editorial spellings are not independent predictions.","Orleyl parallels are development-only; cannot enter HOLD.","No sign-by-sign comparison across different transliteration conventions.","Simple string recurrence cannot establish a word meaning.","Corpus registry is metadata, not a fully readable sign dataset."]
}
dump("manifest.json",{"sources":manifest,"coverage":coverage,"cross_object_editorial_units":independent,"orleyl_comparanda":orleyl})
with (OUT/"editorial_units.csv").open("w",encoding="utf8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=["object_id","unit","source","status"]);w.writeheader();w.writerows(records)
with (OUT/"cross_object_candidates.csv").open("w",encoding="utf8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=["unit","n_objects","objects"]);w.writeheader()
 for r in independent:w.writerow({"unit":r["unit"],"n_objects":r["n_objects"],"objects":";".join(r["objects"])})
# Candidate editorial transformations across distinct physical objects.
# Identify minimum Levenshtein operations; these are not independently read glyph changes.
def lev_ops(a,b):
    n,m=len(a),len(b)
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):dp[i][0]=i
    for j in range(m+1):dp[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+(a[i-1]!=b[j-1]))
    return dp[n][m]
transforms=[]
for a in sorted(byunit):
    if len(a)<5:continue
    for b in sorted(byunit):
        if a>=b or len(b)<5:continue
        ids_a=byunit[a];ids_b=byunit[b]
        if not any(x!=y for x in ids_a for y in ids_b):continue
        d=lev_ops(a,b)
        if d==1 and max(len(a),len(b))>=6:
            transforms.append({"a":a,"b":b,"edit_distance":d,
                               "objects_a":sorted(ids_a),"objects_b":sorted(ids_b),
                               "warning":"editorial orthography; not confirmed independent sign change"})
dump("transform_candidates.json",transforms)
print("Cross-object one-edit editorial candidates:",transforms[:30])

print(json.dumps(coverage,ensure_ascii=False))
print("Top cross-object editorial units:",independent[:15])
