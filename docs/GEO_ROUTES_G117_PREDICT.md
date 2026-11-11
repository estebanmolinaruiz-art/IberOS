# G-117 · GeoRoutes Predict: cálculo matemático predictivo y control arqueológico

## Integración técnica
El módulo `src/iberos/route_prediction.py` incorpora:
- `ensemble_routes(grid,case,trials,seed,terrain_weight_range)`: búsqueda repetida de
  rutas de coste ponderado sobre celdas **documentadas y fechadas**, con variación
  reproducible de pesos de coste y contabilización de frecuencias por celda.
- `audit_picola_ensemble()`: ejecución del caso real La Alcudia–La Picola con
  referencias publicadas y bloqueo explícito si falta una malla paleoambiental
  georreferenciada y fechada.

## Interpretación científica
Es un motor predictivo matemático **basado en escenarios**, no un modelo de
aprendizaje automático entrenado, ni atribuye probabilidades de existencia
histórica. La frecuencia de una celda mide **estabilidad condicional** de
soluciones ante variaciones de coste; nunca confirma que fue un camino ibérico.
La parametrización aleatoria no crea nuevos datos arqueológicos.

Cada paso exige `source_id`, cronología compatible con el periodo completo y
tipo de celda verificable. Lagos/lagunas, áreas desconocidas, ríos sin paso
acreditado, evidencias romanas fuera de periodo y diagonales a través de
obstáculos se bloquean.

### Caso La Picola–La Alcudia
Periodo operativo: aproximadamente 430–350 a. C. (años astronómicos -429 a -349).
Referencias métricas EPSG:25830:
- La Alcudia, Termas Orientales (referencia, no puerta): 701823.285, 4234872.059.
- La Picola, vértice A1 del perímetro BIC (no puerta): 713265, 4230490.

**Dictamen G-117**: distancia rectilínea calculable, pero el ensemble de rutas
reales **no se ejecuta** porque faltan paleosuperficies continuas datadas, límites
lagunares, cauces, vados y los accesos georreferenciados. No existe base válida
para dibujar o puntuar un corredor de 12 km. El Camino del Molar sigue siendo
la mejor **prioridad experta para comprobar una llegada al sector sureste de
Ilici**, no una ruta completa demostrada hasta La Picola.

### Comandos
```bash
python -m unittest discover -s tests -p 'test_route_prediction.py'
python scripts/picola_route_g117.py
```

### Próxima conexión
Al disponer de un modelo temporal georreferenciado: preparar escenarios
(hipótesis de terrenos firmes), ejecutar el ensemble, exportar tramos
reiterados y registrar procedencia de cada celda. Después contrastar las
hipótesis con huellas de tránsito y dataciones arqueológicas **independientes**.

Estado: experimental, sin costes, sin modificación del Core epigráfico.
