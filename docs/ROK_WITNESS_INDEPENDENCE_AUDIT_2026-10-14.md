# IberOS CORE — Auditoría de testigos ROK
Fecha 2026-10-14. Estado: **REVISIÓN DOCUMENTAL PARCIAL; gate ROK-RECIPIENT-02 OPEN**.

## Resultados de cotejo

| Testigo | Identidad y relación verificable | Estado en corpus público | Independencia/cierre |
|---|---|---|---|
| Orleyl F.9.5 | Plomo diferenciado, de tumba II Punta d'Orlell | No confundir con F.9.8, que sí figura en `IBR-PLM-0006` | Testigo físico aparentemente distinto de F.9.7; dependencia de contexto compartido requiere revisión; NP/rol externo no fijados |
| Orleyl F.9.7 | Otro plomo de la misma tumba II | No se ha establecido correspondencia propia con OBJECT_ID curado en la comprobación | Nunca equiparar automáticamente a F.9.5 por compartir tumba; hay dependencia textual en falsificación Marsal C07-003 |
| Marsal H.0.1 | Inscripción identificada por la matriz ROK como réplica formal fuera de muestra | No corresponde al control falso C07-003; cotejo de procedencia/inventario original pendiente | Papel de destinatario no anclado externamente, HOLD no justificado |
| Marsal C07-003 | Falsificación moderna de la colección Marsal; copia material textual de Orleyl, especialmente F.9.7 | `IBR-CTL-0003` `EXCLUDED_CONTROL` | Rechazar como evidencia positiva física o semántica |
| Tivissa T.07.03 | Plomo de Tivissa, Castellet de Banyoles; NP-te-ROK + SALIR + Q | `IBR-PLM-0002` `INCLUDE` | Caso conocido, no nuevo HOLD; no fija dirección ROK |
| Pech-Maho B.7.38 | Pech-Maho V, contexto `ban · kutur · bideŕokan` | `IBR-PLM-0003` `INCLUDE` | Compatibilidad formal, función exacta abierta |

## Principales riesgos metodológicos
1. `F.9.5` y `F.9.7` son testigos físicos distintos según su clasificación como plomos de tumba II; compartir tumba no es una identidad física duplicada. Revisar dependencia arqueológica y textual antes de contarlos como pruebas independientes de un mismo fenómeno.
2. La falsificación **Marsal C07-003** no debe contaminar el testimonio **Marsal H.0.1**, ni sumarse como paralelo externo.
3. El registro público de 38 objetos cubre algunos casos (Tivissa, Pech-Maho, Orleyl F.9.8) pero no permite asumir que los otros candidatos estén incorporados como unidades físicas individuales.
4. La presencia de NP+TE o ROK no fija por sí sola destinatario; la evidencia contextual/onomástica se audita antes de contrastar H1/H2/H3.
5. Mantener la separación `PHYS_ID` de `ARCHAEOLOGICAL_CONTEXT`: la coincidencia de tumba puede representar dependencia de contexto, no fusión física.
6. No trasladar a HOLD retrospectivos anteriores a C474.

## Fuentes de cotejo
- Registro curado `data/curated/iberos_objects_registry_v2.0.csv`.
- Matriz `docs/ROK_RECIPIENT_MATRIX_2026-10-08.md`.
- Estudio sobre Moleta del Remei, donde F.9.5, F.9.6 y F.9.7 se documentan como tres plomos de la tumba II: https://www.researchgate.net/publication/245585243_Una_inscripcion_iberica_sobre_plomo_procedente_del_poblado_de_la_Moleta_del_Remei_Alcanar_Montsia_Tarragona
- Luján y López Fernández, «Nuevas inscripciones paleohispánicas del Museo Arqueológico de Sevilla», `Palaeohispanica` 17 (2017), 125–139, DOI https://doi.org/10.36707/palaeohispanica.v0i17.136 — falsificación de Marsal con copia de Orleyl.
- `docs/ROK_EXTERNAL_EVIDENCE_AUDIT_2026-10-13.md`.

## Resultado operativo
Ninguna de estas referencias proporciona todavía la segunda construcción ROK con destinatario fijado de modo extralingüístico. **ROK-RECIPIENT-02 permanece OPEN; automatic_core_promotion=false.** Pendiente cotejo de imágenes, signaturas museísticas y ediciones originales, especialmente H.0.1 y los plomos Orleyl.
