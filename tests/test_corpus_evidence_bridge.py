import unittest
from pathlib import Path
from iberos.corpus_evidence_bridge import link_corpus, link_repository

class CorpusBridgeTests(unittest.TestCase):
    def test_matching_object(self):
        curated=[{"object_id":"IBR-X","source":"https://example.org/paper"}]
        registry=[{"OBJECT_ID":"IBR-X","Fuente":"https://example.org/paper"}]
        result=link_corpus(curated,registry)
        self.assertEqual(result["linked_objects"],1)
        self.assertFalse(result["automatic_core_promotion"])
        self.assertEqual(result["evidence"]["records"][0]["state"],"CANDIDATE")
    def test_missing_source_is_not_invented(self):
        result=link_corpus([{"object_id":"IBR-X","source":""}],[{"OBJECT_ID":"IBR-X","Fuente":"https://x.example"}])
        self.assertEqual(result["linked_objects"],0)
        self.assertEqual(result["issues"][0]["issue"],"MISSING_CURATED_SOURCE")
    def test_source_conflict_is_quarantined(self):
        result=link_corpus([{"object_id":"X","source":"a"}],[{"OBJECT_ID":"X","Fuente":"b"}])
        self.assertEqual(result["linked_objects"],0)
        self.assertEqual(result["issues"][0]["issue"],"SOURCE_CONFLICT")
    def test_duplicate_object_rejected(self):
        with self.assertRaises(ValueError):
            link_corpus([{"object_id":"X"},{"object_id":"X"}],[])
    def test_repo_real_corpus_runs(self):
        root=Path(__file__).resolve().parents[1]
        result=link_repository(root)
        self.assertGreater(result["curated_objects"],0)
        self.assertEqual(result["linked_objects"]+result["unlinked_curated_objects"],result["curated_objects"])
        self.assertFalse(result["evidence"]["automatic_core_promotion"])
