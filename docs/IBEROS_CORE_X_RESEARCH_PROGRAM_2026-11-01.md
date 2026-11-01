# IberOS CORE-X — Programa de investigación para avanzar en la comprensión del ibérico

**Fecha:** 2026-11-01. **Estatus:** diseño de investigación, no implementación validada ni prueba de traducción.

## Objetivo principal
Aumentar conocimiento falsable sobre secuencias, morfología, distribución y, cuando sea posible, semántica de inscripciones ibéricas auténticas. Separar descodificación de signos, segmentación, lectura fonética provisional, análisis gramatical, propuesta de sentido y traducción. Cada nivel mantiene su incertidumbre.

## Arquitectura mínima ejecutable (software libre, sin servicios de pago)

1. **Evidence Store**: inventario físico, foto o dibujo con licencia, cara, segmento, fecha, autor, transcripción editorial, calidad y metadatos; identificadores persistentes y grafo de variantes. Distinguir grafía original y transliteración normalizada.
2. **Atomic Sign Graph**: trazos -> candidatos de alógrafo -> grafema -> valores fonográficos condicionales -> segmentos -> posibles morfemas. Cada arista: fuente, probabilidad calibrada, alternativas e incompatibilidades.
3. **Pattern Engine**: frecuencias con intervalos, n-gramas, entropía, información mutua y alineación edit-distance; segmentaciones múltiples, permutaciones controladas, inferencia bayesiana de estructuras recurrentes. No confundir asociación con significado.
4. **Hypothesis Search**: beam search, programación por restricciones y optimización combinatoria multiarranque; evaluar propuestas morfológicas y posibles valores bajo restricciones paleográficas y contextuales; hipótesis lingüísticas alternativas y nula.
5. **Contextual Inference**: tipo de soporte, cronología, hallazgo, distribución, fórmulas repetidas, onomástica reconocible, contactos lingüísticos. Evitar usar el contexto como etiqueta semántica creada por el propio sistema.
6. **Prediction Ledger**: predicción sellada, referencia de commit/hash, cohortes de grupos físicos separadas, controles comparativos ciegos, resultado independiente, abstención y tasas de error.

## Orden correcto de implementación
**Fase A — inventario y calidad:** reparar Pech-Maho V, vincular duplicados al objeto físico, anotar cobertura y sesgos por procedencia. No entrenar con transcripciones duplicadas como si fuesen piezas independientes.

**Fase B — análisis sin semántica:** ejecutar recuentos sobre el corpus curado, modelos simples n-gram y segmentación, baselines aleatorios y permutación de frecuencias, y estudiar si mejora la predicción de signos ocultos de objetos nunca vistos. Separación por objeto/yacimiento/edición.

**Fase C — gramática y morfemas:** inducir afijos y fórmulas con segmentaciones alternativas y modelos de incertidumbre; experimentos ablation sin metadatos del contexto para detectar fugas.

**Fase D — hipótesis semánticas:** explorar solo con fuentes independientes y predicciones prospectivas falsables; incluir hipótesis nula, analogías vasco-aquitanas y otras propuestas como candidatas, nunca identidades demostradas a priori.

**Fase E — refutación:** M06/M07, piloto DEVELOPMENT, preregistro baseline, mínimo 20 grupos físicos HOLD inéditos, sellado, evaluación estadística y replicación externa.

## Medidas de resultado
Cobertura de corpus revisada; exactitud y calibración de lectura de grafemas; precisión de segmentación evaluada por expertos; desempeño out-of-sample frente a baselines; estabilidad de morfemas entre soportes y yacimientos; número de hipótesis prospectivas corroboradas frente a refutadas; tasa de abstención. **Una salida plausible de IA no equivale a significado demostrado.**

## Salvaguardas
- Prohibido entrenar y evaluar sobre variantes editoriales de una misma pieza como muestras independientes.
- LLM como generador y crítico de hipótesis, no juez de su propia corrección.
- No presentar porcentajes de preparación administrativa como validez lingüística.
- No reclamar desciframiento por similitud a lenguas modernas, traducciones generadas ni puntuación interna.
- Modelo liviano CPU primero; escalar a IA profunda solo si los datos y una mejora externa lo justifican.
- Mantener VALIDATION-01 NOT_EVALUATED mientras M06/M07 y HOLD sigan pendientes.

## Bibliografía metodológica exploratoria
- Braović et al. (2024), systematic review of computational decipherment: https://aclanthology.org/2024.cl-2.7/
- Tamburini (2025), combinatorial optimization and coupled simulated annealing: https://doi.org/10.3389/frai.2025.1581129
- Assael et al. (2025), multimodal inscription contextualization: https://www.nature.com/articles/s41586-025-09292-5

**Próximo cambio implementable:** prueba de segmentación y predicción de signos ocultos sobre objetos físicos separados con baseline n-gram y baseline frecuentista. Publicar código, particiones, semillas y resultados sin usar semántica inventada.
