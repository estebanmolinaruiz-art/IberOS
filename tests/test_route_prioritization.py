import unittest
from iberos.route_prioritization import DocumentaryLead, text_candidates, prioritize
def lead(id,corridor,group,period=False,coords=False):
    return DocumentaryLead(id,corridor,"source-"+id,group,"trace",True,period,coords)
class G114Tests(unittest.TestCase):
    def test_text_terms_only(self):
        s=text_candidates("camino comercial hacia puerto y guarnición")
        self.assertIn("camino",s["movement"])
        self.assertIn("puerto",s["trade"])
        self.assertIn("guarnicion",s["military"])
    def test_undated_trace_cannot_be_road(self):
        r=prioritize([lead("a","Molar","g")],"430-350 BCE")
        self.assertFalse(r["rankings"][0]["historical_road_proven"])
    def test_duplicate_not_double_counted(self):
        r=prioritize([lead("a","Molar","g"),lead("b","Molar","g")],"430-350 BCE")
        self.assertEqual(r["rankings"][0]["independent_evidence_groups"],1)
    def test_verified_direct_is_prioritized(self):
        r=prioritize([lead("a","Molar","g",True,True),lead("b","Other","h")],"430-350 BCE")
        self.assertEqual(r["rankings"][0]["candidate"],"Molar")
    def test_scores_not_probabilities(self):
        r=prioritize([lead("a","Molar","g")],"430-350 BCE")
        self.assertFalse(r["scores_are_probabilities"])
if __name__=="__main__": unittest.main()
