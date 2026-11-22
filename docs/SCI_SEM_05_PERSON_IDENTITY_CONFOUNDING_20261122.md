# SCI-SEM-05 — Auditoría de confusión por identidad personal y correcciones en La Bastida I

**Fecha:** 2026-11-22. **Estado: CONTROL ADVERSARIAL EJECUTADO**, no desciframiento confirmado. **Coste:** 0 €. Core/FULL3406 inalterados. Datos heredados sin retocar de `SCI-SEM-04`.

## Pregunta

¿El aparente contraste `-ka` vs `-ku` demuestra funciones transaccionales opuestas, o simplemente puede reflejar que **distintos individuos** participan en cuentas de distinta magnitud? Dato de partida: **19 renglones de una única lámina física** de Bastida I, editados por Ferrer i Jané (2026); cantidades en gramos **reconstruidas por modelo**, no mediciones arqueológicas de diecinueve pesas.

Fuentes: Ferrer i Jané (2026), «Algunes reflexions a propòsit del plom ibèric Bastida I: paleografia, metrologia i negoci», *Archivo de Prehistoria Levantina* XXXVI pp.133–166, [edición de acceso abierto](https://mupreva.org/web_mupreva_dedalo/publicaciones/1642/va), y [resumen de Ferrer con descripción del orden de operaciones](https://es.linkedin.com/posts/joanferrer_algunes-reflexions-a-prop%C3%B2sit-del-plom-ib%C3%A8ric-activity-7475065286451404800-WafR). Dataset de trabajo auditado: `data/review/sci_sem04_bastida_19_entries_ferrer2026.json`. **Limitación:** el dataset sigue codificando segmentaciones editoriales, no imágenes originales adjudicadas independientemente.

## Resultado revelador: confusión completa del sufijo con la identidad

**12 antropónimos diferentes** en el dataset, de los que **solo 2** llevan `-ku`:

- `aiduaŕgi`: dos observaciones `-ku`, **441 g** y **423,5 g**.
- `saldulako`: tres `-ku`, **423,5 g**, **504 g**, **441 g**.
- Ninguno de los otros **10 nombres** se presenta con `-ku`. Todas sus anotaciones están en `-ka`, incluidas las cuatro de `beŕśir`: **126, 35, 28, 549,5 g**.

**Número de nombres que aparecen con ambos sufijos = 0.** No existe ninguna comparación *dentro de la misma persona* que permita estimar un efecto independiente del morfema en este documento. Condicionar a la persona deja **cero intercambios de sufijos no triviales**; cualquier contraste «estadístico significativo de sufijo» ajustado por identidad personal está **no identificado**, no tiene valor p calculable con este documento.

Eso no vuelve falso el modelo salida/entrada de Ferrer: ambas direcciones podrían corresponder a dos conjuntos de agentes. Pero la misma distribución se explica por identidad, tipo de cuenta, papel económico permanente, titularidad, procedencia o segmentación editorial, sin comprometer la semántica de `ka/ku`.

## Sensibilidad: comparación exacta condicional al grupo, pero NO al individuo

Las permutaciones enumeran exhaustivamente todas las reasignaciones por 4 grupos editoriales, manteniendo en cada grupo el número observado de `ku`, y suman rangos (empates = rango promedio). Son **pruebas de asociación retrospectiva**: no eliminan dependencia por persona, fuente única, selección ni las reconstrucciones metrológicas.

| Exclusión / ensayo | Renglones | Asignaciones | Tan extremas o más | p unilateral |
|---|---:|---:|---:|---:|
| Serie completa | 19 | **750** | **4** | **0,005333** |
| Excluir solo partida excepcional de `beŕśir`, 549,5 g | 18 | **600** | **1** | **0,001667** |
| Excluir todas las partidas de `beŕśir` | 15 | **270** | **1** | **0,003704** |
| Excluir tres cantidades con anotación `-1` o `bi` | 16 | **240** | **4** | **0,016667** |

La persistencia de la asociación bajo estas exclusiones es compatible con poblaciones de cantidades diferentes, pero **no discrimina morfema vs individuo**. Los análisis por exclusión son exploratorios; no deben tratarse como pruebas independientes o preregistradas.

## Orden del registro y cancelaciones: alcance real

La colocación de una o dos partidas `-ku` al final de cada uno de cuatro grupos es parte de la agrupación editorial del propio registro. La hipótesis de cierre, proveedor, totalización o balance requiere **delimitadores independientes de las etiquetas -ka/-ku**. Calcular una probabilidad suponiendo a priori «`ku` al final» sería **circular** si los grupos se han definido mediante `ku`; no hacerlo.

Hay al menos tres anotaciones editoriales de cantidades corregidas:
- `biuŕtageŕ-ka : ki5(-1)` (secuencia 4).
- `sakaŕbaś-ka : ki3(bi)` (secuencia 8).
- `bodoldiŕ-ka : ki4(-1)` (secuencia 12).

Las tres pertenecen a `-ka` en esta codificación, pero esto **no** prueba que `ka` signifique salida o deuda: la tabla debe verificarse por fotografía y se ha elegido un solo plomo. La partida `beŕśir-ka` de 549,5 g muestra la posibilidad de operaciones atípicas/no liquidadas o ambigüedad de lectura, sin autoridad independiente para optar entre ellas.

## Evaluación de hipótesis

- **H-DIR** (`ka = receptor/salida`, `ku = proveedor/entrada`): **compatible, SIN GOLD EXTERNO**, confusión por dos nombres.
- **H-ROLE** (`ka` y `ku` etiquetan clases de participantes): **compatible**, confusión exacta por persona; requerirá observar cambios de sufijo para la misma persona o roles comprobados de forma independiente.
- **H-BALANCE / H-ACCOUNT** (entradas individuales y agregados, o distintos titulares de cuenta): **compatible**; explicar repetición de nombres y secuencia de grupos.
- **H-VARIANT** (alomorfía libre o por contexto): menos compatible con asociación cuantitativa por grupo, pero no descartada si ligada a los nombres o a secuencia paleográfica.
- **H-NULL**: restringida por asociación cuantitativa, pero no descartada por metrología y edición sin verificación visual directa.

## Siguiente prueba realmente diferenciadora (sin inventar desciframiento)

1. Buscar fuera de Bastida otra inscripción donde **el mismo antropónimo fiable** aparezca con **dos sufijos distintos y referencias a cantidades**, o inscripción con tipo de operación **evidenciado externamente**.
2. Para cada nueva pieza, exigir **lectura diplomática de ambos morfemas, entorno de persona y cantidad, signario y procedencia**. No contar repeticiones editoriales del mismo objeto como réplicas.
3. Si una persona cambia de etiqueta dependiendo de la operación, **queda debilitado el modelo de «clases personales fijas»**, pero todavía faltaría asignar la **dirección** del flujo.
4. Si solo varía por nombre en varios textos, estudiar categorías permanentes o patrones de escriba antes de postular verbos u operaciones.
5. Ejecutar controles predefinidos, tolerar abstenciones, **sin contaminar el HOLD** y sin alterar `SCI-PRED-02` ni `FULL3406`.

## Implementación auditable

- `src/iberos/bastida_suffix_confounding.py`: script estándar Python, sin librerías externas ni costes.
- `tests/test_bastida_suffix_confounding.py`: aserciones de identidad y cuatro enumeraciones exactas.
- `.github/workflows/science-prediction-translation.yml`: reejecuta la auditoría y exige explícitamente `suffix_separable_from_person_within_artifact = false`.

**Veredicto:** cuantificación corregida metodológicamente: **ASOCIACIÓN POR GRUPO CONFIRMADA EN TABLA EDITORIAL**, **EFECTO SEMÁNTICO INDEPENDIENTE DEL MORFEMA NO IDENTIFICABLE**. `independent_semantic_gold=0`; `new_translations_confirmed=0`; `blind_successes=0`; `cost_eur=0`.
