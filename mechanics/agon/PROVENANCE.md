# Agon Provenance Bridge

This is the only active Agon surface that routes back to detailed source-doc
and wave accounting. Use it when you are auditing how an Agon source surface
feeds an active part, not when you need the current operating contract.

## Current route first

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts/](parts/)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)

If those surfaces answer the task, stop there. Do not pull detailed source-doc
history into the active route.

## Source-doc map

| Active part | Detailed source families | Landing ledger |
|---|---|---|
| `imposition-readiness` | pre-Agon baseline, imposition posture, survival criteria, doubt audit, Wave 0 | `LANDING_LOG.md` entries through Agon imposition gate |
| `lawful-move-grammar` | lawful move language, move registry model, move owner handoffs, Wave III | `LANDING_LOG.md` Agon lawful move language |
| `owner-binding` | move owner binding, binding matrix, owner request packet, pre-protocol stop-lines, Wave IV | `LANDING_LOG.md` Agon move owner binding |
| `gate-routing` | gate routing handoff, owner request, stop-lines, Wave V | `LANDING_LOG.md` Agon gate routing handoff |
| `trial-handoff` | trial playbook handoff, owner request, stop-lines, Wave VI | `LANDING_LOG.md` Agon trial playbook handoff |
| `recurrence-adapter` | recurrence adapter, recurrence owner request, recurrence stop-lines | `LANDING_LOG.md` Later Agon center waves |
| `packet-arena` | state packets, arena session, session lifecycle, charter/seat, pressure profile | `LANDING_LOG.md` Later Agon center waves |
| `duel-kernel` | duel kernel, mechanical trial, sealed commit, model-of-other, terminal outcome | `LANDING_LOG.md` Later Agon center waves |
| `verdict-retention-rank` | verdict draft, delta/scar bridge, retention, rank, court/memo/stats prebinding | `LANDING_LOG.md` Later Agon center waves |
| `epistemic-kag` | epistemic agon, epistemic move extension, KAG promotion, evidence bundle boundary | `LANDING_LOG.md` Later Agon center waves |
| `sophian-threshold` | Sophian threshold, ToS threshold packet, canon restraint, Sophian owner handoffs | `LANDING_LOG.md` Later Agon center waves |
| `compatibility-bridges` | law interlocks, schools, lineages, campaigns, bifurcation, closure, contradiction, summon | `LANDING_LOG.md` Later Agon center waves |

## Detailed districts

- `legacy/INDEX.md`: detailed map from every preserved raw source to its active
  part route.
- `legacy/raw/`: preserved source documents, models, wave notes, handoffs, and
  stop-lines.
- `docs/`: compatibility route only.
- `config/`, `generated/`, `schemas/`, `examples/`, `scripts/`, `tests/`:
  package-local technical artifacts for Agon model families.
- `LANDING_LOG.md`: checked landing ledger.
- `ROADMAP.md`: future contour and unresolved route pressure.

## Distillation rule

When a detailed source changes current behavior, update the relevant active part
first, then update this bridge and the landing ledger if the change is a
checked landing. Active part docs must not grow per-source inventories.
