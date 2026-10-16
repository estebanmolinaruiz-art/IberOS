# IberOS — balance verificable del cotejo (16-10-2026)

## Alcance y distinciones

El registro consta de **38 fichas**. La cola `docs/COLA_COTEJO_FICHAS_2026-10-16.md` enumeró **16** con hipótesis y bibliografía general, pero sin campo `citation` específico. Eso no significa que esas 16 carezcan de bibliografía ni que las otras 22 hayan superado control paleográfico independiente.

**Estado actual de las 16 de la cola:** 2 informes de cotejo textual/documental previos (Val de Alegre y Caminreal); 14 sin informe de cotejo individual de ese nivel registrado en esta cola. **0 cotejos paleográficos visuales independientes cerrados en esta tanda; 0 traducciones semánticas validadas.** No alterar automáticamente las publicaciones del Core.

| Caso | Verificación | Fuente | Restricción |
|---|---|---|---|
| `IBR-CER-0005` Val de Alegre I | Lectura editorial preferida `kutuki[---]` y alternativa `[---]kituku`; inventario `vad.2000.25`; páginas 199–200 | Díaz Ariño y Mayayo, *Palaeohispanica* 8 (2008), 197–202, DOI 10.36707/palaeohispanica.v0i8.264, https://ifc.dpz.es/recursos/publicaciones/28/40/11diazmayayo.pdf | Preferencia editorial no resuelve paleografía independiente; lámina 1, figura 4 pendiente de comprobación visual |
| `IBR-MUS-0001` Caminreal | Edición y cuatro ejes del debate identificados: `likine`, `ekiar`, topónimo e identidad de `likine` | Simón Cornago, *Palaeohispanica* 15 (2015), 87–127, DOI 10.36707/palaeohispanica.v0i15.39, https://www.ifc-ojs.es/index.php/palaeohispanica/es/article/view/39 | No hay traducción inequívoca ni asignación funcional cerrada; falta cotejo de láminas y argumentos por variante |
| `IBR-OBJ-0002` Oliete | Bibliografía en la ficha: Ferrer i Jané (2014) y Vicente et al. (1990); localizados metadatos y resumen editorial del primero | Ferrer i Jané, *Veleia* 31 (2014), 227–259, DOI 10.1387/veleia.13345, https://ojs.ehu.eus/index.php/Veleia/article/view/13345 | **No afirmar todavía** que el artículo coteje directamente la tortera de Oliete, ni que confirme la lectura: identificar pasaje, lámina y edición de Vicente et al. primero |

## Hallazgo de calidad editorial

La referencia de 2008 de Val de Alegre en `site/data/ficha-enrichment-1.json` es abreviada. Su identificador editorial preciso es **DOI 10.36707/palaeohispanica.v0i8.264**, con pp. 197–202. El DOI del informe general de IberOS **no sustituye** esta cita original. La atribución textual de `kutuki` debe señalar la alternativa `[---]kituku`.

## Siguientes pasos comprobables

1. Inspeccionar la reproducción original de la lámina 1, figura 4 de Val de Alegre (la captura del PDF desde el buscador ha fallado), y documentar visibilidad real de cada trazo.
2. Contrastar `ekiar` / `likine` en el estudio completo de Caminreal, con argumentos y páginas por interpretación rival.
3. Recuperar la fuente de Oliete de Vicente et al. (1990), cotejar objeto y su lectura antes de integrar una hipótesis de signario.
4. En los 13 restantes de la cola, priorizar ediciones con DOI/identificador de corpus y fotos autorizadas. No asignarles condición de cotejados por tener bibliografía general.

**Estado técnico:** tres workflows `tests`, `Comprobaciones web gratuitas` y `pages` superados para commit `a569df72c13e9b6201a5702e74c9ba9afe0edaa7` en la última consulta previa a guardar este documento.
