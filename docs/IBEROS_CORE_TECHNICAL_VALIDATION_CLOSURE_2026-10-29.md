# IberOS CORE — Acta de cierre de validación técnica (29-10-2026)

## Evidencia CI verificada
Repositorio `estebanmolinaruiz-art/IberOS`, workflow `tests`, ejecución **40943255292**, SHA `3aca816ae391193b68fea196d7dca05b90474b4c`; estado `completed/success` a 29-10-2026 19:47:37 UTC.

Los trabajos detallados de GitHub certifican:
1. Instalación del paquete y dependencias Pillow/PyMuPDF completada.
2. `pytest -q` completado sin error.
3. Diagnóstico VALIDATION-01 ejecutado como evidencia de guardas, **no aprobación científica**.
4. Rechazo M06 estricto comprobado como salida esperada 2.
5. Pipeline de bibliografía hacia revisión CORE completado.
6. Comparación con informes de fichas curadas completada.
7. `node --test tests/test_write.mjs tests/test_talk.mjs tests/test_mobile_core_sync.mjs` completado.

Véase https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/40943255292

## Auditoría de datos
`data/review/validation01_master_physical_objects_v1.csv`: 22 fichas, fuentes URL vacías 0, truncadas 1 (Pech-Maho V), grupos físicos sin resolver 20, lectura de signos plenamente verificada 0, HOLD admitido 0.
Tivissa: enlace a publicación de Palaeohispanica. Villares V: referencia editorial y objeto de museo 13411 concordantes en fuente institucional. No equiparar fuente bibliográfica a lectura paleográfica verificada.

## Dictamen por alcance
- **APROBADO**: pruebas automatizadas que efectivamente ejecuta el workflow `tests` a SHA citado y controles de rechazo de evidencia insuficiente.
- **APROBADO CON RESERVAS**: corpus documental reparado parcialmente; Pech-Maho V todavía con URL truncada y 20 grupos físicos no resueltos.
- **NO AUDITADO EN ESTA ACTA**: navegación manual de la web pública en iPhone/PC, flujos completos reales del navegador, derechos de las nuevas fotografías MARQ y despliegue de la misma revisión.
- **NO VALIDADO CIENTÍFICAMENTE**: reconocimiento autónomo de 17 signos Orleyl, segunda lectura independiente, interpretaciones/traducciones y test prospectivo HOLD.

Resultado VALIDATION-01: `NOT_EVALUATED` y 30 % de preparación administrativa; M06 y M07 `PENDING`.

## Decisión
**Se cierra la validación técnica automatizada de esta revisión con resultado APROBADO, alcance delimitado.** No se declara validación técnica integral de la web ni validación filológica. Próximos cierres separados: 1) reparar enlace Pech-Maho V y su atribución física; 2) recorrido end-to-end en web pública; 3) recepción de respuestas institucionales e independiente para evaluación científica.
