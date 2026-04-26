# Experience Mechanic

Experience is a center mechanic package in `Agents-of-Abyss`. It turns lived work, friction, offices, service posture, and continuity pressure into reviewable contracts without taking operational truth from stronger owner repositories.

## Mechanic card

- Status: `planted`

### Trigger

Use when lived work, friction, releases, offices, incidents, service posture, seed intake, duel pressure, continuity loom, or living-workspace boundaries must become reviewable contracts.

### Center owns

Experience center contracts, release posture, stop-lines, adoption route language, and owner-routing grammar.

### Stronger owner split

- `abyss-stack` owns runtime activation and workspace infrastructure.
- `aoa-memo` owns memory objects, recall, and provenance.
- `aoa-routing` owns live routing behavior and context router implementation.
- `aoa-evals` owns adoption proof, certification checks, and regression evidence.
- `aoa-agents` owns actor, office, role, and handoff posture.
- `aoa-playbooks` owns recurring adoption, release, office, and service choreography.
- `aoa-sdk` owns typed helper and compatibility API surfaces.
- `aoa-stats` owns derived observability and movement summaries.
- `aoa-skills` owns executable workflow skill truth.
- `aoa-techniques` owns reusable practice and technique truth.
- `Tree-of-Sophia` owns ToS-authored meaning and canon.
- Future owner-local repositories own live office and workspace behavior.

### Inputs

- Friction record, release experience, incident, adoption request, office/service contour, duel pressure, or continuity claim.
- A source surface that can be turned into a bounded contract without declaring live runtime authority.

### Outputs

- Reviewable contract, owner adoption request, stop-line, proof route, memory route, or inert projection.
- No live workspace runtime until the stronger owner lands and validates it.

### Must not claim

- live workspace runtime or service dispatch
- hidden memory sovereignty or recall authority
- live router engine authority
- owner-local activation, office installation, or adoption
- proof verdicts, certification truth, or regression evidence before `aoa-evals` lands them
- recurring choreography, helper availability, derived-summary proof, executable skill truth, or reusable technique truth
- `aoa-kag` projections as source-authored meaning
- ToS-authored meaning or canon

### Validation

```bash
python mechanics/experience/scripts/validate_experience_distillation.py
python scripts/validate_mechanic_artifact_topology.py --mechanic experience
python scripts/validate_mechanic_landing_logs.py --mechanic experience
python scripts/validate_mechanics_topology.py --mechanic experience
python scripts/validate_mechanic_readme_cards.py --mechanic experience
python scripts/build_mechanic_card_index.py --check
python scripts/validate_mechanic_card_index.py
python scripts/validate_owner_request_queue.py --mechanic experience
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic experience
```

### Next route

- For runtime or live workspace activation, route to `abyss-stack` and the relevant owner-local gate.
- For memory, route to `aoa-memo`; for adoption proof, route to `aoa-evals`; for recurring choreography, route to `aoa-playbooks`; for helper surfaces, route to `aoa-sdk`; for derived summaries, route to `aoa-stats`; for unclear owner, return to `docs/FEDERATION_RULES.md` and `docs/REPO_ROLES.md`.

## Active route

- [DIRECTION](DIRECTION.md)
- [PARTS](PARTS.md)
- [LANDING_LOG](LANDING_LOG.md)
- [ROADMAP](ROADMAP.md)
- [OWNER_REQUESTS](OWNER_REQUESTS.md)
- [artifact-map](artifact-map.json)
- [provenance-receipts](provenance-receipts.json)
- [PROVENANCE](PROVENANCE.md)

## Functioning parts

- [Capture Kernel](parts/capture-kernel/README.md)
- [Certification Proof](parts/certification-proof/README.md)
- [Adoption Federation](parts/adoption-federation/README.md)
- [Governance Polis](parts/governance-polis/README.md)
- [Release Deployment](parts/release-deployment/README.md)
- [Office Operations](parts/office-operations/README.md)
- [Service Mesh](parts/service-mesh/README.md)
- [Continuity Context](parts/continuity-context/README.md)
- [Runtime Boundary](parts/runtime-boundary/README.md)
- [Compatibility Bridges](parts/compatibility-bridges/README.md)

## Owner-request queue

Use [OWNER_REQUESTS](OWNER_REQUESTS.md) when this mechanic produces an owner-local landing request. The central queue source is [`mechanics/owner-request-queue.json`](../owner-request-queue.json), and the compact generated companion is [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json). Generated surfaces do not author meaning.

A request packet is not owner acceptance. Keep `experience` claims center-bounded until the stronger owner lands the slice and proof routes are satisfied.

## Historical provenance

Use [PROVENANCE](PROVENANCE.md) only when auditing how archived source packets
were distilled. Active artifacts name older sources through
[provenance-receipts](provenance-receipts.json), so the user route stays on the
part map above.

## Owner boundary

Center contracts and stop-lines for capture, certification, adoption,
governance, office, service, continuity, compatibility, and runtime-boundary
contours; live workspace, offices, runtime, routing, proof, KAG, memory,
playbooks, SDK helpers, stats summaries, skills, techniques, and ToS authority
remain owner-local.

## Growth posture

When this mechanic changes, preserve a clean active route: update the relevant functioning part, remove duplicate or stale paths, preserve landing history in `LANDING_LOG.md`, keep historical accounting behind `PROVENANCE.md`, and route proof, memory, runtime, actor, KAG, and ToS claims to their stronger owners.
