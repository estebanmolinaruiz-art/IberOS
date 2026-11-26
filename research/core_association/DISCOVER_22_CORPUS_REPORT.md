# DISCOVER-22 · Auditoría transversal de material legible

Fecha 2026-11-16 · rama de investigación, sin modificar Core/C594/C474/C539/C541/FULL3406. Coste adicional 0 €.

## Fuentes efectivamente procesadas
1. `data/curated/iberos_curated_objects_v1.jsonl`: **38** fichas de objetos, metadatos NO equivalentes a 38 textos completos.
2. `data/review/editorial_readings_pending_v1.jsonl`: **3** lecturas pendientes (Sagunto, Caminreal, Casinos), con variantes dual/no dual que NO deben contarse como piezas independientes.
3. `research/protocols/ORLEYL-EDITORIAL-PARALLELS-2026-10-18.csv`: **3** comparaciones editadas de varios plomos de Orleyl, todos previamente expuestos a IberOS (desarrollo, no HOLD).
4. `data/review/validation01_external_opaque_readings_batch01.csv`: **12** registros de tipografía opaca sin lectura de signos admisible; excluidos de los cómputos lingüísticos.
5. `data/curated/rok_orleyl_editorial_alignment_1981.csv`: una correspondencia editorial Orleyl V/VII-B; no evidencia visual independiente.

Hay más materiales bibliográficos y documentos no normalizados en IberOS. Este experimento NO declara haber procesado todo el contenido textual de cada PDF, Drive ni toda la colección externa: cobertura explícita de cinco fuentes legibles por máquina.

## Salida real del algoritmo
- 9 registros de lectura editorial de **7 ID físicos** (algunos repetidos por comparaciones), con **33 unidades completas** y **26 formas diferentes**; **5 unidades exactas compartidas** entre ID diferentes en las secuencias seleccionadas: `anerai`, `bododaseai`, `iunstir`, `selkeai`, `uskeike`.
- Bajo distancia Levenshtein = 1 sobre la misma normalización editorial, se observaron **2 pares entre ID físicos distintos**: `bardoneai ↔ barduneai` (sustitución **o/u**) e `iunstir ↔ iustir` (inserción o supresión **n**).
- Son **transformaciones editoriales conocidas como variantes de paralelos de Orleyl**, ahora clasificadas por algoritmo; **no son descubrimientos semánticos novedosos**, no se les atribuye morfología ni traducción sin una lectura independiente.
- El cotejo editorial por signo del pasaje BI-TE-R-O-KE de Orleyl V frente VII encuentra cinco bigramas compartidos (`BI-TE`, `TE-R`, `R-O`, `O-KE`, `TI-NE`); no es prueba nueva porque el pasaje está ya seleccionado por semejanza.
- **0** signos individuales leídos de manera autónoma en fotografías; **0** reglas predictivas sobre objeto reservado; **0** resultados estadísticos ajustados capaces de distinguir fonético/logográfico/mixto.

## Hipótesis formuladas para falsación
- **H22-TRANS-O/U:** ¿Las alternancias o/u en una misma familia léxica ocurren de manera sistemática y predecible en nuevas piezas, o son lecturas gráficas discordantes?
- **H22-TRANS-N:** ¿La n en familias tipo `iu(n)stir` refleja morfología, error de segmentación o variación documental?
- **H22-CONTEXT:** ¿Las unidades recurrentes entre plomos tienen posiciones/documentos compartidos más allá de lo esperable por extensión y tipo de soporte?

Para cada una, estratificar por **PHYS_ID, LEAK_GROUP, SCRIPT_TYPE, soporte y cronología**; excluir familias/objetos usados para generarla. Una coincidencia retroactiva de Orleyl NO cuenta como confirmación.

## Reproducibilidad
Código ejecutado: `research/core_association/discover22_corpus.py`; GitHub Actions ejecución completa `43956304145` exitosa; artefacto `iberos-discover22-coverage`: manifiesto SHA-256 de las cinco fuentes, `editorial_units.csv`, `cross_object_candidates.csv`, `transform_candidates.json`. Persistencia de datos de resultados en artefacto GitHub, no en Core.
