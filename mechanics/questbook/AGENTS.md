# AGENTS.md

This file applies to `mechanics/questbook/`.

## Role

Questbook owns the mechanics of public obligations, quest lifecycle, placement,
risk, difficulty, and harvest rules.

Root `QUESTBOOK.md` remains the public index.
`quests/` remains the quest item store.

## Validation

Run `python scripts/validate_mechanics_topology.py --mechanic questbook` after
package changes.
