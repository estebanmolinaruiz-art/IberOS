# GeoSites G-140 / FOTO-CHECK-02 — ajuste fotogramétrico entre fotografías originales

**Fecha:** 2026-11-22. **Coste adicional 0 EUR.** Las 9 fotos del usuario son el material de referencia. Se ha ejecutado un algoritmo reproducible en paquete local `IberOS_FOTO_CHECK_02.zip`.

Método: SIFT, máximo 1700 puntos por JPEG, copias 768×576 (mitad del original), correspondencias descriptor BF-L2, test Lowe ratio < 0,70, homografía foto-a-foto RANSAC con umbral 4 px. RMSE refiere píxeles de copias reducidas **y no metros**.

| Par | Inliers RANSAC | RMSE px |
|---|---:|---:|
| IMG_1285 ↔ IMG_1288 | 592 | 1,834 |
| IMG_1286 ↔ IMG_1287 | 247 | 1,729 |
| IMG_1288 ↔ IMG_1289 | 408 | 1,281 |
| IMG_1283 ↔ IMG_1284 | 429 | 1,192 |
| IMG_1286 ↔ IMG_1288 | 187 | 1,380 |

Pares IMG_1278 ↔ IMG_1283 e IMG_1283 ↔ IMG_1287 no admiten estimación fiable (menos de 6 matches); IMG_1284 ↔ IMG_1290 solo 3 inliers (rechazado). Los emparejamientos pueden corresponder a elementos modernos de la escena tridimensional, por lo que estos ajustes validan **solapamiento entre vistas**, NO son una georreferenciación al yacimiento ni son identificación de muros arqueológicos.

La fuente Moret–Badie 1998 (https://doi.org/10.3989/aespa.1998.v71.274), figura 3 p.55, confirma textualmente R2→puerta NE, cortina NE conservada 56m y foso ancho superior 5–6m, distinguiendo oscuro excavado/gris claro restituido. La captura visual de la figura 3 falló por cache miss: **NO se obtuvo la imagen del plano ni se ejecutó homografía plano→foto**.

**Veredicto:** 0 puntos de control cruzados con plano certificados; 0 posiciones UTM de muros, foso, puerta NE o calle R2 extraídas de las imágenes. La excavación rectangular visible en 1286/1287 no se acredita como foso antiguo. Próximo bloqueo es disponer de figura 3 o planta reciente georreferenciada con al menos 4 correspondencias arqueológicas no colineales y puntos de control independientes de validación.

Informe y código se conservan localmente; rama experimental y Core científico no se fusionan ni alteran.