import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("blind_alias",ROOT/"scripts/validation01_blind_score.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def row(oid,gid,split):
 return {"object_id":oid,"physical_group":gid,"split":split,"source_url":"https://example.org","reading_reviewed":"YES",
 "prediction_locked_at":"2026-10-19T08:00:00Z","gold_reviewed_at":"2026-10-19T09:00:00Z",
 "gold_label":"1","iberos_prediction":"1","baseline_prediction":"0","predictions_frozen_sha256":"a"*64,
 "gold_independent_reviewer":"human"}
def problems(rows,minimum=1):
 return [p[1] for p in m.audit(rows,minimum=minimum).get("problems",[])]
def test_cross_split_alias_is_leakage():
 assert "LEAKAGE_BETWEEN_SPLITS" in problems([row("F.9.7","ORLEYL VII","TRAIN"),row("Orley-VII","x","HOLD")])
def test_intrasplit_normalized_duplicate():
 assert "DUPLICATE_PHYSICAL_GROUP_IN_SPLIT" in problems([row("x1","ABC 17","HOLD"),row("x2","ABC-17","HOLD")])
def test_distinct_objects_not_merged():
 assert m.audit([row("x1","ABC17","HOLD"),row("x2","ABC18","HOLD")],minimum=2)["gate"]=="DESCRIPTIVE_SCORING_ONLY"
