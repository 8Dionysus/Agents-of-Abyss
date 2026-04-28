# Growth Cycle Landing Log

This log records checked center landings for Growth Cycle.

## Route index for agents

Read this index before scanning the full ledger. It names the current shape of
Growth Cycle without requiring every older landing entry to be re-read.

| Entry | Status | Key point |
|---|---|---|
| [Center Growth Cycle landing](#center-growth-cycle-landing) | landed | Establishes the reviewed lifecycle route and owner split. |

Current active route: `mechanics/growth-cycle/README.md`,
`mechanics/growth-cycle/DIRECTION.md`, `mechanics/growth-cycle/PARTS.md`,
`mechanics/growth-cycle/parts/README.md`, and the relevant part README.

## How to update this log

Every landing entry uses the same shape:

- `Status:`
- `Owner boundary:`
- `Surfaces:`
- `Validation:`
- `Stop-lines:`
- `Next route:`

When a change touches Growth Cycle docs, parts, owner requests, source bridges,
validators, or tests, update the relevant entry here or explain in the PR why
the change is not a landing change.

## Entries

### Center Growth Cycle landing

Status: landed

Owner boundary: AoA owns Growth Cycle law, stage order, stop-lines, owner split,
and route grammar. Sibling repositories own hooks, skills, proof, memory, runtime,
stats, route behavior, playbooks, seeds, and owner-local acceptance.

Surfaces:

- `mechanics/growth-cycle/AGENTS.md`
- `mechanics/growth-cycle/README.md`
- `mechanics/growth-cycle/DIRECTION.md`
- `mechanics/growth-cycle/PARTS.md`
- `mechanics/growth-cycle/OWNER_MAP.md`
- `mechanics/growth-cycle/PROVENANCE.md`
- `mechanics/growth-cycle/OWNER_REQUESTS.md`
- `mechanics/growth-cycle/ROADMAP.md`
- `mechanics/growth-cycle/LANDING_LOG.md`
- `mechanics/growth-cycle/docs/GROWTH_CYCLE_LAW.md`
- `mechanics/growth-cycle/docs/GROWTH_CYCLE_OWNER_REPO_REQUESTS.md`
- `mechanics/growth-cycle/parts/README.md`
- `mechanics/growth-cycle/parts/checkpoint-intake/README.md`
- `mechanics/growth-cycle/parts/reviewed-closeout-chain/README.md`
- `mechanics/growth-cycle/parts/donor-harvest/README.md`
- `mechanics/growth-cycle/parts/progression-lift/README.md`
- `mechanics/growth-cycle/parts/route-forks/README.md`
- `mechanics/growth-cycle/parts/automation-opportunity/README.md`
- `mechanics/growth-cycle/parts/diagnosis-gate/README.md`
- `mechanics/growth-cycle/parts/repair-cycle/README.md`
- `mechanics/growth-cycle/parts/quest-promotion/README.md`
- `mechanics/growth-cycle/parts/owner-followthrough/README.md`
- `mechanics/growth-cycle/scripts/validate_growth_cycle_mechanic.py`
- `mechanics/growth-cycle/tests/test_growth_cycle_mechanic.py`
- `mechanics/registry.json`
- `mechanics/owner-request-queue.json`
- `mechanics/OWNER_REQUEST_QUEUE.md`
- `config/agents_mesh.json`
- `generated/mechanic_card_index.min.json`
- `generated/owner_request_queue.min.json`
- `generated/agents_mesh.min.json`
- `generated/center_entry_map.min.json`
- `scripts/center_entry_map_common.py`
- `scripts/validate_ecosystem.py`
- `scripts/validate_mechanic_artifact_topology.py`
- `scripts/validate_mechanic_landing_logs.py`
- `scripts/validate_mechanics_topology.py`
- `scripts/validate_owner_request_docs.py`
- `scripts/validate_owner_request_queue.py`
- `scripts/release_check.py`
- `tests/test_mechanic_landing_logs.py`
- `tests/test_mechanics_topology.py`
- `tests/test_owner_request_queue.py`
- `CHANGELOG.md`

Validation:

- `python mechanics/growth-cycle/scripts/validate_growth_cycle_mechanic.py`
- `python -m pytest -q mechanics/growth-cycle/tests`
- `python scripts/release_check.py`

Stop-lines: Growth Cycle must not claim hook implementation authority,
executable skill truth, proof verdict, memory canon, runtime activation, owner
acceptance, hidden scheduler behavior, autonomous self-repair, universal
progression score, quest promotion authority without reviewed evidence, or
method-growth final object truth.

Next route: Carry owner request IDs into the relevant owner repositories before
claiming operational behavior outside center law.
