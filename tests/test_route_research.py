import unittest
from iberos.route_research import EvidenceCell, RouteCase, analyze, compare

CASE = RouteCase("test", (0,0), (0,2), -429, -349, 10, "EPSG:25830")
LAND = EvidenceCell("land",-500,-300,"study-1")
UNKNOWN = EvidenceCell("unknown",-500,-300,"study-1")

class GeoRoutesTests(unittest.TestCase):
    def test_connected(self):
        grid=[[LAND,LAND,LAND]]
        out=analyze(grid,CASE)
        self.assertEqual(out["status"],"candidate_computed")
        self.assertEqual(out["length_m"],20)
        self.assertFalse(out["historical_path_proven"])

    def test_unknown_is_closed(self):
        self.assertEqual(analyze([[LAND,UNKNOWN,LAND]],CASE)["status"],
                         "no_connected_certified_cells")

    def test_unverified_river_closed(self):
        river=EvidenceCell("river",-500,-300,"study-1")
        self.assertEqual(analyze([[LAND,river,LAND]],CASE)["status"],
                         "no_connected_certified_cells")

    def test_verified_river_open(self):
        river=EvidenceCell("river",-500,-300,"study-1","vado-1")
        self.assertEqual(analyze([[LAND,river,LAND]],CASE)["status"],
                         "candidate_computed")

    def test_wrong_date_closed(self):
        roman=EvidenceCell("land",-100,200,"roman")
        self.assertEqual(analyze([[LAND,roman,LAND]],CASE)["status"],
                         "no_connected_certified_cells")

    def test_diagonal_corner_closed(self):
        grid=[[LAND,UNKNOWN],[UNKNOWN,LAND]]
        c=RouteCase("diag",(0,0),(1,1),-429,-349,10,"EPSG:25830")
        self.assertEqual(analyze(grid,c)["status"],"no_connected_certified_cells")

    def test_methods(self):
        grid=[[LAND,LAND,LAND]]
        self.assertEqual(analyze(grid,CASE,"astar")["length_m"],20)
        self.assertEqual(compare(grid,CASE,trials=3)["trials"],3)

if __name__=="__main__": unittest.main()
