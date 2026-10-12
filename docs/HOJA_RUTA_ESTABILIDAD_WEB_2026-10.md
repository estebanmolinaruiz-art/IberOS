# IberOS+ · Hoja de ruta de estabilización técnica

**Fecha de referencia:** 12 de octubre de 2026  
**Objetivo:** alcanzar un servicio público estable, reproducible, accesible y utilizable en Safari iPhone y escritorio, antes de añadir diseño o nuevas funciones.

## Estado y método

**35 % de progreso global ESTIMADO**: referencia preliminar de planificación; **no** equivale al porcentaje de pruebas aprobadas.  
**Prueba de disponibilidad anterior:** 23/23 recursos accesibles en una sesión automatizada. Eso no valida sus interacciones.  
**Riesgo principal abierto:** comportamiento del catálogo y otros módulos en Safari iPhone sin prueba de aceptación en dispositivo.  
**No declarar 100 %** hasta disponer de pruebas ejecutadas por módulo y plataforma.

Cada área pesa lo mismo (10 % de la puntuación global). El porcentaje de un área se incrementa solo cuando una prueba concreta queda registrada como superada con URL, fecha, navegador y resultado.

| Área | Peso | Progreso inicial estimado | Pendiente para aprobar |
|---|---:|---:|---|
| Despliegue GitHub Pages y caché | 10 % | 65 % | Verificar SHA/versión servida y refresco Safari |
| Core: búsqueda y carga de datos | 10 % | 60 % | Comprobar búsqueda, ausencia de resultados y errores tras migración a datos locales |
| Corpus y filtros | 10 % | 45 % | Buscar, filtrar, limpiar, abrir objetos y preservar contexto |
| Fichas e imágenes | 10 % | 25 % | Probar 38 fichas, evitar repetición y ausencia de imágenes falsas |
| Atlas y enlaces cruzados | 10 % | 45 % | Marcadores, búsquedas, rutas y navegación entre módulos |
| Laboratorio y proyectos | 10 % | 25 % | Guardar, recuperar y exportar JSON/Markdown válidos |
| Write y Talk | 10 % | 35 % | Probar entradas, salidas, estados de incertidumbre y errores |
| Visor 3D | 10 % | 35 % | Carga de ambos modelos, rotación, zoom, fallback y memoria móvil |
| iPhone Safari y accesibilidad | 10 % | 10 % | Pruebas reales iOS, diseño legible y navegación táctil |
| Enlaces, recursos y diagnóstico | 10 % | 5 % | Validación de enlaces externos, fallos visibles y controles de regresión |
| **Total** | **100 %** | **35 % aproximado** | **No validado al 100 %** |

> Los valores iniciales de cada área son una **priorización estimada**, no ensayos realizados. La cifra global del 35 % es la referencia inicial de gestión, no una suma mecánica de esos valores redondeados.

## Etapas de ejecución

### Fase 1 — Bloqueos técnicos (prioridad crítica)
- [ ] Comprobar desde GitHub Pages que Core usa `site/data/objects.csv`, `families.csv` y esquema JSON locales.
- [ ] Probar que la vista de Fichas carga en Safari iPhone sin quedarse en blanco.
- [ ] Instrumentar errores visibles: archivo no encontrado, fallo de red, error de módulos JS y falta de imagen.
- [ ] Confirmar que los enlaces de navegación abren las rutas correctas.

### Fase 2 — Operaciones de investigación
- [ ] Corpus: búsqueda con y sin coincidencias, filtros y selección.
- [ ] Ficha: datos coherentes por OBJECT_ID y acceso a Core, Laboratorio, Write/Talk.
- [ ] Laboratorio: guardar y recuperar proyectos; exportación JSON y Markdown sin corrupción.
- [ ] Atlas: marcadores, búsquedas y enlaces a registros.

### Fase 3 — Experiencia multimedia y móvil
- [ ] Carga y control táctil de dos glTF en Safari.
- [ ] Fallback comprensible cuando WebGL o CDN no están disponibles.
- [ ] Imágenes alojadas localmente y atribuidas; ausencia de recuadros tapados.
- [ ] Contraste, tamaño táctil, carga y disposición adaptativa en iPhone.

### Fase 4 — Regresión y publicación estable
- [ ] Pruebas reproducibles para todas las funciones críticas.
- [ ] Doble verificación: rama main + versión realmente servida por Pages.
- [ ] Pasada integral en Safari iPhone y navegador de escritorio.
- [ ] Registro de incidencias sin resolver, con prioridad, reproducibilidad y responsable.
- [ ] Congelar versión solo cuando no haya fallos bloqueantes.

## Control del avance

Para cada prueba registrar: `fecha | URL | navegador/dispositivo | acción | resultado esperado | resultado observado | evidencia | estado`.

**Estados:** no probado · en curso · superado · bloqueado · regresión.

**Regla de aceptación:** una página que abre pero cuya búsqueda, descarga, imagen, interacción o enlace falla **no está aprobada**. La aprobación en escritorio **no sustituye** la prueba de Safari iPhone.

**Política de cambios:** priorizar correcciones acotadas, preservar portada y datos científicos, probar antes de fusionar y confirmar después del despliegue. No confundir una ilustración conceptual con fotografía arqueológica.
