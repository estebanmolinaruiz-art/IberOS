import unittest
from iberos.route_gate_geometry import SurveyPoint,gate_axis_test
def p(x,y,u=0,source="test"):
    return SurveyPoint(x,y,u,source)
class GateGeometryTests(unittest.TestCase):
    def test_on_observed_segment(self):
        r=gate_axis_test(p(0,0),p(10,0),p(5,0),2.6)
        self.assertEqual(r["gate_distance_to_observed_segment_m"],0)
        self.assertTrue(r["geometric_overlap_possible"])
        self.assertFalse(r["archaeological_connection_proven"])
    def test_extrapolation_not_observed(self):
        r=gate_axis_test(p(0,0),p(10,0),p(20,0),2)
        self.assertFalse(r["projection_on_observed_segment"])
        self.assertEqual(r["gate_distance_to_observed_segment_m"],10)
        self.assertEqual(r["gate_distance_to_extrapolated_axis_m"],0)
    def test_uncertainty(self):
        r=gate_axis_test(p(0,0,1),p(10,0,1),p(5,4,1),2)
        self.assertEqual(r["conservative_distance_interval_m"],[0,8])
    def test_crs_mismatch(self):
        with self.assertRaises(ValueError):
            gate_axis_test(p(0,0),p(10,0),SurveyPoint(0,0,1,"x","EPSG:4326"))
    def test_identical_axis_points(self):
        with self.assertRaises(ValueError):
            gate_axis_test(p(1,1),p(1,1),p(0,0))
    def test_invalid_gate_width(self):
        with self.assertRaises(ValueError):
            gate_axis_test(p(0,0),p(10,0),p(5,0),-1)
if __name__=="__main__":
    unittest.main()
