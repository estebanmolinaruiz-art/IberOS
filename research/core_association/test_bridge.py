"""Documentary bridge contract tests: never pretend to recognise photographed signs."""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("association_bridge", pathlib.Path(__file__).with_name("bridge.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class AssociationBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = mod.build(ROOT)

    def test_signary_and_nonpromotion(self):
        result = self.result
        self.assertEqual(result["write_graphic_values"], 26)
        self.assertEqual(result["catalogue_candidate_rows"], 286)
        self.assertEqual(result["simple_source_labels"], 133)
        self.assertFalse(result["core_modified"])
        self.assertIsNone(result["visual_recognition_accuracy"])
        self.assertEqual(result["semantic_validation"], "NOT_EVALUATED")
        self.assertTrue(all(not x["usable_for_auto_reading"] for x in result["variants"]))

    def test_no_equivalence_fabricated(self):
        self.assertEqual(mod.normalize_value("DA"), "da")
        self.assertEqual(mod.normalize_value("GI"), "gi")
        self.assertEqual(mod.normalize_value("R1"), "r1")
        self.assertNotIn("da", mod.from_write_page(ROOT / "site/write/index.html"))
        self.assertNotIn("gi", mod.from_write_page(ROOT / "site/write/index.html"))

    def test_orleyl_editorial_only(self):
        self.assertGreater(len(self.result["orleyl_alignment"]), 0)
        self.assertEqual(self.result["orleyl_photographically_confirmed_tokens"], 0)
        self.assertTrue(all(x["status"] == "EDITORIAL_ONLY_NOT_INDEPENDENT_READING"
                            for x in self.result["orleyl_alignment"]))


if __name__ == "__main__":
    unittest.main()
