# METRO-AOKI-01 — contraste retrospectivo cuantitativo v1
Fecha: 2026-10-19
**Veredicto: IN_SAMPLE_DESCRIPTIVE_ONLY — no validación científica independiente.**

## Fuente y datos
- Joan Ferrer i Jané, *Una nova proposta híbrida, decimal-duodecimal, pel sistema metrològic de pes ibèric a-o-ki*, Quaderns de Prehistòria i Arqueologia de Castelló, 42 (2026).
- Resumen: https://ub.academia.edu/JoanFerreriJan%C3%A9/Papers
- Descripción pública: https://es.linkedin.com/posts/joanferrer_una-nova-proposta-h%C3%ADbrida-decimal-duodecimal-activity-7514618759228182528-Ryyc
- Complemento primario: https://mupreva.org/web_mupreva_dedalo/publicaciones/1642/va
- Texto completo, inventarios, incertidumbres: **no obtenidos / no auditados**.
- Siete valores citados en publicaciones del autor; se emplearon para desarrollar y explicar la hipótesis y **no** constituyen HOLD.

## Parámetros congelados solo para el ejercicio descriptivo
Se fija `o=42g`, y se comparan modelos: `H:(a/o=10,o/ki=12)`, `D:(10,10)`, `U:(12,12)`.
Para cada masa individual: `error_i=100*(observado/predicho-1)`.
Métrica: `RMSE_pct=sqrt(mean(error_i^2))`; igual peso por observación y sin errores instrumentales.

## Resultado
- Híbrido: **1.781%** RMSE relativo.
- Decimal: **10.168%**.
- Duodecimal: **10.802%**.
Este ranking depende de la selección publicada, del valor de 42g fijo, de asignar cada objeto a a/o/ki y del supuesto de igual importancia de cada masa. Ni el error ni las cifras implican superioridad estadística independiente.

## Restricciones
1. No inferir aquí traducciones verificadas de abaŕ/otar/kitar.
2. No considerar la masa de 493g Bastida como pieza conservada y verificada.
3. Las dos masas de El Cigarralejo y las monedas no son necesariamente observaciones independientes de calibración.
4. Puede existir heterogeneidad cronológica, de series monetarias y desgaste, pendiente de modelar.
5. Cuenco de la Granjuela no incorporado por falta de ecuación y ficha fuente auditadas.
6. Independencia de VALIDATION-01 TE: este análisis **no** lo cierra.

## Próximos requisitos
- Extraer tabla del artículo primario con identificadores, datación, inventario, masa original e incertidumbre.
- Preinscribir criterios de inclusión y tolerancias; probar sensibilidad a `o=41-43g`, outliers y grupos.
- Conseguir mediciones nuevas e independientes, asignar unidad sin conocer el resultado de la evaluación y congelar sus predicciones.
- Comparar también un modelo libre de escalas para evitar ventaja artificial al calibrar a 42g.
