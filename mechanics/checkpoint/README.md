# Checkpoint Mechanic

Checkpoint is a center mechanic package in `Agents-of-Abyss`.
It names how intermediate growth states stay bounded, reviewable, resumable,
and transferable without turning checkpoint carry into owner-local truth.

## Mechanic card

Status: `landed`

### Trigger

Use when work needs a bounded checkpoint for session carry, review gate, return and re-entry, closeout bridge, runtime export boundary, or owner handoff without turning the checkpoint into owner-local truth.

### Center owns

Checkpoint law, vocabulary, owner map, stop-lines, and cross-owner route grammar for intermediate growth states.

### Stronger owner split

- `aoa-sdk` owns checkpoint controls, hooks, local ledgers, typed readers, and closeout-context builders.
- `aoa-skills` owns checkpoint-note protocol and explicit closeout bridge skill.
- `aoa-agents` owns self-agent checkpoint posture, roles, approval, rollback, health, and iteration boundaries.
- `aoa-memo` owns inquiry checkpoints, state capsules, recall anchors, provenance, and checkpoint-to-memory writeback.
- `aoa-playbooks` owns recurring checkpoint choreography and scenario routes.
- `aoa-evals` owns proof and regression readings.
- `aoa-routing` owns re-entry hints without checkpoint meaning.
- `aoa-stats` owns derived checkpoint visibility and never raw checkpoint authority.
- `Dionysus` owns reviewed checkpoint snapshots and seed-stage lineage when promotion is explicit.
- `abyss-stack` owns runtime checkpoint exports, runtime receipts, and runtime closeout plumbing after runtime gates.

### Inputs

- Checkpoint signal, pause point, commit/verify/PR/merge/owner-followthrough boundary, return anchor, runtime export candidate, or reviewed closeout residue.
- Evidence refs and owner hints strong enough to name the next owner without minting owner truth.

### Outputs

- Checkpoint route, review gate, return anchor, closeout bridge request, runtime export stop-line, owner handoff, or owner-request packet.
- No candidate_ref, memory canon, proof verdict, runtime activation, or owner acceptance unless the stronger owner lands it.

### Must not claim

- checkpoint implementation authority
- memory canon or recall sovereignty
- proof verdicts or stats truth
- runtime activation or owner acceptance
- hidden scheduler or autonomous self-repair

### Validation

Use the validation lane in [mechanics/checkpoint/AGENTS.md](AGENTS.md#validation) for executable commands.

### Next route

- For controls, hooks, local ledgers, and closeout-context builders, route to `aoa-sdk`; for checkpoint-note protocol and bridge skills, route to `aoa-skills`; for self-agent posture, route to `aoa-agents`.
- For memory writeback, route to `aoa-memo`; for scenario choreography, route to `aoa-playbooks`; for proof, route to `aoa-evals`; for re-entry hints, route to `aoa-routing`; for derived visibility, route to `aoa-stats`; for reviewed snapshots or seed lineage, route to `Dionysus`; for runtime exports, route to `abyss-stack` after runtime gates; for unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.

## Start Here

- Direction: [DIRECTION](DIRECTION.md)
- Parts atlas: [PARTS](PARTS.md) and [parts](parts/)
- Center law: [CHECKPOINT_LAW](docs/CHECKPOINT_LAW.md)
- Owner boundaries: [OWNER_MAP](OWNER_MAP.md) and [CHECKPOINT_OWNER_BOUNDARY](docs/CHECKPOINT_OWNER_BOUNDARY.md)
- Owner requests: [OWNER_REQUESTS](OWNER_REQUESTS.md)
- Provenance: [PROVENANCE](PROVENANCE.md)
- Status: [LANDING_LOG](LANDING_LOG.md) and [ROADMAP](ROADMAP.md)

## Working Law

Checkpoint is the lawful intermediate form between live work and later owner
truth.

It may preserve evidence, route pressure, review posture, return anchors, and
owner hints. It may not mint stronger object identities, memory canon, proof
verdicts, runtime activation, route authority, stats truth, or owner acceptance.

Generated surfaces may reflect checkpoint cards, queues, or indexes, but they
do not author checkpoint meaning.

## Active Parts

- [Session Carry](parts/session-carry/README.md)
- [Review Gate](parts/review-gate/README.md)
- [Return Re-entry](parts/return-reentry/README.md)
- [Closeout Bridge](parts/closeout-bridge/README.md)
- [Runtime Export](parts/runtime-export/README.md)
- [Owner Handoff](parts/owner-handoff/README.md)

## Owner Boundary

AoA owns the law and map for checkpoint mechanics. `aoa-sdk` operates the
control panel. Owner repositories decide what local checkpoint behavior means
inside their own domains.
