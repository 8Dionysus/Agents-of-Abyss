# Questbook Provenance Bridge

This is the only active Questbook surface that routes back to legacy source
contours. Use it when you are auditing how older Questbook source material was
distilled, not when you need the current operating contract.

## Current route first

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts](parts/)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)

If those surfaces answer the task, stop there. Do not pull legacy detail into
the active route.

## Legacy map

- [legacy index](https://github.com/8Dionysus/Agents-of-Abyss/blob/d31882083296ef457a980d071f55d609e95cce67/mechanics/questbook/legacy/INDEX.md): preserved source contours mapped to active
  Questbook parts.
- [distillation log](https://github.com/8Dionysus/Agents-of-Abyss/blob/d31882083296ef457a980d071f55d609e95cce67/mechanics/questbook/legacy/DISTILLATION_LOG.md): dated accounting for
  raw-to-active distillation decisions.
- [raw source district](https://github.com/8Dionysus/Agents-of-Abyss/blob/d31882083296ef457a980d071f55d609e95cce67/mechanics/questbook/legacy/raw/README.md): preserved historical source
  documents.
- [first wave contour](https://github.com/8Dionysus/Agents-of-Abyss/blob/d31882083296ef457a980d071f55d609e95cce67/mechanics/questbook/legacy/raw/QUESTBOOK_FIRST_WAVE.md): original first
  contour source now routed through active parts.

## Distillation rule

When a legacy source changes current behavior, update the relevant active part
first, then update this bridge, the legacy index, and the landing log if the
change is a checked landing. Active part docs must not grow per-source
inventories.
