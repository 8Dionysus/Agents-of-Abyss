# AGENTS.md

## Applies to

This card applies to `mechanics/method-growth/parts/` and all active part
directories below it.

## Role

Method-growth parts keep the functioning mechanic readable. Each part names a
small center route, allowed outputs, stop-lines, and the next owner route.

## Boundaries

- Do not turn part docs into sibling inventories or raw provenance logs.
- Do not mint `candidate_ref`, `seed_ref`, or `object_ref` in a part.
- Do not claim proof, memory, runtime, technique, skill, playbook, or final
  owner truth from this package.
- Route deeper source history through `../PROVENANCE.md`.

## Validation

Run the package validator after part changes:

```bash
python mechanics/method-growth/scripts/validate_method_growth_mechanic.py
```

Run wider package checks when part changes affect owner requests, registry, or
generated maps:

```bash
python scripts/validate_mechanics_topology.py --mechanic method-growth
python scripts/validate_mechanic_readme_cards.py --mechanic method-growth
python scripts/validate_mechanic_landing_logs.py --mechanic method-growth
```

## Closeout

Name the changed active parts, owner requests affected, whether provenance was
consulted, checks run, checks skipped, remaining risk, and next owner route.
