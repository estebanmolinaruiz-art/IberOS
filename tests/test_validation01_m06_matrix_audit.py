import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location("m06check",ROOT/"scripts/validation01_m06_matrix_audit.py")
m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
def test_17_positions_consistent_but_unverified():
 r=m.audit(m.read(ROOT/"data/review/validation01_orleyl_17_visual_alignment_v1.csv"),m.read(ROOT/"data/review/validation01_m06_mlh_17_candidate_matches_2026-10-22.csv"))
 assert r["alignment_rows"]==17 and r["typology_rows"]==17
 assert r["issues"]==[]
 assert r["coordinate_verified"]==0
 assert r["independent_readings"]==0
 assert r["m06"]=="PENDING" and r["m07"]=="PENDING"
