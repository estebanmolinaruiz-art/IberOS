# G-122 — La Picola: puerta noreste, R2 y salida a través del foso

## Evidencia arqueológica
Moret y Badie (1998) estudian el trazado modular del asentamiento fortificado
construido hacia 430 a. C. La documentación precedente del proyecto identifica
una puerta en la cortina noreste comunicada con la calle R2, foso exterior y
anchura superior aproximada de 5–6 m. Debe revisarse esta anchura contra la
planta primaria y sus secciones, y no atribuirla automáticamente a todo el
recorrido defensivo ni a un único momento de uso.

Referencia primaria: https://doi.org/10.3989/aespa.1998.v71.274
Documentación del Plan Director (2023):
https://museodelmarsantapola.com/plan-director-del-bic-la-picola/

## Cálculo G-122
La distancia para atravesar una banda de ancho W con ángulo θ respecto de
su normal es W / cos(θ). Se prueban escenarios de 0°,15°,30°,45°,60°.
El cálculo **no** ubica una pasarela ni prolonga R2 sobre el territorio real.
Es una sensibilidad dimensional sin coordenadas cartográficas de la puerta,
eje R2, bordes del foso o estratigrafía de un paso.

```bash
python -m unittest discover -s tests -p 'test_route_picola_exit.py'
python scripts/picola_route_g122.py
```

## Puertas lógicas para una ruta acreditable
1. Centro del vano noreste en EPSG:25830, con margen métrico medido.
2. Dos puntos sobre el eje real de R2 y prueba de su orientación respecto al foso.
3. Orillas interior/exterior del foso y su estado durante 430–350 a. C.
4. Evidencia arqueológica concreta de un paso (terraplén, puente, interrupción de
   foso o superficies de tránsito), no deducción solamente geométrica.
5. Paleo-terreno emergido más allá del foso y cruces fechados hacia Ilici.
6. Contrastarlo con el eje del Camino del Molar y la puerta sureste de Ilici.

**Dictamen:** exterior terrestre NO localizado. Los intervalos numéricos
calculados no constituyen una medición histórica de puente ni camino.
Los modelos de GeoRoutes deben seguir absteniéndose en el tramo no documentado.
Sin modificaciones de métricas epigráficas ni publicación de la web. Herramientas gratuitas.
