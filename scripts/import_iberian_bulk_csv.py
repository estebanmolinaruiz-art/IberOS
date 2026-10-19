#!/usr/bin/env python3
"""Mass staged intake: SOURCE RECORDS only. Never derives sign reading from opaque text."""
import argparse,csv,hashlib,json
from pathlib import Path
def build(input_path,output_path,source,license_code,limit=100000):
    if license_code not in ("CC-BY-NC-SA-3.0","PERMISSION_RECORDED","METADATA_ONLY"):
        raise ValueError("Licence must be declared")
    rows=0;seen=set();dupes=0
    with open(input_path,encoding="utf-8-sig",newline="") as inp,open(output_path,"w",encoding="utf-8",newline="") as out:
        reader=csv.DictReader(inp)
        if not reader.fieldnames or not {"reference","transcription_raw"}.issubset(reader.fieldnames):
            raise ValueError("Required columns: reference, transcription_raw; optional: physical_group, support, edition_url, notes, uncertainty")
        writer=csv.DictWriter(out,fieldnames=["record_id","source_id","reference","transcription_raw","physical_group","support","edition_url","notes","uncertainty","license","reading_state","te_status","hold_eligible"])
        writer.writeheader()
        for row in reader:
            if rows>=limit:raise ValueError("Import limit exceeded")
            ref=(row.get("reference") or "").strip(); raw=row.get("transcription_raw") or ""
            if not ref or not raw.strip():continue
            # Never collapse different source readings, editions, or physical specimens.
            rid=hashlib.sha256((source+"\0"+ref+"\0"+raw).encode()).hexdigest()[:20]
            if rid in seen:dupes+=1;continue
            seen.add(rid)
            writer.writerow({"record_id":rid,"source_id":source,"reference":ref,
                "transcription_raw":raw,"physical_group":row.get("physical_group",""),
                "support":row.get("support",""),"edition_url":row.get("edition_url",""),
                "notes":row.get("notes",""),"uncertainty":row.get("uncertainty",""),
                "license":license_code,"reading_state":"RAW_UNREVIEWED",
                "te_status":"UNKNOWN","hold_eligible":"NO"})
            rows+=1
    return {"imported_records":rows,"duplicates_omitted":dupes,"readings_verified":0,"te_labels_verified":0,"prospective_hold":0}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("output");p.add_argument("--source",required=True);p.add_argument("--license",required=True);a=p.parse_args()
    print(json.dumps(build(a.input,a.output,a.source,a.license),indent=2))
