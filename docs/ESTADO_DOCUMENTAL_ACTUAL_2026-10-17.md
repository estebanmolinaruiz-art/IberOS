# IberOS — auditoría documental actual (17 de octubre de 2026)

## Recuento obtenido directamente de los cinco ficheros vigentes

Fuente: `site/data/ficha-enrichment-{1..5}.json` de la rama `main`. Se comprueba presencia de texto no vacío en `citation`, **no** corrección de la referencia frente al original.

| Medida | Resultado |
|---|---:|
| Objetos registrados en los cinco ficheros | 38 |
| Con `citation` no vacío | 36 |
| Sin `citation` | 2 |
| Traducciones semánticas verificadas por esta auditoría | 0 |

**Fichas sin cita específica:** `IBR-LAP-0005` (arquitrabe bilingüe de Sagunto) e `IBR-MUS-0001` (mosaico de Caminreal). Ambas tienen bibliografía general e informes documentales diferenciados, que no sustituyen un cotejo de signos ni justifican copiar una cita sin comprobación de pasajes.

## Reconciliación de la cola histórica de 16

La cola del 16 de octubre es una instantánea y **no** debe repetirse como lista de 16 campos `citation` vacíos. **14 de los 16** expedientes iniciales ya contienen texto en el campo `citation`; quedan dos del inventario inicial sin él.

**Atención:** la cobertura de citas (36/38) **no** equivale a `PUBLICABLE_EDITORIAL`, a un informe de cotejo independiente, a un facsímil con permiso de publicación, ni a traducciones validadas. El manifest de publicación requiere además ficha registrada, hipótesis, evidencia y límites; los objetos de control documental tienen categorías independientes.

## Próximos pasos

1. Sagunto: contrastar *MLH III* F.11.8 y los pasajes de Orduña / Velaza antes de registrar cita y variante paleográfica precisas.
2. Caminreal: contrastar edición, páginas, lectura y posibles variantes en Simón Cornago y *MLH*, sin adoptar una glosa literal de `ekiar`.
3. Revisar por pieza las **36 citas existentes** para confirmar procedencia, página, figura y licencia visual; su presencia no acredita revisión completa.
4. Generar los recuentos futuros automáticamente, nunca usando cifras editoriales congeladas.

## Estado web durante la auditoría

Commit consultado `261a8a6680c869999048a18440bf7b149a65fa75`: `tests` y `pages` = **success**; `Comprobaciones web gratuitas` = **in_progress** en ese momento. Este archivo solo documenta lo observado: nuevas ejecuciones deben verificarse por GitHub Actions.
