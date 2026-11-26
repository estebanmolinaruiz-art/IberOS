# SEGMENT-30 — Segmentación no supervisada de líneas completas (Orleyl)

Fecha: 2026-11-21. Ejecución local sobre imágenes originales derivadas de dibujos editoriales de Fletcher, pp. PDF 65 y 111. Enfoque nuevo distinto de HOG y topología: **detección de cortes sin valores fonéticos**.

## Protocolo
Las entradas son imágenes `orleyl_p65_upright.png` y `orleyl_p111_upright.png`; la franja de renglón se define mediante la envolvente global de las regiones archivadas (solo extremos de imagen), **sin usar las posiciones internas ni las etiquetas editoriales**. Se aplica Otsu a escala de grises, filtro de líneas horizontales largas, densidad de tinta por columna con suavizado gaussiano; se generan mínimos locales y espacios en blanco; una programación dinámica elige las fronteras minimizando un coste de tinta atravesada + desviación respecto al ancho esperado basado en la altura del renglón + penalización por corte. Los parámetros no fueron elegidos a partir de las etiquetas. Se congelan las predicciones y luego se cotejan las coordenadas de las fronteras con las del fichero `IBEROS_RECOGNIZE_28/shape_audit.csv`.

**Diagnóstico retrospectivo (tolerancia ≤6 píxeles)**:
- Orleyl V: 26 cortes previstos, 42 fronteras editoriales revisadas, 23 coincidencias; precisión proxy 88,46 %, recuperación proxy 54,76 %.
- Orleyl VII-B: 17 cortes previstos, 25 fronteras editoriales, 11 coincidencias; precisión 64,71 %, recuperación 44,00 %.
- Total: **43 cortes, 67 fronteras editoriales, 34 coincidencias (precisión 79,07 %, recuperación 50,75 %)**.
- Con tolerancia de 12 píxeles, 41 coincidencias (resultados menos estrictos, no validación de signos).
- 0 lecturas visuales independientes, 0 signos paleográficamente acreditados, 0 traducciones.

**Advertencias**: Los dos dibujos pertenecen a una misma tradición editorial y un mismo conjunto arqueológico, no un holdout interyacimientos. Las posiciones editoriales son referencias imperfectas, no verdad física. El algoritmo tiende a **subsegmentar**; las métricas no son precisión del reconocimiento ni probabilidad de desciframiento. El filtrado de líneas largas puede suprimir trazos auténticos. Las fronteras de baja densidad son hipótesis visuales, no grafemas certificados.

## Artefacto local
`IBEROS_SEGMENT_30.zip`: algoritmo ejecutable `run.py`, manifiesto SHA-256 de las dos fuentes, resultados JSON, informes, CSV de posiciones, imágenes de predicción sin etiquetas y superposiciones editoriales añadidas después. Integridad ZIP comprobada.

## Siguiente paso no repetitivo
Construir un **grafo de segmentaciones alternativas** que mantenga cortes de bajo coste no escogidos en la ruta óptima, permitiendo separar los bloques subsegmentados. Conservar las 67 fronteras editoriales como datos de diagnóstico no como señales de entrenamiento. Registrar abstenciones en zonas de alta ambigüedad y evaluar en objetos de otras procedencias antes de aprobar el motor.

Coste 0 €. Core, FULL3406 y C594/C474/C539/C541 intactos.
