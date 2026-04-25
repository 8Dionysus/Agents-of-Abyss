# Quest District

This directory holds tracked AoA obligations that should survive the current diff.

It is not a private scratchpad and not a second roadmap. Program direction belongs in [`ROADMAP.md`](../ROADMAP.md). The root quest index is [`QUESTBOOK.md`](../QUESTBOOK.md). Quest lifecycle law lives in [`mechanics/questbook/docs/QUESTBOOK_MODEL.md`](../mechanics/questbook/docs/QUESTBOOK_MODEL.md).

## File families

| Family | Meaning | Guardrail |
|---|---|---|
| `AOA-Q-*.yaml` | foundation or federation-level quest records | keep them compact and route-bearing |
| `AOA-Q-AGON-*.md` | Agon-related obligations and owner follow-through | do not grant live arena authority |
| `AOA-Q-EXP-*.md` | Experience-related obligations and staged contract follow-through | do not grant live workspace runtime or hidden memory sovereignty |
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
