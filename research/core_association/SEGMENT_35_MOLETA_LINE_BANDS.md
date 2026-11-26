# SEGMENT-35 — Localización provisional de franjas de escritura en Moleta

Fecha 2026-11-22. **Ejecución GitHub Actions #45069294745 SUCCESS**. Fuente fija: PDF original *Palaeohispanica* 8/2008 con SHA256 `2965fd62b2a040aa99bb5428bbe8018fba56ebfb201b35034e93a2c38b292e22`, páginas PDF base 0 209 (figura fotográfica 4) y 210 (dibujo 5).

El proceso recupera los recortes identificados por SEGMENT-34 y aplica CLAHE, umbral adaptativo, supresión morfológica de líneas horizontales largas, proyección de tinta por filas y agregación de intervalos. No usa ninguna etiqueta fonética de Orleyl ni cortes de signos de la edición.

**Salida observable:** dos bandas candidatas en la foto (imagen 691×691): B01 x69–621, y97–289; B02 x69–621, y400–582. Cinco bandas candidatas en el dibujo (imagen 694×931): B01 x69–624 y134–292; B02 y341–492; B03 y498–551; B04 y604–731; B05 y728–800. Se detectaron dos intervalos de actividad en la primera figura y nueve en la segunda, filtrados hasta dos y cinco por tamaño y densidad. Las bandas pueden incluir varios renglones, decoraciones, bordes y fracturas: **NO SON RENGLONES CONFIRMADOS**.

Se registran **0 filas independientemente verificadas, 0 signos identificados, 0 tasa de acierto externa**. No se puede afirmar generalización del 81.4% de SEGMENT-32. Se requiere inspección visual de cada rectángulo y asignación de límites de signo por un revisor independiente, antes de analizar el reconocimiento.

Código: `research/core_association/segment35_moleta_lines.py`. Artefacto de investigación temporal 1 día: `https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/45069294745/artifacts/14772702234` (CSV, JSON y dos vistas anotadas de las láminas), sin redistribuir imágenes en repositorio público debido a licencia de la publicación. Core/C594/C474/C539/C541/FULL3406 inalterados; coste adicional 0 €.