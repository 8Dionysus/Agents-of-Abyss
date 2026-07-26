# Distillation Landing Log

Canonical landing ledger for the Distillation mechanic.

## Route index for agents

Read this index before scanning the full ledger. It names the current shape of
Distillation without requiring every older landing entry to be re-read.

- Distillation landed as center law, active parts, and owner map without moving technique, skill, playbook, runtime, memory, proof, intake, SDK, ToS, or infrastructure authority into `Agents-of-Abyss`.
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

### Source-local preservation and direct owner intake

Status: landed

Owner boundary: source repositories and their local legacy districts preserve
raw material; final owner repositories own intake and landing without a
federation staging owner.

Surfaces: `mechanics/distillation/README.md`,
`mechanics/distillation/AGENTS.md`, `mechanics/distillation/PARTS.md`,
`mechanics/distillation/OWNER_MAP.md`,
`mechanics/distillation/OWNER_REQUESTS.md`, the package validator, the center
owner-request queue, and decision `AOA-CENTER-D-0033`.

Validation: distillation package tests, mechanic card and topology checks,
owner-request queue validation, and release check.

Stop-lines: preservation does not grant owner acceptance, proof, memory canon,
runtime activation, or deletion authority.

Next route: preserve material with its source owner and carry reviewed
candidates directly to the final owner repository.

### aoa-skills owner-request receipt sync

Status: owner-request accepted.

Owner boundary: the center records the `aoa-skills` acceptance receipt for
`ORQ-DISTILLATION-SKILLS-001` without claiming executable distillation workflow
activation or generic skill-layer landing.

Surfaces:

- `mechanics/distillation/OWNER_REQUESTS.md`
- `mechanics/owner-request-queue.json`
- `mechanics/OWNER_REQUEST_QUEUE.md`
- `generated/owner_request_queue.min.json`
- Owner-local receipt in aoa-skills/mechanics/OWNER_REQUEST_RECEIPTS.md

Validation: use the owner-request validation lane in `mechanics/AGENTS.md`.

Stop-lines: Accepted is not landed. The center must not claim a general
distillation skill package until `aoa-skills` lands one or supersedes the
request.

Next route: Wait for `aoa-skills` distillation package, canonical workflow, or
superseding receipt before advancing this request to `landed`.

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
- `scripts/mechanics_topology/validate_mechanics_topology.py`
- `scripts/mechanics_topology/validate_mechanic_landing_logs.py`
- `scripts/mechanics_topology/validate_mechanic_artifact_topology.py`
- `scripts/release_gate/release_check.py`
- `tests/test_mechanics_topology.py`
- `tests/test_owner_request_queue.py`
- `CHANGELOG.md`

Validation: `python mechanics/distillation/scripts/validate_distillation_mechanic.py`; `python scripts/mechanics_topology/validate_mechanics_topology.py --mechanic distillation`; `python scripts/mechanics_topology/validate_mechanic_readme_cards.py --mechanic distillation`; `python scripts/owner_requests/validate_owner_request_queue.py --mechanic distillation`; `python scripts/release_gate/release_check.py`

Stop-lines: no summarization as distillation, proof verdict, memory canon, runtime activation, owner acceptance, ToS canon or compost authority, raw deletion authority, generated or derived distillation authority.

Next route: land owner-local request packets in the owning repositories before claiming operational distillation behavior.
