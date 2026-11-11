"""L35 isolated family-router regression tests; not external semantic gold."""
import unittest
from iberos.metrology_family_router_l35 import parse_ko_ti, route

class L35FamilyRouterTests(unittest.TestCase):
    def test_patterns(self):
        self.assertEqual(len(parse_ko_ti("ka ko sss ti IIII")), 1)
        self.assertEqual(len(parse_ko_ti("ti II")), 1)
        self.assertEqual(len(parse_ko_ti("ko s L ΠIIII ti ΠΙΙΙ")), 2)

    def test_non_quantity_words(self):
        for s in ("koter", "kotir", "tintileis", "tir", "ko sss", "ti",
                  "ibero", "sakaŕbeś:sos", "akoI", "kotiIIII"):
            self.assertEqual(parse_ko_ti(s), [], s)

    def test_offsets(self):
        s = "ka ko sss ti IIII, ti II"
        for hit in parse_ko_ti(s):
            self.assertEqual(s[hit["start"]:hit["end"]], hit["raw"])

    def test_systems_separated(self):
        self.assertEqual(route("ko sss ti IIII")["decision"], "ko_ti_review")
        self.assertEqual(route("a III")["decision"], "a_o_ki_review")
        self.assertEqual(route("a III ko sss ti IIII")["decision"], "mixed_families_review")

    def test_uncertainty(self):
        for hit in parse_ko_ti("ko s ΠIII ti IIII"):
            self.assertIsNone(hit["numeric_value"])
            self.assertIsNone(hit["semantic_function"])
            self.assertFalse(hit["independently_verified"])

    def test_abstention(self):
        self.assertEqual(route("ko s | ti")["decision"], "abstain")
        self.assertEqual(route("sakaŕbeś:sos")["decision"], "abstain")

if __name__ == "__main__":
    unittest.main()
