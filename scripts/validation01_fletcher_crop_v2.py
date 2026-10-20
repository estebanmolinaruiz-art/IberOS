#!/usr/bin/env python3
"""Render Fletcher plate line bands in a fixed reference frame.
For human inspection only; never assert paleographic review from these crops.
Requires PyMuPDF and Pillow; source PDF supplied separately, not redistributed.
"""
import argparse,json
from pathlib import Path
import fitz
from PIL import Image
SOURCES={"V":{"page":65,"bbox":(80,490,2250,572),"physical_line":3,"figure":22},
         "VIIB":{"page":111,"bbox":(415,410,2015,475),"physical_line":2,"figure":25}}
SIZE=(2287,1727)
def extract(pdf,out):
    result={}
    doc=fitz.open(str(pdf));out=Path(out);out.mkdir(parents=True,exist_ok=True)
    for key,meta in SOURCES.items():
        pix=doc[meta["page"]-1].get_pixmap(matrix=fitz.Matrix(3,3),alpha=False)
        im=Image.frombytes("RGB",(pix.width,pix.height),pix.samples).rotate(270,expand=True)
        if im.size!=SIZE:raise ValueError("Unexpected page dimensions; crop coordinates invalid")
        fn=out/(key+"_line_v2.png");im.crop(meta["bbox"]).save(fn)
        result[key]={"pdf_page":meta["page"],"figure":meta["figure"],
                     "physical_line":meta["physical_line"],"frame_size":list(SIZE),
                     "bbox":list(meta["bbox"]),"image_file":str(fn),
                     "glyphs_individually_verified":0}
    return {"status":"LINE_CROPS_ONLY","results":result,"validation01":"NOT_EVALUATED"}
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("source_pdf");p.add_argument("output_dir");a=p.parse_args()
    print(json.dumps(extract(a.source_pdf,a.output_dir),ensure_ascii=False,indent=2))
