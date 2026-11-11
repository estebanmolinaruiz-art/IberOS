"""L38 verification of scientific anti-promotion gates."""
import unittest
from iberos.independent_evidence_registry_l38 import audit, REQUIRED

def sample(**updates):
    row = dict.fromkeys(REQUIRED, "")
    row.update(object_id="T.06.09", catalog_id="T.06.09",
               transcription="ko II", candidate_family="ko_ti_editorial",
               edition_url="https://example.org/publication",
               edition_reference="Editorial text", audit_decision="PENDING")
    row.update(updates)
    return row

class EvidenceRegistryL38Tests(unittest.TestCase):
    def test_missing_image_and_reading_block(self):
        result = audit(sample())
        self.assertIn("NO_INDEPENDENT_IMAGE_READING", result["issues"])
        self.assertFalse(result["family_confirmed"])

    def test_self_declared_confirmation_rejected(self):
        result = audit(sample(audit_decision="FAMILY_CONFIRMED"))
        self.assertIn("SELF_DECLARED_CONFIRMATION_NOT_ACCEPTED", result["issues"])

    def test_even_complete_metadata_cannot_self_confirm(self):
        result = audit(sample(
            image_url="https://example.org/original.png",
            image_access="DIRECT_PRIMARY_IMAGE_VERIFIED",
            independent_image_reading_id="reading01",
            archaeological_context_source="ctx01",
            chronology_source="date01", reviewer_id="review01",
            review_date="2026-11-11"))
        self.assertIn("EXTERNAL_ADJUDICATION_REQUIRED", result["issues"])
        self.assertFalse(result["family_confirmed"])

    def test_invalid_url(self):
        self.assertIn("INVALID_EDITION_URL",
                      audit(sample(edition_url="http://example.org"))["issues"])

    def test_incomplete_schema_blocked(self):
        self.assertEqual(audit({"object_id": "test"})["state"], "BLOCKED")

    def test_rejected(self):
        self.assertEqual(audit(sample(audit_decision="REJECTED"))["state"], "REJECTED")

    def test_no_numeric_or_semantic_promotion(self):
        result = audit(sample())
        self.assertFalse(result["numeric_value_verified"])
        self.assertFalse(result["new_translation_validated"])

    def test_edition_not_traceable(self):
        self.assertIn("EDITION_NOT_TRACEABLE",
                      audit(sample(edition_url=""))["issues"])

if __name__ == "__main__":
    unittest.main()
