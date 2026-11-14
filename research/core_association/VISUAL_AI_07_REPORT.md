# IBEROS-VISUAL-AI-07 · Robustez de coincidencias gráficas

Fecha: 2026-11-14. Estado: **EXPERIMENTAL; NO ES LECTURA FONÉTICA**.

Fuente: fotografía de Orleyl V, lámina XVIII, página PDF 154 de *Materiales de la necrópolis ibérica de Orleyl* (1981), PDF SHA-256 `cc8e110f12d8047567e30ee6344a345e599ee55638450b78e22bccfbbc9c6551`.

Se reutilizaron 15 regiones propuestas en VISUAL-AI-06 (ninguna certificada como signo completo). Se calcularon **105 comparaciones entre regiones**, repetidas mediante cuatro representaciones: imagen original normalizada, CLAHE, bordes Canny y bordes invertidos. **Cuatro parejas** estuvieron simultáneamente entre las cinco mejor clasificadas de cada representación: B05–B06, B05–B07, B05–B08 y B06–B08. La pareja B06–B08 alcanzó similitud HOG media 0,92147 entre los tratamientos, dispersión 0,07857. No es probabilidad de valor común ni prueba de que sean grafemas.

**Control negativo de interpretación:** todos los recortes pertenecen al mismo objeto físico y pueden compartir textura fotográfica, fondo o trazos vecinos. La estabilidad ante los cuatro tratamientos NO demuestra igualdad epigráfica ni independencia. Se mantienen `lecturas_independientes=0` y `accuracy=null`.

**Nuevas fuentes identificadas:** Commons, categoría *Iberian letters*, contiene 191 archivos gráficos SVG, entre ellos `NE Iberian a2a.svg`, licencia CC0. Estos son dibujos tipográficos, no fotografías de signos excavados, y NO se descargaron ni compararon por píxeles en esta prueba.

Artefacto local reproducible: `IBEROS_VISUAL_AI_07.zip` con `stability_pairs.csv`, `crop_quality.csv`, `stability_contact.png`, `report.json` y script `iberos_visual_ai07.py`; ZIP test OK.

Siguientes controles: comparar sobre fotografía de otro objeto físico y **plantillas SVG realmente descargadas** de fuentes trazables; medir controles anepigráficos y congelar la predicción antes de abrir las lecturas de referencia. Sin mutar el Core, C594/C474/C539/C541 ni FULL3406. Coste adicional 0 €.
