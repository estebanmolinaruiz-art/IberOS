# GOLDSET-40 — Atlas ciego de candidatos gráficos de Moleta (resultado ejecutado)

Fecha: 2026-11-26. Ejecución verificada: [GitHub Actions #45904873102](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/45904873102), éxito.

## Procedimiento
Desde los recortes de las figuras 4 (fotografía) y 5 (dibujo) de Ferrer i Jané et al. 2008 y su PDF original SHA-256 `2965fd62b2a040aa99bb5428bbe8018fba56ebfb201b35034e93a2c38b292e22`, se extrajeron componentes conectados bajo tres representaciones binarias de la imagen: Otsu, contraste local/umbral adaptativo de ventana 31 y 51. Los recortes se procesaron separadamente y se compararon componentes por superposición de sus cajas, sin asignar lecturas ni forzar un total de 21 caracteres o tres líneas.

| Figura | Componentes iniciales (Otsu) | Componentes candidatos estables Otsu/adapt31/adapt51 |
|---|---:|---:|
| Fotografía 4 | 68 | 28 |
| Dibujo 5 | 119 | 94 |
| **Total** | **187** | **122** |

Los métodos adaptativos obtuvieron 469/396 componentes para la fotografía y 164/122 para el dibujo; se trata de propiedades de los umbrales, no de epigrafía. Los 122 componentes designados como candidatos cumplen filtros de persistencia geométrica y tamaño, **no equivalen a 122 signos**. Se pueden duplicar, solapar, fragmentar signos o proceder de roturas, manchas u otros dibujos.

## Puertas de calidad y no filtración
- `editorial_values_used_in_detection=false`.
- `target_sign_count_used_in_detection=false`.
- `independently_approved_glyph_bboxes=0`.
- `blind_review_approved=false`.
- `graphic_ground_truth=false`.
- Los 21 registros de GOLDSET-39 permanecen como **anotaciones de edición**, no son etiquetas ciegas.
- No se ha certificado ninguna traducción o identificación paleográfica nueva.

Entregable efímero (24 horas; solo uso de investigación con reproducción de figuras sujeta a CC BY-NC-ND): [Atlas original y hojas de contacto](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/45904873102/artifacts/15157636433). Contiene `report.json`, `blind_components.csv`, dos imágenes originales con contornos de candidatos y dos hojas de contacto de fragmentos numerados. Código que permite regenerarlos: `goldset40_blind_components.py`, sin imágenes de la edición redistribuidas en el repositorio.

## Dictamen
Primer **atlas de trazos candidatos** generado desde evidencia visual externa, con un registro por componente y coordenadas reproducibles. **Todavía no es un conjunto de signos completos verificados**. Para convertirlo en un patrón de referencia gráfico, hay que observar las hojas originales de figuras 4/5 y asociar manual o independientemente fragmentos a signos enteros y tres líneas en dos zonas, dejando abstenciones. Solo después se cotejarán las alternativas editoriales de GOLDSET-39. No mezclar la misma pieza entre entrenamiento y test.

Core, FULL3406 y C594/C474/C539/C541 intactos. Coste adicional 0 €.
