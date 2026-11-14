# VISUAL-AI-09 · Falsación de umbrales mediante controles de textura
Fecha: 2026-11-14 · **EXPERIMENTAL / NO GLYPH OCR** · 0 € · Core intacto.

Se inspeccionó la lámina XVI de la edición de Orleyl (página PDF 152), que muestra los plomos aún enrollados, y se contrastaron **48 ventanas** (16 de Orleyl VII, 16 de Orleyl V, 16 del fondo de papel) contra los **15 ROI fotográficos** propuestos de Orleyl V, lámina XVIII (página PDF 154). Descriptor idéntico en principio al de VISUAL-AI-06: CLAHE, normalización 64×64, HOG y coseno.

## Medición reproducible
Umbral (máxima similitud al ROI más próximo) → controles aceptados:
- ≥0,65: 32/48
- ≥0,70: 32/48
- ≥0,75: 32/48
- ≥0,80: 30/48
- ≥0,85: 9/48
- ≥0,90: 0/48

Los 32 controles de superficies metálicas llegan a ≥0,75; ninguno de los 16 controles de papel lo hace. Mediana del control 0,82477; máximo 0,87029. **Es un hallazgo de falta de especificidad del descriptor y una objeción directa al empleo de simples scores HOG como reconocimiento epigráfico**. Los 48 controles no poseen anotación independiente signo/no-signo, por lo que estas cifras son **tasas de activación sobre controles exploratorios**, NO tasas de falsos positivos validadas.

No se descargaron plantillas SVG reales de Wikimedia durante esta prueba (acceso binario bloqueado). No se atribuye ningún valor fonético, no se declara accuracy y no se promociona nada al Core. Los 133 registros con etiqueta simple continúan sin validación fotográfica.

## Archivo reproducible del hilo
`IBEROS_VISUAL_AI_09.zip`: `stress_test.py`, `report.json`, `negative_control_matches.csv`, galería visual y README. Requiere fotos ya extraídas del PDF del usuario y ROI de VISUAL-AI-06. El ZIP pasa la verificación CRC. Evitar publicar imágenes del PDF sin verificar derechos de reproducción.

## Cambio metodológico
Antes de entrenar: eliminar textura fotográfica, separar trazos completos y fondo, crear un conjunto negativo validado, comparar con contornos arqueológicos reales de otra pieza física y fijar umbrales usando un conjunto de calibración diferente del HOLD. Preservar PHYS_ID/LEAK_GROUP, C594/C474/C539/C541 y FULL3406.
