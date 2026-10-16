# IberOS — propuestas de dominios semánticos bajo control (16-10-2026)

El módulo `src/iberos/semantic_hypothesis_engine.py` añade `suggest_semantic_domains(object_id,segments)` a la capa interpretativa del CORE. Esta función no traduce signos ni textos: propone **dominios semánticos hipotéticos** únicamente para formas cuya lectura haya sido marcada como revisada por un proceso editorial externo y que aporten `reading_source`.

El catálogo inicial contiene reglas limitadas a ROK (función relacionada con transferencia, dirección desconocida), SALIR (ámbito económico/valor en contraste), KUTUR (escritura/formulario en contraste) y BI/BIN (restricción contextual cuantitativa). Para BI/BIN sin un indicador explícito de cuantificación independiente, el resultado debe abstenerse de valor numeral.

El sistema no identifica automáticamente palabras dentro de una transcripción libre ni garantiza que `reading_reviewed=true` sea auténtico: es un contrato con el sistema de revisión. Ninguna sugerencia se convierte automáticamente en significado seguro, traducción parcial o traducción final. `possible_full_translation=null`, `meaning_validated=false` y `automatic_core_promotion=false`.

**Próxima mejora:** enlazar las lecturas verificadas de la biblioteca al motor, pasar las candidaturas a un examen por inscripción con fuentes/objeciones y mostrar aquellas que superen revisión editorial. Las fichas públicas no deben fabricar propuestas para objetos sin segmentos documentados.

Las autoridades C594/C474/C539/C541 permanecen intactas.
