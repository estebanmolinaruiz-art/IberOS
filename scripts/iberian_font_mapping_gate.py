#!/usr/bin/env python3
"""Conservative conversion of specialty-font codepoints to reviewed sign tokens.
Never guess mappings; unknowns block promotion to atomic-sign TE testing.
"""
import argparse,csv,json,hashlib
from pathlib import Path
def convert(rows,mapping):
    allowed={"REVIEWED_MAPPING"}
    lookup={}
    for row in mapping:
        glyph=row.get("source_codepoint","")
        val=row.get("sign_value","")
        if row.get("review_status") not in allowed or not glyph or not val:continue
        if len(glyph)!=1:raise ValueError("Mapping source_codepoint must be one character")
        if glyph in lookup and lookup[glyph]!=val:raise ValueError("Conflicting signed mappings")
        lookup[glyph]=val
    report=[]
    for row in rows:
        raw=row.get("transcription_raw","")
        parts=[];unknown=[]
        for ch in raw:
            if ch.isspace():continue
            if ch in lookup:parts.append(lookup[ch])
            else:unknown.append("U+%04X"%ord(ch))
        ready=bool(parts) and not unknown and row.get("uncertainty","").strip() in ("","NONE") and not row.get("editorial_markup","").strip()
        report.append({"record_id":row.get("record_id",""),"reference":row.get("reference",""),
          "atomic_sign_tokens":" ".join(parts) if ready else "",
          "decode_status":"CANDIDATE_MAPPING_ONLY" if ready else "BLOCKED",
          "unmapped_codepoints":" ".join(sorted(set(unknown))),
          "te_status":"UNKNOWN","independent_sign_review":"NO",
          "source_reading":raw})
    return report
def main():
    p=argparse.ArgumentParser();p.add_argument("records");p.add_argument("mapping");p.add_argument("out");a=p.parse_args()
    def load(file):
        with open(file,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
    res=convert(load(a.records),load(a.mapping))
    with open(a.out,"w",encoding="utf8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["record_id","reference","atomic_sign_tokens","decode_status","unmapped_codepoints","te_status","independent_sign_review","source_reading"]);w.writeheader();w.writerows(res)
    print(json.dumps({"records":len(res),"candidate_mapping_only":sum(x["decode_status"]=="CANDIDATE_MAPPING_ONLY" for x in res),"scientifically_verified":0}))
if __name__=="__main__":main()
