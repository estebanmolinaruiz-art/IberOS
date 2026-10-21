# IberOS — M06 executable evidence gate

This engineering change preserves C594, C474, C539 and C541. M06 remains PENDING; no scientific promotion is authorized.

The pipeline now checks M06 explicitly. DONE requires exactly the 17 registered sign identities in `data/review/validation01_m06_evidence_v1.json`, key `signs`. Each record must supply object_id, editorial_word, index, status=REVIEWED, editorial_key_hidden=true, bbox (source-image coordinates), reviewer, review_record, variant_id, signary_reference, discrepancy_notes and source/crop/review paths with SHA256 hashes. Paths must resolve inside the repository. Pending or missing evidence blocks. No real manifest is fabricated by this change.

These checks establish reference integrity, not the truth of a reading, reviewer independence, bounding-box correctness or adequacy of an image. M07 remains separate. Synthetic fixtures are only software controls and never enter research data.

Reproduce with:

    python -m pytest -q tests/test_validation01_m06_gate.py tests/test_validation01_pipeline.py tests/test_validation01_readiness.py tests/test_validation01_blind_score.py tests/test_validation01_hold_leakage_guard.py
    python scripts/validation01_pipeline.py --require-ready

On the current corpus, the second command must print BLOCKED / NOT_EVALUATED and exit 2. Without --require-ready the historical diagnostic exit behavior is preserved; existing CI remains diagnostic. Use the strict option only where scientific readiness is explicitly required, not to equate a software test pass with scientific approval.

Local verification: 12 test functions executed directly using Python runpy (pytest unavailable), including synthetic positive reference-integrity control and adversarial mutations; all passed. Strict CLI exit 2 verified. Full CI, browser checks and frozen benchmark were not run.

IberOS — engineering audit, 21 October 2026.
