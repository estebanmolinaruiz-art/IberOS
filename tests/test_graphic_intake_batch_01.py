"""The first ten graphic intake entries are editorial leads, not verified glyphs."""
import json
from pathlib import Path

DATA=Path(__file__).resolve().parents[1]/"data/review/graphic_intake_batch_01_v1.json"

def test_first_batch_graphic_intake_safety():
    data=json.loads(DATA.read_text(encoding="utf-8"))
    rows=data["records"]
    assert len(rows)==10
    assert [x["order"] for x in rows]==list(range(1,11))
    assert len({x["object_id"] for x in rows})==10
    assert all(x["catalogue_source"] and len(x["work_to_do"])==4 for x in rows)
    for entry in rows:
        assert not any(entry[k] for k in ("source_is_primary_verified","figure_page_verified",
                                         "facsimile_inspected","permissions_verified",
                                         "sign_by_sign_verified","semantic_validation"))
    assert data["scientifically_validated_translations"]==0

def test_verified_bibliographic_pages_do_not_imply_facsimile_verification():
    data=json.loads(DATA.read_text(encoding="utf-8"))
    confirmed=[r for r in data["records"] if r.get("bibliographic_landing_page_checked")]
    assert len(confirmed)==data["verified_bibliographic_landing_pages"]==4
    assert {r["object_id"] for r in confirmed}=={"IBR-CER-0002","IBR-LAP-0001","IBR-PLM-0011","IBR-PLM-0012"}
    assert all("ifc-ojs.es/" in r["verified_reference_url"] for r in confirmed)
    assert all(not r["figure_page_verified"] and not r["facsimile_inspected"] for r in confirmed)
