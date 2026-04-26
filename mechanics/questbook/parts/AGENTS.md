# AGENTS.md

## Applies to

This card applies to `mechanics/questbook/parts/` and all active Questbook
part packages.

## Role

Questbook parts hold functioning contracts for public obligations, lifecycle
law, relation shape, owner-route maps, and generated read-model routes.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`,
`mechanics/questbook/AGENTS.md`, `mechanics/questbook/PARTS.md`, and the
specific part `README.md` before changing this lane.

## Boundaries

Do not pull legacy/raw inventories into active part docs. Do not claim owner
acceptance, proof verdicts, runtime activation, hidden memory, or sibling-repo
task truth from this lane.

## Part evolution

A part may grow, split, merge, shrink, or retire when that makes the route more
usable. When a boundary changes, review `PARTS.md`, `ROADMAP.md`,
`LANDING_LOG.md`, `PROVENANCE.md`, and owner-request surfaces before closing.

## Validation

Run:

```bash
python scripts/validate_mechanics_topology.py --mechanic questbook
python scripts/validate_mechanic_readme_cards.py --mechanic questbook
python scripts/validate_mechanic_landing_logs.py --mechanic questbook
python mechanics/questbook/scripts/validate_questbook_lifecycle.py
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
python mechanics/questbook/scripts/validate_quest_relations.py
python mechanics/questbook/scripts/build_ready_owner_routes.py --check
python mechanics/questbook/scripts/validate_ready_owner_routes.py
python mechanics/questbook/scripts/validate_questbook_distillation.py
```

## Closeout

Report the active part changed, whether `PROVENANCE.md` was consulted,
generated mirrors rebuilt or not rebuilt, owner requests affected, checks run,
checks skipped, and remaining route risk.
