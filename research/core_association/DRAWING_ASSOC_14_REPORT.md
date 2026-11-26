# DRAWING-ASSOC-14 · Dos plomos Orleyl, cotejo gráfico automático

Fecha: 2026-11-15. **Experimental / sin lectura fonética validada**. Coste adicional 0 €.

Las figuras originales publicadas de *Materiales de la necrópolis ibérica de Orleyl* (1981) fueron facilitadas por el usuario. Se examinaron **fig. 22 Orleyl V (página PDF 65)** y **fig. 25 Orleyl VII-B (página PDF 111)** tras corregir la orientación de los dibujos.

Se detectaron **27 componentes de tinta** de la primera línea en V y **20** en VII-B; se compararon sus **540 parejas interobjeto** mediante Canny + HOG + coseno, penalizando diferencias de aspecto. Se seleccionaron las **12 mejores parejas sin reutilizar componentes**. Sus scores son semejanzas geométricas (la primera: 0,829), no probabilidades paleográficas.

Limitaciones: componentes no equivalen necesariamente a glifos completos; se trabajó con dibujos editoriales, **no fotografías arqueológicas del original**; no se asignaron valores latinos, traducciones ni identificaciones visuales verificadas independientemente; no hay resultado HOLD ciego. Se conservaron posiciones de las fuentes, SHA256, recortes y resultados detallados.

El paquete local `IBEROS_DRAWING_ASSOC_14.zip`, generado en la conversación, contiene el código ejecutado, `components.csv`, `cross_object_candidates.csv`, 47 recortes, hoja de 12 parejas, overlays y manifiesto. No subir material gráfico editorial al GitHub público sin resolver derechos.

**Siguiente paso:** revisión paleográfica de contornos completos y predicción congelada antes del cotejo con lectura editorial; después contraste de fotografías independientes, control negativo y evaluación por `PHYS_ID/LEAK_GROUP`.

Core oficial, C594/C474/C539/C541 y FULL3406: sin cambios.
