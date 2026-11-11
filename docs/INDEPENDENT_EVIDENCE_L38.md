# L38 independent evidence registry: research gate

This **opt-in** module audits whether documentary fields are populated.
It is **not** an authentication process: even a complete self-declared
record cannot create `FAMILY_CONFIRMED`.

Four documentary candidates inspected at D1 level in the local Lab 38
artifact: Casinos MALL.780, Vieille-Toulouse HGA.01.01, T.06.09,
and Ensérune HER.02.033. Zero physical objects independently reread
from original images during L38; all four remain unconfirmed.

Selected bibliographic leads:
- Ferrer i Jané & Escrivà, *Un plomo ibérico de Casinos*, *Palaeohispanica* 14 (2014), DOI 10.36707/palaeohispanica.v0i14.54.
- Ferrer i Jané, *Annorum vinum*, *Quad. Preh. Arq. Cast.* 41 (2024), https://dialnet.unirioja.es/descarga/articulo/9844117.pdf.
- Secondary corpus Nacryos/ancient-scripts-datasets, iberian.csv, git blob d306bed1a16086a979c9724d4fdaeea4efa93a89.

Source entries in published literature are **not independent IberOS D2 readings**.
The original image link, blind reading, context/date anchors and independent
review remain essential. Metadata must not promote itself.

Usage: `from iberos.independent_evidence_registry_l38 import audit, evaluate_csv`
Tests: `python -m unittest tests.test_independent_evidence_registry_l38 -v`

No edits to L32/L35/L37, semantic metrics, public site or translations.
