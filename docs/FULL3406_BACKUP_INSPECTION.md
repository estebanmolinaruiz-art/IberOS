# FULL3406 — inspección reproducible de respaldos históricos

Un respaldo ZIP antiguo **no es** automáticamente el corpus LEGACY congelado.
Este script examina tablas CSV/TSV/JSON/JSONL sin extraerlas del archivo
y muestra recuentos e indicadores; nunca los importa al CORE.

## Uso en el PC o Codespace

```bash
python scripts/inspect_full3406_backup.py IberOS_Beta_Final_V2_BACKUP_2026-09-23.zip --json /tmp/backup-v2-audit.json
python scripts/inspect_full3406_backup.py IberOS_Catalogo_Objetos_v0.1.zip --json /tmp/catalog-audit.json
pytest -q tests/test_full3406_backup_inspection.py
```

Archivos localizados el 2026-11-03 en el Gmail personal del proyecto:

- Mensaje **IberOS** 24-09-2026: `IberOS_Beta_Final_V2_BACKUP_2026-09-23.zip`
  (300406 bytes), `IberOS_BETA_FINAL_0_1.zip` (6894 bytes), y
  `IberOS_Base_de_Datos_v1_0.pdf` (37331 bytes).
- Mensaje **Iberos tesis** 27-09-2026:
  `IberOS_Catalogo_Objetos_v0.1.zip` (431280 bytes).

La integración Gmail disponible no admite leer adjuntos ZIP, por lo que
**sus contenidos todavía no se han inspeccionado**. No hay evidencia de
que alguno incluya FULL3406. El PDF sí fue revisado y no proporciona las
3406 entradas tabulares.

El inspector tiene límite de 30 MB por fichero interno y no extrae rutas.
Un recuento igual a 3406 solo genera una **candidatura**. Antes de certificar
recuperación deben auditarse origen, hash, esquema original, ENTRY_ID,
PHYS_ID, LEAK_GROUP, splits y edición previa.

Véase `docs/LEGACY_FULL3406_RECOVERY_2026-11-03.md`.
