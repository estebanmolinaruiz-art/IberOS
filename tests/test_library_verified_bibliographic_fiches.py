"""Verified bibliography is not a newly verified physical inscription."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_two_new_bibliographic_fiches_are_source_verified_but_core_blocked():
    d=json.loads((ROOT/"site/data/bibliographic_fichas_v1.json").read_text(encoding="utf-8"))
    rows=d["items"]; ids=[x["doi"].lower() for x in rows]
    assert len(ids)==len(set(ids))==14
    for doi in ("10.36707/palaeohispanica.v0i19.221","10.36707/palaeohispanica.v0i17.142","10.36707/palaeohispanica.v0i15.37","10.36707/palaeohispanica.v21i0.427"):
        r=next(x for x in rows if x["doi"].lower()==doi)
        assert r["review_status"]=="BIBLIOGRAPHIC_METADATA_VERIFIED_FULL_TEXT_PENDING"
        assert r["source_verified"]=="journal_landing_page"
        assert r["object_identity_verified"] is False
        assert r["epigraphic_transcription_verified"] is False
        assert r["core_processing"]["status"]=="BLOCKED_UNVERIFIED_OBJECT"
