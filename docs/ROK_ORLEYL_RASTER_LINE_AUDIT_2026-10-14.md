# IberOS — Orleyl V y VII-B, localización gráfica de líneas (2026-10-14)

**Entrada primaria:** archivo proporcionado por el investigador `mupreva194_mupreva153_101.pdf`, 159 páginas. **Método:** renderización local de las páginas PDF **65** (figura 22, Orleyl V), **111** (figura 25, Orleyl VII-B), **153** (lámina XVII) y **158** (lámina XXII) y orientación +90° horario para los dibujos. Las coordenadas abajo son **píxeles del render a escala 1,7×**, NO coordenadas del soporte arqueológico, y se refieren a bandas de renglón, no a caracteres confirmados.

| Testimonio | Figura | Localizador editorial | Raster girado 90° horario: recorte aproximado (x0,y0,x1,y1) | Imagen/fotografía | Estado |
|---|---|---|---|---|---|
| Orleyl V | Fig. 22, PDF p. 65 | V línea 3, lectura Fletcher `BI-TE-R-O-KE-TE-TI-N-E` | `(0,431,1296,495)` | Lámina XVII, PDF p. 153 | `LINE_REGION_LOCATED; GLYPHS_UNVERIFIED` |
| Orleyl VII cara B | Fig. 25, PDF p. 111 | VII-B línea 2, lectura Fletcher `BA-S-BI-TE-R-O-KE-TI-N-E` | `(0,368,1296,440)` | Lámina XXII, PDF p. 158 | `LINE_REGION_LOCATED; GLYPHS_UNVERIFIED` |

Las bandas incluyen márgenes y en ocasiones trazos de renglones vecinos para preservar contexto. El tamaño orientado al recorte se deriva de una página `575.52 × 762.24` puntos y un raster de aproximadamente `979 × 1296` píxeles, rotado a `1296 × 979`. Las coordenadas son **orientativas para reproducir ventanas de inspección**, no una alineación signo a signo.

## Resultado de inspección
- La figura 22 representa seis líneas y la figura 25 cinco líneas, de acuerdo con sus dibujos y las descripciones editoriales.
- Se identifican bandas gráficas compatibles con la **posición de los renglones publicados**. Las fotografías presentan menor legibilidad que los dibujos: no pueden homologarse automáticamente los caracteres.
- El segmento `TE` interno extra atribuido a Orleyl V permanece confirmado **solo como diferencia editorial de transcripción**, no como grafema individual verificado por fotografía.
- La mención de `BAS-` en VII-B corresponde a la transcripción completa de Fletcher y no debe borrarse de una nueva edición diplomática.
- No afirmar `VISIBLE` para glifos concretos hasta localizar los límites de token, orientación, correspondencia foto/dibujo y paleografía de la rótica.

## Archivo de apoyo
`orleyl_rok_band_comparison_2026-10-14.png` generado en el espacio de trabajo, con las dos bandas de contexto extraídas de los dibujos. Se entrega al investigador como artefacto independiente; **no** consta subido al repositorio por este commit.

## Próxima etapa verificable
Recortar y localizar cada token con un especialista paleográfico, marcando carácter, lectura editorial, dibujo, fotografía, alternativa y grado de certeza. Revisar expresamente transparencia de cara A en VII-B y manchas de la fotografía. No contar recortes como testimonios adicionales.

**ROK-RECIPIENT-02: OPEN.** Sin promoción automática, sin cambios de autoridad ni de métricas.

## Control de calidad de regiones — 2026-10-14

Al volver a inspeccionar el archivo `orleyl_rok_band_comparison_2026-10-14.png` junto con el PDF original, se observa que **la ventana previamente etiquetada como línea 3 de Orleyl V incluye dos hileras de trazos**. En VII-B la ventana de la figura 25 también incluye material visible de un renglón vecino y hay interferencias descritas por Fletcher entre ambas caras.

**Corrección obligatoria:** las coordenadas de la tabla anterior son *regiones candidatas*, no delimitaciones exclusivas o validadas del renglón numerado. Cambiar en la interpretación operativa `LINE_REGION_LOCATED` por `CANDIDATE_REGION_MULTIROW` (V) y `CANDIDATE_REGION_WITH_NEIGHBOR` (VII-B). No asignar posición de glifos, `VISIBLE`, ni una prueba del `TE` adicional sobre estos recortes.

Se generó localmente la imagen de control `orleyl_control_reglones_2026-10-14.png` con advertencias visuales, sin nuevas lecturas. La imagen no se ha subido a este repositorio.

**Siguiente comprobación:** localizar fronteras de cada renglón sobre la figura completa, distinguir línea de signo visible por transparencia y cotejar sector en lámina fotográfica. Se conserva la transcripción de Fletcher como `EDITORIAL_ONLY`; `ROK-RECIPIENT-02` sigue OPEN.
