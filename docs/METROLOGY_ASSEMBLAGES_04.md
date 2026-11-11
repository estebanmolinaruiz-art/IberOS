# METROLOGY-ASSEMBLAGES-04 — 37 piezas en cinco conjuntos publicados

**Lectura documental, no test prospectivo.** Fuente:
Martínez Chico, David y González García, Alberto (2018), «Un conjunto de
ponderales ibéricos procedente de Villanueva de la Jara (Cuenca)»,
*Florentia Iliberritana* 29:381–390.
https://revistaseug.ugr.es/index.php/florentia/article/download/8829/7412/25457

Se han transcrito **todos los pesos citados en cinco conjuntos explícitos**,
incluidos los que no encajan en la serie de 2,1 g.
Esta NO es una colección de todos los ponderales ibéricos, solo una
submuestra reproducible delimitada de esa publicación.

| Conjunto | Piezas | Dentro de ±5 % de serie publicada de 2,1 g |
|--|--:|--:|
| Villanueva de la Jara | 5 | 3 |
| El Cigarralejo, sepultura 200 | 10 | 6 |
| Cabecico del Tesoro, sepultura 117 | 13 | 7 |
| Orleyl, sepultura 11 | 5 | 2 |
| Covalta, construcción 27 | 4 | 4 |
| **Total** | **37** | **22** |

Los cinco pesos de Villanueva (21,0; 41,5; 62,7; 106,5;
214,3 g) se describen **directamente** en el artículo de 2018.
Los otros 32 son cifras **citadas de estudios anteriores** por el
artículo de 2018, no nuevas mediciones de los autores ni de IberOS.
El hallazgo de Villanueva fue superficial, sin excavación controlada.

El ajuste usa **únicamente** las doce razones teóricas de Fletcher y
Silgo (1995), como las recoge la fuente:
1, 2, 2,5, 3, 4, 5, 8, 10, 20, 40, 60, 100.
Por ejemplo, las masas 62,7 g y 106,5 g de Villanueva NO encajan
dentro de ±5 % en esas doce series; la publicación les atribuye
también valores 30 y 50 de una **extensión interpretativa**,
que NO se incorpora retroactivamente para mejorar este diagnóstico.

**La proporción 22/37 no es precisión lingüística, ni validación
de un sistema de denominaciones ni refutación del modelo híbrido.**
No hay lectura independiente del valor marcado en las 37 piezas.
Tampoco existe un diseño ciego ni selección aleatoria de todos los
yacimientos. Las piezas de una sepultura forman grupos dependientes.

La clave científica es pasar de ajustes retrospectivos de masa a
**series materiales completas**, con mediciones instrumentales, marcas
verificadas y contrastes independientes entre nombres de unidades.
La contestación del Museo de Moncada del 5-11-2026 solo promete
documentación futura; no incluye masas primarias.

Ejecutar:
\`\`\`bash
python -m iberos.metrology_assemblages_04 --json /tmp/assemblages04.json
pytest -q tests/test_metrology_assemblages_04.py
\`\`\`

No se consulta ni modifica FULL3406, splits, GOLD o métricas oficiales.
