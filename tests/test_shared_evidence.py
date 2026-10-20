import unittest
from iberos.shared_evidence import validate_evidence

BASE={"evidence_id":"E1","object_id":"IBR-TEST-1","source_reference":"Fletcher 1981 fig.25","layer":"EDITORIAL","state":"CANDIDATE","pillars":["PALEO","CORPUS"]}
class SharedEvidenceTests(unittest.TestCase):
    def test_valid_intake_is_never_promotion(self):
        result=validate_evidence([BASE])
        self.assertEqual(result["count"],1)
        self.assertFalse(result["automatic_core_promotion"])
        self.assertFalse(result["records"][0]["scientifically_validated"])
    def test_duplicate_ids_blocked(self):
        with self.assertRaises(ValueError): validate_evidence([BASE,BASE.copy()])
    def test_no_source_blocked(self):
        with self.assertRaises(ValueError): validate_evidence([{**BASE,"source_reference":""}])
    def test_false_approval_blocked(self):
        with self.assertRaises(ValueError): validate_evidence([{**BASE,"scientifically_validated":True}])
    def test_bad_graphic_coordinates_blocked(self):
        with self.assertRaises(ValueError): validate_evidence([{**BASE,"layer":"GRAPHIC","bbox_xyxy":[50,20,2,100]}])
    def test_cross_record_dependencies(self):
        result=validate_evidence([BASE,{**BASE,"evidence_id":"E2","layer":"LINGUISTIC_HYPOTHESIS","pillars":["MORPH"],"dependent_on":["E1"]}])
        self.assertEqual(result["records"][1]["dependent_on"],["E1"])
if __name__=="__main__": unittest.main()
