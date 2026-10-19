# IberOS — Clasificación preliminar del signario Cathalaunia, 286 códigos
Fecha: 2026-10-19

**Fuente:** https://cathalaunia.org/Iberika/Signari , signario de la fuente iber.ttf v5.0.
**Inventario:** `data/review/cathalaunia_signary_source_codes_v5_2026-10-19.csv`.
**Clasificación derivada:** `data/review/cathalaunia_signary_candidates_286_v1.csv`.

## Resultado de la clasificación formal
Se han procesado 286 códigos fuente. Clasificación heurística basada únicamente en la **etiqueta alfanumérica** del catálogo, no en imágenes ni lecturas de inscripciones:
- 133: `SINGLE_LABEL_CANDIDATE` (etiqueta simple compatible con el inventario convencional).
- 115: `AMBIGUOUS` (signo de interrogación, varias etiquetas o valores alternativos).
- 23: `OTHER_OR_SPECIAL` (categorías distintas del inventario simple, incluidas señales especiales).
- 15: `NEEDS_MANUAL_REVIEW` (signos no reconocidos inequívocamente por la regla simple).

**IMPORTANTE:** Estas cuatro clases son de **triaje informático** y pueden contener errores de clasificación, especialmente el tratamiento de mayúsculas, dualidades y signos no alfabéticos. No son clases paleográficas confirmadas. El campo `value_candidate` NO constituye lectura verificada; todos los registros mantienen `activation_status=NOT_VERIFIED`.

## Qué NO se ha realizado
- Ninguna activación de equivalencias para lectura automatizada.
- Ninguna verificación individual de trazos/grabados o cotejo de fotografías.
- Ningún diccionario de Huertas derivado por analogía de esta tabla.
- Ninguna observación positiva o negativa sobre TE revisada y localizada a línea física.
- Ningún conjunto HOLD prospectivo puntuable.

## Siguiente trabajo
1. Segundo revisor coteja cada uno de los 133 candidatos simples con el signario original, variantes duales y bibliografía; registra decisión explícita y fuente.
2. Resolver 115 ambiguos por imagen y edición, manteniendo múltiples candidatas cuando sea necesario.
3. Registrar sistemáticamente cambios de signo entre diferentes fuentes y codificaciones.
4. Vincular líneas editoriales a objeto físico, edición, cara, renglón e incertidumbre; empezar por fuentes con derechos claros.
5. Preinscribir hipótesis TE exacta y baselines; bloquear HOLD hasta que exista aislamiento documental demostrable.

## Cierre VALIDATION-01
**NO EVALUADO.** El inventario no representa evidencia de rendimiento predictivo. La subtarea «clasificación formal de etiquetas del signario» queda terminada; la revisión científica y validación lingüística siguen abiertas.
