# Quest District

This directory holds tracked AoA obligations that should survive the current diff.

It is not a private scratchpad and not a second roadmap. Program direction belongs in [`ROADMAP.md`](../ROADMAP.md). The root quest index is [`QUESTBOOK.md`](../QUESTBOOK.md). Quest lifecycle law lives in [`mechanics/questbook/docs/QUESTBOOK_MODEL.md`](../mechanics/questbook/docs/QUESTBOOK_MODEL.md).

Quest sources live in lane-first lifecycle directories. Top-level `AOA-Q-*` aliases are intentionally absent; route directly to `quests/<lane>/<state>/AOA-Q-*`.

## Lanes

| Lane | Use |
|---|---|
| [`center/`](center/) | federation-level center obligations and cross-mechanic routing |
| [`agon/`](agon/) | Agon obligations and owner follow-through |
| [`experience/`](experience/) | Experience obligations and staged contract follow-through |
| [`rpg/`](rpg/) | RPG reflection, bridge, and runtime-projection obligations |
| [`recurrence/`](recurrence/) | return, continuity, and re-entry obligations |
| [`questbook/`](questbook/) | Questbook mechanic obligations about quest shape and lifecycle law |
| [`antifragility/`](antifragility/) | antifragility, via negativa, and deletion-pressure obligations |
| [`method-growth/`](method-growth/) | method-growth, candidate lineage, and owner landing obligations |
| [`release-support/`](release-support/) | release posture, direction surface, and support protocol obligations |
| [`tos-bridge/`](tos-bridge/) | Tree-of-Sophia bridge and counterpart obligations |

## Lifecycle States

Each lane may contain:

| State | Use |
|---|---|
| `captured/` | public-safe obligation exists, but route shaping is not complete |
| `triaged/` | route-bearing obligation with enough shape to split, promote, or close |
| `ready/` | next owner action is clear and bounded |
| `active/` | currently being advanced by an owner lane |
| `blocked/` | waiting on a named dependency or owner decision |
| `reanchor/` | old route no longer matches; choose a new owner, band, or evidence path |
| `done/` | landed with enough public evidence to leave the active index |
| `dropped/` | intentionally closed without landing, with a visible reason |

## File Families

| Family | Meaning | Guardrail |
|---|---|---|
| `center/<state>/AOA-Q-*.yaml` | foundation or federation-level quest records | YAML `lane` and `state` must match the path |
| `agon/<state>/AOA-Q-AGON-*.md` | Agon-related obligations and owner follow-through | do not grant live arena authority |
| `experience/<state>/AOA-Q-EXP-*.md` | Experience-related obligations and staged contract follow-through | do not grant live workspace runtime or hidden memory sovereignty |
| `generated/questbook_*.min.json` | global read models built from source quest files | rebuild with the Questbook builder, do not edit by hand |

## Use This Directory When

- an obligation crosses repository boundaries
- a center contract needs public follow-through
- a route must survive beyond the current PR
- a future owner-local landing needs a durable reminder
- a blocker or harvest candidate should remain visible

## Do Not Use It For

- repo-local tasks that belong in a sibling repository
- private todo lists
- roadmap duplication
- proof verdicts
- runtime state
- score or rank ledgers
- ToS-authored canon

## Before Editing

1. Check [`QUESTBOOK.md`](../QUESTBOOK.md).
2. Check [`mechanics/questbook/docs/QUESTBOOK_MODEL.md`](../mechanics/questbook/docs/QUESTBOOK_MODEL.md).
3. If the quest touches a mechanic, check [`mechanics/README.md`](../mechanics/README.md).
4. Choose the lane first, then the lifecycle state.
5. Keep the owner split explicit.
6. Leave a clear follow-up path rather than a placeholder.

## Validation

```bash
python mechanics/questbook/scripts/validate_questbook_lifecycle.py
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
```
