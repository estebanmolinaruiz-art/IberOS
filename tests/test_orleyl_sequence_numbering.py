"""Editorial index reconciliation must never approve physical sign positions."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_comparison_indices_preserve_full_fletcher_sequence_and_pending_review():
    data = json.loads((ROOT / 'data/review/orleyl_te_glyph_review_v1.json').read_text())
    full = data['figure25_ten_candidate_units_2026_10_20']['fletcher_editorial_labels']
    for name, index, token in [
        ('validation01_orleyl_17_visual_alignment_v1.csv', 'index', 'editorial_token'),
        ('validation01_orleyl_17_signs_visual_review_queue.csv', 'glyph_index', 'editorial_sign'),
    ]:
        with (ROOT / 'data/review' / name).open() as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == 17
        vii = [r for r in rows if r['object_id'] == 'ORLEYL-VII']
        assert [int(r[index]) for r in vii] == list(range(1, 9))
        assert [int(r['fletcher_sequence_index']) for r in vii] == list(range(3, 11))
        for row in rows:
            assert row['coordinate_verification'] == 'UNVERIFIED_DO_NOT_USE_AS_SIGN_PROOF'
            assert row['mapping_basis'] == 'EDITORIAL_TOKEN_ORDER_ONLY'
        for row in vii:
            assert full[int(row['fletcher_sequence_index']) - 1].lower() == row[token]
    assert full[:2] == ['BA', 'S']
    assert data['eligible_for_core_execution'] is False
    assert data['figure25_ten_candidate_units_2026_10_20']['individual_sign_identifications_verified'] is False
