# IberOS actualización metodológica para la tesis

11 de octubre de 2026. Autor del proyecto: Esteban Molina Ruiz.

Este complemento documenta controles de reproducibilidad y de generación
sin introducir nuevas interpretaciones lingüísticas confirmadas. La autoridad
se conserva en C594, C474, C539 y C541. D(E/I) permanece en 50; no se incrementan
las métricas oficiales. El progreso del software no mide desciframiento.

## Separación de estructura y significado

El control D(E/I) distingue la arquitectura formal del complejo verbal del
valor gramatical exacto de E frente a I. La documentación vigente corrige
supuestos de las comparaciones históricas: NP-DI-EGIAR sigue NOT_OBSERVED;
Pech-Maho aporta la misma familia sin garantizar raíz idéntica; Castellet
se conserva como paralelo estructural. No se convierten estos antecedentes
en pares mínimos ni en predicciones prospectivas independientes.

## Conexión con el benchmark

El comando `iberos dedi-benchmark evidencia.json` produce dos bloques:
`formal_matrix` y `semantic_gate`. El segundo aplica sobre los mismos registros
la predicción preregistrada y la auditoría de procedencia. Requiere ambas ramas,
identidad física y LEAK_GROUP independientes, raíz y segmentación verificadas,
variable contextual fijada antes de la lectura, fuente fechada con hash,
preregistro y registro de predicción congelados, y revisor independiente.

El control automático comprueba requisitos declarados. La autenticidad de las
fuentes, su independencia, la cronología del preregistro y el valor gramatical
requieren revisión científica externa. Una entrada completa llega como máximo
a AWAITING_INDEPENDENT_REVIEW y mantiene scientific_state UNVERIFIED.
No existe promoción automática al núcleo.

La capa curada de 38 objetos es un benchmark de interoperabilidad y control de
fuga. No acredita por sí misma una prueba ciega ni sustituye el conjunto
histórico congelado de 3406 entradas. Los objetos conocidos siguen siendo
retrospectivos; las pruebas sintéticas no son evidencia epigráfica.

## Controles de Write

El adaptador web mantiene D(E/I) sin resolver y la dirección literal de ŔOK
abierta. Su salida BI-D(E/I)-ŔOK-(AN) se etiqueta como estructura, no como una
traducción semántica confirmada. No asigna EKIAR o EGIAR automáticamente a
«hacer» o «dedicar». Los marcos no cubiertos devuelven abstención.

Se corrige la cobertura del adaptador: anteriormente un ejemplo de transferencia
podía devolver 100 por ciento al contar un segmento experimental opcional y
segmentos probables. Desde WRITE-GRAMMAR v0.3-web.3, semantic_coverage cuenta
solo segmentos etiquetados como semánticamente validados; probable_rate,
structural_rate, infer_rate, fallback_rate y gap_rate se registran por separado.
El denominador es el número de segmentos de salida, no el número de palabras
ni el conjunto de significados de la entrada. Por tanto esta medida no acredita
cobertura de todos los matices españoles ni debe extrapolarse al núcleo.
El ejemplo actual no contiene segmentos semánticos plenamente validados y
su semantic_coverage es cero. Esto corrige la medición; no implica pérdida de
resultados científicos.

La revisión adversarial de WRITE-GRAMMAR v0.3-web.4 corrige además la
detección de roles y del alcance de la frase española. La versión anterior
podía reconstruir «No se entrega un documento a Bastubar» como afirmación
y tratar Bastubar como destinatario en «Bastubar entrega un documento a
Esteban». La generación se restringe ahora a marcos afirmativos pasivos
completos con participante explícito en posición de destinatario; negaciones,
preguntas, pronombres no resueltos y marcos con agente explícito producen
abstención. La falta de destinatario conserva un hueco. Estas restricciones
controlan la entrada castellana y no fijan la dirección semántica de ŔOK.

## Incorporación y límites

Este texto es un complemento metodológico separado del anexo de registros de
8 de octubre. No sustituye la tesis ni reescribe sus resultados congelados.
La incorporación a una tesis definitiva requiere identificar el archivo
autoritativo y comparar versiones. La auditoría posterior de Talk verifica
SQLite, hashes de las 12 demos y el control de producción con cero palabras
aprobadas. Se conserva la distinción entre demostración del navegador y
assets de producción. Mobile permanece pendiente de comprobación material.
El alcance completo figura en TALK_MOBILE_MATERIAL_AUDIT_2026-10-11.md.

## Fuentes materiales

- Repositorio auditado: estebanmolinaruiz-art/IberOS, commit
  0b779d84b22f5ea447f18e346d823b8fdd859c87.
- docs/DEDI_ORTHOGONAL_MATRIX_2026-10-08.md.
- src/iberos/core.py, controles predictivo, documental y conjunto.
- site/write/iberos-write.mjs y site/write/data/write-rules.json.
- IberOS_Tesis_Anexo_Registros_2026-10-08.docx, tres páginas, leído completo.

Las pruebas automatizadas asociadas verifican comportamiento del software.
No prueban hipótesis sobre el significado del ibérico.
