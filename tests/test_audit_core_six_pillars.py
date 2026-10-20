import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
SCRIPT=Path(__file__).resolve().parents[1]/"scripts"/"audit_core_six_pillars.py"
spec=importlib.util.spec_from_file_location("six_pillars",SCRIPT)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
class TestSixPillars(unittest.TestCase):
    def test_empty_repo_is_not_validated(self):
        with tempfile.TemporaryDirectory() as d:
            result=module.audit(Path(d))
            self.assertFalse(result["semantic_promotion_allowed"])
            self.assertFalse(result["orleyl_glyphs_verified"])
            self.assertEqual(result["corpus"]["records"],0)
    def test_duplicate_ids_and_false_validation(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            p=root/"data/curated/iberos_curated_objects_v1.jsonl"
            p.parent.mkdir(parents=True)
            p.write_text('{"object_id":"ONE","source":"a"}\n{"object_id":"ONE","source":"b"}\n')
            q=root/"data/review/validation01_progress_scorecard_v1.json"
            q.parent.mkdir(parents=True)
            q.write_text(json.dumps({"scientific_status":"NOT_EVALUATED","milestones":[{"status":"DONE"}]}))
            result=module.audit(root)
            self.assertEqual(result["corpus"]["duplicate_ids"],["ONE"])
            self.assertEqual(result["validation"]["completed_milestones"],1)
            self.assertFalse(result["semantic_promotion_allowed"])
if __name__=="__main__": unittest.main()
