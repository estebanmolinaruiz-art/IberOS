#!/usr/bin/env python3
"""CORE research utility: inventory sign alternatives without asserting translations."""
import argparse,csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def inspect(rows):
 out=[];counts={"total":0,"editorial_only":0,"independent":0,"unresolved":0}
 for r in rows:
  counts["total"]+=1
  label=r.get("Fletcher_editorial","").strip()
  candidates=r.get("MLH_III_iberian_candidate_group","").strip()
  exact=r.get("exact_MLH_variant","").strip()
  independent=r.get("independent_reading","").upper()=="YES"
  if independent:counts["independent"]+=1
  else:counts["editorial_only"]+=1
  unresolved=exact in ("","UNRESOLVED")
  if unresolved:counts["unresolved"]+=1
  out.append({"object_id":r.get("object"),"index":r.get("index"),
   "editorial_sign":label,"candidate_variants":candidates,
   "exact_variant":None if unresolved else exact,
   "evidence_level":"INDEPENDENT_READING_DECLARED" if independent else "EDITORIAL_WITH_CANDIDATES",
   "semantic_translation":None})
 return {"counts":counts,"records":out,"scientific_status":"NOT_EVALUATED",
 "note":"Candidate variants and editorial signs are not independent paleographic identification or translation."}
def load(path):
 with open(path,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--source",default=str(ROOT/"data/review/validation01_m06_mlh_17_candidate_matches_2026-10-22.csv"));p.add_argument("--output");a=p.parse_args()
 result=inspect(load(a.source));s=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
 if a.output:Path(a.output).write_text(s,encoding="utf8")
 else:print(s,end="")
