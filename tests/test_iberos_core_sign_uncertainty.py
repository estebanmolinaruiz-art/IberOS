import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("uncertainty",ROOT/"scripts/iberos_core_sign_uncertainty.py")
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def test_existing_17_are_all_editorial_and_unresolved():
 result=mod.inspect(mod.load(ROOT/"data/review/validation01_m06_mlh_17_candidate_matches_2026-10-22.csv"))
 assert result["counts"]=={"total":17,"editorial_only":17,"independent":0,"unresolved":17}
 assert all(r["semantic_translation"] is None for r in result["records"])
def test_no_translation_inferred_from_candidate():
 x=mod.inspect([{"object":"X","index":"1","Fletcher_editorial":"te","MLH_III_iberian_candidate_group":"te13","exact_MLH_variant":"UNRESOLVED","independent_reading":"NO"}])
 assert x["records"][0]["exact_variant"] is None
 assert x["records"][0]["semantic_translation"] is None
def test_independent_flag_is_not_automatic_validation():
 x=mod.inspect([{"object":"X","index":"1","Fletcher_editorial":"r","MLH_III_iberian_candidate_group":"r/ŕ","exact_MLH_variant":"UNRESOLVED","independent_reading":"YES"}])
 assert x["scientific_status"]=="NOT_EVALUATED"
