#!/usr/bin/env python3
"""IberOS mass staging: preserve editorial uncertainty and physical-unit identities.
Not a transliteration decoder, OCR or linguistic validation.
"""
import argparse,csv,hashlib,json
from collections import defaultdict
from pathlib import Path

LICENSES={"CC-BY-NC-SA-3.0","PERMISSION_RECORDED","METADATA_ONLY"}
OUTPUT=("record_id","source_id","reference","transcription_raw","physical_group",
        "support","edition_url","notes","uncertainty","editorial_markup",
        "source_row","license","reading_state","te_status","hold_eligible")
def build(input_path,output_path,source,license_code,limit=100000):
    if license_code not in LICENSES:raise ValueError("Licence must be declared")
    if not source.strip():raise ValueError("Source ID required")
    rows=dupes=skipped=0;seen=set();by_object=defaultdict(set);unresolved=0;marked=0
    inp_path=Path(input_path).resolve();out_path=Path(output_path).resolve()
    if inp_path==out_path:raise ValueError("Input and output must differ")
    with open(inp_path,encoding="utf-8-sig",newline="") as inp,open(out_path,"w",encoding="utf-8",newline="") as out:
        reader=csv.DictReader(inp)
        if not reader.fieldnames or not {"reference","transcription_raw"}.issubset(reader.fieldnames):
            raise ValueError("Required columns: reference, transcription_raw")
        writer=csv.DictWriter(out,fieldnames=OUTPUT);writer.writeheader()
        for source_row,row in enumerate(reader,2):
            if source_row-2>=limit:raise ValueError("Import limit exceeded")
            ref=(row.get("reference") or "").strip();raw=row.get("transcription_raw") or ""
            if not ref or not raw.strip():skipped+=1;continue
            # An uncertainty marker is not equivalent to a reviewed reading.
            uncertainty=row.get("uncertainty","") or ""
            markup=row.get("editorial_markup","") or ""
            group=(row.get("physical_group") or "").strip()
            if not group:unresolved+=1
            if uncertainty.strip() or markup.strip():marked+=1
            rid=hashlib.sha256((source+"\0"+ref+"\0"+raw).encode("utf-8")).hexdigest()[:20]
            if rid in seen:dupes+=1;continue
            seen.add(rid)
            if group:by_object[group].add(rid)
            writer.writerow(dict(record_id=rid,source_id=source,reference=ref,transcription_raw=raw,
                physical_group=group,support=row.get("support",""),edition_url=row.get("edition_url",""),
                notes=row.get("notes",""),uncertainty=uncertainty,editorial_markup=markup,
                source_row=source_row,license=license_code,reading_state="RAW_UNREVIEWED",
                te_status="UNKNOWN",hold_eligible="NO"))
            rows+=1
    return {"imported_records":rows,"duplicates_omitted":dupes,"skipped_incomplete":skipped,
      "explicit_physical_groups":len(by_object),
      "physical_groups_with_multiple_readings":sum(len(v)>1 for v in by_object.values()),
      "records_without_physical_identity":unresolved,
      "records_with_uncertainty_or_markup":marked,
      "readings_verified":0,"te_labels_verified":0,"prospective_hold":0,
      "warning":"Counts represent staged editorial rows, not unique verified inscriptions."}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("input");p.add_argument("output")
    p.add_argument("--source",required=True);p.add_argument("--license",required=True)
    p.add_argument("--report");a=p.parse_args()
    result=build(a.input,a.output,a.source,a.license)
    if a.report:Path(a.report).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
