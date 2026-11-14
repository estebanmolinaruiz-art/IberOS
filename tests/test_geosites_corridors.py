import unittest
from iberos.geosites_corridors import SiteNode, RouteLink, audit_corridor, picola_ilici_research_case

class GeoSitesG127Tests(unittest.TestCase):
    def setUp(self):
        self.nodes=[SiteNode("a","A"), SiteNode("b","B"), SiteNode("c","C")]

    def test_actual_case_abstains(self):
        r=picola_ilici_research_case()
        self.assertEqual(r["documentary_links"],6)
        self.assertEqual(r["eligible_links"],0)
        self.assertFalse(r["certified_connected_chain"])
        self.assertEqual(r["straight_baseline_reference_m"],12252.154)
        self.assertIsNone(r["map_polyline"])

    def test_dated_surveyed_transit_only(self):
        ab=RouteLink("ab","a","b","observed","source",-500,-300,True,True)
        bc=RouteLink("bc","b","c","observed","source",-200,-100,True,True)
        r=audit_corridor(self.nodes,[ab,bc],"a","c")
        self.assertEqual(r["eligible_links"],1)
        self.assertFalse(r["certified_connected_chain"])

    def test_ditch_requires_crossing_evidence(self):
        e=RouteLink("ab","a","b","observed","source",-500,-300,True,True,"ditch")
        self.assertIn("obstruction_crossing_unverified",
                      audit_corridor(self.nodes,[e],"a","b")["excluded_links"][0]["blockers"])

    def test_proven_crossing_can_be_traversed(self):
        e=RouteLink("ab","a","b","observed","source",-500,-300,True,True,
                    "ditch","independent-excavation")
        r=audit_corridor(self.nodes,[e],"a","b")
        self.assertTrue(r["certified_connected_chain"])
        self.assertFalse(r["historical_road_proven"])

    def test_restored_not_traversable(self):
        e=RouteLink("ab","a","b","restored","source",-500,-300,True,True)
        self.assertEqual(audit_corridor(self.nodes,[e],"a","b")["eligible_links"],0)

    def test_unsurveyed_not_traversable(self):
        e=RouteLink("ab","a","b","observed","source",-500,-300,True,False)
        self.assertEqual(audit_corridor(self.nodes,[e],"a","b")["eligible_links"],0)

    def test_duplicate_node_rejected(self):
        with self.assertRaises(ValueError):
            audit_corridor([self.nodes[0],self.nodes[0]],[],"a","a")

    def test_incomplete_coordinates_rejected(self):
        with self.assertRaises(ValueError):
            SiteNode("a","A",1,None,"source")
if __name__=="__main__": unittest.main()
