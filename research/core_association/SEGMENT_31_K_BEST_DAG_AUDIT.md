# SEGMENT-31 · Grafo K-mejores, control de precisión y diagnóstico de nodos

Fecha: 2026-11-21. Ejecución local con las mismas dos imágenes originales de SEGMENT-30, huellas SHA-256 contrastadas. Los cortes editoriales no intervienen en la generación del grafo ni en las puntuaciones.

Se generan hasta 12 rutas de mínimo coste por renglón sobre nodos de valle de tinta mediante programación dinámica K-best. Las rutas se comparan después con límites editoriales, tolerancia 6 px y emparejamiento bipartito uno a uno.

- Ruta óptima por renglón: **43 cortes**, **34 coincidencias** con 67 fronteras editoriales; precisión **79,07 %**, recuperación **50,75 %**.
- Unión de 12 rutas por renglón: **51 cortes**, **34 coincidencias**; precisión **66,67 %**, recuperación **50,75 %**. **Resultado negativo:** conservar rutas similares por sí solo no mejora la recuperación.
- Grafo total: **128 nodos candidatos interiores**. Su cobertura máxima retrospectiva contra las fronteras editoriales, con conocimiento de la respuesta, es **60/67**. Esta cifra NO es predicción ni precisión. Indica que gran parte de la pérdida proviene de cómo se seleccionan y puntúan las rutas, mientras siete fronteras carecen de candidato próximo.

**Hipótesis de ingeniería H31:** modificar el objetivo del camino o combinar medidas de continuidad estructural puede rescatar cortes de nodos ya disponibles, sin simplemente aumentar el número de cortes. Falsación: contrastar presupuesto fijo, precisión y cobertura en objetos de otra familia, manteniendo las referencias editoriales ocultas hasta la evaluación. No ajustar hiperparámetros a las 67 posiciones del ensayo.

No hay signos visualmente confirmados de manera independiente, no hay transcripción nueva ni traducción. Ninguna modificación al Core/FULL3406/C594/C474/C539/C541. Coste 0 €.

Entregable local: `IBEROS_SEGMENT_31.zip` (código `run.py`, informe, rutas JSON, PNG, huellas de origen y métricas por línea), verificado con CRC.
