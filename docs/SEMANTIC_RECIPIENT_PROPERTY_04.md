# SEMANTIC-RECIPIENT-PROPERTY-04 — Predicción contextual y contraejemplo

**14-11-2026.** Dejar de asumir que toda escritura externa de un
plomo plegado identifica al destinatario. Tres objetos publicados:

- **GI.10.11, Empúries**: lámina enrollada, breve secuencia externa;
  el papel de **destinatario** de `katulatien` fue propuesto por la
  bibliografía. Fuente primaria Sanmartí-Grego (1988):
  https://www.persee.fr/doc/ran_0557-7705_1988_num_21_1_1325
- **A.04.01a, La Serreta**: `śakariskerarnai` se discute como
  fórmula externa de destinatario. La propuesta de equivalencia
  entre -ar-nai y expresiones de propiedad NO permite darla por
  demostrada en todos los soportes. Fuente: Veleia 40 (2023):
  https://ojs.ehu.eus/index.php/Veleia/article/download/24248/21921
- **Illeta dels Banyets, pieza de 2018, publicada en 2024**:
  tres textos posiblemente reutilizados; exterior con
  `ka+belauŕ` y `nai`; los editores consideran una
  **etiqueta de propiedad o de producto**, contraejemplo
  a exterior = destinatario sin más contexto.
  https://ifc-ojs.es/index.php/palaeohispanica/es/article/view/629

## Regla congelable antes de una muestra futura

Cuando un plomo **nuevo, no expuesto ni usado como desarrollo**
presente simultáneamente pliegue/cierre epistolar, una inscripción
exterior breve y distinta, y un mensaje interior largo, priorizar
**DESTINATARIO** sobre **FABRICANTE**. Registrar por separado
el rival PROPIETARIO y abstenerse si hay reutilización o no se
demuestra qué cara fue visible al cerrarse.

La evidencia de estos tres casos era **pública** antes de la
predicción; NO cuenta como evaluación ciega. El criterio es
funcional (papel del texto), no traducción de `-en` ni `-nai`.
No hay validación externa que permita distinguir dos roles
nuevos. No abrir HOLD ni modificar FULL3406 ni métricas.

```bash
python -m iberos.semantic_recipient_property_04
pytest -q tests/test_semantic_recipient_property_04.py
```
