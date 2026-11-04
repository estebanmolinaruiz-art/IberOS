# FULL3406-BRIDGE-01 · unión controlada entre LEAK-SAFE v3.4.9 y CORE

El respaldo original FULL3406 se recuperó del ZIP de 23-09-2026 el 04-11-2026.
Esta capa **no sustituye** el catálogo público de 38 objetos, no reconstruye
un motor semántico, no cambia métricas y **no publica** las 3.406 entradas.
El archivo congelado permanece fuera del repositorio.

Verifica:
- huella SHA-256 fija `3cf66a5e9abbec2a8a356be3432d507da0d967d3310ffdeb3dc22878055d13a4`;
- 3.406 UID únicos y 1.799 grupos con la clave documental `dependency_key_v3_4_9`;
- `split_v3_4_9`: TRAIN 2378, VAL 346, HOLD 623, EXCLUDED 59;
- ausencia de dependencia activa en los 59 EXCLUDED y ausencia de fuga entre grupos;
- acuerdo entre el recuento efectivo y las estadísticas originales del JSON.

## Ejecución independiente

```bash
python -m iberos.legacy_bridge /ruta/IberOS_LEAK_SAFE_v3_4_9_FULL3406.json --json /tmp/FULL3406_BRIDGE_01.json
pytest -q tests/test_legacy_bridge.py
```

No se certifica identidad entre el agrupamiento histórico y `PHYS_ID`
del catálogo público; 1.799 grupos **no** equivalen a 1.799 piezas físicas.
Xàbia/CIRNE está en TRAIN, pero La Mesa solo tiene ausencia de coincidencia
literal por nombre (`Mesa`/`Alcolea`), sin certificado de independencia.
Sin referencias gramaticales independientes no se mide exactitud semántica.

Las pruebas usan un mini-corpus sintético; el JSON original real no se
incluye en la CI ni se sube al repositorio. El resultado local reproducible
del 04-11-2026 sobre el binario original fue: integridad PASS, 3406 UID,
1799 unidades, cero fugas entre splits, SHA-256 correcto.
