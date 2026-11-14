# IberOS-ASSOC-02 · Refuerzo documental del Core

Status: **EXPERIMENTAL / DOCUMENTARY ONLY** (2026-11-14). No change to `src/iberos/core.py`, C594/C474/C539/C541, FULL3406 or official metrics. Zero additional cost.

This module **reuses**:
- 26 labelled graphical variants exposed by `site/write/index.html`;
- 286 external signary candidates in `data/review/cathalaunia_signary_review_queue_286_v2.csv`, including 133 simple source labels (not independently validated);
- the physical-token/editorial alignment records for Orleyl in `data/curated/rok_orleyl_editorial_alignment_1981.csv`.

It outputs per-row **candidate documentary links** with provenance and source file hashes. An assigned Latin conventional value is neither a semantic translation nor a completed photographic OCR result. Every proposed link remains `usable_for_auto_reading=false`.

Run offline:

```bash
python research/core_association/bridge.py --root . --output /tmp/iberos-assoc-02.json
python -m unittest discover -s research/core_association -p 'test_*.py' -v
```

Next stage (not yet implemented): crop local original archaeological photograph images with correct PHYS_ID and licensing, keep source and expert reading independently, align crop to sign value **after inspection**, and train/evaluate on strictly physically disjoint objects. For glyph vs word vs non-linguistic mark research, register separately predeclared competing hypotheses and HOLD-set predictions. Never auto-promote matches to semantic conclusions. This bridge does not assume logography or substitute reconstructed glyphs for original images.
