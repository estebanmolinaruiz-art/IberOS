# METROLOGY-HYBRID-02 — tres unidades a/o/ki

Ensayo del 4-11-2026; **retrospectivo**. El resumen de Ferrer i Jané
(2026), Quaderns de prehistòria i arqueologia de Castelló 42, 101-122,
propone un sistema **híbrido**: entre a y o base 10; entre o y ki base 12.
Fuente: https://dialnet.unirioja.es/servlet/articulo?codigo=10947076

Datos publicados: anclas posibles para o en Puig de la Misericòrdia
(41,29 g, signo o), La Covalta IV (42,2 g), y El Cigarralejo VII
(41,46 g); clase a de Tos Pelat (418 g), Puig Castellar (423,78 g)
y L'Alcúdia (424 g); ejemplo de moneda pesada de ars para ki
(3,43 g; NO es media de una muestra auditada).
Referencias: https://repositori.udl.cat/bitstreams/7a59a900-1fbe-4251-bef1-6ad1137d9265/download
y https://dialnet.unirioja.es/descarga/articulo/4561912.pdf

Modelos contrastados: híbrido (10,12), uniforme decimal (10,10),
uniforme duodecimal (12,12), alternativo (12,10).
Se publica sensibilidad a la elección de la ancla o y cada error
por pieza, además de promedio puramente descriptivo de los errores
en las dos escalas. Los mismos ejemplos se utilizaron para formular
la hipótesis en la literatura: **no son validación independiente**.

El peso de 493 g de La Bastida se excluye: Ferrer (2026) informa
de un error bibliográfico en su publicación de 1930.

No se consulta FULL3406, ni se alteran particiones. Ningún resultado
certifica bi=2, abaŕ=10, o=otar ni kitar como gold.
Faltan inventario, fotografías, medición instrumental con tolerancia
y una muestra de ponderales no seleccionada por su ajuste previo.

Ejecución:
```bash
python -m iberos.metrology_hybrid_02 --json /tmp/hybrid-02.json
pytest -q tests/test_metrology_hybrid_02.py
```
