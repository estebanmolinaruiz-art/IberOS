# IberOS — comparador de predicciones y hallazgos externos (14-10-2026)

Módulo `src/iberos/prediction_compare.py`, API `compare_prediction(prediction, finding, assessment)`.

**Registros exigidos:** predicción `id`, `source_url`, fecha `fixed_on` y marca opcional `preregistered`; hallazgo `id`, `source_url`, `published_on`; valoración humana explícita `verdict` = SUPPORTS / CONTRADICTS / UNCLEAR, `independence`, `contamination_free` y `evidence_note`.

La salida siempre conserva `scientific_state=AWAITING_INDEPENDENT_REVIEW`, `strict_prospective_pass=false`, `automatic_core_promotion=false`. La mera cronología de fechas suministradas no demuestra prioridad documental o registro prospectivo. El comparador etiqueta convergencia externa declarada cuando hay apoyo, independencia y ausencia de contaminación declaradas; oposición independiente como FAIL; cualquier dato decisivo sin demostrar como INDETERMINATE. Es una **clasificación provisional de trabajo**, no una declaración de pase científico. Si el trabajo externo ya precedía a la predicción se etiqueta RETROSPECTIVE_REPLICATION, incluso si hay acuerdo.

Las pruebas unitarias cubren coincidencia, contradicción, independencia no acreditada y fecha inválida. Un control externo debe confirmar las marcas suministradas antes de aceptar una convergencia.

**Siguiente avance científico concreto:** construir predicciones preregistradas específicas y criterios falsables para los contrastes `BI/BIN`, `KA/KE/KU`, `ROK`, `SALIR` y `D(E/I)` con hashes y documentos de fecha verificable; extraer de los artículos externos resultados precisos y falsadores en lugar de buscar palabras coincidentes. Dar prioridad a refutaciones y a casos no utilizados para formular las reglas.

**No se ha declarado nueva validación lingüística** ni alterado C594, C474, C539 o C541; `ROK-RECIPIENT-02=OPEN`.

## Mejora de integridad de predicciones — 2026-10-14

La versión ampliada de `compare_prediction()` añade `statement`, `statement_sha256` y `timestamp_evidence_url` opcionales. Comprueba localmente la coincidencia SHA-256 exacta del texto UTF-8 y conserva `documentary_priority_candidate` únicamente si el texto coincide, declara preregistro, aporta enlace temporal HTTPS y `fixed_on < published_on`. Todos los enlaces de predicción y hallazgo deben emplear HTTPS.

**La concordancia de hash NO acredita por sí sola que el contenido existiera en la fecha alegada:** es necesaria una revisión independiente de la marca temporal, del contenido archivado y de la secuencia documental. Por ello `timestamp_evidence_checked_independently=false` y `strict_prospective_pass=false` incluso para candidatos completos. Las comparaciones semánticas siguen siendo valoraciones explícitas pendientes de comprobación externa.

Se añadieron pruebas contra modificación de texto con hash antiguo, enlaces inseguros y falsas declaraciones de validación prospectiva. No se ha certificado ningún hallazgo externo como predicción anticipada de IberOS ni se han cambiado los indicadores oficiales.
