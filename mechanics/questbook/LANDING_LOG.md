# Questbook Landing Log

Canonical landing ledger for the questbook mechanic.

## Entries

### Root mechanics topology migration

Status: landed

Owner boundary: `Agents-of-Abyss` owns federation-level quest mechanics and the
root public index; repo-local obligations remain with owner repositories.

Surfaces:

- `mechanics/questbook/README.md`
- `mechanics/questbook/ROADMAP.md`
- `mechanics/questbook/docs/QUESTBOOK_MODEL.md`
- `mechanics/questbook/docs/QUESTBOOK_FIRST_WAVE.md`
- `QUESTBOOK.md`
- `quests/README.md`

Validation: `python scripts/validate_mechanics_topology.py --mechanic questbook`

Stop-lines: no second roadmap, private scratchpad, or owner-local task sink.

Next route: keep quest items in `quests/` and route repo-local tasks to their
owners.
