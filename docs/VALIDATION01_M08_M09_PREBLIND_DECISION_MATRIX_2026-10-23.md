# VALIDATION-01 — Decisiones pre-ciegas para M08 / M09 (23 octubre 2026)

## Comprobación de correspondencia
Se verificó el correo de IberOS al 23-10-2026. El último mensaje identificado del MARQ confirma que prepararán fotografías del detalle `bo/ko` tras autorización. La firma por el solicitante se considera efectuada **por comunicación directa del solicitante**. En esta consulta no se identificó entrega nueva ni respuesta del revisor paleográfico externo.

## Qué pregunta podemos validar
La hipótesis de «traducir» una inscripción no es equiparable a identificar un grafema. El experimento TE-MASK debe registrar por separado:
1. **Paleografía**: acuerdo entre lectores independientes sobre signos concretos, expresando `?` cuando el soporte no permite decidir.
2. **Predicción contextual**: resultado binario previamente definido por datos extralingüísticos independientes de la cadena a predecir, sin utilizar una etiqueta circular derivada de la propia transcripción.
3. **Significado / traducción**: hipótesis semánticas contrastables aparte, sin promover una asociación morfológica a traducción confirmada.

## Decisiones que faltan antes de congelar M09
- Identificar propiedad contextual concreta y criterios de etiquetado reproducibles.
- Elegir baseline B independiente (no entrenado ni derivado de las reglas IberOS).
- Declarar cohorte TRAIN / VAL / HOLD por **pieza física**, alias documentados y exclusión de cualquier objeto visto durante desarrollo.
- Establecer procedimiento de predicciones congeladas con hash del archivo real, commit, hora y revisión gold posterior independiente.
- Definir evaluación preregistrada: intervalos de incertidumbre y análisis por sitio, soporte, escritura y dependencia editorial, evitando fugas.

## Prohibiciones metodológicas
- No clasificar como gold `TE presente/ausente` si ya se usa lectura TE como predictor.
- No convertir una foto del MARQ en muestra HOLD: la Illeta es ya material conocido de desarrollo.
- No considerar M06 completado por revisar figuras de la Illeta: **M06 pide 17 signos concretos de Orleyl V/VII**.
- No publicar fotografías institucionales nuevas sin aclarar permiso.

## Situación
M08 / M09: PENDING. M06 / M07: PENDING. HOLD independientes acreditados: 0. Preparación administrativa: 30 %. Veredicto: NOT_EVALUATED.
