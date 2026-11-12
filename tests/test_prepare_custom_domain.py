"""Tests for zero-cost custom-domain build transformation."""
import tempfile
import unittest
import sys
from pathlib import Path

# pytest may run with tests/ (not the repo root) on sys.path.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.prepare_custom_domain import prepare_site, OLD_BASE, NEW_BASE

class CustomDomainTests(unittest.TestCase):
    def test_rewrites_web_urls_only_and_keeps_external_urls(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "index.html").write_text(
                f'<link rel="canonical" href="{OLD_BASE}/">'
                f'<a href="{OLD_BASE}/corpus/">Corpus</a>'
                '<a href="https://doi.org/10.5281/zenodo.22939179">DOI</a>',
                encoding="utf-8",
            )
            (root / "sitemap.xml").write_text(
                f'<urlset><loc>{OLD_BASE}/</loc></urlset>', encoding="utf-8")
            (root / "robots.txt").write_text(
                f'Sitemap: {OLD_BASE}/sitemap.xml', encoding="utf-8")
            (root / "image.jpg").write_bytes(b"\xff\xd8\x00\xfe")
            result = prepare_site(root)
            self.assertEqual(result["old_base_occurrences"], 4)
            self.assertEqual(result["changed_files"], 3)
            self.assertIn(f'{NEW_BASE}/corpus/', (root / "index.html").read_text())
            self.assertIn("https://doi.org/", (root / "index.html").read_text())
            self.assertEqual((root / "image.jpg").read_bytes(), b"\xff\xd8\x00\xfe")
            self.assertEqual(prepare_site(root, check=True)["old_base_occurrences"], 0)

    def test_check_catches_old_links(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "index.html").write_text(OLD_BASE, encoding="utf-8")
            with self.assertRaises(AssertionError):
                prepare_site(root, check=True)

if __name__ == "__main__":
    unittest.main()
