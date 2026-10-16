# Publicación progresiva: tanda de fichas 2026-10-16

En el archivo `site/data/ficha-enrichment-1.json` aparecen las cuatro primeras prioridades: tinajilla Ballesta, vaso de Llíria, signario Castellet de Bernabé, inscripción La Joncosa. De estas, solo **IBR-CER-0001** tiene actualmente `citation` no vacía que acompaña `evidence`, `hypothesis` y `limits`.

El generador `scripts/export_web_core.py` consulta ahora también los cinco ficheros de enriquecimiento de fichas, sin sobrescribir las seis entradas preferentes, e incorpora los expedientes no destacados que cumplen el requisito mínimo editorial. En la presente tanda son tres: **IBR-CER-0001 (Ballesta), IBR-PLM-0005 e IBR-PLM-0006**. Suman nueve hipótesis editoriales recuperadas a partir de material ya existente; NO son nuevas hipótesis descubiertas automáticamente ni nuevas pruebas independientes.

Los tres documentos pendientes en la primera tanda —Llíria, Castellet de Bernabé y La Joncosa— conservan bibliografía general y comentarios, pero `citation` vacía. No se les atribuye una cita específica sin cotejar la relación entre la afirmación y el estudio correspondiente. Continúan visibles como piezas documentales en espera de cierre editorial.

El estado `PUBLICABLE_EDITORIAL` indica exclusivamente presencia de ficha registrada y campos editoriales documentados. No certifica transcripciones, datos físicos, licencias de imágenes ni significados. El export mantiene `translation_validated=false` y `meaning_validated=false`.
