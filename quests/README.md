# Quest District

This directory holds tracked AoA obligations that should survive the current diff.

It is not a private scratchpad and not a second roadmap. Program direction belongs in [`ROADMAP.md`](../ROADMAP.md). The root quest index is [`QUESTBOOK.md`](../QUESTBOOK.md). Quest lifecycle law lives in [`mechanics/questbook/docs/QUESTBOOK_MODEL.md`](../mechanics/questbook/docs/QUESTBOOK_MODEL.md).

Quest sources live in lifecycle directories. Top-level `AOA-Q-*` paths are compatibility aliases for established links and commands.

## Lifecycle board

| Lane | Use |
|---|---|
| [`captured/`](captured/) | public-safe obligation exists, but route shaping is not complete |
| [`triaged/`](triaged/) | route-bearing obligation with enough shape to split, promote, or close |
| [`ready/`](ready/) | next owner action is clear and bounded |
| [`active/`](active/) | currently being advanced by an owner lane |
| [`blocked/`](blocked/) | waiting on a named dependency or owner decision |
| [`reanchor/`](reanchor/) | old route no longer matches; choose a new owner, band, or evidence path |
| [`done/`](done/) | landed with enough public evidence to leave the active index |
| [`dropped/`](dropped/) | intentionally closed without landing, with a visible reason |

## File families

| Family | Meaning | Guardrail |
|---|---|---|
| `<state>/AOA-Q-*.yaml` | foundation or federation-level quest records | directory must match YAML `state` |
| `<state>/AOA-Q-AGON-*.md` | Agon-related obligations and owner follow-through | do not grant live arena authority |
| `<state>/AOA-Q-EXP-*.md` | Experience-related obligations and staged contract follow-through | do not grant live workspace runtime or hidden memory sovereignty |
| `AOA-Q-*` aliases | compatibility routes to lifecycle sources | do not edit aliases as source files |
| future generated summaries | allowed only after a real builder and validator exist | do not create manual pseudo-generated indexes |

## Use this directory when

- an obligation crosses repository boundaries
- a center contract needs public follow-through
- a route must survive beyond the current PR
- a future owner-local landing needs a durable reminder
- a blocker or harvest candidate should remain visible

## Do not use it for

- repo-local tasks that belong in a sibling repository
- private todo lists
- roadmap duplication
- proof verdicts
- runtime state
- score or rank ledgers
- ToS-authored canon

## Before editing

1. Check [`QUESTBOOK.md`](../QUESTBOOK.md).
2. Check [`mechanics/questbook/docs/QUESTBOOK_MODEL.md`](../mechanics/questbook/docs/QUESTBOOK_MODEL.md).
3. If the quest touches a mechanic, check [`mechanics/README.md`](../mechanics/README.md).
4. Keep the owner split explicit.
5. Leave a clear follow-up path rather than a placeholder.

## Validation

```bash
python scripts/validate_questbook_lifecycle.py
```
