# Antifragility Mechanic

Antifragility is the center mechanic for turning stress, sprawl, authority
inflation, and cleanup pressure into clearer boundaries.

It is not a deletion cult and not a health score. It asks what the system
learned, what owner owns the repair, and what must become smaller, clearer, or
better bounded after stress.

## Mechanic card

- Status: `landed`

### Trigger

Use when stress, sprawl, authority inflation, cleanup pressure, degraded mode,
or a fragile pattern needs bounded review.

### Center owns

Center stress doctrine, via negativa, anti-authority posture, one-in-one-out
pressure, and fragility blacklist posture.

### Stronger owner split

- Owner repositories own their local deletion, repair, resilience, and incident
  evidence.
- `aoa-evals` owns repair proof and regression evidence.
- `aoa-memo` owns incident lessons and retained memory.
- `aoa-stats` owns derived fragility windows without one-score health.
- `aoa-playbooks` owns recurring cleanup and degraded-mode choreography.

### Inputs

- Stress event, fragility pattern, deletion candidate, authority drift, or
  cleanup proposal.
- Evidence that the change makes ownership, proof, or stop-lines clearer rather
  than merely smaller.

### Outputs

- Subtraction route, anti-authority stop-line, repair request, evidence request,
  memory route, or owner-local cleanup handoff.
- No one-score health metric, no deletion theater, and no owner-local cleanup
  authority.

### Must not claim

- one-score health
- deletion theater
- owner-local cleanup authority

### Validation

Use the validation lane in [AGENTS.md](AGENTS.md#validation) for executable
commands.

### Next route

- For owner-local cleanup, route to the owning repository; for repair proof,
  route to `aoa-evals`; for retained lessons, route to `aoa-memo`.
- For recurring cleanup routes, route to `aoa-playbooks`; for derived summaries,
  route to `aoa-stats`.
- For unclear owner, return to `docs/FEDERATION_RULES.md` and
  `docs/REPO_ROLES.md`.

## Active route

- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)
- [OWNER_MAP](OWNER_MAP.md)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [FRAGILITY_BLACKLIST](FRAGILITY_BLACKLIST.md)
- [PROVENANCE](PROVENANCE.md)

## Functioning parts

- [Stress Review](parts/stress-review/README.md)
- [Via Negativa](parts/via-negativa/README.md)
- [Authority Boundary](parts/authority-boundary/README.md)
- [Sprawl Control](parts/sprawl-control/README.md)
- [Fragility Registry](parts/fragility-registry/README.md)
- [Repair Proof](parts/repair-proof/README.md)
- [Memory Return](parts/memory-return/README.md)
- [Owner Handoff](parts/owner-handoff/README.md)

## Owner-request queue

Use [OWNER_REQUESTS](OWNER_REQUESTS.md) when this mechanic produces an
owner-local cleanup, proof, memory, stats, playbook, or owner-local repair
request. The central queue source is
[`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the
compact generated companion is
[`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json).
Generated surfaces do not author meaning.

A request packet is not owner acceptance. Keep `antifragility` claims
center-bounded until the stronger owner lands the slice and proof routes are
satisfied.

## Historical provenance

Use [PROVENANCE](PROVENANCE.md) only when auditing how stress doctrine,
fragility tracking, via negativa, anti-authority rules, or legacy source
material feed the active parts. The default route stays on the active route and
functioning parts above.

Canonical doctrine refs: [ANTIFRAGILITY](docs/ANTIFRAGILITY.md),
[VIA_NEGATIVA](docs/VIA_NEGATIVA.md),
[ANTI_AUTHORITY_RULES](docs/ANTI_AUTHORITY_RULES.md), and
[ONE_IN_ONE_OUT](docs/ONE_IN_ONE_OUT.md).

## Owner boundary

AoA owns antifragility law, subtraction vocabulary, anti-authority posture, and
fragility-pattern routing. Owner repositories own local repair, deletion,
incident receipts, proof, memory, runtime behavior, and accepted cleanup
execution.

Generated surfaces may reflect antifragility cards, queues, indexes, or
manifests, but they do not author antifragility meaning.

## Growth posture

When this mechanic changes, preserve a clean active route: update the relevant
functioning part, preserve landing history in `LANDING_LOG.md`, keep historical
accounting behind `PROVENANCE.md`, and route cleanup, proof, memory, stats,
playbook, and runtime claims to their stronger owners.
