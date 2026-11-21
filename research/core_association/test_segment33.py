import unittest
from pathlib import Path
import json
import segment33_external_gate as g
class ExternalGate(unittest.TestCase):
    def test_source_independent(self):
        self.assertNotIn("Orleyl",g.record["target_site"])
    def test_no_unverified_numeric_confirmation(self):
        self.assertFalse(g.record["generalisation_confirmed"])
        self.assertIsNone(g.record["external_precision"])
        self.assertIsNone(g.record["external_recall"])
    def test_no_reference_invented(self):
        self.assertFalse(g.record["homologous_pre_registered_reference_boundaries"])
if __name__=="__main__":unittest.main()
