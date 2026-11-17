"""Synthetic sanity checks only; NOT archaeological accuracy claims."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

import cv2
import numpy as np

MODULE_PATH = Path(__file__).resolve().parent / "reader.py"
spec = importlib.util.spec_from_file_location("iberos_read_experimental", MODULE_PATH)
read = importlib.util.module_from_spec(spec)
spec.loader.exec_module(read)


class ReadBaselineTests(unittest.TestCase):
    def test_synthetic_exact_and_abstention(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            a = np.full((70, 70), 255, np.uint8)
            cv2.line(a, (10, 10), (60, 60), 0, 6)
            b = np.full((70, 70), 255, np.uint8)
            cv2.circle(b, (35, 35), 20, 0, 6)
            cv2.imwrite(str(root / "a__synthetic.png"), a)
            cv2.imwrite(str(root / "e__synthetic.png"), b)
            templates = read.load_templates(root)
            result = read.classify_crop(a, templates, min_score=.9, min_margin=.05)
            self.assertEqual(result["status"], "CANDIDATE")
            self.assertEqual(result["prediction"], "a")
            blank = np.full((70, 70), 255, np.uint8)
            self.assertEqual(read.classify_crop(blank, templates)["status"], "ABSTAIN")

    def test_report_marks_unvalidated(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            a = np.full((70, 70), 255, np.uint8)
            cv2.line(a, (10, 10), (60, 60), 0, 6)
            cv2.imwrite(str(root / "a__synthetic.png"), a)
            cv2.imwrite(str(root / "object.png"), a)
            (root / "boxes.json").write_text(json.dumps([{"x": 0, "y": 0, "w": 70, "h": 70}]))
            result = read.run(root / "object.png", root / "boxes.json", root)
            self.assertEqual(result["readings"][0]["prediction"], "a")
            self.assertFalse(result["scientifically_validated"])
            self.assertIsNone(result["estimated_translation"])

    def test_invalid_boxes_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            img = np.full((20, 20), 255, np.uint8)
            cv2.line(img, (0, 0), (19, 19), 0, 2)
            cv2.imwrite(str(root / "a__synthetic.png"), img)
            cv2.imwrite(str(root / "object.png"), img)
            (root / "boxes.json").write_text('[{"x":0,"y":0,"w":999,"h":10}]')
            with self.assertRaises(ValueError):
                read.run(root / "object.png", root / "boxes.json", root)


if __name__ == "__main__":
    unittest.main()
