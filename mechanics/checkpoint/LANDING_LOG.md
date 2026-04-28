# Checkpoint Landing Log

Canonical landing ledger for the Checkpoint mechanic.

## Route index for agents

Read this index before scanning the full ledger. It names the current shape of
Checkpoint without requiring every older landing entry to be re-read.

- Checkpoint landed as center law, owner map, active parts, and owner-request
  route without moving implementation, runtime, memory, proof, routing, or stats
  authority into `Agents-of-Abyss`.
- Current active route: `mechanics/checkpoint/README.md`,
  `mechanics/checkpoint/DIRECTION.md`, `mechanics/checkpoint/PARTS.md`,
  `mechanics/checkpoint/parts/README.md`, and the relevant part README.
- Current owner pressure route: `mechanics/checkpoint/OWNER_REQUESTS.md`.
- Current future-pressure route: `mechanics/checkpoint/ROADMAP.md`.
- Current provenance bridge: `mechanics/checkpoint/PROVENANCE.md`; use it only
  when auditing source provenance or sibling evidence history.

## How to update this log

Every landing entry uses the same shape:

- `Status:`
- `Owner boundary:`
- `Surfaces:`
- `Validation:`
- `Stop-lines:`
- `Next route:`

When a change touches Checkpoint docs, parts, owner requests, source bridges,
validators, or tests, update the relevant entry here or explain in the PR why
the change is not a landing change.

## Entries

### Center checkpoint mechanic landing

Status: landed

Owner boundary: `Agents-of-Abyss` owns checkpoint law, vocabulary, owner map, stop-lines, and cross-owner route grammar; `aoa-sdk`, `aoa-skills`, `aoa-agents`, `aoa-memo`, `aoa-playbooks`, `aoa-evals`, `aoa-routing`, `aoa-stats`, `Dionysus`, and `abyss-stack` own stronger local truth.

Surfaces:

- `mechanics/checkpoint/AGENTS.md`
- `mechanics/checkpoint/README.md`
- `mechanics/checkpoint/DIRECTION.md`
- `mechanics/checkpoint/PARTS.md`
- `mechanics/checkpoint/OWNER_MAP.md`
- `mechanics/checkpoint/PROVENANCE.md`
- `mechanics/checkpoint/OWNER_REQUESTS.md`
- `mechanics/checkpoint/ROADMAP.md`
- `mechanics/checkpoint/LANDING_LOG.md`
- `mechanics/checkpoint/docs/CHECKPOINT_LAW.md`
- `mechanics/checkpoint/docs/CHECKPOINT_OWNER_BOUNDARY.md`
- `mechanics/checkpoint/parts/README.md`
- `mechanics/checkpoint/parts/session-carry/README.md`
- `mechanics/checkpoint/parts/review-gate/README.md`
- `mechanics/checkpoint/parts/return-reentry/README.md`
- `mechanics/checkpoint/parts/closeout-bridge/README.md`
- `mechanics/checkpoint/parts/runtime-export/README.md`
- `mechanics/checkpoint/parts/owner-handoff/README.md`
- `mechanics/checkpoint/scripts/validate_checkpoint_mechanic.py`
- `mechanics/checkpoint/tests/test_checkpoint_mechanic.py`
- `mechanics/registry.json`
- `mechanics/owner-request-queue.json`
- `generated/mechanic_card_index.min.json`
- `generated/owner_request_queue.min.json`
- `scripts/validate_mechanics_topology.py`
- `scripts/validate_mechanic_landing_logs.py`
- `scripts/release_check.py`
- `tests/test_mechanics_topology.py`
- `tests/test_owner_request_queue.py`
- `CHANGELOG.md`

Validation: `python mechanics/checkpoint/scripts/validate_checkpoint_mechanic.py`; `python scripts/validate_mechanics_topology.py --mechanic checkpoint`; `python scripts/validate_mechanic_readme_cards.py --mechanic checkpoint`; `python scripts/validate_owner_request_queue.py --mechanic checkpoint`; `python scripts/release_check.py`

Stop-lines: no checkpoint implementation authority, memory canon or recall sovereignty, proof verdicts or stats truth, runtime activation or owner acceptance, hidden scheduler or autonomous self-repair.

Next route: land owner-local request packets in the owning repositories before claiming operational checkpoint behavior.
