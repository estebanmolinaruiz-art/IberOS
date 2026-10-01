# IberOS Interoperability

## Stable identifiers

- `UPSTREAM_ID`: identifier from a source corpus, e.g. `I02572`
- `ENTRY_ID`: internal textual/analytical unit
- `OBJECT_ID`: physical-object unit used for independence
- `LEAK_GROUP`: dependency group preventing duplicated evidence

## Evidence levels

- E1 — primary/material fact
- E2 — recurrence
- E3 — supported structural relation
- E4 — functional interpretation
- E5 — specific semantic hypothesis

## Rule

A downstream program should never collapse E1–E5 into a single unqualified “translation” field.

## Exchange

Programs may consume an IberOS result without using the IberOS engine itself. This is intentional.

Validate a result against `iberos-result-v1.schema.json`.
