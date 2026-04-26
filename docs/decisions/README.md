# Decisions District

This district holds Decision records explaining why a route, owner split, or placement was chosen.

## District law

Keep this district reviewable and labeled. A reader or agent should know whether a surface is current law, evidence, historical receipt, transition note, or compatibility reference before citing it.

## Current surfaces

| Surface | Role |
|---|---|
| [`2026-04-09-aoa-stats-public-layer`](2026-04-09-aoa-stats-public-layer.md) | decision record for `aoa-stats` as public derived layer |
| [`2026-04-10-federation-release-contract`](2026-04-10-federation-release-contract.md) | decision record for federation release contract |
| [`2026-04-11-growth-refinery-lineage-route`](2026-04-11-growth-refinery-lineage-route.md) | decision record for growth refinery lineage routing |
| [`2026-04-26-questbook-model-spine-and-route-registries`](2026-04-26-questbook-model-spine-and-route-registries.md) | decision record for Questbook model split and registry-backed route tables |
| [`2026-04-26-questbook-source-contract-full-distillation`](2026-04-26-questbook-source-contract-full-distillation.md) | decision record for promoting Markdown quest sources to the strict source contract |

## Must not claim

Decisions explain why; current surfaces define what.

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
