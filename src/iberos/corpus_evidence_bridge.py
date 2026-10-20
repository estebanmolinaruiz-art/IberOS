"""6P-03: conservative corpus-to-evidence adapter; no semantic promotion."""
from __future__ import annotations
import csv
import json
from collections import Counter
from pathlib import Path
from .shared_evidence import validate_evidence

def link_corpus(curated: list[dict], registry: list[dict]) -> dict:
    if not isinstance(curated,list) or not isinstance(registry,list):
        raise ValueError("Expected two lists")
    index={}
    for row in registry:
        oid=row.get("OBJECT_ID","")
        if not isinstance(oid,str) or not oid.strip() or oid in index:
            raise ValueError("Invalid or duplicate registry OBJECT_ID")
        index[oid]=row
    seen=set()
    ready=[]
    issues=[]
    for row in curated:
        oid=row.get("object_id")
        if not isinstance(oid,str) or not oid.strip() or oid in seen:
            raise ValueError("Invalid or duplicate curated object_id")
        seen.add(oid)
        if oid not in index:
            issues.append({"object_id":oid,"issue":"NOT_IN_REGISTRY"})
            continue
        registry_row=index[oid]
        source=row.get("source")
        registry_source=registry_row.get("Fuente")
        if not isinstance(source,str) or not source.strip():
            issues.append({"object_id":oid,"issue":"MISSING_CURATED_SOURCE"})
            continue
        if registry_source and registry_source.strip()!=source.strip():
            issues.append({"object_id":oid,"issue":"SOURCE_CONFLICT","curated_source":source,"registry_source":registry_source})
            continue
        ready.append({
            "evidence_id":"CORPUS-"+oid,
            "object_id":oid,
            "source_reference":source.strip(),
            "layer":"ARCHAEOLOGICAL_CONTEXT",
            "state":"CANDIDATE",
            "pillars":["CORPUS","LAB"],
        })
    shared=validate_evidence(ready)
    return {
        "schema":"IberOS-Corpus-Evidence-Bridge/1.0",
        "curated_objects":len(curated),"registry_objects":len(registry),
        "linked_objects":shared["count"],"unlinked_curated_objects":len(issues),
        "issues":issues,
        "evidence":shared,
        "note":"Metadata sourced from registry; linked means structurally connected, not primary-source-reviewed or independent.",
        "automatic_core_promotion":False
    }

def link_repository(root: Path) -> dict:
    root=Path(root)
    curated_path=root/"data/curated/iberos_curated_objects_v1.jsonl"
    registry_path=root/"data/curated/iberos_objects_registry_v2.0.csv"
    curated=[json.loads(s) for s in curated_path.read_text(encoding="utf-8").splitlines() if s.strip()]
    with registry_path.open(encoding="utf-8-sig",newline="") as fh:
        registry=list(csv.DictReader(fh))
    return link_corpus(curated,registry)
