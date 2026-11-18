# IberOS DISCOVER-18 · lectura y contraste de signo-palabra

**Fecha 2026-11-16. Investigación exploratoria, no desciframiento. Core y autoridad congelada intactos. Coste 0 €.**

Se reabrió el artefacto local `IBEROS_FULL_LINE_ALIGN_17/aligned_slots.csv`, derivado de dibujos arqueológicos de Orleyl V (PDF figura 22/página 65) y VII-B (figura 25/página 111). La segmentación previa **usó el número/orden de tokens de Fletcher** y no corresponde a lectura visual independiente: 70 posiciones, 69 con valor editorial de referencia, 9 separadores, 3 restituciones editoriales sin grafema observado. El segmento inicial de Orleyl V contiene una sola casilla **sin lectura**, por lo que NO puede documentarse como signo-palabra.

## Hipótesis confrontadas
- P: grafemas con valor fonético/silábico, control académico.
- L: algunos grafemas representarían palabras completas.
- M: sistema mixto fonético y logográfico/determinativo.
- N: marcas no lingüísticas, control negativo pertinente para otros objetos.

Las dos líneas carecen de etiquetado semántico externo y lectura autónoma. La existencia de patrones recurrentes no permite elegir entre P, L y M. No existe traducción validada.

## Evidencia medida
Se buscaron cadenas contiguas de 2, 3 y 4 tokens **editoriales** compartidas entre dos objetos físicos, sin cruzar separadores. Para grupos completos:
- 7 bigramas compartidos (A-R; N-E; N-W; R-E; R-I; S-E; W-L).
- 2 trigramas compartidos: **A-R-I** y **N-W-L** (el valor editorial W debe cotejarse paleográficamente).
- 0 tetragramas compartidos.

Modelo nulo A: 5.000 permutaciones por objeto conservando frecuencias y longitudes de grupos. p exploratorias: 0,014397, 0,012198, 1,0 respectivamente. Modelo nulo B (reordena solo dentro de cada grupo): p 0,034193, 0,033393, 1,0. Estas pruebas fueron seleccionadas durante análisis exploratorio, no preinscritas; el tamaño es mínimo y los valores proceden de la edición. **No son pruebas de logografía, de traducción ni de capacidad predictiva.** Se requerirá replicación en otros objetos y corrección por multiplicidad.

## Archivos reproducibles del hilo
`IBEROS_DISCOVER_18.zip` incluye `iberos_discover18.py`, `group_inventory.csv`, `shared_ngram_candidates.csv`, `results.json`, `sensitivity_within_groups.json`, `README.md`. El algoritmo es estándar Python, semilla fija, salida con trazabilidad SHA-256 de ALIGN-17. El ZIP ha superado su prueba de integridad.

## Siguiente prueba realmente decisiva
1. Comprobar paleográficamente la transcripción `N-W-L` y extraer secuencias gráficas **sin mostrar valores editoriales**.
2. Obtener objetos físicamente distintos donde las secuencias aparezcan en contextos arqueológicos externamente documentados.
3. Registrar antes del cotejo una hipótesis semántica específica y predicciones sobre el soporte/función; mantener un HOLD protegido.
4. Evaluar P/L/M/N con controles de transcripción, permutaciones y abstención; no declarar significados si la fuente no los acredita.

No se modifica `src/iberos/core.py`; se preservan C594/C474/C539/C541 y FULL3406.