# IberOS Open Research Kit v1.0.1

**IberOS — creado por Esteban Molina Ruiz**

IberOS es un proyecto independiente de investigación orientado al análisis interno reproducible de inscripciones ibéricas. No se presenta como un desciframiento de la lengua ibérica.

## Referencias persistentes

- Informe técnico publicado en Zenodo: **10.5281/zenodo.22939179**
- DOI conceptual del informe: **10.5281/zenodo.22939178**
- Repositorio canónico: **estebanmolinaruiz-art/IberOS**
- Release de software actual en GitHub: **v1.0.1**

Los DOI anteriores corresponden al **informe técnico**. No deben presentarse como DOI de una release del software. El DOI específico del software se considerará demostrado únicamente cuando exista y pueda verificarse públicamente.

## Estado público verificado — 2026-10-11

- GitHub: repositorio público, licencia Apache-2.0 y releases `v1.0.0` y `v1.0.1`.
- PyPI: existe el paquete público `iberos`. La última versión verificada externamente es **1.0.0**; la publicación y verificación de **1.0.1** sigue pendiente.
- GitHub Pages: la infraestructura de Pages está habilitada y el repositorio contiene documentación y herramientas web. La estabilidad pública del sitio debe comprobarse antes de presentarla como requisito EpiHub cumplido.
- Zenodo: informe técnico publicado con DOI de versión **10.5281/zenodo.22939179** y DOI conceptual **10.5281/zenodo.22939178**.
- Software Heritage: existe workflow de solicitud de archivado; queda pendiente registrar el SWHID verificable.
- Benchmark: 38 objetos curados en el repositorio público; falta presentar sus resultados como benchmark reproducible cerrado.
- Hugging Face: repositorio de dataset creado; su carga, licencia, Dataset Card y Viewer deben verificarse antes de citarlo como distribución final.
- Fichas PDF: paquete preparado; la publicación y comprobación de enlaces siguen pendientes.

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
- Fichas PDF preparadas para integración web.

## Fuentes y trazabilidad documental

Registro comprobado el 08-10-2026: [publicaciones y fuentes de la tesis](docs/INTERNET_REGISTRY_2026-10-08.md).

Incluye Corpus Ibèrika, el dataset paleohispánico de 2026 y la revisión de Villares V de Ferrer i Jané (2024). Las fuentes externas requieren concordancias y controles de independencia antes de incorporarse a una validación.

La sincronización documental mantiene C594/C474/C539/C541; no cambia resultados científicos ni métricas. El programa se distribuye bajo Apache-2.0 y el informe de Zenodo bajo CC BY 4.0.

## Preparación para EpiHub

El estado verificable y los bloqueos de reevaluación se mantienen en [EPIHUB_READINESS.md](EPIHUB_READINESS.md). No se marcará un requisito como cumplido sin evidencia pública comprobable.

## Cita del informe técnico

Molina Ruiz, Esteban. *IberOS: marco experimental para el análisis interno y la validación reproducible de inscripciones ibéricas*. DOI: 10.5281/zenodo.22939179
