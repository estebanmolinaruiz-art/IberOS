#!/usr/bin/env python3
"""SEGMENT-35: propose row bands *within* SEGMENT-34 external Moleta figure crops.
No editorial sign labels or Orleyl cut coordinates are used.
"""
from pathlib import Path
import sys,json,hashlib,csv
import numpy as np
import cv2
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parents[2]
# Run SEGMENT-34 if original images not locally present in fresh Actions workspace.
directory=ROOT/"research/core_association/segment34_results"
if not all((directory/f"moleta_fig{n}_candidate_zone.png").exists() for n in [4,5]):
    import subprocess
    subprocess.run([sys.executable,str(ROOT/"research/core_association/segment34_moleta_roi.py")],check=True)
out=ROOT/"research/core_association/segment35_results"
out.mkdir(exist_ok=True)
all_rows=[]
figure_summaries=[]
for fig in (4,5):
    img=Image.open(directory/f"moleta_fig{fig}_candidate_zone.png").convert("RGB")
    raw=np.asarray(img)
    h,w=raw.shape[:2]
    gray=cv2.cvtColor(raw,cv2.COLOR_RGB2GRAY)
    # Extract dark strokes with local contrast, rather than the absolute darkness
    # of the object's photographed surface.
    clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    eq=clahe.apply(gray)
    mask=cv2.adaptiveThreshold(eq,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,31,8)
    # remove horizontal rules (not absolutely all actual strokes)
    long_horiz=cv2.morphologyEx(mask,cv2.MORPH_OPEN,
           cv2.getStructuringElement(cv2.MORPH_RECT,(max(30,w//7),1)))
    clean=cv2.subtract(mask,long_horiz)
    # Crop analysis in x to reduce plate borders.
    xa,xb=int(w*.10),int(w*.90)
    ink=np.count_nonzero(clean[:,xa:xb],axis=1).astype(float)/max(1,xb-xa)
    # locally smooth at approximate stroke scale
    smooth=cv2.GaussianBlur(ink.reshape(-1,1).astype(np.float32),(1,9),0).ravel()
    threshold=max(0.015,float(np.percentile(smooth,68))*0.72)
    active=smooth>threshold
    # Candidate bands contiguous in y. Bridge small gaps, but never use a line count.
    gap=int(np.clip(round(h*.009),4,11))
    ys=np.where(active)[0]
    intervals=[]
    if len(ys):
        start=prev=int(ys[0])
        for y in ys[1:]:
            y=int(y)
            if y-prev>gap:
                intervals.append([start,prev+1]);start=y
            prev=y
        intervals.append([start,prev+1])
    minheight=max(9,round(h*.013))
    raw_intervals=[v for v in intervals if v[1]-v[0]>=minheight]
    # Keep margins so a single glyph's upper/lower strokes aren't clipped.
    padding=max(3,round(h*.007))
    rows=[]
    for a,b in raw_intervals:
        aa=max(0,a-padding);bb=min(h,b+padding)
        sub=clean[aa:bb,xa:xb]
        density=float(np.count_nonzero(sub)/max(1,sub.size))
        # A row candidate is not guaranteed to be a text line; decorative drawing
        # edges, surface damage, scale bars and raster noise can qualify.
        if density<0.01:continue
        rows.append({"figure":fig,"candidate_id":f"MOLETA-FIG{fig}-B{len(rows)+1:02d}",
                     "x0_px":xa,"y0_px":aa,"x1_px":xb,"y1_px":bb,
                     "ink_density":round(density,4),
                     "status":"UNVERIFIED_HORIZONTAL_INK_BAND"})
    # Ranking is diagnostic only; when crowded, output all without forced 12 rows.
    for r in rows:all_rows.append(r)
    canvas=img.copy();draw=ImageDraw.Draw(canvas)
    for r in rows:
        draw.rectangle((r["x0_px"],r["y0_px"],r["x1_px"],r["y1_px"]),
                       outline=(215,25,20),width=2)
        draw.text((r["x0_px"]+3,r["y0_px"]+2),r["candidate_id"].split("-")[-1],fill=(215,25,20))
    preview=out/f"moleta_fig{fig}_bands_UNVERIFIED.png";canvas.save(preview)
    figure_summaries.append({
        "figure":fig,"crop_size":[w,h],"bands":len(rows),
        "x_analysis":[xa,xb],"smoothed_ink_threshold":round(threshold,5),
        "raw_contiguous_intervals":len(intervals),
        "previews_sha256":hashlib.sha256(preview.read_bytes()).hexdigest(),
        "caution":"Bands may include damage and non-text; no sign boundaries verified"
    })
with (out/"candidate_row_bands.csv").open("w",encoding="utf8",newline="") as f:
    keys=["figure","candidate_id","x0_px","y0_px","x1_px","y1_px","ink_density","status"]
    writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader();writer.writerows(all_rows)
report={"protocol":"SEGMENT-35","method":"adaptive contrast, suppress long horizontal rules, 1D projection, contiguous bands",
        "source":"SEGMENT-34 original figure pixel crops",
        "figures":figure_summaries,"total_provisional_bands":len(all_rows),
        "independently_verified_text_rows":0,"independently_verified_glyphs":0,
        "external_segmentation_accuracy":None,"generalization_confirmed":False,
        "next_gate":"Human/independent visual adjudication of figure and row bounds before sign segmentation",
        "warnings":["Not calibrated across photos vs drawings.",
                    "A contiguous ink band can contain multiple actual text lines or decorations.",
                    "Predicted y-bands and x10%-90% zone are heuristic and require visual verification.",
                    "Figure crops remain subject to source reproduction restrictions."]}
(out/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8")
print(json.dumps(report,ensure_ascii=False))
print("CANDIDATE_ROWS",json.dumps(all_rows,ensure_ascii=False))
