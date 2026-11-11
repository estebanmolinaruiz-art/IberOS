# IberOS GeoRoutes — módulo transversal G-109

**Estado:** rama experimental `feature/geo-routes-g109`, sin integración en una release.

Esta función sirve para analizar conectividad espacial en **cualquier yacimiento,
paisaje, periodo o proyecto**; La Picola–La Alcudia es solamente el caso piloto.

## API
```python
from iberos.route_research import EvidenceCell, RouteCase, analyze, compare
case = RouteCase("picola-alcudia",-1,-1,-429,-349,10,"EPSG:25830")
```
Para uso real, reemplazar los puntos -1 por pares (fila,columna) y cargar una
malla rectangular formada por `EvidenceCell`. Cada celda requiere fuente,
interpretación y cobertura cronológica del intervalo completo.

`analyze(grid,case,method="dijkstra"|"astar"|"grade")` calcula un candidato.
`compare(grid,case,trials=20)` contrasta métodos y frecuencia de celdas.
Las lagunas y las zonas desconocidas se bloquean; los ríos solo admiten cruces
con identificación de evidencia. El modelo devuelve siempre
`historical_path_proven: false`.

## Limitaciones
- Malla de prueba no equivale a mapa paleoambiental georreferenciado.
- Los endpoints son índices de malla, no coordenadas geográficas.
- Se debe documentar transformación GIS/CRS y margen de error fuera de este núcleo.
- La evaluación de pendientes solo usa elevaciones aportadas (pueden ser actuales);
  no equivale a paleorrelieve.
- No se trata de detección visual mediante IA ni certifica caminos arqueológicos.
- La frecuencia con diferentes semillas no constituye probabilidad histórica.

## Protocolo
EVIDENCE → INFERENCE → HYPOTHESIS; jamás promoción automática al Core científico.
No modificar las métricas epigráficas, datasets curados ni el despliegue web.
Ejecución: `python -m unittest discover -s tests -p 'test_route_research.py'`.
Dependencias nuevas: ninguna. Coste: gratuito.
