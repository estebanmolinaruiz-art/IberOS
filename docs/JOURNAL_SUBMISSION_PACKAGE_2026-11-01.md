# IberOS — paquete editorial para revistas
Fecha: 2026-11-01
Responsable: Esteban Molina Ruiz

## Estado
Consultas editoriales previas enviadas a:
- Palaeohispanica
- Archivo Español de Arqueología
- Complutum
- Zephyrus
- Digital Scholarship in the Humanities

No se ha enviado simultáneamente un mismo manuscrito formal a varias revistas.

## Título base propuesto
**IberOS: un marco reproducible para el análisis asistido de inscripciones ibéricas**

Alternativa internacional:
**IberOS: A Reproducible Computational Framework for the Assisted Analysis of Ancient Iberian Inscriptions**

## Resumen base
IberOS es un proyecto independiente de investigación experimental orientado al análisis reproducible de inscripciones ibéricas mediante procedimientos documentales, paleográficos y computacionales. El marco separa de forma explícita EVIDENCE → INFERENCE → HYPOTHESIS → ESTIMATED TRANSLATION y conserva estados de incertidumbre, dependencia documental, resultados negativos y gates abiertos. El objetivo no es presentar un desciframiento demostrado de la lengua ibérica, sino evaluar qué aportan los métodos computacionales cuando se integran con identificación arqueológica, lecturas editoriales verificables, control de procedencia y revisión crítica.

El artículo propuesto presentaría la arquitectura metodológica de IberOS y varios casos documentados para mostrar cómo se registran evidencias, se comparan patrones, se bloquean inferencias no justificadas y se preserva la trazabilidad de cada decisión. Los materiales públicos incluyen un corpus curado, fichas científicas, código abierto, documentación metodológica y estudios de caso. Los resultados se interpretarían como evaluación del procedimiento y de sus límites, no como porcentaje de desciframiento ni como traducciones definitivas.

## Contribuciones principales
1. Separación explícita entre evidencia, inferencia, hipótesis y traducción estimada.
2. Control de dependencia entre objetos, copias, ediciones y testimonios.
3. Registro reproducible de decisiones y resultados negativos.
4. Integración de documentación arqueológica y epigráfica con herramientas computacionales.
5. Gates semánticos abiertos que impiden promover automáticamente hipótesis a resultados validados.
6. Materiales públicos auditables en GitHub, Zenodo y web.

## Casos candidatos
### Plomo de Tivissa
Uso: patrón estructural, SALIR / ROK / cuantificación.
Límite: la semántica de ROK permanece abierta.

### Pech-Maho V
Uso: variantes de lectura y control de dependencia documental.
Límite: la lectura paleográfica completa depende del cotejo de fuentes primarias.

### Plomo I de La Serreta
Uso: gestión de variantes editoriales, subentradas físicas y evidencia primaria pendiente.
Límite: la correspondencia exacta de algunas subunidades y signos sigue abierta.

### Mosaico de La Caridad / Caminreal
Uso: contexto arqueológico y recurrencias EKIAR.
Límite: recurrencia funcional no equivale a traducción léxica demostrada.

### Arquitrabe bilingüe de Sagunto
Uso: control bilingüe externo.
Límite: bilingüismo no implica correspondencia palabra por palabra.

## Estructura recomendada
1. Introducción
2. Problema metodológico
3. Arquitectura de IberOS
4. Corpus y control de dependencia
5. Casos de estudio
6. Resultados y resultados negativos
7. Límites científicos
8. Reproducibilidad y materiales abiertos
9. Discusión
10. Conclusiones

## Adaptación por revista
### Palaeohispanica
Prioridad: epigrafía paleohispánica y control de lectura.
Reducir descripción técnica del software.
Reforzar casos, variantes, signarios, dependencia documental y falsabilidad.

### Archivo Español de Arqueología
Prioridad: objeto, contexto arqueológico, procedencia y articulación entre epigrafía y arqueología.
Presentar IberOS como herramienta metodológica, no como producto tecnológico.

### Complutum
Prioridad: metodología interdisciplinar, reproducibilidad y humanidades digitales aplicadas a Protohistoria.
Reforzar diseño de investigación, controles y evaluación crítica.

### Zephyrus
Prioridad: casos arqueológicos delimitados y aportación metodológica.
Puede ser más adecuado un artículo centrado en un subconjunto de piezas y su contexto.

### Digital Scholarship in the Humanities
Prioridad: contribución metodológica en Humanidades Digitales.
Incluir arquitectura, modelo de datos, reproducibilidad, evaluación, código abierto y limitaciones.
Redactar en inglés.

## Recursos públicos
- Web: https://estebanmolinaruiz-art.github.io/IberOS/
- GitHub: https://github.com/estebanmolinaruiz-art/IberOS
- Informe técnico: https://doi.org/10.5281/zenodo.22939179
- Case Studies I: https://doi.org/10.5281/zenodo.22957236
- PyPI: https://pypi.org/project/iberos/1.0.1/

## Reglas editoriales internas
- No afirmar desciframiento demostrado.
- No usar ICS u otras métricas internas como porcentaje de lengua descifrada.
- No presentar transliteración como traducción.
- No ocultar resultados negativos.
- No fusionar testimonios dependientes como evidencia independiente.
- No enviar simultáneamente el mismo manuscrito formal a varias revistas.
