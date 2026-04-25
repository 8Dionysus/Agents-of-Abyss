# Legacy District

This district holds Compatibility aliases and superseded flat docs preserved for provenance.

## District law

Keep this district reviewable and labeled. A reader or agent should know whether a surface is current law, evidence, historical receipt, transition note, or compatibility reference before citing it.

## Current surfaces

Add surfaces here when they match the classifier in [`../thematic_districts.json`](../thematic_districts.json). Keep this README as the local gate.

## Must not claim

Legacy surfaces are not current law when canonical routes exist.

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
