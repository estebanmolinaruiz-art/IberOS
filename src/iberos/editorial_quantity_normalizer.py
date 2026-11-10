"""Experimental L30 editorial quantity notation extractor.

Reads editorial transliterations, not verified physical signs. Never infers
numeric values, metrological equivalences, archaeological function or translations.
L26-L29 specimens are development data, not independent L30 evaluation.
"""
from __future__ import annotations
import re
from dataclasses import asdict, dataclass

LEFT = r'(?<![\wḿŕś])'
RIGHT = r'(?![\wḿŕś])'
PATTERNS = [
    ('e_complex_unresolved', re.compile(
        LEFT + r'(?P<unit>e)(?P<sep>[: \t]*)(?P<val>Π[ \t]*I+|[IV]+)' + RIGHT,
        re.UNICODE)),
    ('unit_editorial', re.compile(
        LEFT + r'(?P<unit>ki|gi|ka|a|o)(?P<sep>[: \t]*)(?P<val>\d{1,4}|[IV]{1,30})'
        + RIGHT + r'(?P<note>\([^()]{1,24}\))?', re.UNICODE)),
]

@dataclass(frozen=True)
class Evidence:
    raw: str
    start: int
    end: int
    unit: str
    editorial_value: str
    classification: str
    separator: str
    annotation: str | None
    numerical_value_verified: bool = False
    original_signs_verified: bool = False

def extract(text: str) -> list[dict]:
    """Return verbatim spans and descriptive categories; no numeric decoding."""
    found: list[Evidence] = []
    for kind, pattern in PATTERNS:
        for m in pattern.finditer(text):
            if any(not (m.end() <= x.start or m.start() >= x.end) for x in found):
                continue
            val = m.group('val')
            category = kind
            if kind == 'unit_editorial':
                category = ('unit_digits' if val.isdigit() else
                            'unit_strokes' if set(val) == {'I'} else
                            'unit_mixed_strokes_unresolved')
            found.append(Evidence(
                m.group(), m.start(), m.end(), m.group('unit'), val,
                category, m.group('sep'), m.groupdict().get('note')))
    return [asdict(x) for x in sorted(found, key=lambda x: x.start)]

def classify(text: str) -> str:
    """Conservative editorial-pattern flag with an abstention option."""
    hits = extract(text)
    certain_format = any(h['classification'] in ('unit_digits', 'unit_strokes') for h in hits)
    ambiguous = any(h['classification'] not in ('unit_digits', 'unit_strokes') for h in hits)
    if certain_format:
        return 'editorial_quantity_pattern_with_uncertainty' if ambiguous else 'editorial_quantity_pattern'
    if ambiguous or sum(ch in 'XS' for ch in text) >= 4:
        return 'ambiguous_numeraliform_abstain'
    return 'abstain'
