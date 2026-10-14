# Inventario de reglas del CORE — 14/10/2026

## Alcance verificable
El nuevo módulo `src/iberos/rule_catalog.py` devuelve un registro estructurado y trazable de **12 entradas**: 4 guardas activas del motor `ACTIVE_PROTOCOLS`, 7 familias sometidas a evaluación prospectiva (6 definidas en `FAMILY_GATE_POLICIES` y D(E/I), codificada aparte) y 1 protocolo de investigación rival ROK.

Este inventario **no es un conteo exhaustivo de todas las condiciones de código ni representa 12 reglas de traducción confirmadas**. Los métodos de independencia, corpus, lectura, reconstrucción y análisis de riesgos también implementan lógica, pero no deben sumarse arbitrariamente a «reglas de desciframiento». No hay actualmente reglas del catálogo certificadas como traducciones semánticas exactas (`verified_translation_rules=0` en el ámbito estricto del registro, no negación de toda la investigación sobre la lengua ibérica).

## 4 guardas científicas activas
- `BI-DISAMBIG-01`: lectura numeral dependiente de contexto cuantitativo independiente.
- `PALEO-RHOTIC-LOCK-01`: preservar R/R1 para identidad, agrupación y promoción.
- `ROK-DIRECTION-GUARD-01`: prohibir asignar dirección de transferencia ROK sin pruebas.
- `EPISTEMIC-LAYER-01`: separar evidencia de hipótesis e interpretación.

## 7 gates prospectivos / familias
SALIR; ROK; KA/KE/KU; KUTUR; BAIDES/BATIR; numerales/medidas; D(E/I). Los identificadores de registro no pretenden sustituir los nombres congelados de los gates científicos de referencia. Todos permanecen OPEN para su resolución semántica estrecha.

## 1 protocolo adicional de falsación
`ROK-SEGMENTATION-PROSPECTIVE-01`: H1/H2/H3, controles y trazabilidad; ninguna hipótesis se eleva automáticamente.

## Volumen de información pública
Benchmark v1.0.1: 38 objetos curados (20 INCLUDE, 9 CONTROL_ONLY, 4 EXCLUDED_CONTROL, 5 CONDITIONAL), 37 unidades documentales independientes. Las 3.406 entradas históricas LEGACY están congeladas y no equivalen a 3.406 testimonios independientes analizados. Indicadores C594/C474/C539/C541 sin cambios; CORE 27/45, CORE+INFER 28/45. No son porcentajes descifrados.

## Uso
```python
from iberos import rule_catalog
report = rule_catalog()
print(report["counts"])
for rule in report["entries"]:
    print(rule["id"], rule["kind"], rule["validation"])
```

## Pendiente para catálogo exhaustivo
Descomponer cada función del CORE en reglas atómicas verificables (condición, evidencia, falsador, salida, versión y pruebas), revisar el mapeo de identificadores exactos con su documentación histórica y agregar referencias bibliográficas por regla. La primera versión contabiliza solamente entradas asociadas explícitamente a estructuras versionadas de código; no pretende medir exhaustivamente la potencia del desciframiento.

## Integridad
`tests/test_rule_catalog.py` protege conteo relativo, unicidad, ausencia de promoción y congelación de indicadores. Las pruebas nuevas quedan sujetas a validación CI posterior a su commit.
