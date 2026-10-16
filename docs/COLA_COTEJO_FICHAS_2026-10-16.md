# IberOS — cola de cotejo bibliográfico por pieza (2026-10-16)

**Auditoría reproducible sobre** `site/data/ficha-enrichment-{1..5}.json` en la rama `main`. Este inventario registra la ausencia de una **cita editorial específica** (`citation`) cuando existe ya una hipótesis documental. No afirma que la bibliografía sea errónea ni que la transcripción se haya revisado. No son 16 nuevos descubrimientos.

**Resultado:** 16 expedientes con hipótesis, campo `citation` vacío y bibliografía general vinculada. **No promover** por el mero hecho de tener referencias. La cobertura publicable debe calcularse separadamente desde `fiche_publication_status_v1.json` generado.

| Orden | OBJECT_ID | Pieza | Referencias generales | Trabajo pendiente |
|---:|---|---|---:|---|
| 1 | `IBR-CER-0005` | Dolium de Val de Alegre I | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 2 | `IBR-LAP-0005` | Arquitrabe bilingüe de Sagunto | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 3 | `IBR-MUS-0001` | Mosaico de La Caridad, Caminreal | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 4 | `IBR-OBJ-0002` | Tortera inscrita de Oliete | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 5 | `IBR-PLM-0007` | Plomo de Casinos (BDH V.02.02) | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 6 | `IBR-PLM-0008` | Signarios del Tos Pelat (BDH V.21.01-02) | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 7 | `IBR-PLM-0009` | Plomo I de La Serreta | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 8 | `IBR-PLM-0010` | Plomo greco-ibérico de El Cigarralejo | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 9 | `IBR-PLM-0011` | Plomo de la Moleta del Remei | 1 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 10 | `IBR-PLM-0012` | Lámina greco-ibérica de la Illeta dels Banyets | 1 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 11 | `IBR-PLM-0013` | Pequeño plomo del Pico de los Ajos (campaña 2018) | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 12 | `IBR-RUP-0001` | Signario rupestre de Ger | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 13 | `IBR-RUP-0002` | Signario rupestre de Bolvir | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 14 | `IBR-RUP-0003` | Signario dual de Latour-de-Carol | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 15 | `IBR-RUP-0004` | Signario no dual de Latour-de-Carol | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |
| 16 | `IBR-RUP-0005` | Abecedario no dual de L'Esquirol | 2 | Cotejar edición primaria, pasaje/página exacta, forma y atribución de lectura |

## Gate para cerrar un expediente

1. Recuperar edición epigráfica primaria o catálogo fiable y registrar enlace, DOI/signatura, páginas y versión consultada.
2. Contrastar la **identidad exacta** del objeto y la atribución de la lectura; diferenciar registro diplomático, lectura normalizada y propuesta de segmentación.
3. Registrar discrepancias y variantes explícitamente, no resolverlas por intuición.
4. Relacionar cada afirmación `evidence`/`inference`/`hypothesis` con el pasaje exacto, consignar contraejemplos y límites.
5. Comprobar independencia documental. Solo entonces completar `citation` y solicitar revisión editorial humana. No modificar `meaning_validated`, `translation_validated` ni los gates congelados del Core.

**Protección:** las imágenes o modelos 3D sin permiso de reproducción verificado deben mantenerse enlazados a la fuente, no copiados a la web.

## Seguimiento

Los nombres y recuentos se han obtenido del repositorio, sin consultar ni avalar aquí las ediciones primarias. El orden es de inventario, no de prioridad científica. Consultar `docs/PROJECT_SYNC_WEB_2026-10-16.md` y `docs/PUBLICATION_BATCH_2026-10-16.md` antes de crear nuevas interpretaciones.
