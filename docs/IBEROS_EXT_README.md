# IberOS-EXT v0.1 — experimental, isolated

**Scope:** auxiliary evidence tools only. Never import or mutate IberOS Core, C439, C474, C539, C541, C594, TRAIN/VAL/HOLD, readings, morphology, semantics or official metrics.

## Modules
- FALSIFY: group-level leakage audit and prospective gate (implemented minimal functions).
- VISION: photo/drawing provenance manifest (implemented; image recognition not yet integrated).
- NETWORK: metadata/physical identity crosswalk (planned).
- RESTORE: damaged inscription proposals (planned; no pretrained Greek model on Iberian).
- LINK: EpiDoc/TEI export and corpus mapping (planned).
- METHOD: registry of external research approaches (documented only).

## External methods, not vendored or claimed as installed
- Kraken/eScriptorium: https://github.com/mittagessen/kraken ; https://gitlab.com/scripta/escriptorium
- EpiDoc/TEI: https://epidoc.stoa.org/ ; https://tei-c.org/
- Ithaca: https://github.com/deepmind/ithaca
- openEtruscan / Indus workbenches: evaluate provenance, licenses and reproducibility before dependency integration.

## C474 PROSPECTIVE LOCK
Any post-2026-09-27 observation must be matched to the literal frozen prediction **before** detailed linguistic interpretation. Record source, publication date, version, PHYS_ID, LEAK_GROUP, independence, contamination, falsifiable prediction, controls and outcome. Missing fields -> INDETERMINATE. A proposed FAIL remains visible and cannot be rescued through post-hoc segmentation. The automated gate deliberately never certifies STRICT_PROSPECTIVE_PASS or FAIL: independent manual verification is mandatory.

## Running
`python -m pytest tests/test_iberos_ext.py` (requires pytest). No network, model training, or writes to Core. No changes to official metrics.

IberOS — scientific auxiliary tooling. Experimental status; not a validated decipherment.
