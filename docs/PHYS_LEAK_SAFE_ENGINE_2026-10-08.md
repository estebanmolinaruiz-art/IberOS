# PHYS / LEAK-SAFE engine guard — 2026-10-08

IberOS core now enforces documentary-independence keys.

Priority:
1. PHYS_ID
2. LEAK_GROUP
3. specific Dependency_Group
4. OBJECT_ID fallback

Generic descriptive labels such as INDEPENDENT_OR_UNRESOLVED and DEPENDENT_COPY are not treated as shared object identity.

The engine can:
- collapse records to documentary independence units;
- report how many raw records are not independent;
- detect TRAIN/VAL/HOLD leakage inside one unit;
- resolve mixed split labels with the frozen policy HOLD > VAL > TRAIN.

This guard changes no semantic release and performs no automatic CORE promotion.
Authority remains C594 / C474 / C539 / C541.
