# IberOS — Auditoría BI/BIN y SALIR (2026-10-14)

El módulo `src/iberos/bi_salir_audit.py` reúne el discriminador `BI-DISAMBIG-01` y la matriz prospectiva congelada `SALIR-PROSPECTIVE-01`. Sus cuatro contextos BI son casos **sintéticos de control** (ninguno es un hallazgo epigráfico). BI no se considera numeral sin contexto cuantitativo independiente, y en complejos verbales BI+D(E/I)+V no se asigna un numeral por defecto. Un contexto que declara simultáneamente `independently_quantitative=True` y `verbal_complex=True` debe resolverse fuera del discriminador.

Nueva protección en `src/iberos/rule_execution.py`: las observaciones con esos dos indicadores a la vez devuelven `BLOCKED / resolve_conflicting_context_flags`, sin adoptar valor numérico ni interpretación semántica. Esta regla de bloqueo afecta al ejecutor documentado, no reescribe ni reentrena `evaluate_bi_context` congelado.

Para SALIR se reutiliza `salir_prospective_candidate_matrix`; la regla continúa abierta. El caso Murcia 2026 presenta contexto económico externo pero no SALIR seguro; Pech-Maho 2025 y El Vilar 2024 no acreditan simultáneamente novedad post-C474 y anclaje económico independiente. Falsador: uso SALIR seguro, replicado, en un referente inequívocamente ajeno al ámbito económico/valor. No hay nuevos documentos analizados en esta tanda.

`new_external_evidence_checked=false`, `automatic_core_promotion=false`. Pruebas: `tests/test_bi_salir_audit.py` y el caso adversarial en `tests/test_rule_execution.py`. Estado científico oficial y métricas C594/C474/C539/C541 intactos.
