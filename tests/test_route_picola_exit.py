import unittest
from iberos.route_picola_exit import ObstacleBand,crossing_sensitivity,assess_picola_gate_exit

class PicolaExitTests(unittest.TestCase):
    def test_normal_crossing(self):
        r=crossing_sensitivity(ObstacleBand("foso",5,6,"source",False),(0,))
        self.assertEqual(r["hypothetical_crossing_scenarios"][0]["crossing_length_min_m"],5)
        self.assertEqual(r["hypothetical_crossing_scenarios"][0]["crossing_length_max_m"],6)
    def test_diagonal_longer(self):
        r=crossing_sensitivity(ObstacleBand("foso",5,6,"source",False),(0,45))
        self.assertGreater(r["hypothetical_crossing_scenarios"][1]["crossing_length_min_m"],5)
    def test_no_proven_bridge(self):
        r=assess_picola_gate_exit()
        self.assertIsNone(r["gate_center_epsg25830"])
        self.assertFalse(r["obstacle_sensitivity"]["causeway_or_bridge_proven"])
        self.assertFalse(r["connection_to_ilici_proven"])
    def test_invalid_angle(self):
        with self.assertRaises(ValueError):
            crossing_sensitivity(ObstacleBand("foso",5,6,"source",False),(90,))
    def test_negative_band(self):
        with self.assertRaises(ValueError):
            ObstacleBand("foso",-2,6,"source",True)
    def test_missing_source(self):
        with self.assertRaises(ValueError):
            ObstacleBand("foso",5,6,"",True)
if __name__=="__main__": unittest.main()
