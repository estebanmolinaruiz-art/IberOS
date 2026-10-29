#!/usr/bin/env python3
"""IberOS: validate M06 evidence references; never certify palaeography automatically."""
import csv
import hashlib
import json
from pathlib import Path


def evaluate(root):
    root = Path(root).resolve()
    problems = []
    try:
        score = json.loads((root / 'data/review/validation01_progress_scorecard_v1.json').read_text())
        milestones = [m for m in score['milestones'] if m.get('id') == 'M06']
        if len(milestones) != 1:
            raise ValueError('M06 must occur exactly once')
        status = milestones[0]['status']
        if status != 'DONE':
            return {'gate': 'BLOCKED', 'status': status, 'problems': ['M06_NOT_DONE']}
        with (root / 'data/review/validation01_orleyl_17_visual_alignment_v1.csv').open(newline='') as f:
            expected = {(r['object_id'], r['editorial_word'], r['index']) for r in csv.DictReader(f)}
        if len(expected) != 17:
            problems.append('INVALID_EXPECTED_SIGN_SET')
        manifest = json.loads((root / 'data/review/validation01_m06_evidence_v1.json').read_text())
        signs = manifest['signs']
        keys = [(s['object_id'], s['editorial_word'], str(s['index'])) for s in signs]
        if len(keys) != 17 or len(set(keys)) != 17 or set(keys) != expected:
            problems.append('INCOMPLETE_OR_DUPLICATE_SIGN_COVERAGE')
        for s in signs:
            # These declarations require attributed human review, not automatic truth inference.
            for field in ('reviewer', 'review_record', 'variant_id', 'signary_reference', 'discrepancy_notes'):
                value = str(s.get(field, '')).strip()
                if not value or value.upper() in {'PENDING', 'UNKNOWN', 'UNRESOLVED', 'TBD'}:
                    problems.append('MISSING_OR_UNRESOLVED_' + field.upper())
            if s.get('status') != 'REVIEWED' or s.get('editorial_key_hidden') is not True:
                problems.append('NON_BLIND_OR_UNREVIEWED_SIGN')
            bbox = s.get('bbox', [])
            if (len(bbox) != 4 or not all(type(v) in (int, float) for v in bbox)
                    or not (0 <= bbox[0] < bbox[2] and 0 <= bbox[1] < bbox[3])):
                problems.append('INVALID_BBOX')
            for prefix in ('source', 'crop', 'review'):
                path = (root / s.get(prefix + '_path', '')).resolve()
                if root not in path.parents or not path.is_file():
                    problems.append('MISSING_OR_UNSAFE_' + prefix.upper() + '_ASSET')
                    continue
                if hashlib.sha256(path.read_bytes()).hexdigest() != s.get(prefix + '_sha256'):
                    problems.append('HASH_MISMATCH_' + prefix.upper())
        return {'gate': 'BLOCKED' if problems else 'EVIDENCE_REFERENCES_CHECKED',
                'status': status, 'problems': sorted(set(problems)),
                'note': 'Reference integrity only; M07 and scientific validation remain separate.'}
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return {'gate': 'BLOCKED', 'problems': ['M06_EVIDENCE_INVALID'], 'detail': str(exc)}
