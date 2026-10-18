# Política de publicación por lotes de 10 cambios

Desde el 18 de octubre de 2026, los commits a `main` **no disparan GitHub Pages automáticamente**. El flujo `.github/workflows/pages.yml` se inicia con `workflow_dispatch`, para **agrupar aproximadamente diez cambios comprobados por publicación pública** y evitar cancelaciones frecuentes.

- **Pruebas:** siguen ejecutándose con cada cambio mediante los flujos específicos de tests y comprobaciones web.
- **Sitio público:** conserva la última versión publicada hasta el siguiente lanzamiento deliberado de Pages.
- **Cómo publicar:** acumular 10 cambios desde la última versión publicada, revisar los resultados de CI y usar `Actions > pages > Run workflow > main`. Se mantiene la verificación de URL pública y SHA desplegada.
- **Excepción:** un problema urgente en la web puede justificar publicar antes de diez cambios.
- **Contador:** contar los commits de `main` posteriores al SHA contenido en `https://estebanmolinaruiz-art.github.io/IberOS/deployment-version.json`. Los commits de preparación del sistema también cuentan si se usa estrictamente el número de commits.
- **Limitación explícita:** **no existe un publicador automático por décimo commit**; el umbral es una política operativa de publicación manual. Automatizarlo exigiría otro workflow independiente con un contador verificable.

Los datos de investigación y las pruebas pueden seguir creciendo en GitHub sin forzar una publicación de la web en cada operación.
