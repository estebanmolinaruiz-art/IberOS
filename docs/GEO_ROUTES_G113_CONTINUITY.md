# G-113 — IberOS GeoRoutes: continuidad histórica por épocas

## Función nueva
`src/iberos/route_continuity.py` compara testimonios de distintos periodos
y registra su procedencia, dependencia, vinculación geográfica y cronología.
No presupone que una vía romana, medieval o moderna herede su trazado de
una comunicación ibérica.

Cada testimonio contiene:
- identificador y grupo de dependencia;
- corredor candidato (identificador provisional, no geometría);
- tipo de evidencia (camino material, itinerario, fotografía/huella, topónimo,
  relación entre asentamientos, superficie datada);
- intervalo de fecha, acreditación editorial y asociación directa al recorrido;
- comprobación de la geometría del tramo.

Criterio conservador por periodo: para proponer revisión arqueológica, requiere
dos grupos independientes de testigos *directamente asociados* al corredor y con
geometría verificada. No demuestra camino: solo da prioridad para revisión.
La conexión entre épocas **permanece siempre no demostrada** hasta documentar
evidencias que cubran los intervalos intermedios y la sucesión estratigráfica.

## Ejecución estricta PICOLA–ALCUDIA

```bash
python -m unittest discover -s tests -p 'test_route_continuity.py'
python scripts/picola_route_g113.py
```

La colección de antecedentes arqueológicos e históricos está documentada en
`data/examples/picola_alcudia_g113.json`; **ninguno** es actualmente un
testimonio directo de un tramo fechado 430–350 a. C. con geometría certificada.
El resultado para esa etapa es `no_qualified_evidence`. Las rutas posteriores
son controles comparativos, no rellenos admisibles de los huecos ibéricos.

## Limitaciones y siguientes datos

El motor no extrae automáticamente textos sin edición verificada y no
georreferencia fuentes gráficas. Requiere planos de puertas, paleosuperficies
fechadas y revisión de los topónimos por especialistas. No estima probabilidades
de continuidad histórica. Nunca altera las métricas del Core epigráfico,
y no tiene dependencias de pago.

Fuentes para las pistas:
- Moratalla 2015: https://doi.org/10.7203/SAGVNTVM.47.5225
- Badie y Moret 1997: https://www.persee.fr/doc/palla_0031-0387_1997_num_46_1_1428
- Puerta sureste de Ilici, UA 2025:
  https://web.ua.es/es/actualidad-universitaria/2025/diciembre2025/8-14/la-identificacion-de-la-puerta-sureste-de-ilici-por-investigadores-de-la-ua-transforma-el-conocimiento-sobre-la-ciudad-iberica-de-la-alcudia.html
