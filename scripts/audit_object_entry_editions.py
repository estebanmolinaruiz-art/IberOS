"""Audit physical object -> entry -> edition provenance without inventing identities."""
from __future__ import annotations
import csv
import json
from collections import Counter
from pathlib import Path

def inspect(root: Path) -> dict:
    root=Path(root)
    objects=[json.loads(s) for s in (root/"data/curated/iberos_curated_objects_v1.jsonl").read_text(encoding="utf-8").splitlines() if s.strip()]
    with (root/"data/curated/iberos_partial_entry_link_v2.4.csv").open(encoding="utf-8-sig",newline="") as fh:
        links=list(csv.DictReader(fh))
    by_id={o["object_id"]:o for o in objects}
    if len(by_id)!=len(objects):
        raise ValueError("Duplicate curated object ID")
    linked, issues=[],[]
    upstream_owners={}
    for row in links:
        oid=row["OBJECT_ID"]
        codes=[x.strip() for x in row.get("UPSTREAM_IDS","").split(";") if x.strip()]
        if oid not in by_id:
            issues.append({"object_id":oid,"code":"LINKED_OBJECT_NOT_CURATED"})
            continue
        for code in codes:
            if code in upstream_owners and upstream_owners[code]!=oid:
                issues.append({"object_id":oid,"code":"UPSTREAM_ID_REUSED_ACROSS_OBJECTS","upstream_id":code,"other_object":upstream_owners[code]})
            upstream_owners[code]=oid
        if len(codes)!=len(set(codes)):
            issues.append({"object_id":oid,"code":"DUPLICATE_ENTRY_IN_GROUP"})
        claimed=row.get("Verified_ID_Count","").strip()
        if not claimed.isdigit() or int(claimed)!=len(codes):
            issues.append({"object_id":oid,"code":"ENTRY_COUNT_MISMATCH","claimed":claimed,"observed":len(codes)})
        linked.append({"object_id":oid,"upstream_ids":codes,"upstream_status":row.get("Link_Status",""),"upstream_source":row.get("Source_URL","")})
    by_link={x["object_id"]:x for x in linked}
    assessment=[]
    for obj in objects:
        oid=obj["object_id"]
        entry=obj.get("entry_status","")
        upstream=by_link.get(oid)
        flags=[]
        if entry=="NEEDS_SUBENTRY_SPLIT":
            flags.append("SUBENTRY_SPLIT_REQUIRED")
        if upstream is None:
            flags.append("NO_INDIVIDUAL_ENTRY_LINK")
        elif upstream["upstream_status"] not in ("VERIFIED","FULL_GROUP_VERIFIED"):
            flags.append("PARTIAL_OR_UNRESOLVED_UPSTREAM_GROUP")
        if not obj.get("source"):
            flags.append("NO_BIBLIOGRAPHIC_REFERENCE")
        if str(obj.get("source","")).startswith("https://es.wikipedia.org/"):
            flags.append("SECONDARY_ENCYCLOPEDIA_NOT_PRIMARY_EDITION")
        # Sources present here have not been checked for text-to-physical-witness correspondence.
        flags.append("EDITION_TO_ENTRY_NOT_INDEPENDENTLY_COLLATED")
        assessment.append({
            "object_id":oid,"name":obj.get("name"),"epigraphic_reference":obj.get("epigraphic_reference"),
            "source_reference":obj.get("source"),"entry_status":entry,
            "upstream":upstream,"open_checks":flags,
            "physical_entry_edition_verified":False
        })
    return {"schema":"IberOS-Object-Entry-Edition-Audit/1.0",
            "object_count":len(objects),"individual_link_table_rows":len(links),
            "objects_with_upstream_anchor":sum(a["upstream"] is not None for a in assessment),
            "needs_subentry_split":sum(a["entry_status"]=="NEEDS_SUBENTRY_SPLIT" for a in assessment),
            "verified_physical_entry_edition":0,
            "structural_issues":issues,"assessments":assessment,
            "scope_note":"A verified upstream ID is an index link, not independent visual or diplomatic collation.",
            "automatic_scientific_promotion":False}

def main():
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument("--out",type=Path)
    args=p.parse_args()
    value=json.dumps(inspect(args.root),ensure_ascii=False,indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(value,encoding="utf-8")
    else:print(value,end="")

if __name__=="__main__":
    main()
