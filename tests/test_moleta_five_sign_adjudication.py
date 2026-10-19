import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_five_adjudications_match_editorial_uncertainties_and_block_core():
    a=json.loads((ROOT/"data/review/moleta_graphic_ambiguities_v1.json").read_text(encoding="utf-8"))
    d=json.loads((ROOT/"data/review/moleta_five_sign_adjudication_v1.json").read_text(encoding="utf-8"))
    assert d["object_id"]==a["object_id"]=="IBR-PLM-0011"
    assert len(d["cases"])==len(a["records"])==5
    for x,y in zip(d["cases"],a["records"]):
        assert x["id"]==y["region"]
        assert x["options"]==y["alternative_readings"]
        assert x["discriminating_evidence_needed"]
        assert x["status"]=="UNRESOLVED_PUBLISHED_IMAGE_INSUFFICIENT"
        assert x["photo_sign_roi"] is None and x["independent_photo_reading"] is None
    assert d["excluded_alternatives"]==d["independent_signs_verified"]==0
    assert d["semantic_translations_validated"]==0
    assert d["global_alignment_accepted"] is False and d["core_promotion"] is False
