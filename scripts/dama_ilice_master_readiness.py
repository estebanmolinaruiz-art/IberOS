#!/usr/bin/env python3
"""Read-only evidence inventory for Dama de IberOS. Does not promote scientific states."""
import csv, json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"data/review/validation01_master_physical_objects_v1.csv"
with SOURCE.open(encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
def yes(row,k): return row.get(k,"").strip().upper()=="YES"
counts={k:sum(yes(r,k) for r in rows) for k in ("object_provenance_verified","full_sign_reading_verified","source_images_verified","HOLD_eligible")}
unresolved=[r["master_id"] for r in rows if r.get("physical_group","").strip().upper() in ("","UNRESOLVED","UNKNOWN")]
truncated=[r["master_id"] for r in rows if "TRUNCAT" in r.get("source_quality","").upper()]
report={"program":"DAMA_DE_IBEROS","inventory_source":str(SOURCE.relative_to(ROOT)),"registered_objects":len(rows),"verified":counts,"unresolved_physical_groups":len(unresolved),"unresolved_ids":unresolved,"truncated_source_ids":truncated,"independent_readers_recorded":sum(bool(r.get("independent_reader","").strip()) for r in rows),"scientific_status":"NOT_EVALUATED","note":"Administrative inventory only; counts do not prove linguistic readings."}
print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__":
 assert len(rows)>0
