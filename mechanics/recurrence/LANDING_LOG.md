# Recurrence Landing Log

Canonical landing ledger for the recurrence mechanic.

## Route index for agents

Read this index before scanning the full ledger. It names the current shape of
Recurrence without requiring every older landing entry to be re-read.

- Recurrence active-part distillation: root package, active parts, provenance
  bridge, owner map, owner requests, and package validation.
- Root mechanics topology migration: first center recurrence package landing.
- Current active route: `mechanics/recurrence/README.md`,
  `mechanics/recurrence/DIRECTION.md`, `mechanics/recurrence/PARTS.md`,
  `mechanics/recurrence/parts/README.md`, and the relevant part README.
- Current owner pressure route: `mechanics/recurrence/OWNER_REQUESTS.md`.
- Current future-pressure route: `mechanics/recurrence/ROADMAP.md`.
- Current provenance bridge: `mechanics/recurrence/PROVENANCE.md`; use it only
  when auditing source provenance or sibling evidence history.

## How to update this log

Every landing entry uses the same shape:

- `Status:`
- `Owner boundary:`
- `Surfaces:`
- `Validation:`
- `Stop-lines:`
- `Next route:`

When a change touches Recurrence docs, parts, owner requests, source bridges,
validators, or tests, update the relevant entry here or explain in the PR why
the change is not a landing change.

## Entries

### Recurrence active-part distillation

Status: landed

Owner boundary: `Agents-of-Abyss` owns recurrence law, active part route,
owner-request packets, and provenance bridge. Owner repositories own typed carry,
route behavior, memory/recall objects, role contracts, playbook choreography,
proof, stats, regrounding, runtime return, and operator recovery.

Surfaces:

- `mechanics/recurrence/AGENTS.md`
- `mechanics/recurrence/README.md`
- `mechanics/recurrence/DIRECTION.md`
- `mechanics/recurrence/PARTS.md`
- `mechanics/recurrence/OWNER_MAP.md`
- `mechanics/recurrence/PROVENANCE.md`
- `mechanics/recurrence/OWNER_REQUESTS.md`
- `mechanics/recurrence/ROADMAP.md`
- `mechanics/recurrence/LANDING_LOG.md`
- `mechanics/recurrence/parts/`
- `mechanics/recurrence/parts/README.md`
- `mechanics/recurrence/parts/anchor-return/README.md`
- `mechanics/recurrence/parts/continuity-window/README.md`
- `mechanics/recurrence/parts/component-refresh/README.md`
- `mechanics/recurrence/parts/control-plane-carry/README.md`
- `mechanics/recurrence/parts/reentry-routing/README.md`
- `mechanics/recurrence/parts/memory-recall/README.md`
- `mechanics/recurrence/parts/scenario-choreography/README.md`
- `mechanics/recurrence/parts/proof-gates/README.md`
- `mechanics/recurrence/parts/runtime-return/README.md`
- `mechanics/recurrence/parts/recursor-boundary/README.md`
- `mechanics/recurrence/scripts/validate_recurrence_mechanic.py`
- `mechanics/recurrence/tests/test_recurrence_mechanic.py`
- `mechanics/owner-request-queue.json`
- `mechanics/OWNER_REQUEST_QUEUE.md`
- `mechanics/registry.json`
- `generated/mechanic_card_index.min.json`
- `generated/owner_request_queue.min.json`
- `scripts/validate_mechanic_landing_logs.py`
- `CHANGELOG.md`

Validation: `python mechanics/recurrence/scripts/validate_recurrence_mechanic.py`

Stop-lines: no ambient continuity, hidden memory sovereignty, runtime
self-healing, direct runtime resume, automatic recursor spawn, proof verdict, or
owner acceptance from the center package.

Next route: carry owner-local requests through `mechanics/recurrence/OWNER_REQUESTS.md`; route
control-plane carry to `aoa-sdk`, re-entry behavior to `aoa-routing`, recall to
`aoa-memo`, role/recursor posture to `aoa-agents`, recurring choreography to
`aoa-playbooks`, proof to `aoa-evals`, derived summaries to `aoa-stats`,
regrounding to `aoa-kag`, runtime return to `abyss-stack`, and operator
recovery to `ATM10-Agent`.

### Root mechanics topology migration

Status: landed

Owner boundary: `Agents-of-Abyss` owns center recurrence law; memory, routing,
playbook, proof, and runtime behavior remain owner-local.

Surfaces:

- `mechanics/recurrence/README.md`
- `mechanics/recurrence/ROADMAP.md`
- `mechanics/recurrence/docs/RECURRENCE_PRINCIPLE.md`
- `mechanics/recurrence/docs/SELF_AGENCY_CONTINUITY.md`
- `mechanics/recurrence/docs/COMPONENT_REFRESH_LAW.md`

Validation: `python scripts/validate_mechanics_topology.py --mechanic recurrence`

Stop-lines: no hidden memory sovereignty, ambient continuity, or runtime
self-healing authority.

Next route: route recurring choreography to `aoa-playbooks` and recall objects
to `aoa-memo` when they become owner-local artifacts.
