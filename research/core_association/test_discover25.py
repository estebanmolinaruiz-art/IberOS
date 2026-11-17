#!/usr/bin/env python3
"""Falsification guards for DISCOVER-25."""
import unittest
import discover25_evidence_model as d

class EvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case,cls.graph=d.load_case()
        cls.rows=d.make_lattice(cls.case,cls.graph)
    def test_no_false_translation(self):
        self.assertTrue(all(x["inferred_translation"] is None for x in self.rows))
        self.assertTrue(all(x["decision"].startswith("ABSTAIN") for x in self.rows))
    def test_alternative_readings_retained(self):
        r=next(x for x in self.rows if x["side"]=="B" and x["line"]==1 and x["unit"]==1)
        self.assertEqual(r["editorial_reading_alternatives"],["ideŕ","iteŕ"])
        self.assertFalse(r["reading_invariant"])
    def test_graphics_not_misattributed(self):
        self.assertTrue(all(x["original_pixel_coordinates"] is None for x in self.rows))
        self.assertTrue(all(x["graphic_evidence_status"]!="SIGN_VERIFIED" for x in self.rows))
    def test_variants_single_object(self):
        self.assertEqual(len(set(x["phys_id"] for x in self.rows)),1)
        self.assertTrue(all(not x["editions_assumed_independent"] for x in self.rows))
    def test_edited_strokes_not_external_quantity(self):
        numeric=[x for x in self.rows if x["editorial_stroke_stability"]]
        self.assertTrue(numeric)
        self.assertTrue(all("QUANTITATIVE_NOTATION_CANDIDATE" in x["possible_function_classes"] for x in numeric))
        self.assertTrue(all(x["external_archaeological_function_evidence"]=="NOT_VERIFIED" for x in numeric))
    def test_abstention_counts(self):
        s=d.assess(self.rows)
        self.assertEqual(s["abstentions"],len(self.rows))
        self.assertEqual(s["translations_validated"],0)

if __name__=="__main__":unittest.main()
