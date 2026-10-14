# IberOS — recuperación de módulos y primera conexión GEO
Fecha 2026-10-14. Estado: inspección del repositorio + puente GEO implementado, pendiente de certificar por CI.

## Inventario con evidencia
| Capa histórica | Evidencia actual | Estado operativo demostrado |
|---|---|---|
| GEO / Atlas | `site/atlas/index.html`, seis referencias topográficas Leaflet/OSM y consultas enlazadas al corpus | Atlas WEB implementado; ahora además puente Python de solo lectura, **no** análisis geolingüístico automático |
| PALEO | `src/iberos/core.py`, control rótico y campos PALEO del registro | Control de lecturas, no motor OCR autónomo verificado |
| TRACE | CORE: independencia, fugas, procedencia, splits | Implementación científica Python |
| MORPH | gates y protocolos de estructura | Implementación parcial, sin desciframiento general |
| LEXSEM | familia ROK, SALIR, KUTUR, etc., epistemic layers | Hipótesis controladas, significado exacto abierto |
| INFER | métricas y procedimientos relacionados | No certificado como motor histórico completo e independiente |
| 3D | `site/modelos3d/index.html` carga visores y `site/data/real_3d_resources.json` | Interfaz web; no confirmado como módulo científico Python |
| Write / Talk / Laboratorio | Interfaces en `site/`, documentación y pruebas | No equivalen a integración completa con CORE publicada |

## GEO: puente mínimo sin crear datos falsos
Archivo `src/iberos/geo.py`: `atlas_nodes()` devuelve una copia de los **seis nodos del Atlas existente**; `geo_context(OBJECT_ID)` busca coincidencias **literales** de `query` con `Yacimiento` o `Localidad` del catálogo, como Tivissa. No utiliza geocodificación automática y **no adjudica la coordenada del nodo al objeto**. Responde siempre `object_coordinates_verified=false`, `scientific_state=CONTEXT_ONLY` y `automatic_core_promotion=false`.

Límites: los seis nodos son referencias territoriales públicas, algunas aproximadas; **la coincidencia literal es conveniencia de búsqueda, no demostración de procedencia arqueológica exacta**. Una coincidencia vacía no implica que el objeto carezca de localización. Los nombres ambiguos deben resolverse manualmente. La web aún mantiene su propio listado: futura fase debería utilizar una fuente de datos compartida y versionada para evitar divergencias.

## Uso Python
```python
from iberos import atlas_nodes, geo_context
print(len(atlas_nodes()))
print(geo_context("IBR-PLM-0002"))
```

## Pruebas y próxima fase
`tests/test_geo.py` protege copia de datos, puente Tivissa sin coordenadas del objeto y rechazo de identificadores inexistentes. Ejecución CI pendiente. A continuación: sincronización web↔CORE desde una fuente única, inventario de clases históricas PALEO/MORPH/LEXSEM y pruebas de integración intermodular. Sin cambios en benchmark congelado ni en gates lingüísticos.

## Segunda tanda — catálogo GEO compartido entre Atlas y Python

- `site/data/geo_atlas_nodes.json`: **fuente versionada de seis nodos**, con `id`, referencia de lugar, coordenadas topográficas, precisión declarada, zona y descripción.
- `site/atlas/index.html`: carga los seis nodos desde JSON; deja de codificar por separado las coordenadas en JavaScript. En caso de error de lectura no inventa coordenadas; muestra advertencia al visitante.
- `src/iberos/geo.py`: en entorno del repositorio carga el JSON versionado; fuera de él usa una instantánea local de compatibilidad de los mismos seis nodos. **Esto conserva la funcionalidad de instalaciones standalone antiguas, pero significa que la unificación completa del empaquetado y generación automática de la copia sigue pendiente.**
- `tests/test_geo.py`: añade prueba de concordancia entre fuente web y copia Python, además de controles de contexto sin promoción semántica.

**Limitaciones y criterio de cierre:** aún no hay conexión automática del Atlas a inferencias lingüísticas y no debe haberla sin validación. Tampoco se ha comprobado todavía la ejecución de CI de estos últimos commits. En versiones posteriores, empaquetar el JSON científico común dentro de la distribución Python y sincronizar la copia web en build, eliminando la lista estática de compatibilidad. La información GEO es contextual, no determinante del significado de una inscripción.
