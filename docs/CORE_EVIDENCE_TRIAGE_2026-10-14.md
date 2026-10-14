# IberOS: bandeja de verificación de evidencias por inscripción

La nueva función `build_evidence_triage()` en `src/iberos/evidence_triage.py` lee el registro curado y **selecciona candidatos de revisión** mediante coincidencias exactas de etiquetas familiares ROK, SALIR, BI/BIN y KA/KU. Es un índice para localizar trabajo pendiente: **no** identifica pasajes, confirma variantes, ni ejecuta el CORE por inferencia de metadatos.

Cada tarea registra `OBJECT_ID`, referencia epigráfica, fuente bibliográfica de ficha si existe, reglas potenciales y cuatro requisitos: transcripción diplomática exacta, relación entre pasaje y regla, identidad/independencia de testimonio, y anclaje semántico o direccional externo. Todos los candidatos nacen con `source_verified_for_rule=false`, `eligible_for_technical_execution=false`, `automatic_core_promotion=false`.

El exportador de la web añade `site/data/core_evidence_triage_v1.json` al artefacto de despliegue. El fichero sigue siendo **lista de revisión**, nunca archivo de aprobaciones. Para ejecutar reglas por pieza debe incorporarse una observación con fuente y revisión individual a la vía `evaluate_reviewed_observations`, tras verificar el pasaje en la fuente.

Limitación: las inscripciones con familias no etiquetadas o etiquetas alternativas pueden quedar fuera; la ausencia en la cola **no descarta** relevancia científica. Ni GitHub Actions ni el generador de triaje sustituyen la revisión epigráfica. La versión científica C594/C474/C539/C541 no cambia.
