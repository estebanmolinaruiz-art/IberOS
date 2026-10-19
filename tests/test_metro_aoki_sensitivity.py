import importlib.util,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("sens",ROOT/"scripts/metro_aoki_sensitivity.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def test_grid_and_leave_one_out():
 with (ROOT/"data/review/metro_aoki_01_exploratory_masses.csv").open() as f:rows=list(csv.DictReader(f))
 r=m.analyze(rows)
 assert r["grid_points"]==9
 assert r["n_cases"]==7
 assert len(r["leave_one_observation_out"])==7
 assert r["loo_hybrid_wins"]==7
 assert r["grid_hybrid_wins"]==9
 assert r["metro_aoki01"]=="NOT_EXTERNALLY_VALIDATED"
def test_invalid_grid():
 import pytest
 with pytest.raises(ValueError):m.analyze([],step=0)
