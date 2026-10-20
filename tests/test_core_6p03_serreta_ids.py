import json
from pathlib import Path

def test_serreta_crosswalk_has_no_invented_iberika_ids():
    path=Path(__file__).resolve().parents[1]/"data/review/core_6p03_serreta_external_ids_2026_10_20.json"
    d=json.loads(path.read_text(encoding="utf-8"))
    assert d["physical_witness_count"]==1
    assert len(d["physical_text_units"])==3
    assert d["external_ids"]["HESPERIA"]==["A.04.01a","A.04.01b"]
    assert d["external_ids"]["MLH"]==["G.1.1a","G.1.1b"]
    assert d["external_ids"]["CATHALAUNIA_IBERIKA"]==[]
    assert d["scientific_gates"]["automatic_promotion"] is False
