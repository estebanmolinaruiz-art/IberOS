# IberOS — ejecución real controlada de reglas BI y ROK

Implementación 2026-10-14: `src/iberos/rule_execution.py`, interfaz `execute_rules(observation)`.

A diferencia del catálogo de aplicabilidad, este módulo **ejecuta funciones existentes de evaluación**. Actualmente solo admite `BI-DISAMBIG-01` y `ROK-DIRECTION-GUARD-01`. Otros protocolos siguen pendientes de ejecutores específicos; no se infieren rasgos a partir de metadatos ni de nombres del objeto.

Cada observación requiere `source_reference` (fuente declarada). Para BI exige dos booleanos explícitos `independently_quantitative`, `verbal_complex`; si se alega contexto cuantitativo, también `quantitative_source_reference`. **No se valida automáticamente la calidad de esa referencia externa**, por lo que la salida es `EVALUATED_NOT_SEMANTICALLY_VERIFIED`, nunca prueba científica. Falta de evidencias: `BLOCKED`. ROK reutiliza el guard existente y conserva `give`, `deliver`, `receive` y `assign` como `PROBABLE_OPEN`, no traducciones.

Ejemplo exclusivamente sintético:
```python
from iberos import execute_rules
print(execute_rules({
    "source_reference": "Manual epigráfico pendiente de revisión",
    "rules": ["BI-DISAMBIG-01", "ROK-DIRECTION-GUARD-01"],
    "independently_quantitative": False,
    "verbal_complex": True,
    "rok_literal": "receive",
}))
```

El motor mantiene C594 / C474 / C539 / C541, `scientific_state=UNVERIFIED` y `automatic_core_promotion=false`. Pruebas: `tests/test_rule_execution.py`. Próximo paso: ejecución de KA/KU con anclaje documental independiente, controles de róticas y trazabilidad de cada premisa.

## Segunda tanda — controles ejecutables KA y PALEO (2026-10-14)
El ejecutor admite ahora **4 reglas**. Se suman:
- `PALEO-RHOTIC-LOCK-01`: recibe `rhotic_purpose` y `rhotic_neutralized`; bloquea explícitamente la neutralización R/R1 para identidad documental, independencia, morfología y splits; admite búsqueda neutralizada con fin de recuperación. Sin entradas tipadas devuelve `BLOCKED`.
- `KA-DIRECTION-PROSPECTIVE-01`: recibe `ka_candidate_reference` correspondiente a una entrada **ya registrada** en `KA_DIRECTION_CANDIDATES`. Reutiliza su evaluación histórica y enumera las condiciones que faltan para fijar dirección. Un candidato no registrado o sin clave se bloquea; no se crean nuevas predicciones por pasar texto libre.

Este paso **no reconoce automáticamente KA ni las róticas sobre imágenes**, y no verifica fuentes, lectura o situación arqueológica del caso. Los metadatos de entrada no son resultados de autopsia. Todas las salidas mantienen `scientific_state=UNVERIFIED` y `automatic_core_promotion=false`. No se cierra KA ni ROK ni se modifican métricas. Pruebas nuevas en `tests/test_rule_execution.py`.
