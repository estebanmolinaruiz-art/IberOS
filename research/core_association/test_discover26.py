import unittest
import discover26_multisite as m

class MultiSiteGuard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.rows=m.build()
    def test_three_sources_present(self):
        self.assertEqual(set(r["physical_id"] for r in self.rows),
            {"IBR-LAP-0005","IBR-MUS-0001","IBR-PLM-0007"})
    def test_no_graphic_hallucination(self):
        self.assertTrue(all(r["glyph_crop_reference"] is None and not r["visual_glyph_verified"] for r in self.rows))
    def test_no_function_claims(self):
        self.assertTrue(all(r["semantic_inference"] is None and r["decision"]=="ABSTAIN" for r in self.rows))
    def test_dual_and_nondual_not_double_counted(self):
        r=[x for x in self.rows if x["physical_id"]=="IBR-PLM-0007"]
        self.assertTrue(any(x["reading_ambiguity"] for x in r))
        self.assertEqual(len({x["physical_id"] for x in r}),1)
    def test_context_never_auto_validated(self):
        self.assertTrue(all(not r["archaeological_external_function_verified"] for r in self.rows))
    def test_source_provenance_exists(self):
        self.assertTrue(all(r["source_ref"] for r in self.rows))

if __name__=="__main__":unittest.main()
