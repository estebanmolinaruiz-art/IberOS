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

## Refuerzo de controles de independencia — 2026-10-14
El módulo prospectivo añade comprobaciones de grupos `LEAK_GROUP` y `Dependency_Group` específicos compartidos por testigos que alegan distintas identidades físicas. La detección produce BLOCKED, no REVIEW. Las etiquetas genéricas `INDEPENDENT_OR_UNRESOLVED` y `DEPENDENT_COPY` no se usan como identidades compartidas. Tests adversariales incorporados.

**Limitación:** se trata de detección directa entre parejas con un mismo identificador; no reemplaza una auditoría completa de componentes conexas ni una comprobación arqueológica de la procedencia. La entrada aún es declarativa. Los nuevos commits necesitan confirmación CI específica. El gate oficial ROK continúa OPEN y no hay modificación de porcentajes.

## Control de componentes transitivas — 2026-10-14
`assess_rok_prospective` agrupa ahora los registros con componentes conexas creadas por `physical_id`, `LEAK_GROUP` y grupos `Dependency_Group` específicos. Por ejemplo, A conectado a B mediante LEAK y B conectado a C mediante un grupo específico impide contar A y C como independientes. El resultado proporciona `documentary_components` y `documentary_unit_count`; dependencias repetidas llevan a `BLOCKED`. Se añaden pruebas de puente transitivo y fuentes separadas.

El catálogo y las identidades siguen siendo **declarativos** y los resultados de pruebas sintéticas no convalidan autenticidad ni independencia real. La ejecución de GitHub Actions para estos commits todavía debe comprobarse. El gate científico oficial ROK-RECIPIENT-02 sigue OPEN.

## Tres dimensiones de independencia — 2026-10-14

- **Identidad física:** `physical_id` repetido implica una sola unidad; diferentes `physical_id` pueden representar piezas diferentes.
- **Dependencia textual:** `TEXT_DEPENDENCY_GROUP` idéntico conecta las ediciones y bloquea su cómputo como corroboraciones independientes, aunque sean objetos físicos distintos. `LEAK_GROUP` y grupos específicos también conectan registros de forma transitiva.
- **Contexto arqueológico:** `archaeological_context` compartido queda registrado en `shared_archaeological_contexts` y activa `context_independence_review_required`, **sin fusionar automáticamente** objetos físicamente separados.

Pruebas añadidas con identificadores ilustrativos Orleyl F.9.5/F.9.7 y copia textual Marsal: verifican el comportamiento del software, no la identificación física definitiva de estas piezas. No introducir controles `EXCLUDED_CONTROL` como evidencia positiva aunque se pueda simular un par de dependencia en tests.

La salida `READY_FOR_INDEPENDENT_REVIEW` no certifica independencia arqueológica ni lectura; exige auditoría humana. ROK-RECIPIENT-02 sigue OPEN.
