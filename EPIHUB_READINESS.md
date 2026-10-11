# IberOS — EpiHub Readiness

Actualizado: 2026-10-11

Este documento traduce los criterios comunicados por EpiHub en entregables verificables. IberOS no declarará un requisito como cumplido mientras la evidencia pública correspondiente no pueda comprobarse.

| Criterio | Evidencia mínima | Estado | Evidencia actual | Bloqueo |
|---|---|---|---|---|
| Sitio web dedicado estable | URL pública estable, navegación y páginas de proyecto/documentación/research/contacto | 🟠 | GitHub Pages habilitada y contenido web en el repositorio | Verificación externa completa y enlaces finales |
| Estructura clara de software | Repositorio público, estructura, licencia, versión, instalación y tests | 🟢 | GitHub público; src/, tests/, docs/, data/, Apache-2.0, releases v1.0.0/v1.0.1 | Ninguno crítico |
| Distribución reproducible | PyPI alineado con la release y prueba limpia de instalación | 🟠 | Paquete iberos público; workflow de publicación | Verificar iberos==1.0.1 y CLI |
| Persistencia/citación | DOI del informe y DOI del software claramente separados | 🟠 | Informe: 10.5281/zenodo.22939179; concepto: 10.5281/zenodo.22939178 | Verificar DOI específico del software v1.0.1 |
| Documentación técnica | README, instalación, arquitectura, API/CLI, ejemplos y límites | 🟠 | README, docs/, workflows y componentes | Consolidar entrada única y arquitectura |
| Marco académico | Documento metodológico citable, fuentes y posición epistemológica | 🟠 | Informe Zenodo, registro de fuentes y separación de niveles inferenciales | Documento metodológico final y evidencia externa |
| Benchmark | Corpus curado + protocolo + resultados reproducibles + negativos | 🟠 | 38 objetos curados | Publicar protocolo, métricas y resultados |
| Trazabilidad | Versiones, autores, licencias, checksums y procedencia | 🟢 | CITATION.cff, AUTHORS.md, LICENSE, MANIFEST_SHA256, políticas | Mantener sincronización |
| Archivo duradero | Zenodo + Software Heritage | 🟠 | Zenodo activo y workflow SWH | Registrar SWHID |

## Condición de reenvío a EpiHub

IberOS estará listo para solicitar reevaluación cuando puedan verificarse conjuntamente:

1. sitio web público estable;
2. GitHub v1.0.1 como repositorio canónico;
3. `iberos==1.0.1` instalado desde PyPI en entorno limpio;
4. DOI específico de software v1.0.1, separado del DOI del informe;
5. metodología pública y citable;
6. benchmark reproducible con resultados y límites.

Hasta entonces, la formulación correcta es **“preparación avanzada para reevaluación”**, no “requisitos EpiHub cumplidos”.
