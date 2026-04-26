# AGENTS.md

## Applies to

This card applies to `mechanics/questbook/` and every nested path under that scope until a nearer `AGENTS.md` narrows the lane.

## Read before editing

Read the repository root `AGENTS.md`, this card, and the nearest `README.md` or protocol surface before changing files in this lane.

## Boundaries

Do not use this lane to override owner-local truth, generated-source boundaries, sibling-repo authority, or release validation contracts.

## Closeout

Closeout must name changed surfaces, checks run, checks skipped, remaining risk, and the next owner route if this lane was only a waypoint.

This file applies to `mechanics/questbook/`.

## Role

Questbook owns the mechanics of public obligations, quest lifecycle, placement,
risk, difficulty, and harvest rules.

Root `QUESTBOOK.md` remains the public index.
`quests/` remains the quest item store. Source quest objects live under
lane-first lifecycle directories such as `quests/center/triaged/`,
`quests/agon/triaged/`, and `quests/experience/triaged/`; root-level
`AOA-Q-*` aliases and root lifecycle directories are intentionally absent.

## Validation

Run after package or quest-store changes:

```bash
python scripts/validate_mechanics_topology.py --mechanic questbook
python mechanics/questbook/scripts/validate_questbook_lifecycle.py
python mechanics/questbook/scripts/build_questbook_index.py --check
python mechanics/questbook/scripts/validate_questbook_index.py
python mechanics/questbook/scripts/validate_quest_relations.py
```
