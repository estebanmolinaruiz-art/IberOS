# SEGMENT-37/38: cotejo fotográfico-dibujo y control físico documental

Fecha: 2026-11-22.

## Ensayo ejecutado
Con dos recortes de figura extraídos de la misma edición original de la Moleta del Remei, se intentó un registro global imagen-fotografía frente a dibujo (SIFT, ORB, orientación original y tres inversiones/giros: ocho configuraciones). [GitHub Actions #45072837770](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/45072837770) finalizó correctamente.

Mejor configuración SIFT original o girada 180°: **9 correspondencias candidatas, 4 inliers RANSAC**. Otras configuraciones 2–6 candidatos, sin homografía válida. Ninguna de las ocho transformaciones superó los criterios previamente definidos: mínimo 18 inliers, ratio ≥0.30, cobertura espacial ≥3% en ambas vistas y área de deformación plausible. No se ha confirmado una correspondencia foto→dibujo global ni se han localizado coordenadas de los signos.

## Hallazgo comprobado en el artículo original
Ferrer i Jané, Garcia i Rubert, Moreno Martínez y Velaza Frías (2008), `Una inscripción ibérica sobre plomo procedente del poblado de la Moleta del Remei`, *Palaeohispanica* 8, pp. 203–216, sección **ANÁLISIS DE LA INSCRIPCIÓN**, pp. 207–208 (PDF índice cero páginas 201–202), establece:
- Restos de **21 signos** ibéricos nororientales en **tres líneas**.
- **Zona física 1: dos líneas**; **zona física 2: una línea**.
- Zona 1 línea 1: tres signos conservados a la derecha, con dudas sobre signos y trazos.
- Zona 1 línea 2: nueve restos de signos; tramo `iltun` sugerido por edición.
- Zona 2: al menos nueve signos, muchos incompletos o ilegibles.
- Los autores advierten que el posible significado/finalidad del plomo no se puede establecer con la evidencia actual.

**Implicación operativa:** las **siete bandas de tinta** generadas por SEGMENT-35 NO pueden tratarse como renglones. Esa lectura queda bloqueada ahora por una condición independiente, documentada y verificada. Tampoco pueden asignarse automáticamente los 21 signos a los recortes extraídos: las coordenadas originales signo-a-píxel no están acreditadas. Las dos figuras completas pueden tener disposición y representación diferentes, lo que explica potencialmente el fracaso del registro global sin demostrarlo.

## Resultado de la prueba
El control documental y las condiciones de no sobreinterpretación están guardados en `segment38_moleta_constraints.json`, con prueba reproducible `test_segment38_constraints.py`. Ejecución [GitHub Actions #45072947356](https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/45072947356) **SUCCESS**.

El siguiente experimento no debe repetir SIFT global: localizar las dos zonas físicas y sus tres renglones sobre el dibujo, con revisión visual de la placa y prueba separada contra la fotografía. Solo entonces establecer 21 posiciones gráficas potenciales (incluidas restituciones y abstenciones) con coordenadas independientes.

**Estado:** tres renglones y veintiún restos **confirmados bibliográficamente**, cero correspondencias píxel-signo confirmadas por IberOS, cero traducciones nuevas. Coste 0 €, Core, FULL3406 y C594/C474/C539/C541 protegidos.