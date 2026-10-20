# IberOS CORE — Acta de inicio de los seis pilares

**Fecha de inicio:** 2026-10-20
**Identificador:** CORE-6P-START-2026-10-20
**Estado:** INICIADO — DESARROLLO Y VALIDACIÓN PENDIENTES
**Ámbito:** motor científico IberOS CORE; la implementación y publicación web son líneas separadas.

## Objetivo verificable
Integrar la evidencia paleográfica, lingüística, simbólica, arqueológica y documental en hipótesis evaluables, con controles negativos y validación independiente, sin promover lecturas o traducciones por mera automatización.

## Seis pilares y entregables mínimos
1. **Paleografía**: registro por signo con imagen, hash, geometría, lectura editorial y lectura revisada, alternativas y revisión independiente.
2. **Hipótesis lingüísticas**: catálogo versionado de hipótesis, predicciones, condiciones de refutación y dependencias.
3. **Tradición simbólica**: vínculos de motivos/signarios con fuente, soporte, lugar, datación e incertidumbre; semejanza no implica significado ni tradición demostrada.
4. **Validación independiente**: preregistro y HOLD por objetos/grupos dependientes, baseline, controles negativos, scoring ciego y réplica.
5. **Corpus**: identificadores únicos, testimonios físicos distinguidos de publicaciones, fuentes y licencias documentadas, trazabilidad de procedencia.
6. **Laboratorio**: informes reproducibles que preserven capas de evidencia, alternativas, niveles de confianza, fallos y versiones del software.

## Base existente: reutilizar, no duplicar
- [Plan integrado](CORE_SIX_PILLAR_EXECUTION_PLAN_2026-10-20.md)
- [Instrumento de auditoría](../scripts/audit_core_six_pillars.py)
- [Pruebas de auditoría](../tests/test_audit_core_six_pillars.py)
- [Orleyl como tarea única](CORE_ORLEYL_SINGLE_TRACK_2026-10-19.md)
- [VALIDATION-01](IBEROS_VALIDATION_01.md)
- `src/iberos/multimodule.py` y `src/iberos/semantic_hypothesis_engine.py`

## Hitos y criterios de cierre
| Clave | Entregable | Criterio de aceptación | Estado |
|---|---|---|---|
| 6P-01 | Auditoría reproducible del estado real | Ejecutada sobre el commit fijado, informe con recuentos y bloqueos | PENDIENTE |
| 6P-02 | Contrato compartido de evidencia | Esquema de datos con fuente, objeto, signo y estado; tests de casos inválidos | PENDIENTE |
| 6P-03 | Corpus enlazado | IDs sin colisiones, referencias a objetos independientes, faltantes visibles | PENDIENTE |
| 6P-04 | Integración PALEO / MORPH / ICONO | Misma unidad de evidencia; inferencias separadas y trazables | PENDIENTE |
| 6P-05 | Piloto prospectivo | Predicciones selladas, HOLD sin filtraciones, controles y baseline | PENDIENTE |
| 6P-06 | Informe reproducible | Código, hash de fuente, hipótesis, resultado y limitaciones documentados | PENDIENTE |

## Regla de avance
Un hito pasa a HECHO solo con ejecución verificable, artefactos y pruebas pertinentes. El cumplimiento técnico no implica validez lingüística o semántica.

## Límites de partida
- Orleyl: la lectura editorial de `BITEROKETETINE` / `BITEROKETINE` está documentada; identidad gráfica independiente y valor morfológico de TE pendientes.
- `ROK-RECIPIENT-02` permanece abierto.
- No atribuir significados demostrados, no reclamar desciframiento y no aumentar métricas por recuentos de candidatos automáticos.
- No se modifica la web pública por esta acta.

## Próxima acción única
Ejecutar `python scripts/audit_core_six_pillars.py --out data/review/core_six_pillar_audit_latest.json` desde un checkout actualizado, revisar el resultado y empezar 6P-02, reutilizando las estructuras existentes.
