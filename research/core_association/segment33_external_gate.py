#!/usr/bin/env python3
"""SEGMENT-33: external physical-source acquisition and honest generalisation gate.
No labels from Orleyl allowed to validate Moleta. No synthetic reference boundaries.
"""
from pathlib import Path
import hashlib,json,urllib.request,subprocess,shutil,re,csv
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"research/core_association/segment33_results"
OUT.mkdir(parents=True,exist_ok=True)
URLS=[
 "https://ifc.dpz.es/recursos/publicaciones/28/40/_ebook.pdf",
 "https://www.ifc-ojs.es/index.php/palaeohispanica/es/article/download/265/270",
]
record={"protocol":"SEGMENT-33","target_site":"La Moleta del Remei, Alcanar, Tarragona",
 "independent_from_orleyl":True,"publication":"Ferrer i Jané et al. 2008, Palaeohispanica 8, pp. 203-216",
 "figures":{"photograph":"fig. 4, p. 215","drawing":"fig. 5, p. 216"},
 "legacy_orleyl_proxy_precision":"35/43 = 81.4% (not externally validated)",
 "attempts":[],"source_downloaded":False,"image_page_verified":False,
 "homologous_pre_registered_reference_boundaries":False,
 "same_fixed_cut_budget_applicable":False,
 "external_precision":None,"external_recall":None,
 "generalisation_confirmed":False,"status":"UNCONFIRMED"}
target=OUT/"external_primary.pdf"
for url in URLS:
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"IberOS-research-evidence-audit/1.0"})
        with urllib.request.urlopen(req,timeout=25) as response:
            data=response.read(45_000_001)
        if data[:4]!=b"%PDF" or len(data)>45_000_000:
            record["attempts"].append({"url":url,"status":"NOT_PDF_OR_EXCESSIVE_SIZE"});continue
        target.write_bytes(data)
        record["source_downloaded"]=True
        record["source_sha256"]=hashlib.sha256(data).hexdigest()
        record["source_bytes"]=len(data)
        record["successful_source_url"]=url
        break
    except Exception as ex:
        record["attempts"].append({"url":url,"error":str(ex)[:180]})
if record["source_downloaded"]:
    try:
        import fitz
        doc=fitz.open(str(target))
        record["pdf_pages"]=len(doc)
        found=[]
        # Search actual page labels rather than assume printed pages==pdf indices.
        for i,page in enumerate(doc):
            tx=page.get_text()
            if re.search(r"Fig\.\s*[45]\s*:",tx,re.IGNORECASE):
                figures=re.findall(r"Fig\.\s*[45]\s*:",tx,re.IGNORECASE)
                found.append({"pdf_page_0based":i,"figures":figures})
                pix=page.get_pixmap(matrix=fitz.Matrix(1.4,1.4))
                pix.save(str(OUT/f"moleta_page_{i}.png"))
        record["figure_pages"]=found
        record["image_page_verified"]=bool(any(any("4" in f for f in x["figures"]) for x in found) and any(any("5" in f for f in x["figures"]) for x in found))
    except Exception as ex:
        record["rendering_error"]=str(ex)[:250]
    # Do not redistribute copied publication PDF as a long-retention artifact.
    target.unlink(missing_ok=True)
# External evaluation requires *independently justified* per-sign reference boundaries and
# a defensible same budget, which the figure metadata in the corpus does not supply.
# Do not invent them by count of transliterated characters (semi-syllabary!).
record["missing_to_confirm"]=[
 "Independent sign-boundary coordinates on Moleta engraving/drawing",
 "Predefined line ROI excluding object outlines, captions and scales",
 "Segmentation budget set without inspecting the answer",
 "Matched metrics for both baseline and candidate on the same new image"]
(OUT/"report.json").write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding="utf8")
print(json.dumps({k:v for k,v in record.items() if k!="attempts"},ensure_ascii=False))
print("Download attempts:",record["attempts"])
