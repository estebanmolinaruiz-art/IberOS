# ADVERSARIAL-01 · five-case epistemic guard

This module converts the five rows of IberOS master register
**Adversarial 01 controles** into deterministic automated checks.
It tests *failure modes of suffix matching*, not grammar classification.

## Run

```bash
python -m pip install -e . pytest
python -m iberos.adversarial_01 --json /tmp/adversarial-01.json
pytest -q tests/test_adversarial_01.py
```

## Five cases

- ADV-01 Orleyl V F.9.5: `biteroketetine`; same contextual group as VII.
- ADV-02 Orleyl VII F.9.7: `basbiteroketine`; segmentation disputed.
- ADV-03 Azaila TE.02.308 = E.1.308 = AZ.330:
  `baśtaŕtine`; potential proper name + `-e`, NOT a gold label.
- ADV-04 Pico de los Ajos III F.20.3: cited `bitarsteti`,
  potentially continued, NOT a secure suffix.
- ADV-05 La Serreta I A.04.01: `bidudenin / bidudedin`;
  only one editorial variant is entered as a baseline and both remain open.

## What passes

All five controls must **abstain** from grammatical assignment despite a
suffix-only heuristic matching every transcription. A deterministic test
asserts physical objects = 5 while contextual leak groups = 4: Orleyl V
and VII share a find context, though they remain physically different.

We run two separate audits because the existing CORE `independence_key`
prioritizes `PHYS_ID` over `LEAK_GROUP`. A physical audit alone would
incorrectly imply contextual independence; the second audit is mandatory.

## Limits

- D1 editorial sources only; no epigraphic D2/D3 visual review.
- No independent gold grammatical annotations; therefore NO classifier
  accuracy or semantic validation can be computed.
- Editorial typology (onomastic/formulaic) is a competing hypothesis, not
  a supervised training label.
- No change to scientific CORE metrics, no automatic release promotion.
- No new model training is claimed.

Sources: Fletcher (1981) *Materiales de la necrópolis ibérica de Orleyl*;
Ngomo Fernández (2021) on La Serreta; Silgo (2015);
López Fernández (2025) on the Azaila amphora;
IberOS master register:
https://docs.google.com/spreadsheets/d/1R1LCYwly1hAGOhMM3TDVR4Jk_V7xuBWOxA4Nsslv3sg/edit
