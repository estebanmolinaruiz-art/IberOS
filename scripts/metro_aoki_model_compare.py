#!/usr/bin/env python3
"""Exploratory metrology fit, NOT independent confirmation.
All data used by author in argument; fixed o=42g and three a/o vs o/ki ratios.
"""
import argparse,csv,json,math
from collections import defaultdict
RATIOS={"HYBRID":(10,12),"DECIMAL":(10,10),"DUODECIMAL":(12,12)}
def evaluate(rows,o_g=42):
    result={}
    for model,(ao,oki) in RATIOS.items():
        pred={"a":ao*o_g,"o":o_g,"ki":o_g/oki}
        detail=[]
        for row in rows:
            unit=row["claimed_unit"];mass=float(row["mass_g"])
            if unit not in pred or mass<=0:raise ValueError("Unknown unit or invalid mass")
            rel=(mass/pred[unit]-1)*100
            detail.append({"id":row["case_id"],"unit":unit,"mass_g":mass,
                          "prediction_g":pred[unit],"relative_error_pct":round(rel,4),
                          "role":row["role"]})
        rms=math.sqrt(sum(x["relative_error_pct"]**2 for x in detail)/len(detail))
        result[model]={"rms_relative_error_pct":round(rms,4),"units_g":pred,"observations":detail}
    return {"status":"IN_SAMPLE_DESCRIPTIVE_ONLY","reference_o_g":o_g,
            "n_observations":len(rows),"model_scores":result,
            "validation01":"NOT_EVALUATED","metro_aoki01":"NOT_EXTERNALLY_VALIDATED"}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("csv_file");p.add_argument("--o-g",type=float,default=42);a=p.parse_args()
    with open(a.csv_file,encoding="utf8",newline="") as f:rows=list(csv.DictReader(f))
    if not rows or any(r.get("role")!="IN_SAMPLE" for r in rows):raise ValueError("Expected disclosed in-sample dataset")
    print(json.dumps(evaluate(rows,a.o_g),indent=2,ensure_ascii=False))
