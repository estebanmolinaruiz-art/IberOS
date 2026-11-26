# TOPOLOGY-29 · Resultado negativo de transferencia gráfica

Fecha 2026-11-21. Experimento local sobre las dos láminas editoriales de Orleyl V y VII-B, sin coste adicional.

Comparación entre 69 consultas de regiones recortadas, con la misma binarización, supresión de reglas horizontales y normalización gráfica para los tres algoritmos:

| Método | Coincidencias con etiquetas editoriales | Porcentaje |
|---|---:|---:|
| HOG | 19/69 | 27,54 % |
| Topología (esqueleto, extremos, bifurcaciones, componentes, huecos, distribución 3×3) | 12/69 | 17,39 % |
| Promedio HOG + topología | 19/69 | 27,54 % |

Sin cuatro regiones con alerta de borde, HOG 19/65, topología 12/65, híbrido 19/65. Las etiquetas son de Fletcher; no son verdad paleográfica verificada, y ambos dibujos proceden de la familia Orleyl. La prueba NO supone OCR ciego ni evaluación interyacimientos. El 13/65 de RECOGNIZE-28 corresponde a otro preprocesado y no debe compararse como si la muestra fuera idéntica. **Resultado: la topología aislada no mejora HOG**.

0 signos gráficamente verificados de manera independiente, 0 traducciones nuevas, 69 abstenciones. No se toca el Core ni los congelados C594/C474/C539/C541/FULL3406.

Entregable local reproducible: `IBEROS_TOPOLOGY_29.zip`, incluye `run.py`, SHA-256 de las imágenes en `report.json`, auditoría por región, galería y `INFORME.md`. Siguiente línea diferente: inferir fronteras mediante continuidad gráfica sobre renglones completos, con etiquetas editoriales ocultas al segmentador.
