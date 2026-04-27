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

## Start Here

- Direction: [DIRECTION](DIRECTION.md)
- Parts atlas: [PARTS](PARTS.md) and [parts](parts/)
- Owner map: [OWNER_MAP](OWNER_MAP.md)
- Owner requests: [OWNER_REQUESTS](OWNER_REQUESTS.md)
- Provenance bridge: [PROVENANCE](PROVENANCE.md)
- Center law: [RECURRENCE_PRINCIPLE](docs/RECURRENCE_PRINCIPLE.md)
- Continuity law: [SELF_AGENCY_CONTINUITY](docs/SELF_AGENCY_CONTINUITY.md)
- Component law: [COMPONENT_REFRESH_LAW](docs/COMPONENT_REFRESH_LAW.md)
- Compatibility route: [RECURRENCE_OWNER_REPO_REQUESTS](docs/RECURRENCE_OWNER_REPO_REQUESTS.md)
- Status: [LANDING_LOG](LANDING_LOG.md) and [ROADMAP](ROADMAP.md)

## Active Parts

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

## Owner Boundary

Center return and continuity law; typed carry, memory, routing, choreography,
proof, derived visibility, regrounding, and runtime behavior remain
owner-local.
The card above is the compact route. The docs listed in **Start Here** remain
the richer source surfaces for this mechanic. Generated surfaces may reflect
recurrence cards, queues, indexes, or manifests, but they do not author
recurrence meaning.

AoA owns recurrence law. `aoa-sdk` carries recurrence control-plane evidence.
Owner repositories own local recurrence behavior.

## Growth Posture

When this mechanic changes, keep active parts lean, owner-routed, and
provenance-aware. Put detailed doctrine in `docs/`, proof in the proof owner,
memory in the memory owner, runtime in the runtime owner, control-plane carry
in `aoa-sdk`, and source meaning in the source owner.
