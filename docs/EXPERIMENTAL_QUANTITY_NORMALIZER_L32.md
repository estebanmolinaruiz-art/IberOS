# L32 — embedded numeraliform candidate guard

The L31 retrospective external excerpt `abaoIIII` (Orleyl) was a missed pattern by L30 due to a strict left-hand word boundary.

L32 **only flags**, as `embedded_unit_strokes_unresolved`, a narrow terminal pattern of lowercase text immediately followed by `o` and at least two editorial `I` strokes: `abaoIIII` -> `oIIII`. The evidence preserves literal offsets and both numeric-verification booleans remain false. `classify` **abstains** for this case, not a confirmed metrological detection.

The gate rejects `bekaI`, `aoI`, `aoIIIIz`. Prior L30 regressions remain unchanged.

**Research integrity:** Orleyl is now development data, not an independent L32 test. The L31 frozen result remains a false negative for L30. Even when tests pass, this narrow fix is not a general solution to word-attached quantities. Future complete-object, site-reserved prospective validation is required. Official semantic metrics and public translations remain unchanged.

Run `python -m unittest tests.test_editorial_quantity_normalizer -v` under the repository environment. No paid service needed.
