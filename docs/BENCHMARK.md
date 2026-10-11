# IberOS Curated Benchmark v1.0.1

**Estado:** reproducible / public benchmark snapshot  
**Software:** IberOS Open Research Kit v1.0.1  
**Fecha:** 2026-10-11  
**Ámbito:** capa pública curada de 38 objetos

## Objetivo

Este benchmark verifica propiedades reproducibles del sistema IberOS: integridad del registro, independencia documental, control de fugas, conservación de gates abiertos, controles negativos y consistencia con la autoridad científica congelada.

No mide “porcentaje de lengua ibérica descifrada” y no convierte los indicadores internos de release en precisión lingüística.

## Datos públicos

Fuente canónica:

- `data/curated/iberos_objects_registry_v2.0.csv`
- `data/curated/iberos_curated_objects_v1.jsonl`
- documentación de gates en `docs/`
- implementación en `src/iberos/core.py`

La capa curada contiene **38 objetos**:

- 20 `INCLUDE`
- 9 `CONTROL_ONLY`
- 4 `EXCLUDED_CONTROL`
- 5 `CONDITIONAL`

La auditoría de independencia produce **37 unidades documentales independientes**. Un par se colapsa por compartir el grupo específico `LATOUR_SAME_LOCALITY`.

La capa histórica de 3.406 ENTRY permanece **LEGACY / FROZEN** y no se presenta como equivalente al benchmark público curado.

## Protocolo reproducible

Entorno de referencia: Python 3.12.

```bash
python -m pip install -e . pytest
pytest -q
python scripts/benchmark_snapshot.py --output /tmp/benchmark.json
diff -u data/benchmark/benchmark_results_v1.0.1.json /tmp/benchmark.json
```

El workflow `.github/workflows/benchmark.yml` ejecuta exactamente esa secuencia en GitHub Actions.

## Reglas de independencia y fuga

Prioridad de identidad documental:

`PHYS_ID > LEAK_GROUP > Dependency_Group específico > OBJECT_ID`

Las etiquetas genéricas como `INDEPENDENT_OR_UNRESOLVED` o `DEPENDENT_COPY` no se usan como identidad compartida.

Si una misma unidad aparece en más de un split, la política congelada es:

`HOLD > VAL > TRAIN`

Una unidad documental cuenta como máximo una vez para evidencia independiente.

## Snapshot de resultados v1.0.1

El resultado machine-readable está en:

`data/benchmark/benchmark_results_v1.0.1.json`

Resultados principales:

| Indicador | Resultado |
|---|---:|
| Objetos curados | 38 |
| Unidades independientes | 37 |
| Registros colapsados por dependencia | 1 |
| INCLUDE | 20 |
| CONTROL_ONLY | 9 |
| EXCLUDED_CONTROL | 4 |
| CONDITIONAL | 5 |
| Gates exactos cerrados para 7/8/9 | 0 |
| Promoción automática a CORE | No |

### Gates que permanecen abiertos

- **ROK:** ningún candidato supera todavía el gate prospectivo de dirección/rol.
- **KA/KE/KU:** ningún candidato fija aún dirección transaccional de forma independiente.
- **SALIR:** no existe todavía pass prospectivo que cierre el gate semántico estrecho.
- **KUTUR:** el gate prospectivo permanece abierto.
- **BAIDES/BATIR:** la oposición funcional se conserva, pero los rótulos institucionales exactos siguen abiertos.
- **NUM 7/8/9:** no hay valores exactos cerrados en el dashboard.
- **D(E/I):** el complejo morfológico se conserva; la variable gramatical exacta sigue abierta.

## Resultados negativos y adversariales

Los negativos forman parte del benchmark, no se eliminan:

- 4 registros están marcados `EXCLUDED_CONTROL`.
- Los controles incluyen pseudoescritura y falsificaciones/copias dependientes.
- **C.1.8 / SORSE** no puede utilizarse como ancla física para `SORSE=8`; el gate correspondiente se mantiene fallido para ese objeto.
- Los ejemplos sintéticos de tests sólo prueban la lógica del software y **no** cuentan como evidencia científica.
- Ningún gate estructural produce promoción automática a CORE.

## Indicadores congelados

La implementación expone los indicadores de release ya autorizados, entre ellos:

- ICS_global = 70.8
- ROK = 75
- KA_KE = 75
- SALIR = 75
- KUTUR = 75
- BAIDES_BATIR = 75
- D_E_I = 50
- CORE = 27/45 = 60.0%
- CORE + INFER = 28/45 = 62.2%

Estos valores son **indicadores internos de estado de release**, no porcentajes de desciframiento ni medidas de exactitud frente a una “traducción verdadera” conocida.

## Criterio de éxito del benchmark

El benchmark v1.0.1 pasa si:

1. todos los tests automatizados pasan;
2. el snapshot regenerado es byte-equivalente al JSON versionado;
3. el registro mantiene 38 objetos;
4. la auditoría mantiene 37 unidades independientes;
5. los controles negativos siguen presentes;
6. los gates declarados abiertos permanecen abiertos salvo una nueva decisión científica explícita y versionada.

## Límites

- No existe ground truth completo para la lengua ibérica.
- El benchmark no evalúa traducción libre contra una referencia gold.
- La cobertura del corpus vivo Cathalaunia / Corpus Ibèrika es parcial.
- Los resultados no deben extrapolarse automáticamente a todas las inscripciones ibéricas.
- La validación externa independiente sigue siendo deseable para cualquier promoción científica.
- Un cambio de estado científico requiere nueva release, trazabilidad y justificación; nunca deriva automáticamente de un test técnico.

## Trazabilidad

Autoridad congelada:

- semantic release: `C594`
- prospective lock: `C474`
- technical floor: `C539`
- ROK network: `C541`

DOI del software v1.0.1: **10.5281/zenodo.22997623**

## Control separado de D(E/I)

`iberos dedi-benchmark evidencia.json` conecta la matriz formal con
`DEDI-COMBINED-GATE-01`. El JSON de entrada contiene `observations`,
`preregistered_rule`, `preregistration_id` y `preregistration_hash`.
Los campos de cada observación se documentan en
`src/iberos/core.py`: `evaluate_dedi_predictive_gate` y
`audit_dedi_prospective_provenance`.

El informe devuelve `formal_matrix` y `semantic_gate` por separado.
Reconocer la estructura no resuelve la oposición gramatical E/I. Evidencia
incompleta devuelve BLOCKED; evidencia documental y predictivamente completa
solo puede devolver AWAITING_INDEPENDENT_REVIEW con scientific_state UNVERIFIED.
Un resultado de software no es una validación epigráfica.

Los 38 objetos curados no se convierten automáticamente en HOLD prospectivo.
Las piezas utilizadas para construir las reglas siguen siendo retrospectivas.
Las pruebas sintéticas verifican controles del programa y no incrementan
D(E/I)=50 ni ninguna métrica oficial. Autoridad: C594+C474+C539+C541.
