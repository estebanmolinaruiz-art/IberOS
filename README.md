# IberOS Open Research Kit v1.0.1

[![PyPI version](https://img.shields.io/pypi/v/iberos.svg)](https://pypi.org/project/iberos/)
[![GitHub release](https://img.shields.io/github/v/release/estebanmolinaruiz-art/IberOS)](https://github.com/estebanmolinaruiz-art/IberOS/releases)
[![Tests](https://github.com/estebanmolinaruiz-art/IberOS/actions/workflows/tests.yml/badge.svg)](https://github.com/estebanmolinaruiz-art/IberOS/actions/workflows/tests.yml)
[![License](https://img.shields.io/github/license/estebanmolinaruiz-art/IberOS)](https://github.com/estebanmolinaruiz-art/IberOS/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22939179.svg)](https://doi.org/10.5281/zenodo.22939179)
[![Software Heritage](https://archive.softwareheritage.org/badge/origin/https://github.com/estebanmolinaruiz-art/IberOS/)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/estebanmolinaruiz-art/IberOS)

**IberOS — created by Esteban Molina Ruiz**

IberOS is an independent research project for reproducible internal analysis of Iberian inscriptions. The public kit exposes interoperable data structures, validation rules, curated objects, examples and lightweight web adapters.

Primary project DOI: **10.5281/zenodo.22939179**

## Scientific method

IberOS keeps four epistemic layers separate:

`EVIDENCE → INFERENCE → HYPOTHESIS → ESTIMATED TRANSLATION`

A narrower interpretation is never promoted merely because it fits the corpus. Promotion requires independent support, adversarial controls and explicit falsifiers.

The project also uses physical/documentary identity controls:

`ENTRY → PHYS_ID / OBJECT_ID → LEAK_GROUP → TRAIN / VAL / HOLD`

This prevents multiple editions, faces or readings of the same physical object from being counted as independent confirmations.

## Validation discipline

- E1–E5 evidence grading.
- PHYS_ID / OBJECT_ID documentary hygiene.
- Leakage-aware TRAIN / VAL / HOLD splits.
- Negative controls and non-regression tests.
- Prospective and blind tests where possible.
- Paleography preserved separately from simplified linguistic forms.
- External corpora and sister systems enter as **candidate evidence**, never as automatic CORE updates.

The current public web adapters consume the frozen scientific authority chain:

- semantic release: **C594**
- prospective lock: **C474**
- technical floor: **C539**
- ŔOK network: **C541**

Official validation indicators in that snapshot include ICS global **70.8%**. These are validation indicators, **not a percentage of the Iberian language deciphered**.

## Public components

- Python package and CLI (`iberos`).
- JSON exchange schema.
- Curated registry of 38 object-level records.
- Family/object links and provenance.
- Partial mapping to Cathalaunia/Corpus Ibèrika identifiers.
- GitHub Pages documentation.
- **IberOS Web Engine 1.0.1-web.2**.
- **IberOS-Write WRITE-GRAMMAR v0.3-web.2**.
- Automated tests and publication workflows.

## Quick start

```bash
pip install iberos
iberos version
iberos list-objects
iberos show-object IBR-PLM-0002
iberos family SALIR
iberos validate data/examples/tivissa.json
```

## Interoperability

Canonical result schema:

`src/iberos/schema/iberos-result-v1.schema.json`

Exchange chain:

`UPSTREAM_ID → ENTRY_ID → OBJECT_ID → LEAK_GROUP → READING → PALEO → SIMPLIFIED → MORPH → CLAIMS`

## Web tools

GitHub Pages exposes:

- `/webengine/` — query the public IberOS registry in-browser.
- `/write/` — conservative IberOS-Write adapter with controlled abstention.

IberOS-Write does not invent missing Iberian vocabulary. Unsupported semantic frames return controlled abstention, and reconstructed/probable/fallback layers remain distinct.

## Authorship and licensing

Creator and primary maintainer: **Esteban Molina Ruiz**

- Original IberOS code: **Apache-2.0**
- Original IberOS documentation and original metadata: **CC BY 4.0**
- Third-party data, transcriptions, images and editions retain their original terms and attribution.

See `LICENSE_POLICY.md`, `LICENSES/` and `NAME_AND_ATTRIBUTION_POLICY.md`.

## Cite

```text
Molina Ruiz, Esteban. IberOS: marco experimental para el análisis interno
y la validación reproducible de inscripciones ibéricas.
DOI: 10.5281/zenodo.22939179
```

Machine-readable citation metadata is in `CITATION.cff`.
