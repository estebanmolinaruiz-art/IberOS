"""Scientific readiness gates for DISCOVER-01."""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("discover", pathlib.Path(__file__).with_name("discover.py"))
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)

class DiscoveryReadinessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = M.assess(ROOT)

    def test_no_fake_semantics(self):
        d = self.d
        self.assertEqual(d["model_comparison"]["result"], "ABSTAIN_NO_INDEPENDENT_SEMANTIC_GOLD")
        self.assertIsNone(d["model_comparison"]["holdout_accuracy"])
        self.assertFalse(d["ready_for_semantic_model_comparison"])
        self.assertTrue(all(not x["eligible_for_blind_semantic_benchmark"] for x in d["object_evidence_queue"]))

    def test_actual_archived_visual_unreadiness(self):
        d = self.d
        self.assertEqual(d["visual_matcher_training_rows"], 0)
        self.assertEqual(d["verified_linked_sign_images"], 0)
        self.assertGreaterEqual(d["existing_visual_alignment_rows"], 1)
        self.assertEqual(d["existing_visual_alignment_rows"], d["unverified_coordinate_rows"])
        self.assertFalse(d["ready_for_automatic_glyph_training"])

    def test_physical_provenance_and_unique_ids(self):
        d = self.d
        self.assertEqual(d["duplicate_object_ids"], [])
        self.assertEqual(d["unique_curated_objects"], d["curated_object_rows"])
        self.assertIn("PHYS_ID", d["physical_split_policy"])
        self.assertEqual(len(d["source_sha256"]), 5)

if __name__ == "__main__":
    unittest.main()
