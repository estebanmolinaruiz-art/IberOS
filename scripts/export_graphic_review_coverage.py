#!/usr/bin/env python3
"""Generate whole-corpus graphic review coverage without implying glyph validation."""
import json
from pathlib import Path
from iberos.core import load_registry

ROOT=Path(__file__).resolve().parents[1]
REVIEW=ROOT/"data/review"
OUTPUT=ROOT/"site/data/graphic_review_coverage_v1.json"

def generate():
    rows=list(load_registry())
    files=("casinos_graphic_uncertainties_v1.json","sagunto_caminreal_graphic_uncertainties_v1.json")
    evidence=[]
    for filename in files:
        obj=json.loads((REVIEW/filename).read_text(encoding="utf-8"))
        evidence.extend(obj["records"])
    by_object={}
    for item in evidence:
        by_object.setdefault(item["object_id"],[]).append(item)
    ids=[r["OBJECT_ID"] for r in rows]
    if len(ids)!=38 or len(set(ids))!=38:
        raise ValueError("Corpus must contain 38 unique objects")
    if not set(by_object).issubset(ids):
        raise ValueError("Graphic evidence references unknown object")
    result=[]
    for oid in ids:
        items=by_object.get(oid,[])
        result.append({
            "object_id":oid,
            "graphic_observation_count":len(items),
            "graphic_review_status":"UNRESOLVED_GRAPHIC_OBSERVATIONS" if items else "NO_STRUCTURED_GRAPHIC_OBSERVATIONS",
            "graphic_evidence_ids":[e["evidence_id"] for e in items],
            "independently_verified_sign_count":0,
            "translation_validated":False,
            "core_semantic_approval":False
        })
    data={"schema":"IberOS-Graphic-Coverage/1.0","object_count":len(result),
          "objects_with_structured_graphic_observations":sum(bool(x["graphic_observation_count"]) for x in result),
          "graphic_observation_count":len(evidence),"independently_verified_sign_count":0,
          "translation_validated_count":0,"records":result}
    return data

if __name__=="__main__":
    data=generate()
    OUTPUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Graphic coverage: {data['object_count']} objects; {data['objects_with_structured_graphic_observations']} with structured observations; {data['graphic_observation_count']} unresolved notes")
