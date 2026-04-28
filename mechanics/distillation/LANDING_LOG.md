# Distillation Landing Log

Canonical landing ledger for the Distillation mechanic.

## Route index for agents

Read this index before scanning the full ledger. It names the current shape of
Distillation without requiring every older landing entry to be re-read.

- Distillation landed as center law, active parts, owner map, and owner-request
  route without moving technique, skill, playbook, runtime, memory, proof, seed,
  SDK, ToS, or infrastructure authority into `Agents-of-Abyss`.
- Current active route: `mechanics/distillation/README.md`,
  `mechanics/distillation/DIRECTION.md`, `mechanics/distillation/PARTS.md`,
  `mechanics/distillation/parts/README.md`, and the relevant part README.
- Current owner pressure route: `mechanics/distillation/OWNER_REQUESTS.md`.
- Current future-pressure route: `mechanics/distillation/ROADMAP.md`.
- Current provenance bridge: `mechanics/distillation/PROVENANCE.md`; use it
  only when auditing source provenance or raw-to-active history.

## How to update this log

Every landing entry uses the same shape:

- `Status:`
- `Owner boundary:`
- `Surfaces:`
- `Validation:`
- `Stop-lines:`
- `Next route:`

When a change touches Distillation docs, parts, owner requests, source bridges,
validators, or tests, update the relevant entry here or explain in the PR why
the change is not a landing change.

## Entries

### Center distillation mechanic landing

Status: landed

Owner boundary: `Agents-of-Abyss` owns distillation law, vocabulary, stop-lines, provenance route grammar, active extraction discipline, and owner handoff boundaries; `aoa-techniques`, `aoa-skills`, `aoa-playbooks`, `aoa-agents`, `aoa-memo`, `aoa-evals`, `aoa-sdk`, `Dionysus`, `Tree-of-Sophia`, and `abyss-stack` own stronger local truth.

Surfaces:

- `mechanics/distillation/AGENTS.md`
- `mechanics/distillation/README.md`
- `mechanics/distillation/DIRECTION.md`
- `mechanics/distillation/PARTS.md`
- `mechanics/distillation/OWNER_MAP.md`
- `mechanics/distillation/PROVENANCE.md`
- `mechanics/distillation/OWNER_REQUESTS.md`
- `mechanics/distillation/ROADMAP.md`
- `mechanics/distillation/LANDING_LOG.md`
- `mechanics/distillation/docs/DISTILLATION_LAW.md`
- `mechanics/distillation/docs/DISTILLATION_OWNER_REPO_REQUESTS.md`
- `mechanics/distillation/parts/README.md`
- `mechanics/distillation/parts/raw-intake/README.md`
- `mechanics/distillation/parts/raw-preservation/README.md`
- `mechanics/distillation/parts/provenance-bridge/README.md`
- `mechanics/distillation/parts/active-extraction/README.md`
- `mechanics/distillation/parts/noise-pruning/README.md`
- `mechanics/distillation/parts/receipt-index/README.md`
- `mechanics/distillation/parts/candidate-handoff/README.md`
- `mechanics/distillation/parts/validation-gate/README.md`
- `mechanics/distillation/parts/runtime-pack-boundary/README.md`
- `mechanics/distillation/parts/compost-boundary/README.md`
- `mechanics/distillation/legacy/README.md`
- `mechanics/distillation/legacy/INDEX.md`
- `mechanics/distillation/legacy/DISTILLATION_LOG.md`
- `mechanics/distillation/legacy/raw/README.md`
- `mechanics/distillation/scripts/validate_distillation_mechanic.py`
- `mechanics/distillation/tests/test_distillation_mechanic.py`
- `mechanics/registry.json`
- `mechanics/owner-request-queue.json`
- `generated/mechanic_card_index.min.json`
- `generated/owner_request_queue.min.json`
- `quests/distillation/README.md`
- `scripts/validate_mechanics_topology.py`
- `scripts/validate_mechanic_landing_logs.py`
- `scripts/validate_mechanic_artifact_topology.py`
- `scripts/release_check.py`
- `tests/test_mechanics_topology.py`
- `tests/test_owner_request_queue.py`
- `CHANGELOG.md`

Validation: `python mechanics/distillation/scripts/validate_distillation_mechanic.py`; `python scripts/validate_mechanics_topology.py --mechanic distillation`; `python scripts/validate_mechanic_readme_cards.py --mechanic distillation`; `python scripts/validate_owner_request_queue.py --mechanic distillation`; `python scripts/release_check.py`

Stop-lines: no summarization as distillation, proof verdict, memory canon, runtime activation, owner acceptance, ToS canon or compost authority, raw deletion authority, generated or derived distillation authority.

Next route: land owner-local request packets in the owning repositories before claiming operational distillation behavior.
