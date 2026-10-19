"""Generate unlabeled regional inspection panels from user-supplied published image crops.

Usage: python scripts/build_moleta_blind_review.py --photo FILE --drawing FILE --out DIR
This creates exploratory panels, NOT sign-level ROIs or an alignment homography.
"""
import argparse
import hashlib
import json
from pathlib import Path
from PIL import Image

BINS=((0.0,0.42),(0.27,0.73),(0.58,1.0))

def build(photo:Path,drawing:Path,out:Path):
    out.mkdir(parents=True,exist_ok=True)
    result={"schema":"IberOS-Blind-Inspection/1.0","source_files":[],
       "panels":[],"glyphs_independently_verified":0,
       "limitation":"Broad overlapping bands are not aligned sign ROIs; blind only to candidate reading labels"}
    for label,path in (("photo",photo),("drawing",drawing)):
        with Image.open(path) as source:
            im=source.convert("RGB")
        result["source_files"].append({"kind":label,"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
                                      "dimensions":list(im.size)})
        for idx,(u,v) in enumerate(BINS,1):
            x0=round(im.width*u);x1=round(im.width*v)
            name=f"{label}_region_{idx}.png"
            im.crop((x0,0,x1,im.height)).save(out/name)
            result["panels"].append({"image":name,"kind":label,"bounds_px":[x0,0,x1,im.height],
              "sign_roi":None,"glyph_labels_hidden":True,"independently_assessed":False})
    (out/"manifest.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    return result

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    for k in ("photo","drawing","out"):
        parser.add_argument("--"+k,required=True,type=Path)
    a=parser.parse_args()
    d=build(a.photo,a.drawing,a.out)
    print(f"{len(d['panels'])} preliminary image panels, zero verified glyphs")
