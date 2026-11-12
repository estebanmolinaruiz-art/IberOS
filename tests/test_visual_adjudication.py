"""Negative controls for visual review. No mock glyph is historical evidence."""
import copy
import unittest
from pathlib import Path

from iberos.visual_adjudication import (
    assess_blind_collation, audit_repository, build_queue, editorial_delta,
)

ROOT = Path(__file__).resolve().parents[1]


def demo_submission():
    """Synthetic QA only; not a photographed Iberian glyph."""
    sha = "a" * 64
    return {
        "review_id": "SYNTHETIC-TEST-ONLY", "object_id": "MOCK-OBJECT",
        "source_page": "test-page-2", "figure_locator": "figure-test-A",
        "source_image_url": "https://example.invalid/test-only",
        "source_image_sha256": sha,
        "bbox_xyxy": [0.10, 0.20, 0.30, 0.40],
        "object_match_reviewed": True,
        "readers": [
            {"reviewer_id": "A", "independence_group": "lab-A", "reading": "X",
             "method": "DIRECT_IMAGE", "blind_to_editorial": True,
             "source_image_sha256": sha},
            {"reviewer_id": "B", "independence_group": "lab-B", "reading": "X",
             "method": "DIRECT_IMAGE", "blind_to_editorial": True,
             "source_image_sha256": sha},
        ],
    }


class VisualAdjudicationTests(unittest.TestCase):
    def test_real_sources_are_not_new_physical_objects(self):
        queue = build_queue(ROOT)
        self.assertEqual(len(queue), 26)
        self.assertEqual(len(set(x["review_id"] for x in queue)), 26)
        self.assertEqual(len(set(x["object_id"] for x in queue)), 5)
        self.assertFalse(any(x["visual_verified"] for x in queue))
        self.assertEqual(len([x for x in queue if x["source_family"] == "SERRETA"]), 7)
        self.assertEqual(len([x for x in queue if x["source_family"] == "VILLARES"]), 14)

    def test_audit_has_non_promoting_evidence_contract(self):
        r = audit_repository(ROOT)
        self.assertEqual(r["evidence_contract"]["count"], 26)
        self.assertEqual(r["review_units"], 26)
        self.assertEqual(r["by_source"], {"PAL": 5, "SERRETA": 7, "VILLARES": 14})
        self.assertEqual(r["editorial_pairs_compared"], 21)
        self.assertEqual(r["independently_verified_glyphs"], 0)
        self.assertEqual(r["scientific_verdict"], "NOT_EVALUATED")
        self.assertFalse(r["automatic_core_promotion"])
        self.assertEqual(r["ready_for_human_adjudication"], 0)
        self.assertTrue(any(x["review_id"] == "VIL5-A3" for x in r["priorities"]))

    def test_two_editorial_decisions_are_not_visual_autopsies(self):
        result = audit_repository(ROOT)
        self.assertEqual(result["editorial_decisions_supported"], 2)
        decisions = {x["review_id"]: x for x in result["editorial_decisions"]}
        self.assertEqual(set(decisions), {"SER-B1-SALIRG", "VIL5-A3"})
        self.assertEqual(decisions["SER-B1-SALIRG"]["preferred_editorial"], "śalirg")
        self.assertEqual(decisions["VIL5-A3"]["preferred_editorial"], "bobai-da")
        self.assertTrue(all(x["status"] == "EDITORIAL_DECISION_ONLY" for x in decisions.values()))
        self.assertTrue(all(x["independent_image_readings"] == 0
                            and x["glyph_photo_verified"] is False
                            and x["automatic_core_promotion"] is False
                            for x in decisions.values()))
        self.assertEqual(result["independently_verified_glyphs"], 0)
        self.assertEqual(result["physical_objects"], 5)

    def test_editorial_difference_not_a_photographic_sign(self):
        out = editorial_delta("SALIRG", "SALIRIG")
        self.assertFalse(out["source_text_identical"])
        self.assertTrue(out["not_photographic_sign_count"])
        self.assertEqual(out["kind"], "EDITORIAL_UNICODE_CODEPOINT_DIFFERENCE")
        self.assertEqual("".join(x["after"] for x in out["edits"]), "I")
        self.assertEqual(editorial_delta("é", "e\u0301")["edit_blocks"], 0)

    def test_blind_readers_only_ready_for_human_review(self):
        r = assess_blind_collation(demo_submission())
        self.assertEqual(r["status"], "READY_FOR_HUMAN_ADJUDICATION")
        self.assertEqual(r["blockers"], [])
        self.assertFalse(r["scientifically_validated"])
        self.assertFalse(r["automatic_core_promotion"])
        self.assertFalse(r["semantic_translation_confirmed"])

    def test_one_reader_does_not_count_as_independent(self):
        s = demo_submission()
        s["readers"] = s["readers"][:1]
        r = assess_blind_collation(s)
        self.assertEqual(r["status"], "BLOCKED")
        self.assertIn("TWO_BLIND_READERS_REQUIRED", r["blockers"])

    def test_same_reader_or_group_rejected(self):
        for key in ("reviewer_id", "independence_group"):
            with self.subTest(key=key):
                s = demo_submission()
                s["readers"][1][key] = s["readers"][0][key]
                r = assess_blind_collation(s)
                self.assertIn("NONINDEPENDENT_REVIEWERS", r["blockers"])

    def test_editorial_copy_does_not_count_as_blind_image_reading(self):
        s = demo_submission()
        s["readers"][1]["method"] = "EDITORIAL_TRANSCRIPTION"
        self.assertIn("NONBLIND_OR_DERIVED_EDITORIAL_READING",
                      assess_blind_collation(s)["blockers"])
        s = demo_submission()
        s["readers"][1]["blind_to_editorial"] = False
        self.assertEqual(assess_blind_collation(s)["status"], "BLOCKED")

    def test_same_image_hash_required(self):
        s = demo_submission()
        s["readers"][1]["source_image_sha256"] = "b" * 64
        self.assertIn("READER_IMAGE_MISMATCH", assess_blind_collation(s)["blockers"])

    def test_conflicting_signs_are_never_adjudicated_automatically(self):
        s = demo_submission()
        s["readers"][1]["reading"] = "Y"
        r = assess_blind_collation(s)
        self.assertIn("READINGS_DISAGREE", r["blockers"])
        self.assertFalse(r["scientifically_validated"])

    def test_missing_or_invalid_image_location_rejected(self):
        for bad in (None, [0.8, 0.2, 0.1, 0.7], [0.0, 0.1, 2.0, 0.2],
                    [True, 0.2, 0.3, 0.4]):
            with self.subTest(bbox=bad):
                s = demo_submission()
                s["bbox_xyxy"] = bad
                self.assertIn("VERIFIED_NORMALIZED_BBOX_REQUIRED",
                              assess_blind_collation(s)["blockers"])
        s = demo_submission()
        s["object_match_reviewed"] = False
        self.assertIn("OBJECT_MATCH_NOT_REVIEWED",
                      assess_blind_collation(s)["blockers"])

    def test_scientific_self_promotion_is_invalid(self):
        for key in ("scientifically_validated", "automatic_core_promotion"):
            s = demo_submission()
            s[key] = True
            with self.assertRaises(ValueError):
                assess_blind_collation(s)


if __name__ == "__main__":
    unittest.main()
