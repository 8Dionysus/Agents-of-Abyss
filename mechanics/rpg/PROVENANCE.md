# RPG Provenance Bridge

This is the only active RPG surface that routes back to detailed source-doc accounting. Use it when you are auditing how an RPG source contour feeds an active part, not when you need the current operating contract.

## Current Route First

Start with the active surfaces:

- [README](README.md)
- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [parts/](parts/)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)

If those surfaces answer the task, stop there. Do not pull detailed source-doc history into the active route.

## Source-Doc Map

| Active part | Preserved source families | Landing ledger |
|---|---|---|
| `world-grammar` | direction note plus old layer-model final rule | `LANDING_LOG.md` RPG world-grammar direction |
| `source-boundary` | layer model, boundary map, and architecture RFC source/proof/runtime/presentation split | `LANDING_LOG.md` RPG parts and legacy distillation |
| `vocabulary-overlay` | canonical terminology and dual-vocabulary overlay artifacts | `LANDING_LOG.md` RPG vocabulary overlay and route polish |
| `quest-campaign` | first wave, bridge wave, questline/campaign, party, navigation card, and chronicle contours | `LANDING_LOG.md` RPG parts and legacy distillation |
| `progression-unlocks` | second wave, skills/feats, rank, mastery axes, reputation, proof, and unlock contours | `LANDING_LOG.md` RPG parts and legacy distillation |
| `runtime-projection` | architecture RFC runtime/session plane and runtime projection wave | `LANDING_LOG.md` RPG parts and legacy distillation |
| `owner-handoffs` | owner request packet and stronger-owner stop-lines | `LANDING_LOG.md` RPG parts and legacy distillation |

## Detailed Districts

- `legacy/INDEX.md`: detailed map from preserved raw source files to active part routes.
- `legacy/raw/`: preserved source documents, RFCs, wave notes, bridge contours, and projection notes.
- `legacy/DISTILLATION_LOG.md`: what was distilled, where it landed, and which boundaries survived.
- `legacy/artifacts/README.md`: receipt route for the dual-vocabulary artifact migration.
- `parts/<part>/`: concise active contracts.
- `parts/vocabulary-overlay/{schemas,examples,generated,scripts,tests}/`: active technical artifacts for the checked vocabulary overlay.
- `LANDING_LOG.md`: checked landing ledger.
- `ROADMAP.md`: future contour and unresolved route pressure.

## Distillation Rule

When a detailed source changes current behavior, update the relevant active part first, then update this bridge and the landing ledger if the change is a checked landing. Active part docs must not grow per-source inventories.
