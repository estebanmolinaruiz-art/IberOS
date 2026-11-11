"""L37 state and provenance protections, not semantic accuracy tests."""
import unittest
from iberos.metrology_evidence_l37 import evaluate


class L37Tests(unittest.TestCase):
    def test_e_indeterminate(self):
        x = evaluate("eΠ I")["candidates"][0]
        self.assertEqual(x["state"], "INDETERMINATE")
        self.assertIsNone(x["proposed_family"])

    def test_ko_is_not_confirmed(self):
        x = evaluate("ko II")
        self.assertEqual(x["candidates"][0]["state"], "GRAPHIC_CANDIDATE")
        self.assertEqual(x["family_confirmed_count"], 0)

    def test_embedded_orleyl_is_indeterminate(self):
        self.assertEqual(evaluate("abaoIIII")["candidates"][0]["state"], "INDETERMINATE")

    def test_no_pattern(self):
        self.assertEqual(evaluate("sakaŕbeś:sos")["candidates"], [])

    def test_editorial_claim_rejected(self):
        r = dict(family="ko_ti_editorial", evidence_type="editorial_interpretation",
                 source_id="paper", verified_independently=True,
                 review_status="approved", supports_family_attribution=True)
        self.assertFalse(evaluate("ko II", independent_evidence=r)["candidates"][0]
                         ["promotion_record_eligible_for_audit"])

    def test_no_source_rejected(self):
        r = dict(family="ko_ti_editorial", evidence_type="independent_original_sign_reading",
                 source_id="", verified_independently=True,
                 review_status="approved", supports_family_attribution=True)
        self.assertEqual(evaluate("ko II", independent_evidence=r)["family_confirmed_count"], 0)

    def test_even_eligible_record_needs_real_audit(self):
        r = dict(family="ko_ti_editorial", evidence_type="independent_archaeological_context",
                 source_id="audit:independent-001", verified_independently=True,
                 review_status="approved", supports_family_attribution=True)
        x = evaluate("ko II", independent_evidence=r)
        self.assertTrue(x["candidates"][0]["promotion_record_eligible_for_audit"])
        self.assertEqual(x["candidates"][0]["state"], "GRAPHIC_CANDIDATE")
        self.assertEqual(x["family_confirmed_count"], 0)

    def test_ambiguous_not_promoted(self):
        r = dict(family="ko_ti_editorial", evidence_type="independent_archaeological_context",
                 source_id="audit:001", verified_independently=True,
                 review_status="approved", supports_family_attribution=True)
        self.assertFalse(evaluate("eΠ I", independent_evidence=r)["candidates"][0]
                         ["promotion_record_eligible_for_audit"])

    def test_exact_spans(self):
        s = "x:ki III ko s ΠIII"
        for item in evaluate(s)["candidates"]:
            self.assertEqual(s[item["start"]:item["end"]], item["raw"])


if __name__ == "__main__":
    unittest.main()
