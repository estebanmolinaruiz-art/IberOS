# IberOS — EpiHub Readiness

Actualizado: 2026-10-11

Este documento traduce los criterios comunicados por EpiHub en entregables verificables. IberOS no declarará un requisito como cumplido mientras la evidencia pública correspondiente no pueda comprobarse.

| Criterio | Evidencia mínima | Estado | Evidencia actual | Bloqueo |
|---|---|---|---|---|
| Sitio web dedicado estable | URL pública estable, navegación y páginas de proyecto/documentación/research/contacto | 🟢 | GitHub Pages verificada externamente; portada y rutas principales responden; Recursos publica el DOI de software y la portada refleja 3 DOI | Ninguno crítico |
| Estructura clara de software | Repositorio público, estructura, licencia, versión, instalación y tests | 🟢 | GitHub público; src/, tests/, docs/, data/, Apache-2.0, releases v1.0.0/v1.0.1 | Ninguno crítico |
| Distribución reproducible | PyPI alineado con la release y artefactos publicados | 🟢 | PyPI publica iberos 1.0.1, wheel y sdist; Trusted Publishing verificado; instalación limpia y CLI verificadas en GitHub Actions run 38158352028 | Ninguno crítico |
| Persistencia académica | Publicaciones citables con DOI y relación clara | 🟢 | Informe 10.5281/zenodo.22939179 + Case Studies I 10.5281/zenodo.22957236 | Ninguno crítico |
| Persistencia del software | DOI específico de la release de software | 🟢 | IberOS Open Research Kit v1.0.1: 10.5281/zenodo.22997623 | Verificar DOI conceptual cuando sea públicamente resoluble |
| Documentación técnica | README, instalación, arquitectura, API/CLI, ejemplos y límites | 🟠 | README, docs/, workflows y componentes | Consolidar entrada única y arquitectura |
| Marco académico | Documento metodológico citable, fuentes y posición epistemológica | 🟢 | Informe técnico, Case Studies I, software con DOI diferenciado y benchmark reproducible público | Ninguno crítico |
| Benchmark | Corpus curado + protocolo + resultados reproducibles + negativos | 🟢 | 38 objetos; 37 unidades independientes; snapshot v1.0.1; controles negativos; workflow `38158963423` reproducido con éxito | Ninguno crítico |
| Trazabilidad | Versiones, autores, licencias, checksums y procedencia | 🟢 | CITATION.cff, AUTHORS.md, LICENSE, MANIFEST_SHA256, políticas | Mantener sincronización |
| Archivo duradero | Zenodo + Software Heritage | 🟢/🟠 | Publicaciones y software en Zenodo; workflow SWH | Recuperar SWHID |

## Evidencia Zenodo

### Informe técnico
- Título: **IberOS: marco experimental para el análisis interno y la validación reproducible de inscripciones ibéricas**
- DOI versión: **10.5281/zenodo.22939179**
- DOI conceptual: **10.5281/zenodo.22939178**
- Tipo: **Report**
- Publicación: **24-09-2026**

### Case Studies I
- Título: **IberOS Case Studies I: cuatro fichas analíticas de validación en epigrafía ibérica**
- DOI versión: **10.5281/zenodo.22957236**
- DOI conceptual: **10.5281/zenodo.22957235**
- Tipo: **Data paper**
- Publicación: **25-09-2026**

### Software
- Título: **IberOS Open Research Kit v1.0.1**
- DOI de versión: **10.5281/zenodo.22997623**
- Tipo: **Software**
- DOI conceptual: pendiente de verificación pública.

## Condición de reenvío a EpiHub

IberOS reúne ya los entregables mínimos que se habían identificado para solicitar una nueva reevaluación de EpiHub: sitio web público estable, estructura de software verificable, distribución PyPI probada externamente, DOI específico del software, marco académico citable y benchmark reproducible con resultados, negativos y límites.

El SWHID sigue pendiente como mejora de archivo duradero, pero no se presenta como requisito ya exigido por EpiHub. La formulación prudente pasa de **“preparación avanzada para reevaluación”** a **“lista para solicitar reevaluación, sujeta a valoración externa de EpiHub”**.
