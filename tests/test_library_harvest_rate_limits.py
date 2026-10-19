"""Rate-limited metadata discovery retains separate scientific approval gates."""
import sys
import json
import urllib.error
from pathlib import Path
from urllib.parse import parse_qs,urlparse
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import collect_library_candidates as harvest

class Response:
    def __init__(self, data): self.data=data
    def __enter__(self): return self
    def __exit__(self,*args): return False
    def read(self): return json.dumps(self.data).encode()

def test_harvest_recovers_from_429_without_duplicate_doIs():
    requests=[]
    def fetch(req,timeout=25):
        q=parse_qs(urlparse(req.full_url).query)
        offset=int(q["offset"][0]); requests.append(offset)
        if len(requests)==1:
            raise urllib.error.HTTPError(req.full_url,429,"Too Many Requests",{},None)
        rows=int(q["rows"][0])
        return Response({"message":{"items":[{"DOI":f"10.1234/test{offset+i}","URL":f"https://doi.org/10.1234/test{offset+i}","title":[f"Example {offset+i}"],"author":[],"publisher":"Demo"} for i in range(rows)]}})
    with patch.object(harvest,"TERMS",["Ibérico"]),patch.object(harvest.urllib.request,"urlopen",side_effect=fetch),patch.object(harvest.time,"sleep") as sleep:
        items=harvest.collect(55,batch_size=25,delay=0,retries=2)
    assert requests==[0,0,25,50]
    assert len(items)==55 and len({x["doi"] for x in items})==55
    assert all(x["status"]=="PENDING_EDITORIAL_REVIEW" and not x["core_evidence_approved"] for x in items)
