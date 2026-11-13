import unittest
from iberos.geosites_alternatives import CorridorSegment,compare_corridors,picola_ilici_alternative_preflight

def valid(key,a,b,length,terrain="land",crossing=""):
    return CorridorSegment(key,a,b,terrain,"observed","dig-01",-500,-300,
                           "survey-01","strat-01",crossing,length,"meas-01")

class G128Tests(unittest.TestCase):
    def test_real_case_abstains(self):
        r=picola_ilici_alternative_preflight()
        self.assertEqual(r["candidate_count"],2)
        self.assertEqual(r["certified_corridors"],0)
        self.assertFalse(r["real_period_raster_loaded"])
    def test_alternatives_rank(self):
        r=compare_corridors([valid("ac","a","c",80),valid("ab","a","b",20),
                             valid("bc","b","c",30)],
                            {"long":["ac"],"short":["ab","bc"]})
        self.assertEqual(r["certified_corridors"],2)
        self.assertEqual(r["ranked_candidates"][0]["candidate"],"short")
        self.assertEqual(r["ranked_candidates"][0]["verified_length_m"],50)
    def test_lagoon_blocks(self):
        r=compare_corridors([valid("a","a","b",10,"lagoon")],{"x":["a"]})
        self.assertIn("independent_crossing_unverified",r["ranked_candidates"][0]["blockers"])
    def test_excavated_crossing_conditional(self):
        r=compare_corridors([valid("a","a","b",10,"moat","independent-02")],{"x":["a"]})
        self.assertEqual(r["certified_corridors"],1)
        self.assertFalse(r["archaeological_road_proven"])
    def test_late_period_rejected(self):
        s=CorridorSegment("a","a","b","land","observed","s",1900,2000,"g","t","",10,"measure")
        r=compare_corridors([s],{"x":["a"]})
        self.assertIn("period_not_covered",r["ranked_candidates"][0]["blockers"])
    def test_restored_rejected(self):
        s=valid("a","a","b",10)
        s=CorridorSegment(s.key,s.start,s.end,s.terrain,"restored",s.source,s.earliest,s.latest,
                          s.geometry_source,s.transit_source,s.crossing_source,s.measured_length_m,s.length_source)
        self.assertEqual(compare_corridors([s],{"x":["a"]})["certified_corridors"],0)
    def test_unknown_terrain_rejected(self):
        r=compare_corridors([valid("a","a","b",10,"unknown")],{"x":["a"]})
        self.assertIn("paleoterrain_unknown",r["ranked_candidates"][0]["blockers"])
    def test_disconnected_rejected(self):
        with self.assertRaises(ValueError):
            compare_corridors([valid("a","a","b",1),valid("b","c","d",1)],{"x":["a","b"]})
    def test_length_requires_source(self):
        with self.assertRaises(ValueError):
            CorridorSegment("a","a","b","land","observed",measured_length_m=10)
    def test_empty_chain(self):
        with self.assertRaises(ValueError):compare_corridors([],{"x":[]})
    def test_duplicate_segment_rejected(self):
        s=valid("a","a","b",1)
        with self.assertRaises(ValueError):compare_corridors([s,s],{"x":["a"]})
