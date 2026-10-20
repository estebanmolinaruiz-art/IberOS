# 6P-03 — Control de correspondencia entre objeto, inscripción y edición (2026-10-20)

## Alcance y fuente
Cruce de los **38 objetos** de `data/curated/iberos_curated_objects_v1.jsonl` con el índice de enlaces individuales `data/curated/iberos_partial_entry_link_v2.4.csv`. El auditor reproducible es `scripts/audit_object_entry_editions.py`.

## Resultados del primer pase
- 38 objetos curados; 13 con al menos una entrada individual enlazada en la tabla; 25 sin enlace de entrada en esa tabla.
- 6 objetos marcados expresamente `NEEDS_SUBENTRY_SPLIT`: IBR-CER-0002, IBR-CER-0004, IBR-OBJ-0001, IBR-PLM-0008, IBR-PLM-0009, IBR-PLM-0012.
- Enlace al índice externo no implica comprobación de correspondencia fotográfica, autopsia, lectura diplomática, edición primaria ni independencia del testimonio.
- `VERIFIED` y `FULL_GROUP_VERIFIED` son estados del enlace de índice, **no** validación paleográfica o lingüística.
- La verificación rigurosa del tríptico objeto físico / subinscripción / edición **no se ha completado** para los 38 objetos. En el auditor comienza con 0 trípticos independientemente corroborados, no porque todos sean falsos sino porque falta la evidencia de cotejo.

## Cola de alta prioridad
1. Dividir los seis objetos `NEEDS_SUBENTRY_SPLIT` sin crear nuevos objetos físicos para sus caras o inscripciones.
2. Recuperar las entradas individuales de los 25 objetos ausentes del enlace parcial, conservando la identificación de objeto físico.
3. Revisar **Pech-Maho V** y **Coimbra** contra ediciones concretas, y **La Serreta** contra edición primaria en lugar de una referencia enciclopédica.
4. Reconciliar diferencias entre referencias MLH/BDH, entradas Cathalaunia y publicaciones; anotar en la ficha página/figura y alternativas.
5. Registrar explícitamente el grupo de dependencia física antes de construir conjuntos independientes para VALIDATION-01.

## Datos obligatorios para cerrar una correspondencia
`object_id`; ID de subinscripción/cara; referencia epigráfica; ID de catálogo externo si existe; edición primaria; página/figura; imagen/facsímil y derechos; lectura diplomática; variantes; comprobación del soporte; revisor, fecha y segundo contraste; estado de independencia.

**Puerta de seguridad:** no convertir citas o marcadores `PALEO_Status=READY` en aprobaciones científicas. No cerrar 6P-03 hasta probar cotejos de ejemplo con documentación y pruebas.
