import unittest
from iberos.route_picola_local import assess_picola_local_axes,PicolaLocalReference

class PicolaLocalTests(unittest.TestCase):
    def test_metrics(self):
        out=assess_picola_local_axes()
        self.assertEqual(out["local_curtain_midpoint_from_end_m"],28)
        self.assertEqual(out["observed_scarp_side_difference_m"],0.65)
        self.assertEqual(out["r2_street_width_m"],3.55)
    def test_not_proof(self):
        out=assess_picola_local_axes()
        self.assertIsNone(out["moat_exit_point"])
        self.assertIsNone(out["world_coordinates"])
        self.assertFalse(out["external_route_proven"])
    def test_invalid(self):
        with self.assertRaises(ValueError):
            assess_picola_local_axes(PicolaLocalReference(curtain_ne_length_m=-56))

if __name__=="__main__":
    unittest.main()
