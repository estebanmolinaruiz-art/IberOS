# G-124 — Picola: medición local de eje R2 y foso, a coste 0 €

Fuente primaria revisada: Moret y Badie 1998, *Archivo Español de
Arqueología*, 71, 53–61, fig. 3 (planta de estructuras ibéricas):
https://doi.org/10.3989/aespa.1998.v71.274

La fuente indica que R2 desemboca en la puerta noreste, situada en el centro
de la cortina de 56 m. La calle tiene 3,55 m de anchura; su eje está a
34 m de la base del escarpe NO y 33,35 m del talud erosionado SE (interpretado
por los autores como ≈34 m originalmente a ambos lados). El foso tiene
5–6 m de anchura superior y la franja defensiva completa mide 12–13 m.

## Resultado reproducible y límites

La **posición central nominal en una coordenada local de la cortina**
es 56/2 = **28 m desde cualquiera de sus extremos**.
Esta es una inferencia métrica del diseño, NO una coordenada excavada
del centro de la puerta. La diferencia de medidas laterales observadas
es 34−33,35=**0,65 m**, compatible con la erosión mencionada por
los autores; NO desplazar R2 medio metro para compensarla.

La publicación presenta planos con una barra gráfica, pero la captura
de la página no se pudo recuperar con resolución suficiente en esta
ejecución. No es posible medir los bordes del foso frente a la
puerta ni georreferenciar el vano a EPSG:25830. No se identifica un
puente o paso inequívoco. Ningún resultado constituye prueba de una
ruta exterior hacia Ilici.

Datos adicionales: Lorrio 2012, figura 3:
https://rua.ua.es/dspace/bitstream/10045/36269/1/2012_Lorrio_RAP.pdf

Reproducir:
```bash
python -m unittest discover -s tests -p 'test_route_picola_local.py'
python -c "from iberos.route_picola_local import assess_picola_local_axes; print(assess_picola_local_axes())"
```

**Siguiente falsación concreta:** conseguir planimetría acotada revisada
de la zona noreste y localizar el punto en que el eje R2, extendido,
intersectaría los bordes interiores y exteriores del foso, especificando
si ese punto coincide con una obra de paso estratigráficamente fechada.
Precio de cualquier fuente o procesamiento: **0 €**.
