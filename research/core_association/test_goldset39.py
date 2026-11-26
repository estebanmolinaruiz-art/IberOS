from pathlib import Path
import json
d=json.loads((Path(__file__).parent/"goldset39_moleta_records.json").read_text(encoding="utf-8"))
r=d["records"]
assert len(r)==21 and len({x["id"] for x in r})==21
assert [sum(x["line"]==v for x in r) for v in ("Z1-L1","Z1-L2","Z2-L1")]==[3,9,9]
assert all(x["independent_image_bbox"] is None and x["independent_graphic_label"] is None for x in r)
assert all(x["graphic_validation"]=="PENDING" for x in r)
assert len({x["holdout_family"] for x in r})==1
assert d["counts"]["independent_graphic_labels"]==0
print("PASS: 21 editorial slots source-backed; 0 graphical gold labels; leakage blocked")
