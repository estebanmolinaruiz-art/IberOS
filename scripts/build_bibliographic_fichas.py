#!/usr/bin/env python3
"""Build reviewable bibliographic fichas. Only run Core on verified catalogue objects."""
import json
import pathlib
import re

ROOT=pathlib.Path(__file__).resolve().parents[1]
DATA=ROOT/"site"/"data"
def normalized(value):
    return re.sub(r"[^a-z0-9]+","",str(value).casefold())
def build():
    queue=json.loads((DATA/"library_candidates_v1.json").read_text(encoding="utf-8"))
    seen=set()
    fichas=[]
    for entry in queue.get("items",[]):
        doi=str(entry.get("doi") or "").lower().strip()
        title=str(entry.get("title") or "").strip()
        url=str(entry.get("url") or "").strip()
        key=doi or normalized(title)
        if not title or not url.startswith("https://") or not key or key in seen:
            continue
        seen.add(key)
        fichas.append({
            "id":"BIB-"+str(len(fichas)+1).zfill(6),
            "type":"BIBLIOGRAPHIC_SOURCE_NOT_OBJECT",
            "title":title,"doi":doi or None,"url":url,
            "authors":entry.get("authors",""),"publisher":entry.get("publisher",""),
            "review_status":"PENDING_EDITORIAL_REVIEW",
            "object_identity_verified":False,"epigraphic_transcription_verified":False,
            "core_processing":{"status":"BLOCKED_UNVERIFIED_OBJECT","rule_results":[],
              "reason":"Una publicación no equivale a una inscripción del catálogo; falta identificar pieza, lectura y evidencia verificadas."},
            "source_rights":"Metadata and external link only"
        })
    return {"schema":"IberOS-Bibliographic-Fichas/1.0","items":fichas,
            "scientific_policy":"No automatic Core analysis of unverified bibliographic titles"}
def main():
    output=DATA/"bibliographic_fichas_v1.json"
    result=build()
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"{len(result['items'])} provisional bibliographic fichas; 0 automatic Core validations")
if __name__=="__main__":
    main()
