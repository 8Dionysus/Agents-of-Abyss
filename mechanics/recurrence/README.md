# Recurrence Mechanic
Recurrence is a center mechanic package in `Agents-of-Abyss`. It names the center-owned route, stop-lines, and owner handoffs without taking operational truth from stronger owner repositories.
## Mechanic card
- Status: `landed`
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

### Validation
Use the validation lane in [mechanics/recurrence/AGENTS.md](AGENTS.md#validation) for executable commands.
### Next route
- For memory, route to `aoa-memo`; for routing behavior, route to `aoa-routing`; for runtime wrappers, route to `abyss-stack` after runtime gates.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.


## Owner-request queue

Use [`RECURRENCE_OWNER_REPO_REQUESTS.md`](docs/RECURRENCE_OWNER_REPO_REQUESTS.md) when this mechanic produces an owner-local landing request. The central queue source is [`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the compact generated companion is [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).

A request packet is not owner acceptance. Keep `recurrence` claims center-bounded until the stronger owner lands the slice and proof routes are satisfied.

## Start here
- [RECURRENCE_PRINCIPLE](docs/RECURRENCE_PRINCIPLE.md)
- [SELF_AGENCY_CONTINUITY](docs/SELF_AGENCY_CONTINUITY.md)
- [COMPONENT_REFRESH_LAW](docs/COMPONENT_REFRESH_LAW.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)

- [RECURRENCE_OWNER_REPO_REQUESTS](docs/RECURRENCE_OWNER_REPO_REQUESTS.md)

## Owner boundary
Center return and continuity law; memory, routing, choreography, proof, and runtime behavior remain owner-local.
The card above is the compact route. The docs listed in **Start here** remain the richer source surfaces for this mechanic. Generated card indexes may reflect this package, but they do not author meaning.
## Growth posture
When this mechanic changes, keep the card small enough for a low-context agent to act safely, then place detailed doctrine in `docs/`, proof in the proof owner, memory in the memory owner, runtime in the runtime owner, and source meaning in the source owner.
