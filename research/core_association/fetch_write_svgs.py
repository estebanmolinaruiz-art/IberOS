#!/usr/bin/env python3
"""Fetch the 26 actual Wikimedia SVG files used by IberOS-Write; never invent glyphs."""
import argparse
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from bridge import from_write_page

UA = "IberOS-Scientific-Research/0.1 (public open scientific project)"
BASE = "https://commons.wikimedia.org/w/api.php"


def request(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json,image/svg+xml,*/*"})
    with urllib.request.urlopen(req, timeout=35) as response:
        data = response.read(1_000_000)
        final_url = response.url
    return data, final_url


def fetch_one(name):
    query = urllib.parse.urlencode({
        "action":"query","prop":"imageinfo","iiprop":"url|size|extmetadata",
        "titles":"File:"+name,"format":"json","formatversion":"2"
    })
    data,_ = request(BASE+"?"+query)
    pages=json.loads(data)["query"]["pages"]
    ii=pages[0].get("imageinfo")
    if not ii or not ii[0].get("url"):
        raise ValueError("Missing file on Commons: "+name)
    metadata=ii[0]
    url=metadata["url"]
    if not url.startswith("https://upload.wikimedia.org/"):
        raise ValueError("Unexpected source server")
    # Wikimedia serves some valid SVG URLs with percent-encoded path names or query parameters.
    # Validate the actual XML root instead of relying on a URL suffix.
    body,final_url=request(url)
    if len(body)<100 or b"<!DOCTYPE" in body.upper():
        raise ValueError("Unexpected file content")
    tree=ET.fromstring(body)
    if not tree.tag.endswith("svg"):
        raise ValueError("Payload not an SVG")
    # No automatic assertion of CC0 for all 26 files. Record each source license verbatim.
    ext=metadata.get("extmetadata",{})
    rights={k:ext.get(k,{}).get("value") for k in
            ("LicenseShortName","LicenseUrl","UsageTerms","AttributionRequired")}
    return body,final_url,rights


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--root",default=".")
    p.add_argument("--dest",default="signary-source")
    args=p.parse_args()
    root=Path(args.root)
    dest=Path(args.dest)
    dest.mkdir(parents=True,exist_ok=True)
    glyphs=from_write_page(root/"site/write/index.html")
    records=[]
    errors=[]
    for value,name in glyphs.items():
        try:
            time.sleep(1.6)  # Wikimedia courteous rate limiting
            body,url,rights=fetch_one(name)
            path=dest/name
            path.write_bytes(body)
            records.append({"value":value,"filename":name,"url":url,
                            "size":len(body),"sha256":hashlib.sha256(body).hexdigest(),
                            "rights_metadata":rights,"status":"VERIFIED_SVG_DOWNLOAD"})
            print("OK",value,name,len(body),flush=True)
        except Exception as e:
            errors.append({"value":value,"filename":name,"error":str(e)})
            print("FAIL",value,name,str(e),flush=True)
            if isinstance(e, urllib.error.HTTPError) and e.code==429:
                print("Stopping: Wikimedia requests throttled; preserve partial evidence.",flush=True)
                break
    manifest={"protocol":"IBEROS-WRITE-SVG-SOURCE-01","expected":len(glyphs),
              "downloaded":len(records),"errors":errors,"items":records,
              "warning":"These SVGs are schematic graphics, not archaeological photographs. License must be checked individually."}
    (dest/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
    with zipfile.ZipFile(dest/"iberos-write-svg-references.zip","w",zipfile.ZIP_DEFLATED) as z:
        for rec in records:
            z.write(dest/rec["filename"],arcname="svg/"+rec["filename"])
        z.write(dest/"manifest.json",arcname="manifest.json")
    print("Download summary:",len(records),"/",len(glyphs),flush=True)
    if len(records)!=len(glyphs):
        raise SystemExit(2)


if __name__=="__main__":
    main()
