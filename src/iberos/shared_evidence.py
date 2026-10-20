"""Shared, conservative evidence contract for the six IberOS CORE pillars.

This is an intake and linking contract, not a decoder or approval engine.
"""
from __future__ import annotations

from collections import Counter

LAYERS = frozenset(("EDITORIAL", "GRAPHIC", "LINGUISTIC_HYPOTHESIS", "SYMBOLIC_HYPOTHESIS", "ARCHAEOLOGICAL_CONTEXT", "VALIDATION"))
STATES = frozenset(("UNVERIFIED", "CANDIDATE", "REVIEWED", "REJECTED"))
PILLARS = frozenset(("PALEO", "MORPH", "ICONO", "VALIDATION", "CORPUS", "LAB"))

def validate_evidence(records: list[dict]) -> dict:
    if not isinstance(records, list):
        raise ValueError("Evidence input must be a list")
    seen = set()
    out = []
    for i, item in enumerate(records):
        if not isinstance(item, dict):
            raise ValueError(f"Evidence {i} must be a dictionary")
        eid = item.get("evidence_id")
        oid = item.get("object_id")
        source = item.get("source_reference")
        layer = item.get("layer")
        state = item.get("state")
        pillars = item.get("pillars")
        if not isinstance(eid, str) or not eid.strip() or eid in seen:
            raise ValueError("Every evidence_id must be unique and nonempty")
        seen.add(eid)
        if not isinstance(oid, str) or not oid.strip():
            raise ValueError("object_id is mandatory")
        if not isinstance(source, str) or not source.strip():
            raise ValueError("source_reference is mandatory")
        if layer not in LAYERS or state not in STATES:
            raise ValueError("Unknown evidence layer or state")
        if not isinstance(pillars, list) or not pillars or any(p not in PILLARS for p in pillars):
            raise ValueError("At least one valid pillar is mandatory")
        if len(pillars) != len(set(pillars)):
            raise ValueError("Duplicate pillar labels")
        if layer == "GRAPHIC":
            if item.get("source_image_sha256") is not None:
                value = item["source_image_sha256"]
                if not isinstance(value, str) or len(value) != 64 or any(c not in "0123456789abcdefABCDEF" for c in value):
                    raise ValueError("Invalid graphic source SHA-256")
            coords = item.get("bbox_xyxy")
            if coords is not None:
                if not isinstance(coords, list) or len(coords) != 4 or not all(type(n) in (int, float) for n in coords):
                    raise ValueError("bbox_xyxy must be four numeric coordinates")
                if not (coords[0] < coords[2] and coords[1] < coords[3]):
                    raise ValueError("Invalid evidence bounding box")
        if item.get("scientifically_validated") is True or item.get("automatic_core_promotion") is True:
            raise ValueError("Evidence intake cannot assert scientific validation or promotion")
        dependencies = item.get("dependent_on", [])
        if not isinstance(dependencies, list):
            raise ValueError("dependent_on must be a list")
        preserved = {k:item[k] for k in ("source_image_sha256", "bbox_xyxy", "source_page", "sign_label", "reading_alternatives", "reviewer") if k in item}
        out.append({
            "evidence_id":eid,"object_id":oid,"source_reference":source,
            "layer":layer,"state":state,"pillars":list(pillars),
            "dependent_on":list(dependencies),
            **preserved,
            "scientifically_validated":False,"automatic_core_promotion":False
        })
    ids = set(seen)
    for record in out:
        deps = record["dependent_on"]
        if any(not isinstance(dep, str) or dep not in ids or dep == record["evidence_id"] for dep in deps):
            raise ValueError("Dependencies must refer to other records in the same batch")
        if len(deps) != len(set(deps)):
            raise ValueError("Duplicate evidence dependency")
    graph = {record["evidence_id"]:record["dependent_on"] for record in out}
    visited, visiting = set(), set()
    def visit(node):
        if node in visiting:
            raise ValueError("Circular evidence dependency")
        if node in visited:
            return
        visiting.add(node)
        for dep in graph[node]:
            visit(dep)
        visiting.remove(node)
        visited.add(node)
    for node in graph:
        visit(node)
    return {"schema":"IberOS-Core-Shared-Evidence/1.0","count":len(out),
            "layers":dict(Counter(x["layer"] for x in out)),
            "records":out,"automatic_core_promotion":False,
            "scientific_validation":"NOT_ESTABLISHED_BY_THIS_CONTRACT"}
