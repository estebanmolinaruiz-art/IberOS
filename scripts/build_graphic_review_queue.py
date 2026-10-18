#!/usr/bin/env python3
"""Deterministic review queue: catalogue priority, not proven photographic quality."""
import csv
import io
import json
from pathlib import Path
from iberos.core import load_registry

ROOT=Path(__file__).resolve().parents[1]
CSV=ROOT/"src/iberos/data/iberos_objects_registry_v2.0.csv"
OUT=ROOT/"site/data/graphic_review_queue_v1.json"

def build_queue():
    with CSV.open(encoding="utf-8-sig",newline="") as fh:
        catalogue={r["OBJECT_ID"]:r for r in csv.DictReader(fh)}
    known={r["OBJECT_ID"] for r in load_registry()}
    if known!=set(catalogue) or len(known)!=38:
        raise ValueError("Registry and catalogue disagree")
    files=("casinos_graphic_uncertainties_v1.json","sagunto_caminreal_graphic_uncertainties_v1.json")
    counts={}
    for name in files:
        dataset=json.loads((ROOT/"data/review"/name).read_text(encoding="utf-8"))
        for r in dataset["records"]:
            counts[r["object_id"]]=counts.get(r["object_id"],0)+1
    output=[]
    for oid,row in catalogue.items():
        if counts.get(oid):
            continue
        modules=row.get("Modulos_Activos","").split(";")
        status=row.get("PALEO_Status","").upper()
        # Priority scores reflect operational triage only. No image was inspected here.
        score=(3 if "HIGH_UNCERTAINTY" in status else 0)+(2 if "NEEDS_SUBENTRY_SPLIT" in row.get("ENTRY_Status","") else 0)+(1 if "DUAL_LOCK" in modules else 0)
        output.append({"object_id":oid,"name":row.get("Nombre_objeto",""),"reference":row.get("Referencia_epigráfica",""),
            "source_url":row.get("Fuente",""),"paleo_status_catalogue":row.get("PALEO_Status",""),
            "entry_status_catalogue":row.get("ENTRY_Status",""),"triage_score":score,
            "corpus_role":row.get("IberOS_Inclusion",""),
            "review_lanes":("NEGATIVE_CONTROL" if row.get("IberOS_Inclusion")=="EXCLUDED_CONTROL" else ("SIGNARY_CONTROL" if row.get("IberOS_Inclusion")=="CONTROL_ONLY" else "EPIGRAPHIC_REVIEW")),
            "core_semantic_eligible":False,
            "priority_basis":"CATALOGUE_WORKFLOW_ONLY","image_access_checked":False,
            "image_rights_checked":False,"graphic_reading_verified":False,"translation_validated":False,
            "next_step":"Locate primary edition and image, verify licensing and original sign legibility"})
    output.sort(key=lambda x:(-x["triage_score"],x["object_id"]))
    return {"schema":"IberOS-Graphic-Queue/1.0","total_objects":38,"unreviewed_queue_count":len(output),
        "objects_with_existing_graphic_observations":len(counts),"prioritization":"Operational triage based on existing catalogue; NOT image-source availability or quality ranking",
        "first_batch":[{"object_id":r["object_id"],"name":r["name"],"source_url":r["source_url"],"review_lanes":r["review_lanes"],"task":"Verify edition, figure, reproduction rights and sign legibility"} for r in output[:10]],
        "records":output,"validated_translations":0}

if __name__=="__main__":
    data=build_queue()
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Review queue: {data['unreviewed_queue_count']} unobserved objects")
