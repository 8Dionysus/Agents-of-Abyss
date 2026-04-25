# Agent Lane District

This district holds Agent-lane references that support AGENTS.md without becoming root doctrine.

## District law

Keep this district reviewable and labeled. A reader or agent should know whether a surface is current law, evidence, historical receipt, transition note, or compatibility reference before citing it.

## Current surfaces

| Surface | Role |
|---|---|
| [`AGENTS_ROOT_REFERENCE`](AGENTS_ROOT_REFERENCE.md) | preserved detailed root guidance for specialized agent-lane checks |

## Must not claim

Does not replace root or nearest AGENTS.md.

Do not use this district to absorb owner-local truth from sibling repositories.

## Promotion path

A document in this district may influence current law only when a change names the surviving canonical surface, updates links, rebuilds generated indexes, and runs the Wave D validators.

## Validation

```bash
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_docs_thematic_districts.py
python scripts/build_docs_thematic_index.py --check
python scripts/validate_docs_thematic_index.py
```
