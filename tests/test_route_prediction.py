import unittest
from iberos.route_research import EvidenceCell,RouteCase
from iberos.route_prediction import ensemble_routes,audit_picola_ensemble
L=EvidenceCell("land",-500,-300,"core-test")
U=EvidenceCell("unknown",-500,-300,"core-test")
R=EvidenceCell("river",-500,-300,"core-test")
V=EvidenceCell("river",-500,-300,"core-test","verified-vado")
CASE=RouteCase("fixture",(0,0),(0,2),-429,-349,10,"EPSG:25830")
class PredictionTests(unittest.TestCase):
    def test_all_land_is_computable(self):
        r=ensemble_routes([[L,L,L]],CASE,10,3)
        self.assertEqual(r["connected_runs"],10)
        self.assertEqual(r["length_range_m"],[20.0,20.0])
        self.assertFalse(r["historical_path_proven"])
    def test_unknown_blocks_even_when_shortest(self):
        r=ensemble_routes([[L,U,L]],CASE,10,3)
        self.assertEqual(r["connected_runs"],0)
    def test_river_requires_credible_crossing(self):
        self.assertEqual(ensemble_routes([[L,R,L]],CASE,4)["connected_runs"],0)
        self.assertEqual(ensemble_routes([[L,V,L]],CASE,4)["connected_runs"],4)
    def test_antiquity_is_enforced(self):
        roman=EvidenceCell("land",1,200,"roman")
        self.assertEqual(ensemble_routes([[L,roman,L]],CASE,4)["connected_runs"],0)
    def test_seed_reproducible(self):
        grid=[[L,L,L],[L,L,L],[L,L,L]]
        a=ensemble_routes(grid,CASE,16,10)
        self.assertEqual(a,ensemble_routes(grid,CASE,16,10))
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            ensemble_routes([[L,L,L]],CASE,0)
    def test_picola_real_case_not_faked(self):
        r=audit_picola_ensemble()
        self.assertIsNone(r["ensemble_run"])
        self.assertEqual(r["audit"]["route_status"],"not_evaluable_missing_evidence")
        self.assertFalse(r["model_trained"])
if __name__=="__main__": unittest.main()
