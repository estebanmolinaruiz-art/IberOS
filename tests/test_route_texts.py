import unittest
from iberos.route_texts import TextWitness, evaluate_texts

def sample(wid="a", group="g", typ="explicit_itinerary", verified="verified", 
           start="alcudia",end="picola",first=-429,last=-350,direct=True):
    return TextWitness(wid,"source-"+wid,group,typ,first,last,-50,0,start,end,
                       (), "short excerpt","page 12",verified,direct)

class RouteTextTests(unittest.TestCase):
    def test_direct_but_never_proves_geometry(self):
        result=evaluate_texts([sample()],"alcudia","picola",-429,-349)
        self.assertEqual(result["status"],"textual_route_candidate")
        self.assertIsNone(result["geometry"])
        self.assertFalse(result["road_proven"])
    def test_unverified_excluded(self):
        result=evaluate_texts([sample(verified="unverified")],"alcudia","picola",-429,-349)
        self.assertEqual(result["status"],"no_qualified_textual_evidence")
    def test_only_contextual(self):
        result=evaluate_texts([sample(typ="trade",direct=False)],"alcudia","picola",-429,-349)
        self.assertEqual(result["status"],"contextual_hypothesis_only")
    def test_dependency_collapse(self):
        result=evaluate_texts([sample("a","same"),sample("b","same")],"alcudia","picola",-429,-349)
        self.assertEqual(len(result["independent_witnesses"]),1)
    def test_wrong_time(self):
        result=evaluate_texts([sample(first=1,last=50)],"alcudia","picola",-429,-349)
        self.assertEqual(result["status"],"no_qualified_textual_evidence")
    def test_other_places_do_not_support_link(self):
        result=evaluate_texts([sample(end="somewhere_else")],"alcudia","picola",-429,-349)
        self.assertEqual(result["status"],"no_qualified_textual_evidence")

if __name__=="__main__": unittest.main()
