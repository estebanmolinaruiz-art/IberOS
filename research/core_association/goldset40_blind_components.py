#!/usr/bin/env python3
"""GOLDSET-40: image-only independent review proposals for Moleta, no phonetic readings.
This is a candidate atlas, NOT gold labels.
"""
from pathlib import Path
import cv2,numpy as np,json,csv,hashlib,subprocess,sys
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).resolve().parents[2]
work=root/"research/core_association"
source=work/"segment34_results"
out=work/"goldset40_results"
out.mkdir(parents=True,exist_ok=True)
if not all((source/f"moleta_fig{fig}_candidate_zone.png").exists() for fig in (4,5)):
    subprocess.run([sys.executable,str(work/"segment34_moleta_roi.py")],check=True)
rows=[];figures=[]
for fig in (4,5):
    filename=source/f"moleta_fig{fig}_candidate_zone.png"
    img=np.array(Image.open(filename).convert("RGB"))
    h,w=img.shape[:2]
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # Independent detector: only image pixels. No editorial spatial positions,
    # no fixed 21-count, no signary candidates or prior seven band positions.
    variants={}
    # Three distinct binary representations to measure robust external ink.
    clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8)).apply(gray)
    _,variants["otsu"]=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    for kernel in (31,51):
        variants[f"adapt{kernel}"]=cv2.adaptiveThreshold(
            clahe,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,kernel,8)
    components={}
    for key,mask in variants.items():
        n,lab,stat,cent=cv2.connectedComponentsWithStats(mask,connectivity=8)
        accepted=[]
        for j in range(1,n):
            x,y,bw,bh,area=[int(v) for v in stat[j]]
            if area<8 or bw<2 or bh<3:continue
            if bw>int(.60*w) or bh>int(.60*h):continue
            if bw*bh>int(.11*w*h):continue
            if x<4 or y<4 or x+bw>w-4 or y+bh>h-4:continue
            # At this stage CCs are trace fragments, not necessarily glyphs!
            accepted.append({"bbox":(x,y,x+bw,y+bh),"area":area,
                             "centre":(x+bw/2,y+bh/2)})
        components[key]=accepted
    # Match Otsu trace components to adaptive components through relaxed
    # centroid distance and overlap, retaining uncertain and nonmatches.
    base=components["otsu"]; canvas=Image.fromarray(img);drawing=ImageDraw.Draw(canvas)
    records=[]
    for i,c in enumerate(base):
        x0,y0,x1,y1=c["bbox"];p=np.array(c["centre"])
        consistency={}
        for method in ("adapt31","adapt51"):
            candidates=components[method]
            best=0.0; bestidx=None
            for k,cc in enumerate(candidates):
                xx0,yy0,xx1,yy1=cc["bbox"]
                inter=max(0,min(x1,xx1)-max(x0,xx0))*max(0,min(y1,yy1)-max(y0,yy0))
                small=min((x1-x0)*(y1-y0),(xx1-xx0)*(yy1-yy0))
                overlap=inter/max(1,small)
                centerdist=float(np.linalg.norm(p-np.array(cc["centre"])))
                limit=max(8,0.65*max(x1-x0,y1-y0,xx1-xx0,yy1-yy0))
                score=overlap if centerdist<=limit else 0
                if score>best:best=score;bestidx=k
            consistency[method]={"overlap_small_bbox":round(best,3),"matched_component_index":bestidx}
        stable=all(consistency[k]["overlap_small_bbox"]>=.55 for k in consistency)
        if stable and 5<=y1-y0<=min(75,int(.14*h)) and 2<=x1-x0<=min(85,int(.16*w)):
            category="TRACE_CANDIDATE_CROSS_THRESHOLD"
        elif stable:category="STABLE_COMPONENT_NOT_SIGN"
        else:category="THRESHOLD_DEPENDENT_COMPONENT"
        rid=f"MOL40-F{fig}-C{i+1:04d}"
        rec={"id":rid,"figure":fig,"x0":x0,"y0":y0,"x1":x1,"y1":y1,
             "area_otsu":c["area"],"geometric_stability":category,
             "adapt31_overlap":consistency["adapt31"]["overlap_small_bbox"],
             "adapt51_overlap":consistency["adapt51"]["overlap_small_bbox"],
             "glyph_label":None,"glyph_integrity":"NOT_REVIEWED",
             "line_assignment":None,"source_sha256":hashlib.sha256(filename.read_bytes()).hexdigest()}
        records.append(rec);rows.append(rec)
        if category=="TRACE_CANDIDATE_CROSS_THRESHOLD":
            drawing.rectangle((x0,y0,x1,y1),outline=(0,140,230),width=1)
    canvas.save(out/f"moleta_fig{fig}_blind_component_atlas.png")
    # Render a contact sheet of candidates WITHOUT editorial values.
    selected=[r for r in records if r["geometric_stability"]=="TRACE_CANDIDATE_CROSS_THRESHOLD"]
    selected=sorted(selected,key=lambda r:(r["y0"],r["x0"]))[:90]
    tilew,tileh=112,112;cols=8
    sheet=Image.new("RGB",(cols*tilew,((len(selected)+cols-1)//cols)*tileh),(255,255,255))
    sdraw=ImageDraw.Draw(sheet)
    original=Image.fromarray(img)
    for ii,r in enumerate(selected):
        xx=ii%cols*tilew; yy=ii//cols*tileh
        patch=original.crop((max(0,r["x0"]-7),max(0,r["y0"]-7),
                             min(w,r["x1"]+7),min(h,r["y1"]+7)))
        patch.thumbnail((tilew-12,tileh-26))
        sheet.paste(patch,(xx+(tilew-patch.width)//2,yy+5))
        sdraw.text((xx+4,yy+tileh-18),r["id"].split("-")[-1],fill=(0,0,0))
    if selected:sheet.save(out/f"moleta_fig{fig}_blind_trace_contact_sheet.png")
    figures.append({"figure":fig,"pixel_width":w,"pixel_height":h,
         "component_counts_by_method":{k:len(v) for k,v in components.items()},
         "image_only_candidate_components":len(records),
         "cross_threshold_trace_candidates":len([r for r in records if r["geometric_stability"]=="TRACE_CANDIDATE_CROSS_THRESHOLD"]),
         "blind_atlas":f"moleta_fig{fig}_blind_component_atlas.png",
         "blind_contact_sheet":f"moleta_fig{fig}_blind_trace_contact_sheet.png" if selected else None})
keys=list(rows[0].keys()) if rows else []
if rows:
    with (out/"blind_components.csv").open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader();writer.writerows(rows)
report={"protocol":"GOLDSET-40","status":"REVIEW_CANDIDATES_ONLY",
    "figures":figures,"candidate_components":len(rows),
    "source_photo":"Fig. 4, Moleta del Remei, Palaeohispanica 8 (2008)",
    "source_drawing":"Fig. 5, Moleta del Remei, Palaeohispanica 8 (2008)",
    "original_pdf_sha256":"2965fd62b2a040aa99bb5428bbe8018fba56ebfb201b35034e93a2c38b292e22",
    "image_derived_contours_are_not_automatically_complete_signs":True,
    "editorial_values_used_in_detection":False,"target_sign_count_used_in_detection":False,
    "independently_approved_glyph_bboxes":0,
    "blind_review_approved":False,"graphic_ground_truth":False,
    "review_next":"Inspect original two figure crops and contact sheets. Mark true glyph instances on full image and compare to editorial readings only after blind bbox freeze.",
    "license":"CC BY-NC-ND; extracted plates stay in private ephemeral artifact (1 day). Metadata is reproducible via code."}
(out/"report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
assert report["editorial_values_used_in_detection"] is False
assert report["independently_approved_glyph_bboxes"]==0
assert all(r["glyph_label"] is None for r in rows)
print("GOLDSET40_SUMMARY",json.dumps({"n":len(rows),"figures":figures,"approved":0},ensure_ascii=False))
