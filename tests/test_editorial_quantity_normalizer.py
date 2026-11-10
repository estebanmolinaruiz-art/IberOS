"""L30 regression/negative controls. Tests syntax, not external accuracy."""
import unittest
from iberos.editorial_quantity_normalizer import extract, classify

class EditorialQuantityNormalizerTests(unittest.TestCase):
    def test_regressions(self):
        self.assertEqual(len(extract('ki6 o3 a1 ki5(-1)')), 4)
        self.assertEqual(len(extract('a IIIIIII || ki III o I')), 3)
        self.assertEqual(len(extract('śalir ka IIIIIIIIIII : śalir ka IIIIIIIIIII')), 2)
        self.assertEqual(len(extract(']ilurka:ki:II:eIIIIII')), 2)

    def test_e_is_ambiguous(self):
        hits = extract('neitika:śorośalir:eI:kitaśal ir:eΠ I')
        self.assertEqual(len(hits), 2)
        self.assertTrue(all(h['classification'] == 'e_complex_unresolved' for h in hits))
        self.assertEqual(classify('eI:eΠ I'), 'ambiguous_numeraliform_abstain')

    def test_negative_controls(self):
        for s in ['kaike iberico', 'bekaI', 'kilo', 'eŕkaike', 'kaŕ', 'aorta', 'ki6ko', 'o3a']:
            self.assertEqual(extract(s), [], s)

    def test_original_spans_preserved(self):
        s = 'abc:ka:IIII:eΠ I / ki5(-1)'
        for hit in extract(s):
            self.assertEqual(s[hit['start']:hit['end']], hit['raw'])

    def test_no_decipherment_claim(self):
        for hit in extract('ka III ki:II eI'):
            self.assertFalse(hit['numerical_value_verified'])
            self.assertFalse(hit['original_signs_verified'])

    def test_abstentions(self):
        self.assertEqual(classify('XX SS'), 'ambiguous_numeraliform_abstain')
        self.assertEqual(classify('sakaŕbeś:sos'), 'abstain')

if __name__ == '__main__':
    unittest.main()
