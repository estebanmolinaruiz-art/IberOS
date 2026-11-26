# GeoSites G-146 — Prueba de giro mínimo, 22-11-2026

**Nuevo cálculo matemático independiente.** El azimut auténtico de la puerta noreste no ha podido medirse: el visor original de la figura 3 de Moret y Badie 1998 falla en la extracción de imagen. Los resultados siguientes son **condicionales**, no identificación de un camino.

Puntos de referencia EPSG:25830: BIC Picola A1 (713265,4230490), termas orientales Alcudia (701823.285,4234872.059). **No son centros de puertas.** Distancia 12252.154228m, azimut hacia Alcudia 290.956325°.

Si una salida hipotética se prolonga s metros a azimut α, Q=A+s(sinα,cosα), y gira después hacia B siguiendo un segmento recto, el cambio mínimo neto de dirección es T=|wrap180(azimut(Q→B)−α)|. Sobrelongitud mínima por Q: E=s+||Q−B||−||A−B||.

Para **s=10 m**:
- α 25°: T=94.0903°, E=10.7092m.
- α 45°: T=114.0864°, E=14.0777m.
- α 65°: T=134.0773°, E=16.9542m.
La predicción no demuestra un giro brusco ni dice dónde ocurriría: trayectorias curvas distribuyen ese cambio por el recorrido.

Para un radio hipotético de perturbación de r=250m en cada extremo, cota conservadora de desvío angular arcsin(2r/D)=2.3388°; el caso 25° aún supera 91.75°. Con r=450m ya no se puede garantizar superar 90°. Estos radios **NO son errores topográficos medidos**.

El umbral instantáneo de salida NE que hace crecer la distancia a B es α=20.956325°; orientación del eje R2 no medida. Se ejecutaron **13 pruebas locales** sobre código Python reproducible, escenarios CSV, JSON y curva PNG; el paquete se entrega como G146. La ausencia de una planta gráfica calibrada impide confirmar el azimut real y por tanto **no se ha validado arqueológicamente** esta predicción.

Próximo control independiente: capturar figura 3 con norte+escala, puntos de muros excavados y no restituidos, medir eje R2 con incertidumbre, identificar coordenadas de puertas y algún tramo fechado tras el foso. No alterar el Core ni publicar un trazado inexistente. Coste adicional 0 EUR.

Fuente: https://doi.org/10.3989/aespa.1998.v71.274 (R2 desemboca en puerta NE, eje interno simétrico).