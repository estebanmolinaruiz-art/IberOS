# L37 — Separate patterns from metrological-family attribution

The L36 retrospective corpus comparison showed that the L35 router assigns
the same review label to unrelated graphic variants, particularly `eΠ I`
and `ko II`. L37 is an **opt-in overlay** on the unchanged L35 router.

- `GRAPHIC_CANDIDATE`: a regular expression detects an editorial form; **not** an independently confirmed metrological system.
- `INDETERMINATE`: ambiguous `e`, embedded `oIIII`, or mixed editorial strokes.
- `FAMILY_CONFIRMED`: reserved; **never generated** from user-supplied claims, editorial labels, or unreviewed metadata.

External records may be **eligible for an audit queue** if fields are
complete, but are not fact-checked by this software. Promotion needs a
separate independently audited evidence registry, image-based reading where
possible, and documented reviewer approval. Do not infer numeric values,
item/document functions, semantic translations, or increase official scores.

Example:

```python
from iberos.metrology_evidence_l37 import evaluate
evaluate("eΠ I")["candidates"][0]["state"]  # INDETERMINATE
evaluate("ko II")["candidates"][0]["state"]  # GRAPHIC_CANDIDATE
```

Run: `python -m unittest tests.test_metrology_evidence_l37 -v`.

The L36 retrospective examples are development inputs, not a new blind
validation. No modifications to the original L32 or L35 APIs or to the web.
