import unittest
from iberos.route_picola_exit_window import PicolaDefenceGeometry,estimate_exit_window
class ExitWindowTests(unittest.TestCase):
    def test_normal_offsets(self):
        r=estimate_exit_window()
        self.assertEqual(r["moat_near_edge_normal_offset_m"],[5,5.5])
        self.assertEqual(r["moat_far_edge_normal_offset_m"],[10,11.5])
        self.assertEqual(r["curtain_midpoint_nominal_m"],28)
    def test_oblique_widens(self):
        r=estimate_exit_window(angle_deg=45)
        self.assertGreater(r["crossing_to_far_edge_along_hypothetical_axis_m"][1],11.5)
    def test_not_archaeological_proof(self):
        r=estimate_exit_window()
        self.assertIsNone(r["site_epsg25830_geometry"])
        self.assertFalse(r["moat_crossing_observed"])
        self.assertFalse(r["historical_road_proven"])
    def test_bad_dimensions(self):
        with self.assertRaises(ValueError):
            estimate_exit_window(PicolaDefenceGeometry(glacis_min_m=7,glacis_max_m=5))
    def test_bad_angle(self):
        with self.assertRaises(ValueError):
            estimate_exit_window(angle_deg=90)
if __name__=="__main__": unittest.main()
