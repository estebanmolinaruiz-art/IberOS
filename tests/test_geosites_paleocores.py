import unittest
from iberos.geosites_paleocores import Borehole,decode_local_grid,distance_bounds,audit_picola_paleocores
class G129Tests(unittest.TestCase):
    def test_grid_100m(self):
        p=decode_local_grid("30SYH133 305")
        self.assertEqual(p["easting_m"],[713300,713400])
        self.assertEqual(p["northing_m"],[4230500,4230600])
        self.assertFalse(p["datum_verified"])
    def test_fondo_tile(self):
        self.assertEqual(decode_local_grid("30SXH996 292")["center_m"],[699650,4229250])
    def test_riegos_not_autocorrected(self):
        r=audit_picola_paleocores()
        self.assertEqual(r["riegos_anomaly"]["east_difference_m"],100000)
        self.assertEqual(r["cores"][-1]["published_grid"],"30SYH954 322")
    def test_no_paleoland(self):
        r=audit_picola_paleocores()
        self.assertEqual(r["paleoland_cells_eligible"],0)
        self.assertIsNone(r["period_raster"])
    def test_bounded_distance(self):
        cell=decode_local_grid("30SYH133 305")
        lo,hi=distance_bounds(cell,713265,4230490)
        self.assertLess(lo,hi)
        self.assertGreater(lo,0)
    def test_inside_square(self):
        cell=decode_local_grid("30SYH133 305")
        self.assertEqual(distance_bounds(cell,713350,4230550)[0],0)
    def test_environment_requires_date(self):
        with self.assertRaises(ValueError):
            Borehole("p","30SYH133 305",2,23,period_environment="land")
    def test_bad_reference(self):
        with self.assertRaises(ValueError):
            decode_local_grid("30SYH133305123")
    def test_six_cores(self):
        r=audit_picola_paleocores()
        self.assertEqual([a["total_depth_m"] for a in r["cores"]],[36,23,31,30,12,8])
if __name__=="__main__":unittest.main()
