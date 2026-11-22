#!/usr/bin/env python3
"""SEGMENT-34: extract provenance-grounded Moleta figure zones from source PDF.
NO independent glyph boundary labels; no performance claims.
Figures retained only in short-lived private Actions artifact.
"""
from pathlib import Path
import json, hashlib, urllib.request, re, math
import numpy as np
from PIL import Image, ImageDraw
import fitz

OUT=Path("research/core_association/segment34_results")
OUT.mkdir(parents=True,exist_ok=True)
URL="https://ifc.dpz.es/recursos/publicaciones/28/40/_ebook.pdf"
request=urllib.request.Request(URL,headers={"User-Agent":"IberOS-epigraphic-audit/1.0"})
data=urllib.request.urlopen(request,timeout=50).read(25_000_000)
assert data[:4]==b"%PDF" and len(data)<25_000_000
source_hash=hashlib.sha256(data).hexdigest()
doc=fitz.open(stream=data,filetype="pdf")
# Immutable source gate: fail if source silently changes from SEGMENT-33.
assert source_hash=="2965fd62b2a040aa99bb5428bbe8018fba56ebfb201b35034e93a2c38b292e22", "Source version changed: review PDF before running"
records=[]
for page_id,figure_number in [(209,4),(210,5)]:
    page=doc[page_id]
    words=page.get_text("words")
    # Label is not a glyph guide, it just locates the figure region.
    cap=[w for w in words if w[4].strip().lower() in ("fig.","fig","figura","fig.")]
    captions=[]
    for w in cap:
        same_line=" ".join(x[4] for x in words if x[5]==w[5] and x[6]==w[6])
        if re.search(r"fig\.?\s*"+str(figure_number)+r"\s*:",same_line,re.I):
            captions.append({"bbox":[float(w[i]) for i in range(4)],"text":same_line})
    # Locate using text search if word grouping differs
    if not captions:
        matches=page.search_for(f"Fig. {figure_number}")
        for m in matches:captions.append({"bbox":[m.x0,m.y0,m.x1,m.y1],"text":f"Fig. {figure_number}"})
    if not captions:raise RuntimeError(f"Figure {figure_number} caption not located")
    caption_y=min(x["bbox"][1] for x in captions)
    # Exclude title, page footer; candidate region ABOVE caption.
    # Use actual embedded raster image bounding rectangles to avoid text and margin.
    embeds=[]
    for info in page.get_images(full=True):
        for rec in page.get_image_rects(info[0]):
            if rec.y1<=caption_y+10 and rec.width>50 and rec.height>35:
                embeds.append(rec)
    embeds.sort(key=lambda r:r.width*r.height,reverse=True)
    if embeds:
        rect=embeds[0]
        region=fitz.Rect(max(0,rect.x0-3),max(0,rect.y0-3),min(page.rect.width,rect.x1+3),min(page.rect.height,rect.y1+3))
        method="largest_embedded_raster_above_fig_caption"
    else:
        # Geometric fallback: whole content zone immediately above caption, not yet a sign ROI.
        region=fitz.Rect(page.rect.width*.07,page.rect.height*.15,page.rect.width*.93,caption_y-4)
        method="page_area_above_fig_caption_NOT_SEGMENTED"
    if region.width<90 or region.height<35:raise RuntimeError(f"Bad candidate rect for fig {figure_number}: {region}")
    pix=page.get_pixmap(matrix=fitz.Matrix(2.0,2.0),clip=region,alpha=False)
    im=Image.frombytes("RGB",(pix.width,pix.height),pix.samples)
    gray=np.array(im.convert("L"))
    # PROXY ink, not automatically actual engraving (photo backgrounds may be dark).
    projections={}
    for q in (0.20,0.35,0.50):
        thresh=float(np.quantile(gray,q))
        density=np.mean(gray<=thresh,axis=0)
        # only report robust information, don't call all valleys "sign boundaries"
        low=np.where(density<np.quantile(density,0.25))[0]
        projections[str(q)]={"threshold_gray_quantile":round(thresh,1),
                            "low_density_columns_count":int(len(low)),
                            "fraction_dark":round(float((gray<=thresh).mean()),4)}
    image_name=f"moleta_fig{figure_number}_candidate_zone.png"
    im.save(OUT/image_name,optimize=True)
    rec={"figure":figure_number,"page_pdf_zero_based":page_id,"source_pdf_sha256":source_hash,
         "source_pdf_url":URL,"method":method,
         "crop_pdf_points":[round(float(x),2) for x in (region.x0,region.y0,region.x1,region.y1)],
         "caption_y_pdf_points":round(float(caption_y),2),
         "candidate_image_size_px":[pix.width,pix.height],
         "figure_image_sha256":hashlib.sha256((OUT/image_name).read_bytes()).hexdigest(),
         "image_filename":image_name,
         "embedded_raster_count_above_caption":len(embeds),
         "projection_sensitivity":projections,
         "status":"PAGE_FIGURE_ZONE_NOT_INDEPENDENT_SIGN_BOUNDARIES"}
    records.append(rec)
report={"protocol":"SEGMENT-34","source_sha256":source_hash,
        "source_bytes":len(data),"figures":records,
        "source_is_external_to_orleyl":True,
        "figure_zones_extracted":len(records),
        "glyph_bounds_independently_verified":0,
        "external_segmentation_accuracy":None,
        "generalisation_confirmed":False,
        "limitations":["Figures are crops of page content, not proven glyph-only ROIs.",
                       "Captions and raster bounds are machine located; visual figure review remains pending.",
                       "Projection sensitivity describes possible binarization, not true-sign segmentation.",
                       "No independent sign boundary labels or intersite recognition benchmark.",
                       "Publication carries CC BY-NC-ND licensing: figures retained only as short-lived internal artifacts."]}
(OUT/"report.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf8")
for rec in records:
    print("FIGURE",rec["figure"],"PDF_CROP",rec["crop_pdf_points"],"PX",rec["candidate_image_size_px"],"METHOD",rec["method"])
print("GATES",json.dumps({k:report[k] for k in ("figure_zones_extracted","glyph_bounds_independently_verified","external_segmentation_accuracy","generalisation_confirmed")}))
