# IberOS — auditoría de reglas por objeto (2026-10-14)

El nuevo módulo `src/iberos/object_rule_audit.py` implementa `audit_object_rules(OBJECT_ID)` enlazando registro curado, `rule_catalog()` y `research_pipeline()`.

Para cada objeto curado muestra las 12 entradas catalogadas, las familias declaradas en `Familias_Tags`, el estado de los seis módulos GEO/PALEO/MORPH/LEXSEM/TRACE/INFER y el origen documental. Los estados de aplicabilidad son `GENERAL_GUARD_AVAILABLE`, `CANDIDATE_FROM_REGISTRY_TAGS` o `NOT_EVALUATED_FOR_OBJECT`.

Importante: las coincidencias de etiquetas son heurísticas de **enrutamiento para revisión**, no reconocimientos paleográficos, ejecuciones de reglas, demostraciones de fenómenos morfológicos ni traducciones. Por ello los campos `rule_passed=null`, `evidence_verified=false` y `semantic_translation_verified=false` no cambian aunque haya coincidencia nominal.

API:
```python
from iberos import audit_object_rules
report = audit_object_rules("IBR-PLM-0002")
print(report["families_tagged"])
print(report["rules"])
```

`tests/test_object_rule_audit.py` verifica exposición de las doce entradas, seis módulos, ausencia de promoción y rechazo de objetos desconocidos. Las pruebas técnicas no son evidencia científica nueva.

**Siguiente salto funcional:** implementar ejecutores puros por protocolo con entradas epigráficas explícitas (lectura, datación, dependencia, split, indicadores cuantitativos) y salidas tipadas `BLOCKED`/`UNVERIFIED`/`REVIEW`. Sin lectura auténtica segura, ninguna regla debe declararse aplicada con éxito. Métricas oficiales C594/C474/C539/C541 congeladas.
