import importlib.util
from pathlib import Path
s=importlib.util.spec_from_file_location("mask",Path(__file__).resolve().parents[1]/"scripts/validation01_te_mask_pilot.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def valid():
 return {"object_id":"x","physical_group":"g1","cohort":"DEVELOPMENT","reading_status":"REVIEWED",
  "full_line_reviewed":"YES","independent_reviewer":"independent","sign_tokens":"a te r",
  "source_url":"https://example.org","edition_locator":"line-1"}
def test_mask_has_no_visible_target():
 r=m.make([valid()],"fixed-development-seed")
 assert len(r["examples"])==1
 e=r["examples"][0]
 assert e["masked_tokens"].split()[e["masked_index"]]=="[MASK]"
 assert e["cohort"]=="DEVELOPMENT" and r["hold_examples"]==0
def test_no_hold_import():
 q=valid();q["cohort"]="HOLD"
 assert m.make([q],"fixed")["examples"]==[]
def test_unreviewed_not_promoted():
 q=valid();q["reading_status"]="UNREVIEWED"
 assert m.make([q],"fixed")["examples"]==[]
def test_same_physical_object_not_counted_twice():
 assert len(m.make([valid(),valid()],"fixed")["examples"])==1
def test_no_t_or_e_split():
 q=valid();q["sign_tokens"]="ta e r"
 r=m.make([q],"fixed");assert len(r["examples"])==1
