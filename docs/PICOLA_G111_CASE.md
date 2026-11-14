# G-111 — Ejecución conservadora La Alcudia–La Picola

**Ventana de contraste:** aproximadamente 430–350 a. C. (años astronómicos -429 a -349).

Se analizan dos referencias publicadas en EPSG:25830 que **no** son coordenadas de puertas:

- La Alcudia (referencia de las Termas Orientales, ASTERO 2017): E 701823.285, N 4234872.059.
- La Picola (vértice A1 de su perímetro BIC): E 713265, N 4230490.

**Resultado reproducible:** distancia rectilínea 12252.154 m, rumbo desde La Alcudia hacia La Picola 110.956° respecto al norte. No es longitud de camino.

Se ejecuta la auditoría con `inspect_case`, **sin declarar verificadas** las siguientes capas: terreno emergido georreferenciado para el periodo, polígonos de lagunas datados, cauces datados, vados acreditados, puertas georreferenciadas y malla continua de evidencias. El resultado correcto es `not_evaluable_missing_evidence`. No se ha ejecutado un SIG histórico real ni obtenido corredores, porque ninguna de esas capas de control está disponible de forma validada en la rama.

No se ha identificado con esta ejecución ningún camino comercial, militar o mixto. Cero rutas computadas **no** significa cero rutas históricas.

Para continuar: digitalizar y auditar primero los sondeos Picola–Mórtoles y figuras de paleogeografía; obtener las plantas de las puertas; comprobar datum, escala, datación y procedencia de cada unidad; después rasterizar y ejecutar las distintas variantes de coste. Nunca usar caminos modernos para rellenar celdas desconocidas.

```python
from iberos.route_case_audit import GeoAnchor, inspect_case
a=GeoAnchor("La Alcudia",701823.285,4234872.059,"EPSG:25830","ASTERO-2017")
b=GeoAnchor("La Picola",713265,4230490,"EPSG:25830","BIC-Picola-A1")
print(inspect_case(a,b,-429,-349))
```

Sin costes ni dependencia adicional. No modifica estadísticas del Core ni web pública.
