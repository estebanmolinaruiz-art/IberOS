# Despliegue controlado del flyer oficial IberOS+

Estado: **pendiente de integración binaria**. No publicar ni fusionar por ahora.

Paquete local comprobado: `IberOS_Flyer_Restauracion_Desplegable.zip`, con `index.html`, `flyer-portada.jpg` y `README.md`.

## Integración
1. Extraer el ZIP.
2. Subir `flyer-portada.jpg` a `site/flyer-portada.jpg` en esta rama.
3. Sustituir `site/index.html` por el `index.html` del paquete **solo en esta rama**.
4. Verificar que la página carga el JPG y cada zona clicable abre su ruta correcta.
5. Revisar en escritorio y móvil. La versión móvil actual es una alternativa HTML; no reproduce la captura pixel a pixel.
6. Validar navegación, búsquedas, estado real del acceso/registro y métricas científicas.
7. No fusionar en `main` hasta confirmar la equivalencia visual y la preservación funcional.

## Advertencias científicas y de producto
La imagen del flyer incluye métricas ilustrativas incrustadas que no deben confundirse con recuentos validados. La portada basada en una sola imagen no sustituye una implementación accesible de componentes HTML. El botón de acceso/registro enlaza provisionalmente a Comunidad y no constituye autenticación.

**No se ha verificado ni realizado el despliegue público de esta portada.**
