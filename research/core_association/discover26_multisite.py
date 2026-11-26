#!/usr/bin/env python3
"""DISCOVER-26: run evidence engine on three physical objects, test counterfactual safety.
Only documentary inferences. The function evidence is not independently labeled.
"""
import json,re,csv,hashlib,collections
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"research/core_association/discover26_results"
SOURCE=ROOT/"data/review/editorial_readings_pending_v1.jsonl"
GRAPH=ROOT/"data/review/casinos_graphic_uncertainties_v1.json"
CASE_ID={"IBR-LAP-0005":"Sagunto","IBR-MUS-0001":"Caminreal","IBR-PLM-0007":"Casinos"}

def terms(text):
    # Editorial units; rejects incomplete fragments and notes, retains provenance.
    return [v.strip() for v in re.split(r"[·.]",text) if v.strip()]

def build():
    original=[json.loads(x) for x in SOURCE.read_text(encoding="utf8").splitlines() if x.strip()]
    graphics=json.loads(GRAPH.read_text(encoding="utf8"))
    out=[]
    for case in original:
        phys=case["object_id"]
        if phys not in CASE_ID:continue
        t=case["editorial_transcription"]
        if phys=="IBR-PLM-0007":
            # Note: this is ONE physical inscription with alternative editions; not two documents.
            a,b=t["dual"],t["nondual"]
            for side in ("A","B"):
                for line,(dual,nondual) in enumerate(zip(a[side],b[side]),1):
                    x,y=terms(dual),terms(nondual)
                    if len(x)!=len(y):raise ValueError("Misaligned editorial readings")
                    for index,(u,v) in enumerate(zip(x,y),1):
                        key=f"{side}{line}"
                        matches=[z for z in graphics["records"] if z["region"]==key]
                        out.append(record(phys,side,line,index,[u,v],case, matches[0]["evidence_id"] if matches else None))
        else:
            text=t["iberian"]
            for index,u in enumerate(terms(text),1):
                out.append(record(phys,None,None,index,[u],case,None))
    return out

def record(phys,side,line,index,alternatives,case,graphic_ref):
    distinct=sorted(set(alternatives))
    uncertain=any("[" in x or "]" in x or "lacuna" in x or x.startswith(")") for x in distinct)
    numeral=any(bool(re.search(r"(?<![A-Za-z])I+(?![A-Za-z])",x)) for x in distinct)
    return {
        "id":f"{phys}-{side or 'U'}{line or 0}-{index}",
        "physical_id":phys,"site_alias":CASE_ID[phys],
        "face":side,"line":line,"editorial_unit_position":index,
        "possible_editorial_readings":distinct,
        "reading_ambiguity":len(distinct)>1,
        "damaged_or_incomplete":uncertain,
        "graphic_review_ref":graphic_ref,
        "glyph_crop_reference":None,
        "visual_glyph_verified":False,
        "archaeological_external_function_verified":False,
        "editorial_numeral_pattern":numeral,
        "function_hypotheses":(["QUANTITATIVE_NOTATION_CANDIDATE"] if numeral else [])+
              ["PHONETIC","ABBREVIATIVE","LOGOGRAPHIC","NONLINGUISTIC"],
        "semantic_inference":None,"decision":"ABSTAIN",
        "source_ref":case["review_reference"]}

def run():
    rows=build()
    OUT.mkdir(parents=True,exist_ok=True)
    family=collections.defaultdict(list)
    for r in rows:family[r["physical_id"]].append(r)
    source_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (SOURCE,GRAPH)}
    # Counterfactual ablation: removing context or alternative readings may NOT turn
    # unverified claims into an accepted meaning.
    ablations={}
    for name in ("baseline","context_removed","one_reading_only","numeric_markers_removed"):
        copy=json.loads(json.dumps(rows))
        if name=="context_removed":
            for r in copy:r["graphic_review_ref"]=None
        if name=="one_reading_only":
            for r in copy:r["possible_editorial_readings"]=r["possible_editorial_readings"][:1]
        if name=="numeric_markers_removed":
            for r in copy:r["editorial_numeral_pattern"]=False
        admitted=[r for r in copy if r["visual_glyph_verified"] and r["archaeological_external_function_verified"]]
        ablations[name]={"admitted_semantic_claims":len(admitted),
                         "abstentions":len(copy)-len(admitted)}
    summary={"protocol":"DISCOVER-26","source_hashes":source_hashes,
             "total_editorial_units":len(rows),"objects":len(family),
             "objects_by_id":{k:len(v) for k,v in sorted(family.items())},
             "alternative_reading_units":sum(r["reading_ambiguity"] for r in rows),
             "incomplete_or_damaged_units":sum(r["damaged_or_incomplete"] for r in rows),
             "edited_numerical_units":sum(r["editorial_numeral_pattern"] for r in rows),
             "graphical_links_to_review":sum(bool(r["graphic_review_ref"]) for r in rows),
             "independently_verified_glyphs":0,"new_translations":0,
             "abstentions":len(rows),"ablation":ablations,
             "limitations":["Coverage only three editorial-reading entries, not full IberOS corpus.",
               "Source texts are editorial and partial, no image-to-sign coordinates.",
               "Function hypotheses are a possibility set, not numeric posterior probabilities.",
               "Repeated units within one physical object are not independent evidence."]}
    (OUT/"report.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf8")
    (OUT/"uncertainty_ledger.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf8")
    with (OUT/"review_queue.csv").open("w",encoding="utf8",newline="") as f:
        keys=["id","physical_id","graphic_review_ref","reading_ambiguity","damaged_or_incomplete",
              "editorial_numeral_pattern","visual_glyph_verified","decision"]
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows([{k:r[k] for k in keys} for r in rows])
    print(json.dumps(summary,ensure_ascii=False))
    return summary

if __name__=="__main__":run()
