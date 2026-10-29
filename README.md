# IberOS Open Research Kit v1.0.1

**IberOS — creado por Esteban Molina Ruiz**

IberOS es un proyecto independiente de investigación orientado al análisis interno reproducible de inscripciones ibéricas. No se presenta como un desciframiento de la lengua ibérica.

## Referencias persistentes

- Informe técnico Zenodo, versión v1: **10.5281/zenodo.22939179**
- DOI conceptual del informe: **10.5281/zenodo.22939178**
- IberOS Case Studies I, versión v1: **10.5281/zenodo.22957236**
- DOI conceptual de Case Studies I: **10.5281/zenodo.22957235**
- Repositorio canónico: **estebanmolinaruiz-art/IberOS**
- Release de software actual en GitHub: **v1.0.1**
- Distribución pública actual en PyPI: **iberos 1.0.1**

Los DOI 22939179/22939178 corresponden al **informe técnico** y los DOI 22957236/22957235 a **IberOS Case Studies I**. El DOI conceptual del software se incorporará cuando pueda verificarse públicamente en Zenodo.

## Estado público — 2026-10-11

- GitHub: repositorio público, licencia Apache-2.0 y releases `v1.0.0` y `v1.0.1`.
- PyPI: `iberos 1.0.1` publicado mediante GitHub Actions / Trusted Publishing.
- Zenodo software: depósito preparado; el identificador `10.5281/zenodo.22997623` no resuelve públicamente y se trata como reservado / pendiente de publicación hasta nueva verificación.
- Zenodo: informe técnico v1 publicado como **Report** en DOI 10.5281/zenodo.22939179.
- Zenodo: **IberOS Case Studies I** publicado como **Data paper** en DOI 10.5281/zenodo.22957236.
- GitHub Pages: sitio público verificado externamente el 2026-10-11; portada y rutas principales accesibles, con 3 DOI públicos reflejados y el software v1.0.1 incluido en Recursos.
- Software Heritage: origen reconocido con SWHID `swh:1:ori:f6fe971ad750db06a1531a232d2f9213677138cc`; la confirmación de una visita/snapshot archivado completo sigue pendiente.
- Benchmark: protocolo reproducible publicado en `docs/BENCHMARK.md`; snapshot v1.0.1 en `data/benchmark/benchmark_results_v1.0.1.json`; workflow de verificación completado con éxito en GitHub Actions run `38158963423`.

## Instalación

```bash
python -m pip install iberos==1.0.1
iberos --help
```

PyPI publica los artefactos `iberos-1.0.1-py3-none-any.whl` y `iberos-1.0.1.tar.gz`. La instalación limpia desde PyPI y la ejecución de `iberos --help` se verificaron correctamente en un runner independiente de GitHub Actions (run 38158352028, 2026-10-11).

## Método científico

IberOS mantiene separadas las capas:

`EVIDENCE → INFERENCE → HYPOTHESIS → ESTIMATED TRANSLATION`

También controla la identidad documental y física:

`ENTRY → PHYS_ID / OBJECT_ID → LEAK_GROUP → TRAIN / VAL / HOLD`

## Componentes

- Paquete Python y CLI (`iberos`).
- Esquema JSON de intercambio.
- Registro curado de 38 objetos.
- Enlaces de familias y procedencia.
- Mapeo parcial a identificadores Cathalaunia / Corpus Ibèrika.
- GitHub Pages e IberOS Web Engine.
- IberOS-Write.
- Workflows de tests y publicación.

## Arquitectura y documentación

La arquitectura completa del sistema, los módulos, los datos, los workflows, la publicación y la reproducibilidad se describen en [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Fuentes y trazabilidad documental

Registro comprobado el 08-10-2026: [publicaciones y fuentes de la tesis](docs/INTERNET_REGISTRY_2026-10-08.md).

Sincronización transversal vigente: [FORMULAICITY-STRATA-01 (2026-10-16)](docs/CROSS_THREAD_SYNC_2026-10-16_FORMULAICITY.md). Se aplica como candidato metodológico no promocional a Motor/Validation, D(E/I), KUTUR, Write, Talk, tesis y La Picola.

Incluye Corpus Ibèrika, el dataset paleohispánico de 2026 y la revisión de Villares V de Ferrer i Jané (2024). Las fuentes externas requieren concordancias y controles de independencia antes de incorporarse a una validación.

La sincronización documental mantiene C594/C474/C539/C541; no cambia resultados científicos ni métricas. El programa se distribuye bajo Apache-2.0; el informe y los Case Studies en Zenodo se publican bajo CC BY 4.0.

## Preparación para EpiHub

El estado verificable y los bloqueos de reevaluación se mantienen en [EPIHUB_READINESS.md](EPIHUB_READINESS.md). No se marcará un requisito como cumplido sin evidencia pública comprobable.

## Citas

Software:

Molina Ruiz, Esteban. *IberOS Open Research Kit v1.0.1*. Software release; Zenodo DOI pendiente de publicación/verificación pública.

Informe técnico:

Molina Ruiz, Esteban. *IberOS: marco experimental para el análisis interno y la validación reproducible de inscripciones ibéricas*. DOI: 10.5281/zenodo.22939179

Casos de estudio:

Molina Ruiz, Esteban. *IberOS Case Studies I: cuatro fichas analíticas de validación en epigrafía ibérica*. DOI: 10.5281/zenodo.22957236

## Descubrir y compartir IberOS (acceso gratuito)

- **Explorar la web:** https://estebanmolinaruiz-art.github.io/IberOS/
- **Consultar el corpus:** https://estebanmolinaruiz-art.github.io/IberOS/corpus/
- **Consultar fichas:** https://estebanmolinaruiz-art.github.io/IberOS/fichas/
- **Instalar el paquete Python:** https://pypi.org/project/iberos/
- **Dataset / perfil en Hugging Face:** https://huggingface.co/EstebanMR
- **Consultar metodología y límites:** [Arquitectura](docs/ARCHITECTURE.md) y [benchmark](docs/BENCHMARK.md).
- **Leer el informe técnico:** https://doi.org/10.5281/zenodo.22939179
- **Consultar casos de estudio:** https://doi.org/10.5281/zenodo.22957236
- **Material de difusión reutilizable:** [kit de difusión gratuito](docs/DIFUSION_GRATUITA.md).

IberOS es un **marco experimental de análisis y validación reproducible**, no un desciframiento demostrado del ibérico. Las hipótesis, inferencias y lecturas documentadas se mantienen diferenciadas. La participación y la revisión crítica son bienvenidas.
