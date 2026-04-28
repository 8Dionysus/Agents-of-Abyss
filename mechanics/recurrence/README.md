# Recurrence Mechanic

Recurrence is a center mechanic package in `Agents-of-Abyss`. It names the
center-owned route, stop-lines, active parts, and owner handoffs without taking
operational truth from stronger owner repositories.

## Mechanic card

Status: `landed`

### Trigger

Use when a route loses its axis, must return to a valid anchor, or needs bounded continuity across a handoff.

### Center owns

Center return law, drift/anchor/re-entry vocabulary, component refresh boundary, and safe-stop posture.

### Stronger owner split

- `aoa-routing` owns local routing implementation and route graph behavior.
- `aoa-memo` owns checkpoint, recall, and provenance.
- `aoa-agents` owns role and handoff posture.
- `aoa-playbooks` owns recurring return choreography.
- `aoa-evals` owns drift and recovery-quality proof.
- `abyss-stack` owns runtime wrappers after runtime-owner gates.
- `aoa-sdk` owns typed recurrence carry, manifests, graph closure, projections,
  and reviewed handoff packets.
- `aoa-stats` owns derived recurrence visibility.
- `aoa-kag` owns derived regrounding toward stronger source refs.

### Inputs

- A drifting route, lost axis, stale component, broken handoff, or continuity claim that needs an anchor.
- The last reviewable anchor and the expected next route from that anchor.

### Outputs

- Return point, re-entry step, safe stop, component refresh request, or owner-local handoff.
- No ambient continuity claim and no hidden memory sovereignty.

### Must not claim

- ambient continuity
- hidden memory sovereignty
- runtime self-healing
- direct runtime resume
- automatic recursor spawn

### Validation

Use the validation lane in [mechanics/recurrence/AGENTS.md](AGENTS.md#validation) for executable commands.

### Next route

- For memory, route to `aoa-memo`; for routing behavior, route to `aoa-routing`; for runtime wrappers, route to `abyss-stack` after runtime gates.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.

## Active route

- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)
- [OWNER_MAP](OWNER_MAP.md)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [PROVENANCE](PROVENANCE.md)

## Functioning parts

- [Anchor Return](parts/anchor-return/README.md)
- [Continuity Window](parts/continuity-window/README.md)
- [Component Refresh](parts/component-refresh/README.md)
- [Control Plane Carry](parts/control-plane-carry/README.md)
- [Reentry Routing](parts/reentry-routing/README.md)
- [Memory Recall](parts/memory-recall/README.md)
- [Scenario Choreography](parts/scenario-choreography/README.md)
- [Proof Gates](parts/proof-gates/README.md)
- [Runtime Return](parts/runtime-return/README.md)
- [Recursor Boundary](parts/recursor-boundary/README.md)

## Owner-request queue

Use [OWNER_REQUESTS](OWNER_REQUESTS.md) when this mechanic produces an
owner-local landing request. The central queue source is
[`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the
compact generated companion is
[`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).

A request packet is not owner acceptance. Keep `recurrence` claims
center-bounded until the stronger owner lands the slice and proof routes are
satisfied.

## Historical provenance

Use [PROVENANCE](PROVENANCE.md) only when auditing how recurrence principle,
self-agency continuity, component refresh law, or owner request doctrine feeds
the active parts. The default route stays on the active route and functioning
parts above.

Canonical doctrine refs: [RECURRENCE_PRINCIPLE](docs/RECURRENCE_PRINCIPLE.md),
[SELF_AGENCY_CONTINUITY](docs/SELF_AGENCY_CONTINUITY.md),
[COMPONENT_REFRESH_LAW](docs/COMPONENT_REFRESH_LAW.md), and
[RECURRENCE_OWNER_REPO_REQUESTS](docs/RECURRENCE_OWNER_REPO_REQUESTS.md).

## Owner boundary

Center return and continuity law; typed carry, memory, routing, choreography,
proof, derived visibility, regrounding, and runtime behavior remain
owner-local.

AoA owns recurrence law. `aoa-sdk` carries recurrence control-plane evidence.
Owner repositories own local recurrence behavior.

Generated surfaces may reflect recurrence cards, queues, indexes, or manifests,
but they do not author recurrence meaning.

## Growth posture

When this mechanic changes, preserve a clean active route: update the relevant
functioning part, preserve landing history in `LANDING_LOG.md`, keep historical
accounting behind `PROVENANCE.md`, and route proof, memory, runtime,
control-plane carry, routing, stats, KAG, and source meaning to their stronger
owners.
