# Method-growth Mechanic

Method-growth is a center mechanic package in `Agents-of-Abyss`. It names the
center-owned route, stop-lines, active parts, and owner handoffs for turning
repeated work into reviewable growth without taking operational truth from
stronger owner repositories.

## Mechanic card

Status: `landed`

### Trigger

Use when repeated work may become a reusable method, candidate object, seed,
proof, memory lesson, derived summary, or owner-local doctrine.

### Center owns

Center growth route, lineage vocabulary, reviewable-growth discipline, and
owner landing/pruning rules.

### Stronger owner split

- `aoa-sdk` owns provisional carry and typed helper hints.
- `aoa-skills` owns reviewed candidate identity and skill-shaped object truth.
- `Dionysus` owns seed staging.
- `aoa-evals` owns proof.
- `aoa-playbooks` owns recurring method.
- `aoa-techniques` owns reusable practice.
- `aoa-stats` owns derived summary.
- `aoa-memo` owns bounded memory and lessons.
- The final owner repository owns final object truth.

### Inputs

- Repeated work, donor-route residue, checkpoint pressure, or candidate lineage
  needing owner landing.
- A reviewable friction, seed, or object candidate with enough context to name a
  stronger owner.

### Outputs

- Owner route, candidate reference, seed reference, proof request, method
  request, memory request, or pruning decision.
- No final object truth until the final owner repository lands it.

### Must not claim

- center-owned final object truth
- owner-local activation
- proof verdict
- memory canon
- candidate_ref minting in center
- seed_ref minting in center
- object_ref minting in center

### Validation

Use the validation lane in [mechanics/method-growth/AGENTS.md](AGENTS.md#validation)
for executable commands.

### Next route

- For final object truth, route to the final owner repo before claiming
  activation.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and
  `docs/REPO_ROLES.md`.

## Active route

- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)
- [OWNER_MAP](OWNER_MAP.md)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [PROVENANCE](PROVENANCE.md)

## Functioning parts

- [Donor Refinery](parts/donor-refinery/README.md)
- [Candidate Lineage](parts/candidate-lineage/README.md)
- [Owner Landing](parts/owner-landing/README.md)
- [Pruning](parts/pruning/README.md)
- [Proof Route](parts/proof-route/README.md)
- [Method Promotion](parts/method-promotion/README.md)
- [Technique Skill Split](parts/technique-skill-split/README.md)
- [Memory Writeback](parts/memory-writeback/README.md)
- [Maturity Ladder](parts/maturity-ladder/README.md)
- [Growth Closeout](parts/growth-closeout/README.md)

## Owner-request queue

Use [OWNER_REQUESTS](OWNER_REQUESTS.md) when this mechanic produces an
owner-local landing request. The central queue source is
[`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the
compact generated companion is
[`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).

A request packet is not owner acceptance. Keep `method-growth` claims
center-bounded until the stronger owner lands the slice and proof routes are
satisfied.

## Historical provenance

Use [PROVENANCE](PROVENANCE.md) only when auditing how rootline, method spine,
reviewable growth, candidate lineage, owner landing, or pruning doctrine feeds
the active parts. The default route stays on the active route and functioning
parts above.

Canonical doctrine refs: [ROOTLINE](docs/ROOTLINE.md),
[METHOD_SPINE](docs/METHOD_SPINE.md),
[REVIEWABLE_GROWTH_REFINERY](docs/REVIEWABLE_GROWTH_REFINERY.md),
[CANDIDATE_LINEAGE_CROSSWALK](docs/CANDIDATE_LINEAGE_CROSSWALK.md),
[OWNER_LANDING_AND_PRUNING](docs/OWNER_LANDING_AND_PRUNING.md), and
[METHOD_GROWTH_OWNER_REPO_REQUESTS](docs/METHOD_GROWTH_OWNER_REPO_REQUESTS.md).

## Owner boundary

Center route from repeated work to candidate, seed, owner landing, proof,
method, memory, derived summary, and pruning; final object truth remains
owner-local.

AoA owns growth-route law. Owner repositories own local method, technique,
skill, proof, memory, seed, and runtime truth.

Generated surfaces may reflect method-growth cards, queues, indexes, or
manifests, but they do not author method-growth meaning.

## Growth posture

When this mechanic changes, preserve a clean active route: update the relevant
functioning part, preserve landing history in `LANDING_LOG.md`, keep historical
accounting behind `PROVENANCE.md`, and route proof, memory, reusable practice,
bounded execution, recurring method, seed, runtime, and final object truth to
their stronger owners.
