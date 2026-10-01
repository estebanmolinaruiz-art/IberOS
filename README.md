# IberOS Open Research Kit v1.0

[![PyPI version](https://img.shields.io/pypi/v/iberos.svg)](https://pypi.org/project/iberos/)
[![GitHub release](https://img.shields.io/github/v/release/estebanmolinaruiz-art/IberOS)](https://github.com/estebanmolinaruiz-art/IberOS/releases)
[![Tests](https://github.com/estebanmolinaruiz-art/IberOS/actions/workflows/tests.yml/badge.svg)](https://github.com/estebanmolinaruiz-art/IberOS/actions/workflows/tests.yml)
[![License](https://img.shields.io/github/license/estebanmolinaruiz-art/IberOS)](https://github.com/estebanmolinaruiz-art/IberOS/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22939179.svg)](https://doi.org/10.5281/zenodo.22939179)
[![Software Heritage](https://archive.softwareheritage.org/badge/origin/https://github.com/estebanmolinaruiz-art/IberOS/)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/estebanmolinaruiz-art/IberOS)

**IberOS — created by Esteban Molina Ruiz**

IberOS is an independent, amateur research project focused on reproducible internal analysis of Iberian inscriptions.

This public kit is designed so that researchers, developers and comparable software can **inspect, validate, query and exchange IberOS results in machine-readable form**.

Primary project DOI: **10.5281/zenodo.22939179**

## Distribution

- **PyPI:** `pip install iberos`
- **GitHub Releases:** versioned source releases
- **GitHub Pages:** project documentation
- **Software Heritage:** archival request enabled on releases
- **Zenodo:** GitHub integration enabled for DOI-backed software archiving

## What this release contains

- a Python package and command-line interface (`iberos`);
- an open JSON exchange schema for IberOS result records;
- a curated registry of 38 IberOS objects;
- family/object links used by the project;
- a verified partial mapping to live Cathalaunia/Iberika `Ixxxxx` identifiers;
- representative machine-readable case examples;
- provenance and reproducibility rules;
- a static documentation site;
- GitHub Actions templates for testing, GitHub Pages, PyPI trusted publishing and Software Heritage archival.

## Important scientific scope

This kit exposes the **interoperability, benchmark, provenance and validation layer** of IberOS.

It does **not** claim that all historical/private IberOS analysis modules are fully reimplemented in this public v1.0 package. Results imported from prior IberOS releases are versioned and explicitly labelled.

The historical Beta Final V2 metrics refer to the legacy snapshot of **3,406 ENTRY**. They are not automatically metrics of the current live Cathalaunia/Iberika corpus.

## Quick start

```bash
pip install iberos
iberos version
iberos list-objects
iberos show-object IBR-PLM-0002
iberos family SALIR
iberos validate data/examples/tivissa.json
```

## Python API

```python
from iberos import load_registry, validate_result

objects = load_registry()
print(objects[0]["OBJECT_ID"])

ok, errors = validate_result("data/examples/tivissa.json")
print(ok, errors)
```

## Interoperability

The canonical result format is defined in:

`src/iberos/schema/iberos-result-v1.schema.json`

The intended exchange chain is:

`UPSTREAM_ID → ENTRY_ID → OBJECT_ID → LEAK_GROUP → READING → PALEO → SIMPLIFIED → MORPH → CLAIMS`

## Authorship and name

The official project name is **IberOS**.

Creator and primary maintainer: **Esteban Molina Ruiz**

Forks and derivatives should preserve attribution and clearly identify themselves as modified or unofficial.

See `NAME_AND_ATTRIBUTION_POLICY.md`.

## Licensing

- Original IberOS code: **Apache-2.0**
- Original IberOS documentation and original metadata: **CC BY 4.0**
- Third-party data, transcriptions, images and editions: retain their original terms and attribution.

The Apache license does not relicense external corpora.

See `LICENSE_POLICY.md` and `LICENSES/`.

## Cite

```text
Molina Ruiz, Esteban. IberOS: marco experimental para el análisis interno
y la validación reproducible de inscripciones ibéricas.
DOI: 10.5281/zenodo.22939179
```

Machine-readable citation metadata is in `CITATION.cff`.
