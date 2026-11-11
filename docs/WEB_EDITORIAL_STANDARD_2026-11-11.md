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
