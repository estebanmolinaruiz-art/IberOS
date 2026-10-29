#!/usr/bin/env python3
"""Check M06 evidence completeness without equating editorial alignment to validation."""
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(path):
 with open(path,encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def audit(align,typology):
 issues=[]
 expected={("ORLEYL-V",i) for i in range(1,10)}|{("ORLEYL-VII",i) for i in range(1,9)}
 keys=set()
 for row in align:
  try:k=(row["object_id"],int(row["index"]))
  except (ValueError,KeyError):issues.append("INVALID_ALIGNMENT_INDEX");continue
  if k in keys:issues.append("DUPLICATED_ALIGNMENT_INDEX:"+str(k))
  keys.add(k)
  if row.get("coordinate_verification")!="VERIFIED":pass
  if row.get("mapping_basis")=="EDITORIAL_TOKEN_ORDER_ONLY":pass
 for k in expected-keys:issues.append("MISSING_ALIGNMENT:"+str(k))
 for k in keys-expected:issues.append("EXTRA_ALIGNMENT:"+str(k))
 tkeys=set()
 for row in typology:
  try:k=(("ORLEYL-VII" if row["object"]=="ORLEYL-VIIB" else row["object"]),int(row["index"]))
  except (ValueError,KeyError):issues.append("INVALID_TYPOLOGY_INDEX");continue
  if k in tkeys:issues.append("DUPLICATED_TYPOLOGY_INDEX:"+str(k))
  tkeys.add(k)
 for k in expected-tkeys:issues.append("MISSING_TYPOLOGY:"+str(k))
 editor={(r["object_id"],int(r["index"])):r.get("editorial_token","") for r in align if r.get("index","").isdigit()}
 for row in typology:
  k=("ORLEYL-VII" if row.get("object")=="ORLEYL-VIIB" else row.get("object"),int(row["index"]))
  if k in editor and editor[k]!=row.get("Fletcher_editorial"):issues.append("EDITORIAL_TOKEN_DISAGREEMENT:"+str(k))
 verified=sum(r.get("coordinate_verification")=="VERIFIED" for r in align)
 independently_read=sum(r.get("independent_reading")=="YES" for r in typology)
 resolved=sum(r.get("exact_MLH_variant") not in ("","UNRESOLVED") for r in typology)
 return {"alignment_rows":len(align),"typology_rows":len(typology),"coordinate_verified":verified,"independent_readings":independently_read,"exact_variants_recorded":resolved,"issues":sorted(issues),"m06":"PENDING" if verified!=17 or resolved!=17 or issues else "REQUIRES_HUMAN_REVIEW","m07":"PENDING" if independently_read!=17 else "REQUIRES_REVIEW_OF_INDEPENDENCE","scientific_result":"NOT_EVALUATED"}
if __name__=="__main__":
 print(json.dumps(audit(read(ROOT/"data/review/validation01_orleyl_17_visual_alignment_v1.csv"),read(ROOT/"data/review/validation01_m06_mlh_17_candidate_matches_2026-10-22.csv")),ensure_ascii=False,indent=2))
