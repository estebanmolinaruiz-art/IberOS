"""Crossref collection must paginate, deduplicate and leave scientific gates closed."""
import sys
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import collect_library_candidates as harvest

class Response:
    def __init__(self, data): self.data=data
    def __enter__(self): return self
    def __exit__(self,*a): return False
    def read(self): return json.dumps(self.data).encode("utf-8")

def test_harvest_over_100_paginates_and_never_approves_core():
    calls=[]
    def fake_open(request,timeout):
        q=parse_qs(urlparse(request.full_url).query)
        offset=int(q.get("offset",["0"])[0])
        count=int(q["rows"][0])
        calls.append((offset,count))
        items=[{"DOI":f"10.5555/mock{offset+i}","URL":f"https://doi.org/10.5555/mock{offset+i}",
          "title":[f"Palaeohispanic test {offset+i}"],"author":[],"publisher":"Test"} for i in range(count)]
        return Response({"message":{"items":items}})
    with patch.object(harvest,"TERMS",["Palaeohispanic epigraphy"]),patch.object(harvest.urllib.request,"urlopen",side_effect=fake_open):
        items=harvest.collect(125)
    assert calls==[(0,100),(100,25)]
    assert len(items)==125 and len({x["doi"] for x in items})==125
    assert all(x["status"]=="PENDING_EDITORIAL_REVIEW" for x in items)
    assert all(x["core_evidence_approved"] is False and x["metadata_relevance_verified"] is False for x in items)
