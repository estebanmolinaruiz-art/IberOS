# Mas de Moreno — banco de evidencia contextual (L48)

**Fecha:** 13-11-2026. **Coste:** 0 €. **Estado:** desarrollo retrospectivo. No modifica CORE, FULL3406, predicción congelada SCI-PRED-02 ni HOLD.

## Alcance y datos reales

- Gorgues (2009, *Palaeohispanica* 9:481–500, figura 3) publica estampillas precocción: `kaku`, `aiunin`, grafía parcialmente conservada `o[...]`, `ilturatin`, `balkei`, `ACINI[...]`. La figura incluye **paralelos externos** (Tiro de Cañón y Azaila): **no** deben contarse como piezas extra del horno de Mas de Moreno.
- Gorgues, Ruiz Darasse y Sacilotto (2021, *Palaeohispanica* 21:495–511, p. 496) sitúan `iluratin` / `ilturatin`, `balkei` y `ACINI` en el entorno de un horno tardío y documentan estampillas `iluratin` y `ACINI` en la **misma US 13 358**. Son **improntas distintas**, no un texto bilingüe ni una equivalencia léxica.
- Sacilotto (tesis 2021, apartado 4.2) cita **15 estampillas hasta 2015: 13 ibéricas y 2 latinas**. Es un conteo histórico, no inventario individual, ni un censo actualizado de todas las campañas.
- `oŕtinko` procede de la información de 2021. En la fuente de 2009 el ejemplo figura como `O[...] `. La grafía `ilturatin / iluratin` se mantiene como variante editorial **sin resolución propia de signos**.

## Qué prueba la IA y qué no

El fichero `data/review/mas_moreno_context_evidence_v1.json` almacena **familias editoriales**, referencias publicadas y asociaciones. No asigna inventarios físicos no verificados ni considera personas únicas las improntas repetidas.

El módulo `src/iberos/mas_moreno_context_evidence.py` verifica:
1. Referencias bibliográficas HTTPS y pertenencia de cada dato a una fuente.
2. Integridad del par de estampillas de US 13 358, expresamente **no la misma vasija**.
3. Conteo histórico 13+2=15.
4. Ninguna lectura D2/D3 ni papel semántico se puede declarar automáticamente.
5. Prohibición de promoción del gold de identidad individual por mero contexto.

**Hallazgo sostenible:** determinadas familias de sellos están asociadas físicamente a producción cerámica y coexistieron estratigráficamente en un horno. **Hipótesis pendientes:** artesano, propietario, comitente, equivalencia entre antropónimos latinos e ibéricos.

## Ejecutar

```bash
python -m iberos.mas_moreno_context_evidence
python -m pytest -q tests/test_mas_moreno_context_evidence.py
```

## Futura evaluación contextual (independiente de SCI-PRED-02)

Antes de intentar una prueba predictiva:
1. Crear `physical_id`, `stamp_matrix_id`, `US`, tipo de recipiente, precocción/postcocción, fuente y fotografía **por cada impronta verificada**, no por mera familia editorial.
2. Separar matrices de un mismo sello y nuevas piezas; identificar el mismo punzón mediante fotografías.
3. Construir controles negativos por tipo de soporte y cronología (talleres sin marcas, grafitos poscocción de contextos residenciales, piezas importadas); registrar tanto positivos como negativos.
4. Congelar con antelación las variables, la regla, grupos de independencia, baseline y métricas; ocultar contextos del conjunto reservado hasta predecir.
5. Evaluar sensibilidad, cobertura y falsos positivos por matriz y contexto, **sin usar el mismo artículo para entrenar y evaluar**.

**Vinculado a:** [expediente #180](https://github.com/estebanmolinaruiz-art/IberOS/issues/180). No hay predicción ciega nueva ni traducción demostrada; este experimento suministra un dato contextual material valioso para entrenar controles del motor de IA.

**Restricción de imágenes:** se han contrastado textos y pies de figura originales; el visor PDF no permitió recuperar la captura de la figura 3 en esta ejecución. No se declara autopsia ni se redistribuyen fotografías.
