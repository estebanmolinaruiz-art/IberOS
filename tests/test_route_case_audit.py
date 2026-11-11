import unittest
from iberos.route_case_audit import GeoAnchor, inspect_case

A=GeoAnchor("La Alcudia",701823.285,4234872.059,"EPSG:25830","ASTERO-2017")
B=GeoAnchor("La Picola",713265,4230490,"EPSG:25830","BIC-Picola-A1")

class CaseAuditTests(unittest.TestCase):
    def test_real_case_blocked(self):
        r=inspect_case(A,B,-429,-349)
        self.assertEqual(r["route_status"],"not_evaluable_missing_evidence")
        self.assertEqual(len(r["missing_verifications"]),6)
        self.assertIsNone(r["route_geometry"])
        self.assertFalse(r["archaeological_road_proven"])
        self.assertGreater(r["straight_line_m"],12000)
        self.assertLess(r["straight_line_m"],12500)
    def test_wrong_crs(self):
        other=GeoAnchor("other",100,200,"EPSG:4326","test")
        with self.assertRaises(ValueError): inspect_case(A,other,-429,-349)
    def test_readiness_not_proof(self):
        full={k:True for k in ("georeferenced_ancient_land","dated_lagoon_mask","dated_river_mask","verified_crossings","ancient_access_points","continuous_evidence_grid")}
        r=inspect_case(A,B,-429,-349,full)
        self.assertEqual(r["route_status"],"ready_for_routing_only")
        self.assertFalse(r["archaeological_road_proven"])
    def test_nan_rejected(self):
        with self.assertRaises(ValueError):
            GeoAnchor("bad",float("nan"),1,"EPSG:25830","x")

if __name__=="__main__":
    unittest.main()
