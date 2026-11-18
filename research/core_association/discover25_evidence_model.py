#!/usr/bin/env python3
"""DISCOVER-25: observation -> reading lattice -> archaeological function, with abstention.
No calibrated probabilities: editorial alternatives are *possible*, not equiprobable.
"""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/"data/review/editorial_readings_pending_v1.jsonl"
GRAPH=ROOT/"data/review/casinos_graphic_uncertainties_v1.json"
OUT=ROOT/"research/core_association/discover25_results"

def load_case():
    entries=[json.loads(x) for x in SOURCE.read_text(encoding="utf-8").splitlines() if x.strip()]
    case=next(x for x in entries if x["object_id"]=="IBR-PLM-0007")
    graphic=json.loads(GRAPH.read_text(encoding="utf-8"))
    assert graphic["object_id"]==case["object_id"]
    return case,graphic

def phrases(line):
    return [part.strip() for part in line.split(".") if part.strip()]

def classify_phrase(phrase):
    # Detect *editorial typographic notation*, not archaeological meaning.
    matches=re.findall(r"(?<![a-zA-Z])I+(?![a-zA-Z])",phrase)
    return {"contains_editorial_strokes":bool(matches),
            "stroke_runs_in_edition":[len(s) for s in matches],
            "contains_editorial_lacuna":"(])" in phrase,
            "carries_known_external_quantity":False}

def make_lattice(case,graphic):
    d=case["editorial_edition_transcription"]
    g_by_region={g["region"]:g for g in graphic["records"]}
    rows=[]
    for side in ("A","B"):
        lhs,rhs=d["dual"][side],d["nondual"][side]
        assert len(lhs)==len(rhs)
        for line,(a,b) in enumerate(zip(lhs,rhs),1):
            p,q=phrases(a),phrases(b)
            if len(p)!=len(q):raise ValueError(f"Unaligned phrases at {side}{line}")
            region=side+str(line)
            g=g_by_region.get(region)
            for ordinal,(u,v) in enumerate(zip(p,q),1):
                # two editorial readings give a SET, not probabilities
                readings=sorted(set([u,v]))
                features=[classify_phrase(x) for x in readings]
                shared_runs=all(x["stroke_runs_in_edition"]==features[0]["stroke_runs_in_edition"] for x in features)
                has_num=any(x["contains_editorial_strokes"] for x in features)
                possible=["UNDETERMINED"]
                if has_num: possible.append("QUANTITATIVE_NOTATION_CANDIDATE")
                # Does not turn a bare string into lexeme/abbreviation evidence.
                row={"id":f"CASINOS-{region}-U{ordinal:02d}","phys_id":case["object_id"],
                     "side":side,"line":line,"unit":ordinal,
                     "source_reference":case["review_reference"],
                     "figure_photo":"2014 fig.1 p.207; repository reports reproduction inspected",
                     "figure_drawing":"2014 fig.2 p.208; repository reports reproduction inspected",
                     "graphic_region":region,"graphic_evidence_id":g["evidence_id"] if g else None,
                     "graphic_evidence_status":"REPRODUCTION_INSPECTED_NOT_SIGN_VERIFIED" if g else "NOT_LINKED_TO_IMAGE",
                     "original_pixel_coordinates":None,
                     "editorial_reading_alternatives":readings,
                     "reading_invariant":len(readings)==1,
                     "reading_weights":"UNASSIGNED_NOT_CALIBRATED",
                     "editions_assumed_independent":False,
                     "editorial_stroke_runs":features[0]["stroke_runs_in_edition"] if shared_runs else None,
                     "editorial_stroke_stability":bool(has_num and shared_runs),
                     "possible_function_classes":possible,
                     "external_archaeological_function_evidence":"NOT_VERIFIED",
                     "inferred_translation":None,
                     "decision":"ABSTAIN_NO_INDEPENDENT_GRAPHIC_OR_CONTEXT"}
                rows.append(row)
    return rows

def assess(rows):
    invariant=sum(x["reading_invariant"] for x in rows)
    alternatives=[x for x in rows if not x["reading_invariant"]]
    numeric=[x for x in rows if x["editorial_stroke_stability"]]
    # Never treat structural editorial invariance as an archaeological prediction.
    return {"unit_count":len(rows),"editorial_invariant_units":invariant,
            "alternative_units":len(alternatives),"editorial_numeric_notation_units":len(numeric),
            "glyphs_independently_verified":sum(bool(x["original_pixel_coordinates"]) and
                      x["graphic_evidence_status"]=="SIGN_VERIFIED" for x in rows),
            "functional_attributions_validated":0,"translations_validated":0,
            "abstentions":sum(x["decision"].startswith("ABSTAIN") for x in rows),
            "status":"EXPLORATORY_MODEL_WITH_EXPLICIT_ABSTENTION"}

def run():
    case,graphic=load_case()
    rows=make_lattice(case,graphic)
    summary=assess(rows)
    OUT.mkdir(parents=True,exist_ok=True)
    report={"protocol":"DISCOVER-25","object":"IBR-PLM-0007",
            "source_hashes":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (SOURCE,GRAPH)},
            "summary":summary,
            "method":"Editorial lattice + graphic provenance + function eligibility; no posterior probabilities without calibrated likelihoods.",
            "semantic_hypotheses":["PHONETIC","ABBREVIATION","LOGOGRAM","QUANTITATIVE_MARK","NONLINGUISTIC"],
            "limitations":["One object with alternative readings; not independent replicates.",
                           "Figure-level references are not region-coordinate glyph evidence.",
                           "Editorial Roman strokes not independently authenticated in image.",
                           "No independent archaeological meaning labels.",
                           "Any confidence percentages here would be unfounded."]}
    (OUT/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    (OUT/"evidence_lattice.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf-8")
    with (OUT/"review_queue.csv").open("w",encoding="utf-8",newline="") as f:
        fields=["id","side","line","unit","graphic_evidence_id","graphic_evidence_status",
                "reading_invariant","editorial_stroke_stability","decision"]
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        w.writerows([{k:r[k] for k in fields} for r in rows])
    print(json.dumps(summary,ensure_ascii=False))
    return summary

if __name__=="__main__":run()
