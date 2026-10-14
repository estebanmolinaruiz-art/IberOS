# Orleyl V y VII-B — registro reproducible de signos y límites

Fecha: 2026-10-14. Fuente primaria: Lázaro, Mesado, Aranegui y Fletcher (1981), *Materiales de la necrópolis ibérica de Orleyl*, capítulo IV, PDF digital aportado por el investigador `mupreva194_mupreva153_101.pdf`.

## Procedencia y observaciones comprobadas
- Orleyl **V**, cara única, línea **3**: `BI-TE-R-O-KE-TE-TI-N-E`, Fletcher, **PDF p. 67** (impresa 66); dibujo fig. 22 **PDF p. 65**; fotografía lámina XVII **PDF p. 153**.
- Orleyl **VII-B**, línea **2**: `BA-S-BI-TE-R-O-KE-TI-N-E`, Fletcher, **PDF p. 110** (impresa 109); dibujo fig. 25 **PDF p. 111**; fotografía lámina XXII **PDF p. 158**.
- **PDF p. 118**, «Notas finales»: paralelo editorial `GUDUR BITEROKETETINE` (V-18/19) frente a `GUDUBOIKE BITEROKETINE` (VII-B-6/7). En el segundo el editor emplea una unidad comparada **sin el segmento `BAS-`**, aunque este figura en la transcripción completa de la línea.
- **PDF p. 110**, Fletcher advierte de signos transparentados desde la cara A en zonas no inscritas de la cara B, y del deterioro de un extremo. No confundir transparencia con incisiones propias.
- **PDF p. 66**, el editor señala que los separadores no son garantía universal de límites de palabra. En consecuencia el aislamiento editorial de `BAS-` o `TE` no es demostración de morfema.

## Alineación por signos editoriales (no autopsia)
| Posición alineada | V | VII-B comparada | Estado |
|---|---|---|---|
| 1 | BI | BI | EDITORIAL_ONLY |
| 2 | TE | TE | EDITORIAL_ONLY |
| 3 | R | R | EDITORIAL_ONLY |
| 4 | O | O | EDITORIAL_ONLY |
| 5 | KE | KE | EDITORIAL_ONLY |
| 6 | **TE** | — | **Diferencia editorial principal** |
| 7 | TI | TI | EDITORIAL_ONLY |
| 8 | NE | NE | EDITORIAL_ONLY |

Además hay `BAS-` al principio de la unidad de **VII-B** cuando se reproduce la transcripción completa de su línea. No añadirlo o suprimirlo silenciosamente en comparaciones. El valor de la rótica y la dualidad gráfica exigen cotejo paleográfico por edición.

## Archivo de trabajo
`data/curated/rok_orleyl_editorial_alignment_1981.csv`: **16** filas documentales por segmento de lectura editorial (8 para V, 7 para VII-B más 1 para `BAS`), con cara, línea y referencias PDF. Campo `graphic_photo_verified=false` en todos los casos deliberadamente: la disponibilidad de un dibujo o una fotografía **no demuestra el valor de cada grafema**. Su propósito es permitir auditoría ordenada, no añadir 16 objetos ni 16 evidencias lingüísticas.

## Siguiente validación material
1. Anotar coordenadas de los signos del renglón 3 de V y renglón 2 de VII-B en imagen de alta resolución **con identificación confirmada del sentido de escritura**.
2. Para cada posición mantener `image_observation`, `drawing_observation`, `editorial_reading`, `reading_confidence`, `alternative` y justificación de separadores.
3. Resolver primero transparencia de la otra cara y sectores erosionados, antes de asignar `VISIBLE` o `UNCERTAIN`.
4. No elevar lecturas reconstruidas, equivalencias fonéticas no comprobadas, traducciones ni `HOLD` sin evidencia independiente y revisión externa.

## Dictamen
La variante `TE` es reproducible **como diferencia transcripcional en Fletcher**; la validación gráfica signo a signo permanece abierta. **ROK-RECIPIENT-02 = OPEN**, `automatic_core_promotion=false`, métricas congeladas.
