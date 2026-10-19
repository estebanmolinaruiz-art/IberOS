# VALIDATION-01 — Adquisición primaria Orleyl, lote 01 (2026-10-19)
Fuente primaria identificada: *Materiales de la necrópolis ibérica de Orley (Vall d'Uxó, Castellón)*, accesible desde el museo: https://mupreva.org/web_mupreva_dedalo/publicaciones/101/va

Se localizó una discusión editorial de VII-B-15 donde se menciona `-TE`, y pasajes colindantes VII-B-16 así como referencias a Orleyl V-26. La extracción textual disponible del original presenta corrupción de caracteres y no permite reconstruir con seguridad signos y líneas completas.

Datos de trabajo: `data/review/validation01_orleyl_primary_candidate_batch01.csv`. Son tres localizadores editoriales; **0 lecturas atómicas verificadas**, **0 líneas admitidas al piloto**, **0 objetos HOLD**. Las dos entradas VII-B pertenecen a un mismo objeto físico.

Para admitir una línea:
1. Recuperar la página y lámina o fotografía primaria correspondientes, localizar cara, línea y número editorial.
2. Verificar cada signo con la lectura publicada, registrando lagunas, alternativas y escritura.
3. Dos revisiones cuando proceda; consignar `independent_reviewer`, `full_line_reviewed=YES` solo tras inspección, no por OCR.
4. Transcribir cada signo en tokens atómicos separados. `te` no es `t` + `e`.
5. Registrar como DEVELOPMENT (Orleyl ya fue usado en la hipótesis). Nunca convertirlo en HOLD nuevo.
6. Ejecutar `validation01_te_mask_pilot.py` cuando al menos una línea cumpla los requisitos. El modelo IberOS y baselines todavía necesitan una interfaz predictiva comparada.

Ninguna lectura o glosa se ha promovido de este lote. Estado VALIDATION-01: NOT_EVALUATED.
