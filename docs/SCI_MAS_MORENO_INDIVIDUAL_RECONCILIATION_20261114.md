# Mas de Moreno — conciliación individual de improntas, 14/11/2026

Estado: **INVENTARIO DOCUMENTAL PROVISIONAL, NO INVENTARIO FÍSICO CERTIFICADO**. Coste 0 €. Sin cambios en el Core oficial ni en SCI-PRED-02. Contribución a PR #181.

## Resultados verificables

- **Gorgues 2009, pp. 484–487 y fig. 3 (p. 499):** nueve improntas descritas. Tres `balkei` (dos bordes de jarra, una pesa de telar de 1981), dos `[il](tu)ratin` (pesa y cerámica común), una marca `O(?)…` incompleta en borde de jarra, una `[..](u)nin` en pesa, una `kaku` en pesa, una latina `ACINI[..]` en ánfora. Para `balkei` y `ilturatin`, el autor vincula dos hallazgos a contextos distintos **sin asignar cada figura a una UE determinada**. No se inventan esas correspondencias.
- **Sacilotto, tesis 2021, §4.2:** quince estampillas hasta 2015: trece ibéricas (siete bordes de jarra tipo B14, cinco pesas, una cerámica común), dos latinas (una ánfora Leetana 1 y una jarra B14). El excedente sobre 2009 es **seis estampillas**.
- **Conciliación exacta por tipo de soporte:** 2009 (3 jarras, 4 pesas, 1 cerámica común y 1 ánfora) + seis pendientes (4 jarras ibéricas, 1 pesa ibérica, 1 jarra latina) = 2015 (8 jarras, 5 pesas, 1 cerámica común y 1 ánfora). **Las seis entradas MM15-U-… son posiciones contables, no identificadores de objetos localizados.**
- **Cautelas sobre escrituras:** `kaku` figura como ibérico o celtibérico; `O(?)…` no se convierte automáticamente en `oŕtinko`; `[..](u)nin` no es la lectura completa `aiunin` del paralelismo exterior. El grupo `ilturatin` tiene variantes editoriales y lecturas fragmentarias. Las trece categorías «ibéricas» de la tesis son un **agregado**, no certificación propia de cada signo en 2009.
- **No sumar paralelos externos:** la figura 3, paneles 2.2 (Tiro de Cañón) y 4.3 (Azaila), **no** añade dos piezas de Mas de Moreno.
- **Asociación 2021, US 13 358:** `ilturatin` y `ACINI` son improntas distintas, no una misma pieza bilingüe; ni su mención tardía permite identificarlas sin prueba como una de las nueve descritas en 2009.

## Archivos

- `data/review/mas_moreno_impression_inventory_v1.json`: 15 filas y trazabilidad por fuente/figura; 9 descripciones + 6 posiciones anónimas; `official_inventory_id=null`, `stamp_matrix_id=null`, `photo_independently_read=false`.
- `src/iberos/mas_moreno_impression_inventory.py`: auditor de restricciones y conciliación con evidencia histórica.
- `tests/test_mas_moreno_impression_inventory.py`: controles contra IDs de museo inventados, lecturas sin fotografía, identidades de matriz no auditadas, distribución errónea de soportes, inferencia automática de nombres y gold semántico.

## Pendiente de validación D2 por objeto

1. Numeración o signatura arqueológica completa, fecha/campaña, fotografía y correspondencia figura ↔ objeto para nueve impresiones descritas.
2. Publicación de las **seis improntas adicionales** de 2015 con fotografía, clase, UE, signos y matriz; un total contable nunca sustituye un catálogo.
3. Cotejo geométrico de matrices sobre imágenes y dos lecturas independientes cuando existan.
4. Separación de la muestra de desarrollo frente a controles nuevos externos a Mas de Moreno, con regla congelada antes de destapar contexto.

## Fuentes primarias
- Gorgues 2009: https://ifc.dpz.es/recursos/publicaciones/29/54/33gorgues.pdf (pp. 484–487, 499).
- Sacilotto 2021: https://dante.univ-tlse2.fr/access/files/original/13893/Sacilotto_Charlotte.pdf (§4.2).
- Gorgues, Ruiz Darasse y Sacilotto 2021: https://doi.org/10.36707/palaeohispanica.v21i0.426.

**Resultado científico:** distribución de soportes conciliada documentalmente; **0** inventarios físicos autenticados, **0** relecturas dobles y **0** equivalencias semánticas validadas. No se afirma que el sistema haya aprendido una traducción.
