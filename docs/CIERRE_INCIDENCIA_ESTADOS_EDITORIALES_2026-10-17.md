# IberOS — cierre de incidencia web y distinción editorial (17-10-2026)

## Incidencia cerrada

El workflow «Comprobaciones web gratuitas» falló en commit `2a878bdf` por una aserción que trataba `DOCUMENTARY_CONTROL_AVAILABLE` como documentación pendiente. La prueba de integración fue corregida para excluir tanto `PUBLICABLE_EDITORIAL` como `DOCUMENTARY_CONTROL_AVAILABLE` del recuento de pendientes.

**Versión verificada:** `757d08f552810ed9834121b4b008d7cf0b650b5d`; workflows `tests`, `Comprobaciones web gratuitas` y `pages`: **success**.

## Significado de los estados (según src/iberos/publication_gate.py)

- `PUBLICABLE_EDITORIAL`: ficha normal con hipótesis, evidencias, límites y cita, y ficha registrada. **No** garantiza una traducción válida.
- `EDITORIAL_REVIEW_REQUIRED`: ficha normal que necesita documentación editorial.
- `DOCUMENTARY_CONTROL_AVAILABLE`: ficha de control con material documental suficiente para mostrarse **sin tratarla como interpretación semántica**; incluye `IBR-CTL-*` y `IBR-COI-0002`.
- `DOCUMENTARY_CONTROL_REVIEW`: ficha de control aún pendiente de revisión documental.

Los controles documentales no cuentan como traducciones ni deben presentarse como hipótesis semánticas. Todos los registros mantienen `translation_validated=false`, `scientific_validation_status=UNVERIFIED` y `automatic_core_promotion=false`.

## Observación sobre los recuentos

Los recuentos editoriales deben derivarse del **manifest generado de la versión actual**; no reutilizar cifras históricas de una tanda de publicación para redactar titulares o pruebas rígidas. La cola de 16 casos identifica una necesidad de cotejo en un instante inicial y debe actualizarse cuando las fuentes específicas ya figuren en el corpus.

## Próxima prioridad

Conservar estabilidad de publicación y avanzar en el cotejo independiente de las ediciones e imágenes, dejando explícita la diferencia entre reproducción localizada, lectura editorial y cotejo paleográfico visual. No publicar como logros verificados hipótesis, métricas de difusión inexistentes o imágenes sin permiso.
