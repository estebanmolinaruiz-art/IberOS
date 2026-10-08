# IberOS Open Research Kit v1.0.1

**IberOS — creado por Esteban Molina Ruiz**

IberOS es un proyecto independiente de investigación orientado al análisis interno reproducible de inscripciones ibéricas. No se presenta como un desciframiento de la lengua ibérica.

DOI principal del informe técnico: **10.5281/zenodo.22939179**

## Estado público verificado

- GitHub: repositorio público y releases `v1.0.0` y `v1.0.1`.
- PyPI: paquete `iberos` instalable con `pip install iberos`; la API pública indica **1.0.0** como última versión a 08-10-2026. GitHub publica v1.0.1; queda pendiente alinear la distribución PyPI.
- GitHub Pages: documentación y herramientas web públicas.
- Zenodo: informe técnico publicado el 24-09-2026, DOI de versión **10.5281/zenodo.22939179**, DOI de concepto **10.5281/zenodo.22939178**, licencia CC BY 4.0. Estos DOI corresponden al informe; no identifican una release del programa.
- Software Heritage: workflow de solicitud de archivado ejecutado correctamente.
- Benchmark: 38 objetos curados en el repositorio público.
- Hugging Face: repositorio de dataset creado; la carga y validación completa del contenido debe comprobarse antes de presentarlo como distribución final.
- Fichas PDF: paquete web preparado para publicación.

## Método científico

IberOS mantiene separadas las capas:

`EVIDENCE → INFERENCE → HYPOTHESIS → ESTIMATED TRANSLATION`

También controla la identidad documental y física:

`ENTRY → PHYS_ID / OBJECT_ID → LEAK_GROUP → TRAIN / VAL / HOLD`

## Componentes públicos

- Paquete Python y CLI (`iberos`).
- Esquema JSON de intercambio.
- Registro curado de 38 objetos.
- Enlaces de familias y procedencia.
- Mapeo parcial a identificadores Cathalaunia / Corpus Ibèrika.
- GitHub Pages.
- IberOS Web Engine.
- IberOS-Write.
- Workflows de tests y publicación.
- Fichas PDF preparadas para integración web.

## Fuentes y trazabilidad documental

Registro comprobado el 08-10-2026: [publicaciones y fuentes de la tesis](docs/INTERNET_REGISTRY_2026-10-08.md).

Incluye Corpus Ibèrika, el dataset paleohispánico de 2026 y la revisión de Villares V de Ferrer i Jané (2024). Las fuentes externas requieren concordancias y controles de independencia antes de incorporarse a una validación.

La sincronización documental mantiene C594/C474/C539/C541; no cambia resultados científicos ni métricas. El programa se distribuye bajo Apache-2.0 y el informe de Zenodo bajo CC BY 4.0.

## Cita

Molina Ruiz, Esteban. *IberOS: marco experimental para el análisis interno y la validación reproducible de inscripciones ibéricas*. DOI: 10.5281/zenodo.22939179
