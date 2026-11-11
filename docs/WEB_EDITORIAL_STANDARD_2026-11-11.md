# IberOS WEB-05 — Norma editorial y funcional obligatoria

**Vigencia:** 2026-11-11. **Ámbito:** todas las nuevas pantallas y cambios de la web pública.

## Principios no negociables

1. **Primero el objeto, después la interpretación.** Toda ficha identificará el registro físico o textual, yacimiento y soporte antes de desarrollar hipótesis.
2. **Evidencia ≠ inferencia ≠ hipótesis ≠ traducción estimada.** No se afirmará un desciframiento o función gramatical sin contraste independiente.
3. **Imagen auténtica o ausencia explícita.** Fotografías, calcos y 3D deberán tener correspondencia de pieza, procedencia, atribución y derechos; nunca se sustituirán por diseños decorativos presentados como originales.
4. **Lectura rápida y expediente íntegro.** La vista inicial ofrece identidad, estado de la imagen, alcance científico y enlaces de lectura, fuentes y controles. El detalle técnico sigue disponible sin inundar la portada.
5. **Interfaz comprensible.** Los códigos internos (p. ej., READY, INFER, OBJECT_ID) deberán llevar una etiqueta clara o estar bajo detalles técnicos; el JSON no será el resultado principal.
6. **Sin duplicación visible.** No se repetirá una misma tarjeta, bloque News ni llamada a la acción de forma accidental. Mantener los enlaces redundantes si tienen finalidades de navegación distintas, sin multiplicar contenido.
7. **Búsqueda y conexión.** Cada registro enlazará ficha, consulta Core, referencias y contexto disponibles, diferenciando concordancias verificadas de candidatas.
8. **Interoperabilidad sin inventar datos.** Mantener exportaciones y preparar TEI/EpiDoc y concordancias cuando los campos estén fundamentados; no inventar imágenes, inscripciones, DOI ni identificadores externos.
9. **Datos reproducibles y honestidad del estado.** Distinguir resultados de entorno de pruebas, rama main y versión desplegada. No afirmar publicado algo hasta comprobar el marcador público `deployment-version.json`.
10. **Coste cero.** No adquirir servicios, saldos, suscripciones, licencias o pruebas de pago. Preferir GitHub Pages, GitHub Actions, herramientas libres y recursos públicos legalmente reutilizables.

## WEB-12 — Paquetes de cambio obligatorios (control de saturación)

Este procedimiento sustituye las ediciones repetidas de archivos en `main`. Se aplica a cambios de web, datos y Core que requieran despliegue.

1. **Preparación en una rama temática.** Crear una sola rama `feature/... `, `fix/...` o `chore/...` por objetivo. Agrupar en ella cambios de código, datos, documentación y pruebas; no modificar `main` archivo a archivo.
2. **Cierre del paquete antes de abrir PR.** Revisar correspondencias de objetos, fuentes, cambios, dependencias, permisos y regresiones; evitar editar la PR varias veces si es posible.
3. **Una revisión automática por paquete.** Abrir la pull request cuando el lote esté listo. GitHub Actions ejecuta las comprobaciones completas ante la apertura o actualización de la PR; los commits preparatorios en ramas aún sin PR no disparan esas pruebas.
4. **Bloqueo por fallo.** Si falla alguna prueba, corregir el paquete en la misma rama y revalidar. No fusionar ni publicar mientras falle. Las notificaciones históricas de ejecuciones fallidas no implican que la versión final siga fallando.
5. **Fusión consolidada.** Fusionar por `squash` únicamente después de que la ejecución correspondiente al HEAD de la PR esté verde, sin mover en paralelo ese HEAD.
6. **Un único lanzamiento público.** Tras la fusión, activar Pages mediante un solo archivo en `.github/release-trigger/` o un lanzamiento manual autorizado. Confirmar el SHA público en `deployment-version.json` y comprobar las páginas afectadas.
7. **Trazabilidad y volumen.** Cada paquete registra objetivo, cambios, prueba, errores corregidos, limitaciones científicas y versión pública. No existe una obligación de exactamente diez commits: el tamaño del lote depende de su coherencia funcional, no de un contador.
8. **Trabajo paralelo.** No mezclar ramas de La Picola, Core y web en la misma PR salvo cuando haya dependencia real; sincronizar con `main` antes de fusionar para evitar sobrescribir cambios ajenos.
9. **Sin costes nuevos.** Solo usar herramientas gratuitas ya aprobadas. Nunca activar licencias, planes de pago ni recursos cloud facturables.

**Importante:** este flujo reduce CI redundante pero no elimina GitHub Actions en las PR existentes de otros hilos. Evitar publicaciones simultáneas; y si una revisión requiere cambios posteriores, esos cambios forman parte del mismo paquete.

## WEB-14 — Control obligatorio de disparadores CI

- Los flujos generales `tests.yml`, `web-e2e-free.yml` y `qa-web.yml` se ejecutan mediante `pull_request` o `workflow_dispatch`, **no** mediante `push` redundante. Se conserva su cobertura: tests Python, Core, pruebas de Chromium, interfaz y navegación.
- La comprobación `scripts/check-ci-trigger-policy.mjs` impide volver a introducir disparadores `push` en estos flujos y mantiene el lanzamiento explícito de Pages.
- Los flujos especializados de Core o de otras ramas no se desactivan indiscriminadamente; requieren su propia evaluación para preservar controles de investigación.
- Los `push` a ramas de preparación, sin PR abierta, no generan las baterías generales anteriores. Abrir la PR del paquete una vez que estén agrupados código, datos, documentación y pruebas.
- **Límite:** esta configuración elimina ejecuciones duplicadas por eventos; no garantiza que GitHub asigne inmediatamente los trabajos si la cola de Actions está detenida, ni elimina los avisos históricos de fallos.

## Pruebas mínimas de aceptación

- Menús principales y los ocho accesos del cartel deben ser navegables desde móvil.
- No debe existir la placa flotante `.ib-news-rock`; conservar un solo bloque News `.flyer-frame .ib-project-feature`.
- Herramientas: 4 módulos diferenciados; Contacto: 4 tarjetas; Publicaciones: 2 registros públicos actuales.
- Fichas: panel de lectura rápida, identificación, condición de imagen, cautela semántica y enlaces internos; conservar expediente completo y controles.
- Core: resultados visuales y límites explícitos; JSON técnico oculto por defecto.
- Sin errores JavaScript manifiestos, HTML/JSON técnico crudo visible o enlaces internos rotos.
- Comprobar herramientas y datos dinámicos con navegador, no solamente inspeccionar HTML.
- Solo publicar después de pruebas satisfactorias y verificar el SHA del despliegue público.

## Aclaraciones de alcance

La norma no certifica la validez lingüística de ninguna hipótesis. El número de fichas, entradas de interfaz, objetos, bibliografía y DOI son magnitudes diferentes. Los objetivos de biblioteca (500 o 1000 referencias) no cuentan como logros hasta tener referencias curadas. Las reconstrucciones de La Picola permanecen identificadas como hipótesis hasta que la evidencia permita mayor certidumbre.

**Control de cambios:** toda modificación relevante deberá registrar propósito, archivos, pruebas y resultado de despliegue.
