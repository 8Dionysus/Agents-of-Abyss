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

### Quest lifecycle board activation

Status: landed

Owner boundary: `Agents-of-Abyss` owns center quest lifecycle shape and the
public item store; owner repositories still own repo-local work truth.

Surfaces:

- `mechanics/questbook/docs/QUESTBOOK_MODEL.md`
- `mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `mechanics/questbook/tests/test_questbook_lifecycle.py`
- `QUESTBOOK.md`
- `quests/README.md`
- `quests/<lifecycle-state>/`

Validation: `python scripts/validate_questbook_lifecycle.py`

Stop-lines: lifecycle placement is not a roadmap, scheduler, private memory, or
owner-local task claim.

Next route: promote quest objects by state only when the owner lane and evidence
path justify the move.
