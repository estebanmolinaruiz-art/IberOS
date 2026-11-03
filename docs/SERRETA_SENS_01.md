# SERRETA-SENS-01 · formal editorial-sensitivity test

This experimental module belongs to IberOS CORE's **non-promotional** test layer.
It does **not** translate Iberian or adjudicate disputed paleographic signs.

## Reproduce

From an installed editable IberOS checkout:

```bash
python -m pip install -e . pytest
python -m iberos.serreta_sensitivity --json /tmp/serreta-sens.json --csv /tmp/serreta-sens.csv
pytest -q tests/test_serreta_sensitivity.py
```

The eight scenarios use the prior Drive register's canonical order:
B2 `dai/darr` toggles fastest; B3 `gadenin/gadedin` next;
B4 `bidudenin/bidudedin` slowest. The B3 segment is
`sesdiŕ` + the chosen ending. Segment boundaries follow the
editorial witness rather than new paleographic investigation.

### Sources

- Velaza (2011), p. 85, as transcribed in Ngomo Fernández (2021),
  *Boletín del Archivo Epigráfico* 7, pp. 58–67.
- Silgo (2015), *Recerques del Museu d'Alcoi* 24, pp. 37–42.
  Its alternate transliteration conventions cannot be mistaken for
  independently observed signs.
- Master register: https://docs.google.com/spreadsheets/d/1R1LCYwly1hAGOhMM3TDVR4Jk_V7xuBWOxA4Nsslv3sg/edit

### Guards

- Source status stays D1. No D2/D3 claims.
- All eight alternatives belong to one physical object (PHYS_ID).
- The experiment calculates literal token occurrence counts only; suffix
  stability here is not a grammatical inference.
- Scientific CORE release metrics and validation gates remain untouched.
- No photo authorization or republication is implied.

This code extends, rather than replaces, the public IberOS v1.0.1 suite.
