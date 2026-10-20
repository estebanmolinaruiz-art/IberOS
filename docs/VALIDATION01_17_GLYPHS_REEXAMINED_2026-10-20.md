# VALIDATION-01 — Auditoría visual individual: 17 signos (2026-10-20)

**Fuente gráfica auditada:** Fletcher et al. (1981), *Materiales de la necrópolis ibérica de Orleyl*, pp. PDF 65 y 111, figuras 22 y 25; edición aportada por el usuario.

**Procedimiento reproducible:** PyMuPDF, matriz 4×, rotación Pillow 270°, marco de 3049×2303 píxeles. Las 17 cajas preliminares constan en `data/review/validation01_orleyl_17_visual_alignment_v1.csv`. Se creó localmente `VALIDATION01_17_glyphs_audit_expanded_2026-10-20.png` mostrando nueve pares (la posición sexta solo existe en V según Fletcher), y `validation01_17_glyph_bbox_quality_review_2026-10-20.csv` con 17 propuestas de **ampliación de ventana**, no cajas definitivas de segmentación. Los recortes ampliados añaden 24 píxeles a cada lado y 8 arriba/abajo; inevitablemente contienen trazos de signos vecinos, por lo que **no deben utilizarse como glifos aislados para clasificación automática**.

## Observación directa con la nueva lámina
- Tres te editoriales: V índice 2, V índice 6 y VII-B índice 2 representan cuadriláteros/rombos subdivididos por dos líneas internas que se cruzan. El signo adicional V-06 es una figura completa dibujada, no simple rasguño aislado. **Concordancia de familia morfológica**, no identidad certificada de variante dual ni incisión original.
- KE: V índice 5 tiene contorno más redondeado/curvo; VII-B índice 5 se representa con trazos angulosos. Una diferencia de contorno no resuelve si la clase es simple o compleja.
- BI: V índice 1 y VII índice 1 estaban junto al límite izquierdo de las cajas iniciales; ventanas ampliadas mejoran contexto y muestran signos cercanos. Se exige comprobación de trazo en original antes de declarar recorte individual completo.
- Restantes signos `r, o, ti, n, e` se colocan en la nueva lámina emparejados, pero no han sido evaluados a ciegas frente a un repertorio paleográfico.

## Restricciones científicas
Esta lámina deriva de una edición **ya transcrita** y la comparación es retrospectiva: ninguna posición es HOLD. La atribución de fonemas proviene de Fletcher, no de un segundo lector ni de signario independiente. La figura 9 de Ferrer (2013), p. 454, **sí fue inspeccionada** en el turno anterior y no permite discriminar con rigor todas las variantes particulares del corpus de Orleyl.

**M06=PENDING. M07=PENDING. Preparación 30/100. VALIDATION-01 NOT_EVALUATED.**

Próximo: obtención de lámina tipológica explícita de las variantes `te` nororientales y contraste 1:1 de cada signo; completar 17 fichas con fuente de comparación identificada, evidencia de trazo y resolución de desacuerdos.
