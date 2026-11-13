# SCI-PRED-08 · Anclajes externos de Cástulo, 12-XI-2026

**Objetivo principal IberOS:** predicción lingüística contrastable con evidencia independiente. **Gasto 0 €**. Ninguna nueva traducción validada.

## Conclusión documental

Se han identificado dos familias de evidencia complementarias del mismo centro histórico **Cástulo**:

1. **Lápida opistógrafa H.6.1 / BDHesp J.03.01 / ELRH U53**, una sola piedra reutilizada para dos textos de momentos distintos. La cara B contiene `P(ublius) Cornelius P(ublii) l(ibertus) Diphilus / CASTLOSAIC`. Las posiciones de **patrono (P. Cornelius)** y **liberto (Diphilus)** son expresadas mediante **latín y la abreviatura `l.`**, no inferidas del ibérico. `castlosaic` ha sido relacionado con Cástulo y se ha propuesto valor gentilicio, pero el segmento sigue **sin traducción validada**. Cara A anterior y de interpretación difícil; no existe equivalencia bilingüe comprobada de ambas caras.
2. **Cuatro fichas de inventario oficiales sobre moneda de Cástulo**:
   - [MAN 1993/67/5852](https://ceres.mcu.es/pages/Main?inventary=1993%2F67%2F5852&museum=51): mitad, 90–70 a. C., reverso `kastilo` en escritura ibérica y leyendas latinas de anverso/reverso. Denominación, datación y metal según CERES. Las abreviaturas latinas deben cotejarse por separado.
   - [MAN 1993/67/5407](https://ceres.mcu.es/pages/Main?inventary=1993%2F67%2F5407&museum=51): duplo, 225–206 a. C., reverso con `kastilo` retrógrado, serie cronológicamente anterior.
   - [MAN 1993/67/5552](https://ceres.mcu.es/pages/Main?inventary=1993%2F67%2F5552&museum=51): unidad, 150–80 a. C., reverso con `kastilo`, cuño y grupo de emisión por cotejar.
   - [Museo de Cádiz CE00893](https://ceres.mcu.es/pages/Main?idt=122408&inventary=CE00893&museum=MCA&table=FMUS): mitad, reverso `kastilo` y `L` latina considerada posible marca de valor, **no interpretar como valor confirmado**.

**Fuentes bibliográficas secundarias:**
- Pieter van Houten 2024, *Palaeohispanica* 24, pp. 132–133, DOI https://doi.org/10.36707/palaeohispanica.v24i1.641: tabla con ambas caras de H.6.1 y discusión de `castlosaic`.
- Simón Cornago, *Lenguas vernáculas de Hispania escritas en alfabeto latino*, https://digibug.ugr.es/bitstream/handle/10481/99649/Athenaeum%20SimonCornago.pdf?isAllowed=y&sequence=1, relaciona Cástulo con el término indígena.
- Estarán Tolosa 2019, https://doi.org/10.3989/aespa.092.019.009, contexto de numismática y transición lingüística.
- Repertorio BDHesp de numismática https://addi.ehu.es/handle/10810/15618 para clasificación por ceca; no suponer que cada moneda es una lectura humana ciega.

## Qué sí sabemos y qué no

| Afirmación | Grado |
| --- | --- |
| La lápida cara B contiene una fórmula latina de liberto/patrono | Documentado externamente como texto latino |
| La palabra `castlosaic` está documentada en la misma cara | Edición publicada; cotejo gráfico autónomo pendiente |
| `kastilo` aparece como rótulo monetal de Cástulo, en múltiples series | Cuatro fichas museísticas con inventario; fotografías originales aún sin cotejo signo a signo |
| `castlosaic` significa sin duda «natural de Cástulo» | **NO**, hipótesis gentilicia, sufijo y lengua no probados |
| Dos nombres ibéricos con roles diferenciados en H.6.1 | **NO**, los dos papeles están en latín |
| Una predicción de IberOS acertó un significado nuevo y previamente desconocido | **NO**, interpretaciones publicadas hace décadas |
| Los ejemplares monetales son cuatro observaciones semánticas independientes | **NO**, controlar familias de emisión/cuño |

## Corrección filológica por bibliografía independiente

La atribución de `CASTLOSAIC` a la **lengua ibérica** es **discutida**, aunque su relación con Cástulo resulte plausible: Simón Cornago, *Palaeohispanica* 17 (2017), p. 119, menciona posible sufijo ibérico `-sa-i-c` frente a una lectura **turdetana** propuesta por Correa por la estructura consonántica de la base. Moncunill y Velaza, «Iberian», *Palaeohispanica* 20 (2020), p. 1087, clasifican el epígrafe de Cástulo J.03.01 entre los testimonios de adscripción indígena/ibérica **incierta**. Fuentes:

- https://ifc.dpz.es/recursos/publicaciones/36/49/_ebook.pdf
- https://ifc.dpz.es/recursos/publicaciones/38/77/17moncunillvelaza.pdf

**Decisión:** `LANGUAGE_UNCERTAIN: IBERIAN_OR_OTHER_INDIGENOUS`; `CASTULO_TOPONYM_RELATION=PLAUSIBLE_RESEARCH_HYPOTHESIS`; `ETYMOLOGY_AND_SUFFIX=NOT_VALIDATED`. No se utilizará como un positivo seguro de lengua ibérica ni en entrenamiento supervisado semántico. Solo **control de ambigüedad lingüística**, y el nombre latino de patrono/liberto como hecho documental distinto.

## Hipótesis que se puede testar en el futuro (sin alterar SCI-PRED-02)

**SCI-TOP-01 — función documental del rótulo**, no equivalencia léxica ya demostrada: en un conjunto de emisiones **nuevas para el entrenamiento**, IberOS deberá clasificar cada leyenda gráfica o transliterada como `CECA_TOPONIMO`, `PERSONA_MAGISTRADO`, `MARCA_VALOR` o `ABSTENCION`, con criterios de elegibilidad y baseline acordados **antes de que un tercero entregue las fichas de contraste**. Prohibido usar la edición/catalogación de ese lote como features.

**Limitación esencial:** el corpus aquí documentado está **expuesto a los investigadores** en esta iteración: debe etiquetarse `RETROSPECTIVE_TRAIN`. No puede designarse a posteriori como HOLD prospectivo.

## Work de evidencia siguiente

1. Confirmar inventario/localización y fotografía de ambas caras de H.6.1 con el museo o en repositorio autorizado, sin pagar ni publicar imágenes ajenas sin derechos.
2. Cotejar leyendas de las cuatro monedas en fotografías exactas y documentar sus emisiones/cuños. No confundir variaciones de edición con signos nuevos.
3. Consolidar las referencias en una matriz de **objeto físico → lado → rótulo → escritura → función inferida por evidencia externa → dependencia**.
4. Utilizar solo futuras monedas no examinadas para predicción de clase funcional cuando el protocolo esté fijado, y conservar TODOS los falsos positivos y las abstenciones.

**Veredicto SCI-PRED-08:** nueva agrupación de fuentes **materiales y funcionales con inventarios específicos**, sin prueba prospectiva aún. Se conserva línea prioritaria de dos roles de SCI-PRED-02 con 0 casos admisibles y 0 traducciones confirmadas. No modificar CORE, FULL3406, los umbrales científicos ni el sitio.
