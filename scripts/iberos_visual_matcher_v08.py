#!/usr/bin/env python3
"""IberOS visual nearest-neighbour prototype. Not validated palaeographic OCR."""
import argparse,csv,hashlib,json
from pathlib import Path
from collections import Counter
def samples(manifest,root):
    from PIL import Image,ImageOps
    import numpy as np
    root=Path(root).resolve()
    def vector(p):
        with Image.open(p) as im:
            v=ImageOps.contain(ImageOps.autocontrast(im.convert("L")),(28,28))
            canvas=Image.new("L",(32,32),255)
            canvas.paste(v,((32-v.width)//2,(32-v.height)//2))
            return 1-np.asarray(canvas,dtype=float).ravel()/255
    with open(manifest,encoding="utf-8-sig",newline="") as f:rows=list(csv.DictReader(f))
    groups={};out=[];ids=set()
    for r in rows:
        if r["evidence_status"]!="REVIEWED_SIGN":continue
        if not r["sample_id"] or r["sample_id"] in ids:raise ValueError("Invalid sample_id")
        ids.add(r["sample_id"]);g=r["physical_group"];split=r["split"].upper()
        if not g or split not in ("TRAIN","HOLD") or not r["sign_value"]:raise ValueError("Invalid split, group or sign")
        groups.setdefault(g,set()).add(split)
        p=(root/r["image_path"]).resolve()
        if not p.is_relative_to(root) or not p.is_file():raise ValueError("Missing or unsafe file")
        if hashlib.sha256(p.read_bytes()).hexdigest()!=r["image_sha256"].lower():raise ValueError("Bad SHA-256")
        out.append((r,split,vector(p)))
    if any(len(v)>1 for v in groups.values()):raise ValueError("Physical-object leakage")
    return out,vector
def nearest(query,train):
    import numpy as np
    return sorted(((float(np.mean((query-v)**2)),r["sign_value"],r["sample_id"]) for r,split,v in train if split=="TRAIN"))
def evaluate(data):
    train=[r for r,s,v in data if s=="TRAIN"]; hold=[(r,v) for r,s,v in data if s=="HOLD"]
    if not train or not hold:return {"state":"NOT_EVALUATED","reason":"REVIEWED_TRAIN_AND_INDEPENDENT_HOLD_REQUIRED"}
    baseline=Counter(r["sign_value"] for r in train).most_common(1)[0][0]
    observations=[{"truth":r["sign_value"],"prediction":nearest(v,data)[0][1],"baseline":baseline,"physical_group":r["physical_group"]} for r,v in hold]
    return {"state":"DESCRIPTIVE_ONLY","n":len(hold),"independent_hold_groups":len({x["physical_group"] for x in observations}),"matcher_accuracy":sum(x["truth"]==x["prediction"] for x in observations)/len(hold),"majority_baseline_accuracy":sum(x["truth"]==baseline for x in observations)/len(hold),"observations":observations,"linguistic_validation":"NOT_DEMONSTRATED"}
def main():
    p=argparse.ArgumentParser();p.add_argument("manifest");p.add_argument("--root",default=".");p.add_argument("--query");p.add_argument("--evaluate",action="store_true");args=p.parse_args()
    data,vector=samples(args.manifest,args.root)
    if args.evaluate:out=evaluate(data)
    elif args.query:
        ranks=nearest(vector(Path(args.query)),data)
        out={"state":"UNVERIFIED_VISUAL_SIMILARITY" if ranks else "ABSTAIN","alternatives":[{"value":v,"distance":round(d,6),"sample_id":sid} for d,v,sid in ranks[:5]],"confidence":"UNCALIBRATED"}
    else:out={"train":sum(s=="TRAIN" for r,s,v in data),"hold":sum(s=="HOLD" for r,s,v in data),"linguistic_validation":"NOT_DEMONSTRATED"}
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
