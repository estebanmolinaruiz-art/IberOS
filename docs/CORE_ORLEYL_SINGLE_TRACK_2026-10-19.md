# IberOS CORE — Punto único de control Orleyl (19-10-2026)

## Propósito
Evitar duplicar en varios hilos las mismas revisiones de Orleyl. Este archivo es un índice de coordinación documental, no una validación paleográfica.

## Expediente canónico
- [Registro de signos y las cinco bandas](../data/review/orleyl_te_glyph_review_v1.json)
- [Cotejo de edición primaria](ROK_ORLEYL_PRIMARY_EDITION_COLLATION_2026-10-14.md)
- [Auditoría de bandas raster](ROK_ORLEYL_RASTER_LINE_AUDIT_2026-10-14.md)
- [Matriz de pruebas](../research/protocols/ORLEYL-CROSSCHECK-MATRIX-2026-10-18.csv)
- [Puertas de validación](../research/protocols/ORLEYL-SOURCE-REVIEW-2026-10-18.md)

## Hechos ya documentados: no repetir pruebas
1. Fletcher (1981) publica V-19 BITEROKETETINE y VII-B-7 BITEROKETINE, con diferencia editorial -TE-.
2. Se documentaron y corrigieron errores de orientación y recortes defectuosos de la figura 25. No usar los recortes retirados como evidencia.
3. Hay cinco bandas de inspección para el raster orientado de la figura 25 (2287 × 1727); ninguna está asignada a la secuencia con verificación signo a signo.
4. Hay recortes candidatos históricos con otro raster y giro. Sus coordenadas son incompatibles con las cinco bandas corregidas.
5. La transcripción secundaria ofrece contexto areŕe : kutuboike : basbiteŕoketine : iŕika. Los anclajes editoriales no son coordenadas visuales.
6. El segmento -TE- y una interpretación de destinatario siguen siendo hipótesis sin corroboración paleográfica y morfológica suficiente.

## Única tarea de investigación abierta
**ORL-GLYPH-MAP-01**: conseguir la imagen íntegra y legible del testimonio fig. 25 (y lámina XXII); verificar orientación y hash; localizar la secuencia delimitada por separadores; asignar fila y cajas por cada signo; cotejar fig. 22 y lámina XVII; revisión independiente.

No reabrir las fases de identificación documental, reorientación o selección de bandas salvo nueva prueba específica.

## Gate
ROK-RECIPIENT-02 = OPEN. exact_glyph_coordinates_verified = false. te_morpheme_confirmed = false. eligible_for_core_execution = false.

## Coordinación entre hilos
- **Progreso/Revisión del CORE**: única línea conductora para investigación y decisiones paleográficas.
- **VALIDATION01 — IBEROS**: contrastación independiente que remite al expediente canónico; no duplicar la investigación principal.
- **IberOS+ · Web pública / IberOS+web v2**: visualización y despliegue solamente después de consultar el estado de evidencia del expediente.
- Cualquier avance en otro hilo debe mencionar la clave de tarea, el archivo canónico, el commit y el nuevo dato observado.
- Los hilos no pueden renombrarse, cerrarse ni sincronizarse automáticamente por este archivo; es una convención de coordinación.
