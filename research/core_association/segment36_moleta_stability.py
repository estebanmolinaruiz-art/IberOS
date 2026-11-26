#!/usr/bin/env python3
"""SEGMENT-36: stability audit and split proposals inside SEGMENT-35 bands.
Does not estimate glyph accuracy nor use any editorial labels.
"""
import csv,json,hashlib,sys,subprocess
from pathlib import Path
import cv2,numpy as np
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[2]
PARENT=ROOT/"research/core_association"
INPUT=PARENT/"segment35_results"
SOURCE=PARENT/"segment34_results"
OUT=PARENT/"segment36_results"
OUT.mkdir(parents=True,exist_ok=True)
if not (INPUT/"candidate_row_bands.csv").exists():
    subprocess.run([sys.executable,str(PARENT/"segment35_moleta_lines.py")],check=True,capture_output=True)
with (INPUT/"candidate_row_bands.csv").open(newline="",encoding="utf8") as f:
    bands=list(csv.DictReader(f))
assert len(bands)>0
def runs(ys,max_gap=3):
    if len(ys)==0:return []
    out=[];start=prev=int(ys[0])
    for yy in ys[1:]:
        y=int(yy)
        if y-prev>max_gap:out.append((start,prev+1));start=y
        prev=y
    out.append((start,prev+1));return out
records=[]
for fig in (4,5):
    image_path=SOURCE/f"moleta_fig{fig}_candidate_zone.png"
    image=np.asarray(Image.open(image_path).convert("L"))
    rgb=Image.open(image_path).convert("RGB")
    draw=ImageDraw.Draw(rgb)
    for b in bands:
        if int(b["figure"])!=fig:continue
        xa,xb,ya,yb=(int(b[v]) for v in ["x0_px","x1_px","y0_px","y1_px"])
        roi=image[ya:yb,xa:xb]
        if roi.size==0:continue
        variants=[]
        # Independently create candidate subline components under distinct reasonable contrast techniques.
        for variant in ("otsu","adaptive31","adaptive51"):
            if variant=="otsu":
                _,binary=cv2.threshold(roi,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            else:
                win=int(variant.replace("adaptive",""))
                eq=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8)).apply(roi)
                binary=cv2.adaptiveThreshold(eq,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY_INV,win,8)
            # exclude horizontal rules, as in previous work, but inspect how results vary.
            long_h=cv2.morphologyEx(binary,cv2.MORPH_OPEN,
                                   cv2.getStructuringElement(cv2.MORPH_RECT,(max(30,roi.shape[1]//7),1)))
            binary=cv2.subtract(binary,long_h)
            # projection detects feasible internal blank corridors, not genuine glyph boundaries
            ink=(binary>0).sum(axis=1)/binary.shape[1]
            z=cv2.GaussianBlur(ink.astype(np.float32).reshape(-1,1),(1,7),0).ravel()
            th=max(0.012,float(np.quantile(z,0.50))*.35)
            empty=z<th
            corridors=runs(np.where(empty)[0],max_gap=3)
            # Disallow cuts near ROI edge and very short gaps.
            middle=[(a+bb)/2 for a,bb in corridors
                    if bb-a>=max(4,int(roi.shape[0]*.025))
                    and a>=int(roi.shape[0]*.12) and bb<=int(roi.shape[0]*.88)]
            variants.append({"method":variant,"candidate_separators_local_y":[round(float(v),1) for v in middle],
                             "ink_occupancy":round(float((binary>0).mean()),4)})
        # Trust only separators appearing across ALL three binarisations near same row.
        stable=[]
        tolerance=max(6,round(roi.shape[0]*.045))
        for pos in variants[0]["candidate_separators_local_y"]:
            if all(any(abs(pos-x)<=tolerance for x in v["candidate_separators_local_y"]) for v in variants[1:]):
                if not any(abs(pos-x)<=tolerance for x in stable):stable.append(pos)
        absolute=[int(round(ya+y)) for y in stable]
        for pos in absolute:
            draw.line((xa,pos,xb,pos),fill=(0,130,220),width=3)
        draw.rectangle((xa,ya,xb,yb),outline=(225,60,40),width=2)
        draw.text((xa+5,ya+4),b["candidate_id"].split("-")[-1],fill=(225,60,40))
        records.append({"figure":fig,"band_id":b["candidate_id"],
                        "original_band":[xa,ya,xb,yb],
                        "methods":variants,"stable_separator_y":absolute,
                        "stable_count":len(absolute),
                        "status":"STABLE_IMAGE_CORRIDORS_NOT_VERIFIED_TEXT_LINES"})
    rgb.save(OUT/f"moleta_fig{fig}_subbands_UNVERIFIED.png")
report={"protocol":"SEGMENT-36","source":"SEGMENT-34 source PDF image crops; SEGMENT-35 candidate bands",
        "input_band_count":len(bands),"processed_band_count":len(records),
        "stable_internal_separator_candidates":sum(r["stable_count"] for r in records),
        "bands_with_stable_internal_separator":sum(r["stable_count"]>0 for r in records),
        "independently_confirmed_text_lines":0,"independently_verified_glyphs":0,
        "external_segmentation_accuracy":None,
        "method":"Otsu/adaptive31/adaptive51 thresholding followed by ink-projection blank corridors; intersection consensus",
        "caution":"A stable blank corridor may be between decorative elements, damaged areas or multiple unrelated figures; it is not independently confirmed writing.",
        "regions":records}
(OUT/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8")
with (OUT/"candidate_subdivisions.csv").open("w",encoding="utf8",newline="") as f:
    writer=csv.writer(f);writer.writerow(["figure","band_id","stable_separator_y","status"])
    for r in records:
        if r["stable_separator_y"]:
            for y in r["stable_separator_y"]:writer.writerow([r["figure"],r["band_id"],y,r["status"]])
        else:writer.writerow([r["figure"],r["band_id"],"",r["status"]])
print(json.dumps({k:v for k,v in report.items() if k!="regions"},ensure_ascii=False))
print("DETAIL",json.dumps([{"band":r["band_id"],"stable_y":r["stable_separator_y"],"alt_counts":[len(x["candidate_separators_local_y"]) for x in r["methods"]]} for r in records],ensure_ascii=False))
