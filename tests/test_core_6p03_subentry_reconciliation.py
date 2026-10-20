"""6P-03 sourced subentry index reconciliation smoke tests."""
import json
from pathlib import Path

def test_six_case_index_inventory():
    path=Path(__file__).resolve().parents[1]/"data/review/core_6p03_six_subentry_reconciliation_2026_10_20.json"
    result=json.loads(path.read_text(encoding="utf-8"))
    cases={v["object_id"]:v for v in result["cases"]}
    assert len(cases)==6
    lliria=cases["IBR-CER-0002"]
    assert len(lliria["index_group_entries"])==22
    assert lliria["index_group_entries"][0]=="I01994"
    assert lliria["index_group_entries"][-1]=="I02015"
    assert not lliria["physical_inscriptions_confirmed"]
    assert not result["automatic_scientific_promotion"]
    assert cases["IBR-PLM-0008"]["status"]=="V_21_01_ONLY_PARTIAL_GROUP"
