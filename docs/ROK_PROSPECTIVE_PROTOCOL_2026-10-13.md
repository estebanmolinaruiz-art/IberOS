# ROK-SEGMENTATION-PROSPECTIVE-01
Fecha: 2026-10-13. Estado: protocolo de evaluación **experimental**; no sustituye ROK-RECIPIENT-02 ni altera autoridad C594/C474/C539/C541.

## Hipótesis rivales
- H1: NP + TE y ROK como elemento formal separado; destinatario/beneficiario solo si se fija con evidencia externa.
- H2: TE pertenece a `terokan` o a otra segmentación de bloque; no atribuimos papel al NP por morfología sola.
- H3: la distribución ROK refleja un formulario o género epigráfico, sin forzar semántica de transferencia.

## Datos mínimos por inscripción
`witness_id`, `physical_id`, `source`, `passage`, `lock_id`, `lock_hash`, `prediction_id`, `prediction` (H1/H2/H3), `segmentation`, `external_role`, `external_role_source`, `independent_context`, `held_out`, `reading_secure`, `genre`, `control_type`.

El verificador `assess_rok_prospective` necesita al menos un candidato TARGET y un testimonio control NON_ROK/NEGATIVE con identidad física distinta y procedencia declarada. Rechaza repeticiones exactas de `physical_id`, roles no anclados en TARGET, registros incompletos y predicciones ajenas al protocolo.

## Límites obligatorios
La inclusión de `lock_hash`, `source` o `external_role_source` es declarativa: el software **no** acredita que el registro se realizara antes de observar el texto, que un hash corresponda a una fuente fechada, ni que el papel externo esté demostrado. Tampoco comprueba todavía grafos transversales PHYS/LEAK ni dependencias interedición de forma exhaustiva.

La salida `READY_FOR_INDEPENDENT_REVIEW` significa exclusivamente que los campos y controles mínimos están completos. No es `PASS`, no cierra ROK-RECIPIENT-02, no da porcentaje de desciframiento ni modifica la puntuación CORE. Los fixtures sintéticos prueban ingeniería, no lingüística.

## Próximas pruebas de investigación real
1. Revisar foto/edición y segmentación de C.21.10 y Orleyl por separado, sin adjudicar destinatario.
2. Buscar controles documentales de NP+TE con y sin ROK en géneros comparables.
3. Exigir a dos revisores independientes anclajes no lingüísticos de papel antes de contrastar H1/H2/H3.
4. Vincular la identidad física con LEAK_GROUP y Dependency_Group mediante el auditor de reconstrucciones.
5. Mantener ROK exacto OPEN hasta cumplir el gate oficial y una revisión humana de nueva evidencia.
