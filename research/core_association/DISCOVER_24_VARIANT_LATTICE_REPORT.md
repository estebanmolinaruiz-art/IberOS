# DISCOVER-24 · Retícula de lecturas alternativas, Casinos

Fecha: 2026-11-16. **Ejecución satisfactoria** GitHub Actions #43958910763. Nuevo método de sensibilidad a la interpretación, NO búsqueda reiterada de secuencias Orleyl.

## Datos
Fuente ya incorporada al repositorio: `data/review/editorial_readings_pending_v1.jsonl`, lectura de Casinos `IBR-PLM-0007` con variantes dual/no dual tomadas de la transcripción editorial de Ferrer i Jané y Escrivà Torres 2014, p. 212. **Es un único objeto**: sus dos lecturas alternativas no son muestras independientes. Imágenes originales fig. 1 y 2 identificadas en el expediente, pero no se han cotejado en este experimento.

## Método nuevo
Se alinea cada posición textual editorial entre las alternativas dual y no dual, se construye una **retícula de incertidumbre**, se marca si su identidad textual se conserva y se aísla el patrón numérico por expresión regular (sin confundir glifos con valores editoriales). Las divergencias se puntúan por distancia Levenshtein a nivel de caracteres, no signos gráficos.

## Resultado
- **14 unidades posicionales** (delimitadas por puntuación editorial), de las cuales **10 invariantes** y **4 variables**.
- Las cuatro posiciones variables: `abaŕgeŕes / abaŕkeŕes`, `ideŕ / iteŕ`, `dagan / takan`, `gi I / / ki I /`.
- **Cuatro menciones de numerales romanos editoriales** (una serie de siete `I` y tres `I` individuales), que son exactamente idénticas bajo ambas lecturas. Los 7+1+1+1 trazos son **cifras tal como aparecen representadas en la transcripción**, no conteos certificados sobre la foto original.
- La representación de barras puede ser estable frente a dualidad fonética; su significado monetario, cuantitativo o lexical **NO está verificado**.
- La mera constancia no distingue entre hipótesis logográfica, abreviativa, numérica o fonética.

## Siguiente falsación
Comprobar con la figura original los diez trazos editoriales `I` y la segmentación; después usar un segundo objeto **físicamente independiente** con magnitudes respaldadas por su contexto para entrenar/contrastar una hipótesis sobre medida. El modelo deberá admitir alternativas de lectura, no forzar una sola. Conservar un HOLD reservado.

## Artefactos
Código reproducible `research/core_association/discover24_variant_lattice.py`; outputs descargables de GitHub Actions #43958910763: `report.json`, `variant_lattice.csv`, `numeral_invariants.csv`. Dos ejecuciones previas fallaron en la exportación CSV y fueron corregidas antes de declarar el resultado. **Core, C594/C474/C539/C541 y FULL3406 sin cambios. Coste 0 €**.
