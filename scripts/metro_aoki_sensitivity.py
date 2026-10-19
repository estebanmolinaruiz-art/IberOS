#!/usr/bin/env python3
"""Sensitivity analysis of *in-sample* a/o/ki model; NOT a validation claim."""
import csv,json,math,argparse
RATIOS={"HYBRID":(10,12),"DECIMAL":(10,10),"DUODECIMAL":(12,12)}
def score(rows,o,excluded=None):
    data=[r for r in rows if r["case_id"]!=excluded]
    if not data:raise ValueError("Empty sample")
    out={}
    for name,(a_ratio,ki_ratio) in RATIOS.items():
        pred={"a":o*a_ratio,"o":o,"ki":o/ki_ratio}
        errors=[100*(float(r["mass_g"])/pred[r["claimed_unit"]]-1) for r in data]
        out[name]=math.sqrt(sum(x*x for x in errors)/len(errors))
    return out
def analyze(rows,low=41,high=43,step=.25):
    if step<=0 or low<=0 or low>high:raise ValueError("Invalid range")
    values=[];n=round((high-low)/step)
    for i in range(n+1):
        o=round(low+i*step,8)
        if o>high+1e-7:break
        scores=score(rows,o)
        values.append({"reference_o_g":o,"rmse_pct":{k:round(v,5) for k,v in scores.items()},
                       "winner":min(scores,key=scores.get)})
    loo=[]
    for r in rows:
        scores=score(rows,42,excluded=r["case_id"])
        loo.append({"excluded":r["case_id"],"winner":min(scores,key=scores.get()),
                    "rmse_pct":{k:round(v,5) for k,v in scores.items()}})
    return {"kind":"RETROSPECTIVE_IN_SAMPLE_SENSITIVITY","n_cases":len(rows),"grid":values,
            "leave_one_observation_out":loo,"grid_hybrid_wins":sum(x["winner"]=="HYBRID" for x in values),
            "grid_points":len(values),"loo_hybrid_wins":sum(x["winner"]=="HYBRID" for x in loo),
            "validation01":"NOT_EVALUATED","metro_aoki01":"NOT_EXTERNALLY_VALIDATED"}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("csv_file");p.add_argument("--output");a=p.parse_args()
    with open(a.csv_file,encoding="utf8",newline="") as f:rows=list(csv.DictReader(f))
    if any(r["role"]!="IN_SAMPLE" for r in rows):raise ValueError("Only explicitly in-sample observations are supported")
    result=analyze(rows)
    body=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if a.output:
        from pathlib import Path
        Path(a.output).write_text(body,encoding="utf8")
    else:print(body)
