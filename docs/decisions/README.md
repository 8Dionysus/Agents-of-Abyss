# Decisions District

This district holds decision records explaining why a center route, owner split,
placement law, or workflow expectation was chosen.

## District law

Decision records explain why; current surfaces define what.

Use canonical `AOA-CENTER-D-####` decision IDs and full canonical-ID filenames:

```text
docs/decisions/AOA-CENTER-D-####-kebab-title.md
```

Previous date-prefixed decision paths are historical git/PR addresses only.
Do not recreate them as compatibility aliases.

## Current surfaces

Generated lookup indexes live under [`indexes/`](indexes/README.md):

| Index | Use |
|---|---|
| [By number](indexes/by-number.md) | canonical sequence and file path |
| [By date](indexes/by-date.md) | original decision date |
| [By surface class](indexes/by-surface.md) | center surface or district type |
| [By center facet](indexes/by-center-facet.md) | federation, route, release, or guidance facet |
| [By mechanic parent](indexes/by-mechanic.md) | center mechanic family affected |
| [By validation or guard family](indexes/by-guard.md) | guard, validator, or workflow family |

The indexes are generated read models from each record's `## Index Metadata`.
They do not author meaning.

## Record shape

Use [TEMPLATE](TEMPLATE.md) for new records. The standard shape is:

- `- Decision ID: AOA-CENTER-D-####`
- `## Status`
- `## Index Metadata`
- `## Context`
- `## Options considered`
- `## Decision`
- `## Rationale`
- `## Consequences`
- `## Source surfaces`
- `## Follow-up route`

## Must not claim

Do not use this district to absorb owner-local truth from sibling repositories.

Do not treat a generated decision index as stronger than its source decision
record, and do not treat a decision record as stronger than the current source
surface it routes to.

## Promotion path

A document in this district may influence current law only when a change names
the surviving canonical surface, updates links, rebuilds generated indexes, and
runs the decision record validators.

## Validation

Use the decision lane in [root validation](../../VALIDATION.md); the local
`AGENTS.md` keeps decision boundaries and the route, not executable commands.
