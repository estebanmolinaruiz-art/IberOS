# VALIDATION-01 — Diseño operacional de tarea ciega, borrador v2 (2026-10-19)

## Tarea seleccionada para preinscripción (NO CONGELADA)
**Predicción de un signo atómico oculto mediante su contexto**, restringida a determinar si el signo oculto es el silabograma `te` o no. Esta prueba evalúa *regularidad distribucional de signos*, NO significado, morfología ni traducción. Es una alternativa operativa a una etiqueta semántica imposible de auditar con los recursos actuales. Debe identificarse como `VALIDATION-01-TE-MASK` y nunca confundirse con verificación de la hipótesis morfológica original.

### Unidad y entrada
Una posición elegida por un procedimiento fijado antes de revelar la lectura de prueba en una **línea completa**, segmentada en signos atómicos y validada por editor independiente. La entrada al predictor contiene **todos los signos salvo el signo central**, sustituido por `[MASK]`; contexto izquierda y derecha y categoría de escritura; sin token del centro, sin transcripción original completa ni información que codifique el centro. Aceptar solamente líneas inequívocas sin lagunas que afecten a la ventana. Los ejemplos del mismo objeto físico deben asignarse al mismo split.

### Etiqueta gold
`1` si el revisor registra en la posición oculta el signo indivisible `te`, `0` si registra cualquier otro signo inequívoco del signario establecido. La etiqueta se **obtiene de la lectura editorial independiente de la posición ocultada**, nunca del texto de entrada al modelo. Esta prueba mide predicción de signo, no teoría del valor semántico de TE.

### Construcción de posiciones
Para impedir selección oportunista de casos: seleccionar una posición por objeto físico mediante un algoritmo preinscrito (por ejemplo SHA256 del ID físico más sal secreta custodiada por revisor independiente); revelar al predictor solamente la línea enmascarada. La distribución de clases no se fuerza una vez visto el gold; si hay desbalance extremo, se informan cobertura y métricas por clase sin cambiar el muestreo a posteriori. Una línea con cero o múltiples signos controvertidos puede quedar fuera por regla objetiva anterior al gold.

### Baselines a congelar en TRAIN
- A: probabilidad de TE global en TRAIN, decisión binaria con umbral fijo de 0,5 y regla de empate definida.
- B: modelo contextual de unigramas vecinos / n-gramas entrenado exclusivamente sobre TRAIN, sin acceso a HOLD.
- IberOS: predictor independiente sobre el mismo input enmascarado, interfaz y versión congelados. No afirmar que existe si aún no se ha implementado y probado.

### Separación y auditoría
Primero separar grupos físicos y editoriales, excluir objetos ya vistos por IberOS del HOLD. Congelar selección, firma de predicciones, código, métrica y baselines antes de la apertura gold. El revisor independiente conserva mapa de posiciones y signos completos hasta entonces. Mínimo 20 objetos HOLD según protocolo actual: **umbral operativo mínimo, no potencia estadística garantizada**.

### Éxito / fracaso
Registrar la accuracy, balanced accuracy si ambas clases aparecen, abstenciones y delta vs baseline B con intervalo de confianza por grupo físico. Una diferencia positiva retrospectiva o con 20 muestras **no basta** para afirmar superioridad: requieren umbral de efecto y procedimiento inferencial preinscritos y replicación independiente. Por defecto `NOT_EVALUATED` hasta completar el protocolo.

## Riesgos críticos
- Seleccionar máscaras después de conocer TE sesga la frecuencia y sobreestima el rendimiento.
- Las líneas de Orleyl y los 20 objetos ya trabajados pertenecen a desarrollo, no son HOLD.
- Las variantes `te1`–`te16` catalogadas sin cotejo independiente no constituyen signos leídos en una inscripción.
- Un clasificador que ve `te` en su entrada no cumple la tarea.
- El corpus real y la organización de una revisión independiente continúan faltando.

## Próximos entregables prioritarios
1. Cerrar selección de máscara y regla de clase sin ver HOLD; acordar tamaño y potencia.
2. Revisar primeras líneas DEVELOPMENT con signos atómicos reales, cara, renglón y lectura editorial; ejecutar una prueba piloto **solo en desarrollo**.
3. Congelar predictor de IberOS, baselines y separaciones después del piloto.
4. Adquirir HOLD nuevo sin filtración y obtener gold independiente.
