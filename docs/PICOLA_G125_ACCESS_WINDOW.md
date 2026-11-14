# G-125 — La Picola, eje R2 y ventana métrica de salida noreste

## Fuente primaria abierta efectivamente recuperada
Moret y Badie (1998), *Archivo Español de Arqueología* 71, pp. 53–61,
figuras 2 y 3. Copia PDF accesible e indexada:
https://pdfs.semanticscholar.org/2d93/6af1694fb61a90aced5cb26dade6f609dd35.pdf
Revista original: https://doi.org/10.3989/aespa.1998.v71.274

La **página impresa 55, figura 3** contiene el plano ibérico y una
barra de escala 0–5–10 m; el texto asocia R2 con la puerta central NE.
La **página impresa 54, figura 2** contiene el perfil restituido de las
defensas. El texto de la página 55 identifica:
- cortina NE: 56 m (posición central nominal: 28 m desde cada extremo);
- glacis desde la muralla al foso: 5–5,5 m;
- foso: ancho superior 5–6 m y profundidad ~2 m;
- conjunto defensivo: 12–13 m, incluyendo más estructuras que el glacis y el foso.

El texto detallado de R2 da 3,55 m de ancho (véanse pp. 56–57).
La figura describe estructuras documentadas en oscuro y restituciones en gris
claro. No se puede asumir que las restituciones son estructuras conservadas.

## Resultado G-125: ventana de búsqueda transversal, NO un paso excavado

Tomando como origen 0 la **cara externa de la muralla NE**, y solo
con un modelo normal al frente, el borde cercano del foso puede estar a
**5–5,5 m**, y el borde lejano del foso a **10–11,5 m**.

Esta suma de intervalos sigue siendo dimensional: el borde real,
la salida de R2, el glacis y el foso no han sido georreferenciados
simultáneamente. La franja defensiva total de 12–13 m no debe
confundirse con la suma glacis + foso.

La lámina PDF de 1998 se ha localizado en un espejo de acceso abierto,
pero la herramienta de captura de la página devolvió fallo de caché.
**No ha sido posible digitalizar píxeles y ajustar una transformación
a EPSG:25830**; sin ello no hay incertidumbre cartográfica estimable,
intersección real ni longitud de un puente medido.

## Modelo
`iberos.route_picola_exit_window.estimate_exit_window()` calcula las
envolventes para ángulos hipotéticos, conserva su procedencia y devuelve
siempre `site_epsg25830_geometry: null` y ausencia de puente acreditado.

Pruebas:
```bash
python -m unittest discover -s tests -p 'test_route_picola_exit_window.py'
```

## Próxima medición que cambia el dictamen

1. Capturar con escala la figura 3 y digitalizar la prolongación del eje R2
   desde su tramo conservado.
2. Diferenciar bordes excavados del foso y trazos restituidos.
3. Identificar un mismo punto topográfico en esa planta y en la nueva
   planimetría del Plan Director; obtener al menos 3 puntos de control no
   colineales y residuos de ajuste.
4. Recalcular las intersecciones con el foso y atribuir intervalos de error.
5. Contrastarlas estratigráficamente con eventuales obras de paso y
   su cronología 430–350 a. C.

**Política inalterable: 0 € de coste adicional.**
