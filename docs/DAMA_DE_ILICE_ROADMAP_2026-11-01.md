# DAMA DE ILICE — Hoja de ruta del programa de desciframiento IberOS
Fecha de referencia: 2026-11-01
Versión: 1.0

## Propósito
**Dama de Ilice** es el nombre del programa global de investigación de IberOS para maximizar la comprensión comprobable de la lengua ibérica mediante corpus auténtico, paleografía, modelos lingüísticos, inferencia histórico-arqueológica y experimentación independiente. No implica que la Dama de Ilice contenga una inscripción que se pretenda traducir.

## Dos indicadores, nunca intercambiables
1. **Progreso del programa (0–100 %):** avance ponderado de entregables y controles observables hacia un sistema científico reproducible. **Línea de base provisional: 19 % (01-11-2026)**.
2. **Desciframiento validado:** porcentaje de lecturas/interpretaciones corroboradas con referencia externa sobre un conjunto de evaluación definido. **No medible todavía / NOT_EVALUATED**. No sustituir por el 19 %, ni por el 30/100 de preparación administrativa de VALIDATION-01.

## Fases y pesos de progreso
| Fase | Peso | Avance reconocido | Evidencia mínima para cierre |
|---|---:|---:|---|
| F1. Infraestructura y reproducibilidad básica | 15 | 15 | CORE, pruebas automatizadas, trazabilidad documental y publicación técnica básica |
| F2. Corpus arqueológico independiente y curado | 15 | 4 | objetos físicos identificados, lecturas y procedencias revisadas, licencias y agrupación de duplicados |
| F3. Paleografía y lectura de signos | 15 | 0 | 17 signos Orleyl adjudicados con evidencia individual, segunda lectura externa, incertidumbre |
| F4. IA y lógica computacional CORE-X | 20 | 0 | código ejecutable, baselines, predicción fuera de muestra, métricas y ablaciones |
| F5. Inferencia histórica y semántica contextual | 15 | 0 | etiquetas arqueológicas independientes, hipótesis con alternativas, pruebas prospectivas sin circularidad |
| F6. Validación ciega y predicción prospectiva | 15 | 0 | preregistro, 20 grupos físicos HOLD, predicciones selladas y evaluación estadística |
| F7. Replicación y publicación científica externa | 5 | 0 | replicación independiente, datos reproducibles y publicación con límites |
| **TOTAL** | **100** | **19** | |

El 19 % es una **estimación conservadora de gestión**, no una medición científica externa. F2 reconoce 4 puntos de inventario preliminar, pero no su cierre: en auditoría previa 22 objetos, 20 agrupaciones físicas pendientes, 1 referencia URL truncada, 0 lecturas completas verificadas, 0 HOLD. F1 reconoce la base de software y pruebas ya documentadas, no certificación integral del producto.

## Hitos y rutas críticas
- **R1 (19 → 25 %)**: corregir Pech-Maho V, resolver identidad física/duplicados, incorporar fuentes con permiso y mapear incertidumbres. No contar documentos nuevos sin control de calidad.
- **R2 (hasta 40 %)**: cerrar M06 (17 grafemas Orleyl) y M07 (segunda lectura independiente), con evidencia revisable.
- **R3 (hasta 60 %)**: ejecutar motor CORE-X reproducible: tokenización incierta, análisis de afijos, n-gram, baselines simples, segmentación e inferencia probabilística. No promocionar traducciones generadas.
- **R4 (hasta 75 %)**: corpus contextual externo, hipótesis de funciones documentales, pruebas de predicción y análisis de causalidad/circularidad.
- **R5 (hasta 95 %)**: HOLD prospectivo por objeto físico, sellado antes del gold, controles, análisis de errores y resultados negativos.
- **R6 (hasta 100 %)**: replicación externa y dictamen científico reproducible, incluso si el resultado es no concluyente o refuta hipótesis.

Las rutas intermedias son objetivos de gestión aproximados, **no suma automática** de porcentajes. El avance oficial se recalcula solo por puntos de fase efectivamente acreditados.

## Reglas de actualización
- Registrar cada incremento con fecha, commit, archivo de evidencia, revisión y puntos de fase ganados; nunca subir puntos por intención, redacción de protocolos o ejecución sin métricas.
- Mostrar siempre porcentaje total, puntos por fase, estatus científico (NOT_EVALUATED/PARTIAL/REPLICATED según evidencia), bloqueos y próximo experimento.
- Separar progreso de interfaz web de progreso de desciframiento.
- No convertir similitud histórica, coincidencia de patrones o plausibilidad de un LLM en traducción certificada.
- No pagar servicios externos sin autorización previa; preferencia por software libre y cómputo disponible.
- No prometer desciframiento total: el éxito es máxima comprensión verificable y exposición honesta de los límites.

## Primera siguiente tarea ejecutable
CORE-X Piloto P01: cargar corpus revisado, separar por objeto físico, construir baseline de frecuencia y n-gram sobre secuencias transliteradas con incertidumbre; medir recuperación de signos ocultos y hacer ablación del contexto arqueológico, sin contaminar el test con ediciones duplicadas. Registrar software, resultados, semillas y errores. Paralelamente, continuar M06/M07.
