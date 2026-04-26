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
- `quests/*/*/` after the later lane-first topology landing

Validation: `python mechanics/questbook/scripts/validate_questbook_lifecycle.py`

Stop-lines: lifecycle placement is not a roadmap, scheduler, private memory, or
owner-local task claim.

Next route: promote quest objects by state only when the owner lane and evidence
path justify the move.

### Lane-first quest topology

Status: landed

Owner boundary: `Agents-of-Abyss` owns the center Questbook topology and public
read models; lanes name owner route, while lifecycle state names current
posture. Owner repositories still own repo-local task truth.

Surfaces:

- `QUESTBOOK.md`
- `quests/README.md`
- `quests/center/README.md`
- `quests/agon/README.md`
- `quests/experience/README.md`
- `quests/*/README.md`
- `quests/<lane>/<state>/AOA-Q-*`
- `mechanics/questbook/DIRECTION.md`
- `mechanics/questbook/PARTS.md`
- `mechanics/questbook/scripts/build_questbook_index.py`
- `mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `mechanics/questbook/scripts/validate_questbook_index.py`
- `generated/questbook_index.min.json`
- `generated/questbook_frontier.min.json`

Validation:

- `python mechanics/questbook/scripts/validate_questbook_lifecycle.py`
- `python mechanics/questbook/scripts/build_questbook_index.py --check`
- `python mechanics/questbook/scripts/validate_questbook_index.py`

Stop-lines: no root quest aliases, no root lifecycle source directories, no
generated surface as quest authority, and no repo-local task truth in the center
unless it is a federation obligation.

Next route: use lane-first promotion for real quest movement, then harvest
repeated quest families into the stronger owner mechanic or repository.
