# IberOS — Reconciliación de métricas históricas y actuales
Fecha: 2026-10-13
Estado: contraste parcial, pendiente de registros históricos completos.

## Conclusión
Los números 60 %, 62,2 %, 70,8 % y 98 % coexisten en `OFFICIAL_METRICS` (src/iberos/core.py) porque se refieren a indicadores distintos. No existe base para deducir regresión ni progreso neto comparándolos directamente. Tampoco existe evidencia aquí de que los porcentajes iniciales hayan sido idénticos a la escala de la release actual.

## Cuadro de equivalencias verificadas
| Indicador | Valor | Denominador/definición que figura | Naturaleza | Comparabilidad |
|---|---:|---|---|---|
| CORE | 27/45 = 60,0 % | 45 unidades del indicador congelado | Estado científico interno de release | Solo comparable con otras versiones de la misma rúbrica de 45 |
| CORE + INFER | 28/45 = 62,2 % | 45 unidades del indicador congelado | Estado ampliado con INFER | No mezclar con CORE estricto |
| ICS_global | 70,8 | Definición histórica detallada no establecida en esta auditoría | Indicador congelado de release | Comparabilidad histórica no demostrada |
| INFER_progress | 98 | Sin denominador expresado en `OFFICIAL_METRICS` | Progreso interno de inferencia | No equiparable a desciframiento ni CORE |
| ROK / KA_KE / SALIR / KUTUR / BAIDES_BATIR | 75 cada uno | Métrica interna de familia | Estado de release, no cierre léxico | No equiparable a precisión lingüística |
| D_E_I | 50 | Métrica interna de familia | Estado de release con gate exacto abierto | No equiparable a traducción |
| Benchmark | 38 objetos, 37 unidades independientes, 4 excluded controls | Registro curado público v1.0.1 | Cobertura documental y controles | No es porcentaje científico |
| CORE original de primeras conversaciones | No verificado | Falta serie histórica con definición y fecha | Histórica | No comparable hasta recuperar actas/archivos |

## Investigación pendiente
1. Recuperar de archivos o mensajes de los primeros hilos los porcentajes literales, fecha, versión, rúbrica, denominador y evidencia.
2. Identificar si `ICS_global` e `INFER_progress` estaban calibrados con el mismo universo de objetos y protocolos que CORE 27/45.
3. Crear una tabla histórica de *versiones y definiciones*, no solo valores.
4. Validar que la migración al paquete público no descartó resultados científicos autorizados. No promover datos anteriores sin trazabilidad.
5. Solo publicar un **avance global único** si se define expresamente un denominador estable, criterios de puntuación y mecanismo de revisión.

## Principio de conservación
No cambiar `OFFICIAL_METRICS`, C594/C474/C539/C541 ni gates semánticos a partir de esta auditoría de metadatos. 60 % no significa 60 % del ibérico descifrado; 98 % INFER tampoco. Los nuevos tests e interfaces miden capacidad técnica, no cierre científico.

## Evidencia consultada
- `src/iberos/core.py` → `OFFICIAL_METRICS`, `AUTHORITY`
- `docs/BENCHMARK.md` → métricas congeladas y restricciones
- `docs/ARCHITECTURE.md` → alcance y separación entre core y web
- `docs/PROJECT_SYNC_2026-10-13.md` → estado entre hilos, con límites de acceso.

## Comprobación histórica adicional del código (2026-10-13)

Se han leído `src/iberos/core.py` en cuatro revisiones anteriores de GitHub:

- `1d8d416a238f8650c4c6ef6da3f87eadcc12418d`
- `03cb8378f404ab68d8802687df526d62e262d4cf`
- `b046cb7cc8c5b0ea5fa015e833d019bac56d5c01`
- `a11aa9f09a8fd8445625fcaa5a95ecb2470a8b7e`

Las cuatro contienen los mismos valores de `OFFICIAL_METRICS`: `CORE=27/45=60.0%`, `CORE_plus_INFER=28/45=62.2%`, `ICS_global=70.8`, `INFER_progress=98`, familias ROK/KA_KE/SALIR/KUTUR/BAIDES_BATIR=75 y D_E_I=50.

**Resultado:** la discrepancia no parece haberse producido por las últimas modificaciones del módulo de reconstrucción. **Límite:** esto no verifica las métricas originales anteriores a dichas revisiones ni identifica la rúbrica detallada de ICS/INFER. No se ha demostrado regresión científica.

### Serie verificable (sin inventar fechas ni porcentajes)

| Fuente de versión | CORE | CORE+INFER | ICS | INFER | Naturaleza |
|---|---|---|---|---|---|
| 4 revisiones históricas señaladas arriba | 27/45 | 28/45 | 70.8 | 98 | Código GitHub, igualdad comprobada |
| CORE público main, 2026-10-13 | 27/45 | 28/45 | 70.8 | 98 | Código actual |
| IberOS anterior a los archivos rastreados | Sin verificar | Sin verificar | Sin verificar | Sin verificar | Requiere expediente histórico fuente |

Próxima evidencia necesaria: actas, exportaciones o documentación originales que incluyan las métricas históricas, sus denominadores y fechas. No cambiar la autoridad congelada sin esa comparación.
