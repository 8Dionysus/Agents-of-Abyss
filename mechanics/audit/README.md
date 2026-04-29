# Audit Mechanic

Audit is a center mechanic package in `Agents-of-Abyss`. It makes a surface legible enough to route the next honest move: what source owns it, what evidence exists, what risk is visible, what finding can be stated, and where the work should go next.

## Mechanic card

- Status: `planted`

### Trigger

Use when a surface, claim, route, owner boundary, evidence trail, or change result must be seen clearly enough to route the next honest move.

### Center owns

Audit grammar, finding lifecycle, evidence-ledger posture, owner routing, validation honesty, and campaign route language for center work.

### Stronger owner split

- Source repositories own the surface being audited and any owner-local remediation.
- `aoa-evals` owns proof verdicts, regression evidence, comparison gates, and quality claims.
- `aoa-memo` owns durable memory, recall objects, and memory writeback.
- `aoa-playbooks` owns recurring audit choreography and campaign routes.
- `aoa-skills` owns executable audit workflows.
- `aoa-techniques` owns reusable audit techniques.
- `aoa-stats` owns derived observability and movement summaries.
- `mechanics/release-support` owns release readiness, public-claim, and transition support.
- `abyss-stack`, `aoa-sdk`, `aoa-routing`, `aoa-kag`, `aoa-agents`, `8Dionysus`, and `Tree-of-Sophia` own their local authority surfaces.

### Inputs

- Source surface, changed diff, route claim, finding candidate, drift signal, cleanup pressure, validation result, generated report, owner request, or archived audit receipt.
- Enough context to identify the owning surface and the next honest route.

### Outputs

- Source map, evidence ledger, risk signal, finding packet, owner route, validation gate result, campaign route, or event bridge.
- No proof verdict, owner-local remediation, runtime authority, memory truth, release support, generated authority, or archive evidence as active law.

### Must not claim

- proof verdict
- owner-local remediation
- runtime authority
- memory truth
- release support authority
- generated authority
- archive evidence as active law
- private scratch notes as public audit evidence
- cleanup candidate as deletion approval

### Validation

Use the validation lane in [mechanics/audit/AGENTS.md](AGENTS.md#validation) for executable commands.

### Next route

- For proof, comparison, regression, or verdicts, route to `aoa-evals`.
- For memory writeback, route to `aoa-memo`; for recurring audit campaigns, route to `aoa-playbooks`; for executable audit workflows, route to `aoa-skills`; for reusable practice, route to `aoa-techniques`; for derived movement summaries, route to `aoa-stats`.
- For release readiness or public claims, route to `mechanics/release-support`; for fragility, pruning, and deletion candidates, route to `mechanics/antifragility`; for checkpoint evidence, route to `mechanics/checkpoint`; for owner uncertainty, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.

## Active route

- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)
- [OWNER_MAP](OWNER_MAP.md)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [PROVENANCE](PROVENANCE.md)
- [AUDIT_LAW](docs/AUDIT_LAW.md)
- [AUDIT_OWNER_REPO_REQUESTS](docs/AUDIT_OWNER_REPO_REQUESTS.md)

## Functioning parts

- [Source Map](parts/source-map/README.md)
- [Evidence Ledger](parts/evidence-ledger/README.md)
- [Risk Signal](parts/risk-signal/README.md)
- [Finding Lifecycle](parts/finding-lifecycle/README.md)
- [Owner Routing](parts/owner-routing/README.md)
- [Validation Gate](parts/validation-gate/README.md)
- [Campaign Route](parts/campaign-route/README.md)
- [Audit Event Bridge](parts/audit-event-bridge/README.md)

## Owner-request queue

Use [OWNER_REQUESTS](OWNER_REQUESTS.md) when this mechanic produces an owner-local landing request. The central queue source is [`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the compact generated companion is [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json). Generated surfaces do not author meaning.

A request packet is not owner acceptance. Keep `audit` claims center-bounded until the stronger owner lands the slice and proof routes are satisfied.

## Historical provenance

Use [PROVENANCE](PROVENANCE.md) only when auditing how older audit surfaces were distilled. Use the [legacy index](legacy/INDEX.md) only when the task needs archive accounting. The working path begins in the active route above.

## Owner boundary

Center audit grammar and route discipline for seeing source ownership, evidence, risk, finding state, validation posture, campaign shape, and next route. Proof, remediation, runtime, memory, release, generated, and source-authored authority remain owner-local.

## Growth posture

When this mechanic changes, preserve a clean active route: update the affected part, route archival accounting through `PROVENANCE.md`, keep `LANDING_LOG.md` for checked landings, and route owner-local work to stronger owners instead of expanding the center into a universal review warehouse.
