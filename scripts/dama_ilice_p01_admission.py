#!/usr/bin/env python3
"""Dama de Ilice P01: execute strictly evidence-gated pilot against Orleyl editorial inventory."""
import csv, json, tempfile
from pathlib import Path
from corex_p01 import load, run
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"data/curated/rok_orleyl_editorial_alignment_1981.csv"
OUT=ROOT/"data/benchmark/dama_ilice_p01_admission_v1.json"
seen={}
with SOURCE.open(encoding="utf-8-sig",newline="") as f:
    for row in csv.DictReader(f):
        if row.get("sequence_role")!="comparandum":continue
        key=(row.get("phys_key"),row.get("editorial_sequence"))
        seen[key]=row
with tempfile.TemporaryDirectory() as d:
    p=Path(d)/"candidates.jsonl"
    with p.open("w",encoding="utf-8") as out:
        for (physical,sequence),row in sorted(seen.items()):
            out.write(json.dumps({
                "object_id":physical,"physical_group":physical,
                "transcription":sequence,"source":str(SOURCE.relative_to(ROOT)),
                "reading_status":row.get("editorial_status","EDITORIAL_ONLY"),
                "graphic_photo_verified":row.get("graphic_photo_verified","false")
            },ensure_ascii=False)+"\n")
    accepted,rejected=load(p)
    outcome=run(accepted)
summary={
  "program":"DAMA_DE_ILICE","pilot":"COREX_P01","input":str(SOURCE.relative_to(ROOT)),
  "candidate_physical_groups":len({k[0] for k in seen}),
  "candidate_sequences":len(seen),"accepted_sequences":len(accepted),
  "rejected_sequences":len(rejected),"rejection_reasons":rejected,
  "outcome":outcome,"scientific_status":"NOT_EVALUATED",
  "note":"Editorial-only Orleyl transcriptions are not independently verified. No model performance or translation may be claimed."
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(summary,ensure_ascii=False,indent=2))
assert not accepted,"No editorial-only sequence may enter P01"
assert outcome["status"]=="INSUFFICIENT_INDEPENDENT_GROUPS"
