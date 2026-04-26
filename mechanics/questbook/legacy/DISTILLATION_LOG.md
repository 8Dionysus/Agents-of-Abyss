# Questbook Distillation Log

## 2026-04-26 - Parts and Legacy Split

Status: landed

Moved the first-wave source contour into `legacy/raw/` and routed active
Questbook behavior through `parts/`.

Active destinations:

- `parts/model-spine/`
- `parts/public-index/`
- `parts/quest-store/`
- `parts/lifecycle-law/`
- `parts/generated-views/`
- `parts/relation-shape/`
- `parts/execution-passport/`
- `parts/harvest-route/`
- `parts/owner-handoffs/`
- `parts/lane-owner-routes/`

Stop-line: legacy preserves provenance; it is not the normal first route for
current Questbook edits.
