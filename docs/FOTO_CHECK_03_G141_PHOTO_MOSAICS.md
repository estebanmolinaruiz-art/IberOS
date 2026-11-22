# FOTO-CHECK-03 / GeoSites G-141 — mosaicos reales de La Picola y búsqueda de planos independientes
Fecha: 2026-11-22. Coste adicional: **0 EUR**.

## Proceso ejecutado
Procesados los originales JPEG subidos por el usuario, sin GPS ni rumbo EXIF verificable. OpenCV SIFT con 1700 puntos, test Lowe 0.70 y RANSAC umbral 4 px sobre copias a media resolución (768×576). Homografía foto→foto para visualizar elementos solapados; **NO** es homografía plano→foto y las zonas con paralaje pueden aparecer duplicadas o desalineadas.

| Pareja | Correspondencias válidas | RMSE (px, media resolución) |
|---|---:|---:|
| IMG_1286/IMG_1287 | 255 | 1.695 |
| IMG_1288/IMG_1289 | 412 | 1.291 |
| IMG_1283/IMG_1284 | 431 | 1.194 |

Se generaron tres panoramas JPG y paquete local ZIP con código fuente reproducible, métricas CSV y registro JSON. **No están integrados en el Core ni se han desplegado en web.** La calibración es solo en píxeles, no cartográfica.

## Nuevas referencias para comprobación cruzada
- Moret y Badie, 1998, *AEspA* 71, fig. 3 p.55, DOI: https://doi.org/10.3989/aespa.1998.v71.274 (original textual accesible: R2 se dirige a puerta NE; planos distingue conservado/restituido; foso anchura 5–6 m en superficie; cortina NE 56m). Se intentó captura gráfica con resultado cache miss; **la imagen del plano NO fue obtenida ni digitalizada**.
- Moret 2000–2001, *Zephyrus* 53–54 fig.4a, reproduce planta, norte y escala 0–50m: https://revistas.usal.es/uno/index.php/0514-7336/es/article/download/4997/5033/0 ; imagen no digitalizada.
- Museo del Mar Santa Pola, recurso visual aéreo de la protección BIC y fortificación: https://museodelmarsantapola.com/estar-preparado-para-cuando-venga-la-oportunidad-un-proyecto-tecnico-para-la-puesta-en-valor-de-un-area-relevante-y-degradada-del-bic-picola/ . Es un localizador institucional, no mapa de GCP arqueológicos.
- BOE-A-2022-4134 acredita perímetro de BIC, sin calibrar esquinas de cada estructura visibles en fotos.

## Dictamen
Las tres uniones de fotografías están respaldadas por correspondencias matemáticas; **cero** puntos arqueológicos idénticos foto–planta fueron verificados. No se han localizado en las fotos con certeza la puerta NE, R2, el foso o un paso. La excavación rectangular visible en 1286/1287 no se debe etiquetar como foso. No se promueven polígonos geográficos ni se altera el Core.

## Próximo dato requerido
Plano de excavación actual en coordenadas ETRS89 o la figura 3 original legible y orientada, con cuatro vértices arqueológicos identificables en fotografías y puntos independientes para estimar error fuera del ajuste.
