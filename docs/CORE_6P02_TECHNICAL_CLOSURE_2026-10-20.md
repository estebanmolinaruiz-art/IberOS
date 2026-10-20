# Cierre técnico 6P-02 — Registro compartido de evidencia

**Fecha:** 2026-10-20
**Estado:** CERRADO (contrato e integración de expediente piloto)
**GitHub Actions verificado:** https://github.com/estebanmolinaruiz-art/IberOS/actions/runs/39419310640
**Commit sometido a pruebas:** `7fd3e33c4ad42593b0e5a2b500fceab5b21fd76b`
**Resultado:** `completed / success`, incluido `pytest -q`.

## Criterios cumplidos
- `src/iberos/shared_evidence.py` gestiona identificadores únicos, fuentes, capas, estados y pilares.
- Conserva coordenadas, hash de imagen si existe, página y metadatos de revisión.
- Bloquea dependencias huérfanas, autorreferencias y ciclos.
- Bloquea la promoción automática a conocimiento o interpretación científica validada.
- `tests/test_shared_evidence.py` comprueba controles del contrato.
- `tests/test_shared_evidence_orleyl.py` procesa tres evidencias del expediente real de Orleyl (lectura editorial, caja de dibujo candidata, hipótesis TE), mantiene cadena documental e incertidumbre y comprueba que la promoción está bloqueada.

## Límites
- La verificación es **técnica**, no paleográfica ni lingüística.
- La caja y las atribuciones individuales de signos de Orleyl continúan como candidatos de revisión; `ROK-RECIPIENT-02` queda OPEN.
- El registro compartido está preparado para integraciones posteriores: **no** significa que todos los motores científicos consuman ya el mismo contrato.
- El hito de integración multimódulo completa corresponde a 6P-04; normalización del corpus a 6P-03.

**Siguiente hito:** 6P-03 — resolver IDs, relaciones entre objetos y fuentes y los vínculos del corpus con este contrato.
