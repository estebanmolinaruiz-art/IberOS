# HOLD-01: evaluation packet without leakage or invented gold labels

HOLD-01 reserves two independent **candidate** objects not found by name
in the 38-object curated list: Xàbia Fundació CIRNE lead (Ferrer i Jané
et al., 2022, DOI 10.3989/aespa.095.022.07) and the La Mesa lead
(Luján & López Fernández, PalHisp 17, DOI 10.36707/palaeohispanica.v0i17.136).

Their exact corpus concordances, full editions, physical provenance, and
overlap with historical IberOS training data (3,406 legacy ENTRY) still require
independent audit. They are **not** certified prospective HOLD items.
Do not import them into training before a preregistered split audit.

Two attractive mosaic controls (Caminreal, Andelo) are **explicitly
excluded** because they already occur in the 38-object curated registry
as IBR-MUS-0001 and IBR-MUS-0002, respectively.

The command generates a blind packet without texts or source links, plus a
separate traceable inventory in this document and code. It does not produce
labels or a semantic prediction, so accuracy is null rather than zero.

```bash
python -m iberos.holdout_01 --json /tmp/hold-01.json
pytest -q tests/test_holdout_01.py
```

Before a **true** blind assessment: verify external identifiers, cross-check
all legacy and curated occurrences, freeze predictions in a new immutable
commit before revealing any independent reference labels, and only evaluate
functions with defensible gold evidence. No such gold has been established
for these two inscriptions as of 2026-11-03.

Source details:
- Ferrer i Jané et al. (2022), *Archivo Español de Arqueología* 95,
  https://doi.org/10.3989/aespa.095.022.07
- Luján & López Fernández (2017), *Palaeohispanica* 17, 125-139,
  https://doi.org/10.36707/palaeohispanica.v0i17.136
- Master register:
  https://docs.google.com/spreadsheets/d/1R1LCYwly1hAGOhMM3TDVR4Jk_V7xuBWOxA4Nsslv3sg/edit
