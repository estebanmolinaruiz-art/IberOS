"""Source-localized bo/ko ambiguity cannot become a scientifically approved sign by inference."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_illeta_sign_ambiguity_stays_unresolved():
    d=json.loads((ROOT/"data/review/illeta_bo_ko_decision_v1.json").read_text(encoding="utf-8"))
    assert d["source"]["figure"]==8 and d["source"]["printed_page"]==260
    assert d["source"]["figure_panel"]=="bottom-left photograph, explicitly captioned bo o ko"
    assert d["inscription_face"]=="A" and d["inscription_line"]==1
    assert {x["target_sign"] for x in d["editorial_options"]}=={"bo","ko"}
    assert d["evidence"]["local_pixel_roi"] is None
    assert not d["evidence"]["independent_stroke_tracing"]
    assert d["decision"]["graphic_status"]=="UNRESOLVED_BO_KO"
    assert d["decision"]["independently_read_sign"] is None
    assert not d["decision"]["eligible_for_core"] and not d["decision"]["semantic_validation"]
