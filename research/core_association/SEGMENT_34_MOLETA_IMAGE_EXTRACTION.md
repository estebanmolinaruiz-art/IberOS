# SEGMENT-34 · Extracción gráfica independiente de la Moleta del Remei

Fecha: 2026-11-22. **Resultado ejecutado: SUCCESS** [GitHub Actions #45068774854](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/45068774854).

Fuente: PDF de *Palaeohispanica* 8 (2008), `https://ifc.dpz.es/recursos/publicaciones/28/40/_ebook.pdf`. La descarga ha sido verificada contra SHA-256 previamente congelado: `2965fd62b2a040aa99bb5428bbe8018fba56ebfb201b35034e93a2c38b292e22`.

A diferencia del experimento anterior, se localizaron rectángulos del contenido gráfico incrustado *por encima de los pies de figura* y se extrajeron píxeles directamente a 2×. Las etiquetas de signos de Fletcher y los 67 límites de Orleyl NO se utilizaron.

| Figura | Página PDF base cero | Rectángulo PDF (pt) x0,y0,x1,y1 | Imagen resultante | Identificación |
|---|---:|---|---|---|
| Foto 4 | 209 | 96.84,225.72,441.84,570.72 | 691 × 691 px | Mayor imagen incrustada próxima al pie |
| Dibujo 5 | 210 | 91.08,156.36,437.94,621.36 | 694 × 931 px | Mayor imagen incrustada próxima al pie |

Se midió sensibilidad básica a tres cuantiles de gris sobre cada recorte. Estos son indicadores diagnósticos; **no son límites de signos ni una interpretación de surcos**. Los recortes no se han revisado individualmente de manera ciega y todavía podrían incluir entorno de la figura o elementos extraepigráficos.

**Puertas científicas:** 2 zonas de figura obtenidas, 0 fronteras de signos verificadas independientemente, 0 lecturas o traducciones nuevas, **sin medida externa de precisión y sin confirmación de generalización del 81,4 % de Orleyl**. El resultado de SEGMENT-32 sigue siendo exclusivamente retrospectivo.

Archivos de análisis en artefacto temporal `iberos-segment34-moleta-private-figure-zones` del run #45068774854. Por restricciones de reproducción de la edición (licencia CC BY-NC-ND indicada en el propio PDF) no se incorporan láminas derivadas a GitHub; artefacto de retención de un día para investigación interna. El código fuente sí se preserva: `research/core_association/segment34_moleta_roi.py`.

**Siguiente prueba:** determinar visualmente las franjas epigráficas y sus zonas dudosas; congelar las cajas antes de aplicar SEGMENT-31/32 sin reajustar parámetros. Después medir solo aquello que tenga límites de referencia genuinamente independientes.

Coste adicional: **0 €**. Core / C594 / C474 / C539 / C541 / FULL3406 sin alteraciones.