# Experimental editorial quantity normalizer (L30)

`src/iberos/editorial_quantity_normalizer.py` is a **non-default** experimental module
from IberOS Laboratories 26–30. This integration does **not** change the core
semantic engine, official benchmark figures, or public translation outputs.

## Use

```python
from iberos.editorial_quantity_normalizer import extract, classify

extract("ki6 ka:III eΠ I")
classify("ki6 ka:III eΠ I")
```

`extract` returns original text offsets, raw substrings, editorial unit,
separators, editorial digit/stroke strings, annotations and uncertainty flags.
`classify` returns editorial-pattern flags, **not** an object's documented
function, a decoded number or a translation.

Important distinctions:
- `unit_digits`: digits are present in the edition, **not measured physical quantities**.
- `unit_strokes`: editorial `I` strokes, not validated numerical equivalences.
- `unit_mixed_strokes_unresolved`, `e_complex_unresolved`: uncertain.
- `abstain`: no supported determination.
- `original_signs_verified` and `numerical_value_verified` always remain false.

## Reproducibility

```bash
python -m unittest tests.test_editorial_quantity_normalizer -v
```

Six regression and negative checks are included. Bastida I, Casinos,
Coimbra, El Cigarralejo, Los Villares and Pico de los Ajos are development
or diagnostic sources and cannot be used as independent external L30 tests.
Prospective, site-reserved evaluation remains **pending**. This module
must not be used to raise semantic accuracy or decipherment claims.

Source: IberOS Laboratory 30, 2026-11-10. See archaeological editions
and source provenance in the original Laboratory 30 package.
