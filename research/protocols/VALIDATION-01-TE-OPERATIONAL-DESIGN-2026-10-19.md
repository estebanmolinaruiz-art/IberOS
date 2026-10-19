# VALIDATION-01 / TE — protocolo operacional previo a la selección HOLD
Versión: 0.2; 2026-10-19. Estado: DISEÑO EXPLORATORIO, NO PRERREGISTRO CONFIRMATORIO.

## Separación obligatoria de las preguntas
1. **Paleografía**: ¿un grafema ha sido leído editorialmente como `te`? Se requiere fuente específica, cara/línea y alternativas; no equiparar un dibujo al valor `te` sin cotejo.
2. **Predicción estructural**: ¿existe una regularidad contextual de `te` no incluida en la construcción de la regla? No hay todavía regla específica congelada ni corpus cerrado.
3. **Semántica**: ¿denota `te` alguna función morfológica? No puede inferirse de (1) o (2).

## Unidad, selección, identidad
La unidad principal para inferencia es **OBJETO FÍSICO**. Varias líneas, caras, calcos o reediciones del mismo objeto comparten `physical_group`. La exposición editorial previa también puede invalidar la categoría de prospectivo aunque el objeto sea independiente. Se prohíbe reutilizar las 20 fichas revisadas o Orleyl como HOLD genuinamente no visto; pueden ser corpus de desarrollo o análisis retrospectivo declarado.

## Definición candidata de tarea (NO FROZEN)
Para cada ventana contextual predefinida, predicción binaria `te` presente / ausente **en la transcripción editorial auditada**, con `UNKNOWN` o abstención ante laguna o lectura ambigua. El muestreo de ventanas, posición, límites de palabra, corpus de referencia y criterio de selección no están fijados; no asignar etiquetas hasta completar esas decisiones. Ausencia requiere **cobertura epigráfica revisada**, no silencio de la ficha.

## Comparadores y anti-filtración
A: mayoría positiva/negativa calculada en TRAIN.
B: frecuencia de `te` condicionada a longitud de ventana/posición, estimada únicamente con TRAIN.
C: IberOS versión y configuración con hash; los tres deben abstenerse bajo la misma regla de visibilidad.
Variables como objeto, procedencia, atribución editorial o fuente no deben filtrar la etiqueta al sistema si no están preregistradas. Ninguna regla debe entrenarse con muestras HOLD ni ajustarse tras ver las etiquetas.

## Compromiso, revisión y puntuación
Sellar protocolo, índice de corpus, software, predicciones individuales de IberOS y baseline, semilla y reglas de abstención ANTES del desbloqueo por revisor independiente.
Validar físicamente hashes y sello temporal; la simple columna `predictions_frozen_sha256` no acredita precompromiso.
Predefinir muestra y potencia, tamaño por clase, balance, corrección por comparaciones múltiples, intervalos por clusters y criterio de replicación.
Un mínimo de 20 objetos es solo barrera programática. Las métricas informativas incluirán cobertura, balanced accuracy, diferencias pareadas, bootstrap por objeto e intervalos; distinguir análisis retrospectivo de confirmatorio.

## Fuentes externas relevantes
- Hesperia (BDH) ofrece registros y ediciones: https://hesperia.ucm.es/
- Orduña, Luján y Estarán, «El banco de datos Hesperia»: https://doi.org/10.36707/palaeohispanica.v0i9.213
- Ferrer i Jané y colaboradores, «El plomo ibérico de la Fundació CIRNE (Museu de Xàbia...)»: https://aespa.revistas.csic.es/index.php/aespa/article/download/619/689
Las referencias son pistas de recopilación, **no** transcripciones `te` cotejadas o nuevas unidades HOLD autorizadas.

## Registro de decisiones abiertas
- Dataset de textos editados y transcripción individual por pieza: PENDIENTE
- Desambiguación de valores / variantes: PENDIENTE
- Definición exacta de ventana y etiqueta: PENDIENTE
- Revisión de negativos y casos UNKNOWN: PENDIENTE
- Predicción congelada y baseline B entrenado: PENDIENTE
- HOLD prospectivo no expuesto: 0 casos
**DICTAMEN: VALIDATION-01 NO EVALUABLE; no hay descubrimiento lingüístico demostrado.**
