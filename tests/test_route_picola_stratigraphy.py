import unittest
from iberos.route_picola_stratigraphy import Feature,evaluate,picola_1998_case

class G126Tests(unittest.TestCase):
    def test_picola_does_not_demonstrate_crossing(self):
        r=picola_1998_case()
        self.assertEqual(r["verdict"],"NO_DIRECT_DATED_CROSSING_EVIDENCE")
        self.assertFalse(r["bridge_or_causeway_confirmed"])
    def test_restored_cannot_pass(self):
        f=Feature("b","restored","s","scheme",-450,-300,True,True)
        self.assertEqual(evaluate([f])["crossing_review_candidates"],[])
    def test_undated_excavated_cannot_pass(self):
        f=Feature("b","excavated","s","finding",crossing_feature=True)
        self.assertEqual(evaluate([f])["crossing_review_candidates"],[])
    def test_dated_triggers_review_only(self):
        f=Feature("b","excavated","s","finding",-450,-300,True,True)
        r=evaluate([f])
        self.assertEqual(r["verdict"],"REQUIRES_EXTERNAL_REVIEW")
        self.assertFalse(r["bridge_or_causeway_confirmed"])
    def test_roman_not_backdated(self):
        f=Feature("b","excavated","s","Roman",1,200,True,True)
        self.assertEqual(evaluate([f])["crossing_review_candidates"],[])
    def test_inverted_dates_rejected(self):
        with self.assertRaises(ValueError):
            Feature("b","excavated","s","wrong",100,0)

if __name__=="__main__":unittest.main()
