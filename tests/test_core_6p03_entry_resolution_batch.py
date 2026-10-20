import json
from pathlib import Path

def test_entry_resolution_keeps_physical_witnesses_distinct():
    path=Path(__file__).resolve().parents[1]/"data/review/core_6p03_entry_resolution_batch_2026_10_20.json"
    report=json.loads(path.read_text(encoding="utf-8"))
    by_id={r["object_id"]:r for r in report["entries"]}
    assert len(by_id)==3
    assert all(r["support_count"]==1 for r in by_id.values())
    assert by_id["IBR-OBJ-0001"]["upstream_ids"]==["I03095","I03096"]
    assert len(by_id["IBR-PLM-0009"]["provisional_units"])==3
    assert len(by_id["IBR-PLM-0012"]["provisional_units"])==3
    assert report["invariants"]["new_physical_objects"]==0
    assert not report["invariants"]["automatic_semantic_promotion"]
