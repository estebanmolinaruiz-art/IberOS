# Independent evidence gate — 2026-10-08

The core engine now counts E1–E5 evidence after PHYS_ID / LEAK_GROUP de-duplication.

Rules:
- one documentary independence unit contributes at most one independent unit;
- if duplicate records have different E-levels, the strongest level describes that unit;
- promotion review can require a minimum number of independent units;
- promotion review can require orthogonal evidence classes (for example METROLOGY + NUMISMATIC);
- passing the structural gate never promotes CORE automatically.

This is a non-regression guard against inflated evidence from multiple faces, editions, readings or duplicate entries.
Scientific authority remains C594 / C474 / C539 / C541.
