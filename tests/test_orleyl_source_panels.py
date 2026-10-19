"""Tests for Orleyl source-panel evidence boundaries (no PDF dependency)."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "orleyl_prepare_source_panels.py"
spec = importlib.util.spec_from_file_location("orleyl_panels", MODULE)
panels = importlib.util.module_from_spec(spec)
spec.loader.exec_module(panels)

class TestOrleylPanels(unittest.TestCase):
    def test_page_mapping_is_pdf_one_based(self):
        self.assertEqual(panels.PAGES["orleyl_viib_figure25"], 111)
        self.assertEqual(panels.PAGES["orleyl_viib_photo_plate22"], 158)
        self.assertEqual(panels.PAGES["orleyl_v_figure22"], 65)
        self.assertEqual(panels.PAGES["orleyl_v_photo_plate17"], 153)

    def test_manifest_does_not_certify_signs_or_rotation(self):
        with tempfile.TemporaryDirectory() as d:
            pdf = Path(d) / "source.pdf"
            pdf.write_bytes(b"%PDF dummy for hash only")
            manifest = panels.source_manifest(pdf, 159, 2.0, [])
            self.assertFalse(manifest["glyph_positions_verified"])
            self.assertIn("NOT_VERIFIED", manifest["orientation"])
            self.assertEqual(len(manifest["pdf_sha256"]), 64)

if __name__ == "__main__":
    unittest.main()
