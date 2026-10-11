# IberOS — Architecture and Documentation Map

Version: 1.0.1  
Updated: 2026-10-11

## Purpose

IberOS is an independent research-software framework for reproducible analysis, comparison, provenance control and hypothesis testing in Iberian epigraphy.

It does not claim a definitive decipherment of the Iberian language.

The project keeps four epistemic layers separate:

`EVIDENCE → INFERENCE → HYPOTHESIS → ESTIMATED TRANSLATION`

## System overview

IberOS is organized into five connected layers:

1. **Curated research data**
2. **Research core and validation guards**
3. **Command-line and reusable software interfaces**
4. **Public web interface**
5. **Persistence, publication and reproducibility infrastructure**

## 1. Curated research data

Canonical public data:

- `data/curated/iberos_objects_registry_v2.0.csv`
- `data/curated/iberos_curated_objects_v1.jsonl`
- `data/curated/iberos_family_links_v2.0.csv`
- `data/curated/iberos_partial_entry_link_v2.4.csv`
- `data/examples/`

The public curated layer contains 38 objects.

Documentary independence follows:

`PHYS_ID > LEAK_GROUP > specific Dependency_Group > OBJECT_ID`

This prevents duplicated editions, copies or shared physical objects from being counted as independent confirmations.

## 2. Research core

Main implementation:

- `src/iberos/core.py`
- `src/iberos/schema/iberos-result-v1.schema.json`

The core provides:

- object registry access;
- family lookup;
- JSON result validation;
- documentary-independence audit;
- split-leakage controls;
- evidence de-duplication;
- semantic guards;
- prospective gates;
- family dashboards;
- negative/adversarial controls.

Scientific authority is frozen through the current release chain:

- semantic release: `C594`
- prospective lock: `C474`
- technical floor: `C539`
- ROK network: `C541`

No technical test automatically promotes a scientific claim to CORE.

## 3. CLI and package interface

Public package:

`iberos==1.0.1`

Installation:

```bash
python -m pip install iberos==1.0.1
```

Main CLI entry point:

```bash
iberos --help
```

Important commands include:

- `iberos status`
- `iberos list-objects`
- `iberos show-object <OBJECT_ID>`
- `iberos family <FAMILY>`
- `iberos validate <json_file>`
- `iberos audit-independence`
- `iberos dashboard`
- `iberos bottlenecks`
- `iberos rok-recipient-matrix`
- `iberos ka-direction-matrix`
- `iberos salir-prospective-matrix`
- `iberos kutur-prospective-matrix`
- `iberos baides-batir-matrix`
- `iberos numeral-789-dashboard`
- `iberos dedi-orthogonal-matrix`

The clean external installation and CLI check were verified successfully in GitHub Actions run `38158352028`.

## 4. Public web interface

Public site:

https://estebanmolinaruiz-art.github.io/IberOS/

Main public areas:

- Corpus
- Atlas
- Fichas
- Laboratorio
- Arqueología 3D
- Recursos
- Casos de estudio
- Comunidad
- Contactar
- Acerca de

The site is deployed from `site/` using GitHub Pages.

The public web layer is a research interface over the curated material. It must not be treated as a substitute for the canonical data and software sources in `data/` and `src/`.

## 5. Reproducibility and benchmark

Canonical benchmark documentation:

- `docs/BENCHMARK.md`
- `data/benchmark/benchmark_results_v1.0.1.json`
- `scripts/benchmark_snapshot.py`
- `.github/workflows/benchmark.yml`

The benchmark verifies:

- curated object count;
- independent documentary units;
- negative/excluded controls;
- preservation of open scientific gates;
- frozen release indicators;
- exact regeneration of the versioned machine-readable snapshot.

Verified GitHub Actions benchmark run:

`38158963423`

Current public benchmark snapshot:

- 38 curated objects;
- 37 independent documentary units;
- 4 excluded controls;
- no automatic CORE promotion;
- open gates remain explicitly open where evidence is insufficient.

## Testing

Automated tests:

- `tests/test_core.py`
- `.github/workflows/tests.yml`

The suite covers:

- registry integrity;
- schema validation;
- independence and leakage;
- split resolution;
- family gates;
- prospective controls;
- negative and adversarial cases;
- non-promotion rules.

## Documentation map

### Entry points

- `README.md` — project overview, installation, citation and public status.
- `docs/ARCHITECTURE.md` — this system map.
- `docs/BENCHMARK.md` — reproducible benchmark protocol.
- `docs/INTEROPERABILITY.md` — identifiers, evidence levels and interchange model.
- `PUBLISHING_CHECKLIST.md` — publication and release verification.
- `EPIHUB_READINESS.md` — EpiHub-specific readiness evidence.

### Scientific control documents

- `docs/PHYS_LEAK_SAFE_ENGINE_2026-10-08.md`
- `docs/EVIDENCE_INDEPENDENCE_GATE_2026-10-08.md`
- `docs/FAMILY_GATE_01_2026-10-08.md`
- `docs/FAMILY_DASHBOARD_01_2026-10-08.md`
- `docs/ROK_RECIPIENT_MATRIX_2026-10-08.md`
- `docs/KA_DIRECTION_MATRIX_2026-10-08.md`
- `docs/SALIR_PROSPECTIVE_MATRIX_2026-10-08.md`
- `docs/KUTUR_PROSPECTIVE_MATRIX_2026-10-08.md`
- `docs/BAIDES_BATIR_ROLE_MATRIX_2026-10-08.md`
- `docs/NUM_789_AUDIT_2026-10-08.md`
- `docs/NUM_789_EXACT_VALUE_GATES_2026-10-08.md`
- `docs/DEDI_ORTHOGONAL_MATRIX_2026-10-08.md`

## Publication and persistence

### Software

- GitHub release: `v1.0.1`
- PyPI: `iberos 1.0.1`
- Zenodo software DOI: `10.5281/zenodo.22997623`

### Research outputs

- Technical report DOI: `10.5281/zenodo.22939179`
- Case Studies I DOI: `10.5281/zenodo.22957236`

### Software Heritage

A Software Heritage archiving workflow exists. The final public SWHID remains to be recorded when verified.

## Release workflow

The intended release chain is:

`source → tests → release → PyPI → Zenodo → public documentation`

Supporting workflows:

- `.github/workflows/tests.yml`
- `.github/workflows/benchmark.yml`
- `.github/workflows/pypi.yml`
- `.github/workflows/pages.yml`
- `.github/workflows/software-heritage.yml`
- `.github/workflows/verify-pypi-install.yml`

## Scientific limits

IberOS explicitly does not claim:

- full ingestion of the living Iberian epigraphic corpus;
- complete decipherment of Iberian;
- gold-standard free translation accuracy;
- automatic scientific validity from software tests;
- independence where PHYS/LEAK controls do not support it.

Any scientific state change requires an explicit, versioned research decision and supporting evidence.

## Canonical chain

For v1.0.1 the public technical chain is:

`GitHub v1.0.1 = PyPI 1.0.1 = CITATION.cff 1.0.1 = Zenodo software v1.0.1`

This document is the canonical map for how IberOS software, data, documentation, validation and publication components fit together.
