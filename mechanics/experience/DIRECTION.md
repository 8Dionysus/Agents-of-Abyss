# Experience Direction

Experience is the center mechanic for making lived work reviewable. The active package keeps a clean route: current direction, functioning parts, owner requests, landing history, and stop-lines each have a distinct job. Historical source accounting stays behind the provenance bridge.

## Active surfaces

- `README.md`: package entry card and shortest route.
- `DIRECTION.md`: current operating direction for the mechanic.
- `PARTS.md`: map of functioning Experience parts.
- `parts/`: concise active part contracts.
- `OWNER_REQUESTS.md`: center-side owner request packet.
- `LANDING_LOG.md`: canonical landing ledger.
- `ROADMAP.md`: future contour, not a historical ledger.
- `provenance-receipts.json`: receipt IDs used by active artifacts when they
  must cite older packets, seed inputs, or sibling surfaces.
- `PROVENANCE.md`: the only active bridge back to archival accounting.

## Functioning parts

- [Capture Kernel](parts/capture-kernel/README.md): the first bounded conversion of lived friction, incidents, candidates, verdict routes, memory gates, and inert projections into reviewable Experience inputs.
- [Certification Proof](parts/certification-proof/README.md): certification discipline, watchtower posture, canary gates, regression checks, drift alarms, smoke gates, and proof handoff language.
- [Adoption Federation](parts/adoption-federation/README.md): federation harvest, adoption gates, owner consent, compatibility, rollback, retention, event kinds, state machines, and owner request routing.
- [Governance Polis](parts/governance-polis/README.md): polis governance, constitution runtime boundary, council model, votes, vetoes, appeals, stays, quarantine, disputes, precedents, and authority resolver language.
- [Release Deployment](parts/release-deployment/README.md): installation, deployment, release train, rollout rings, rollback drills, first governed release, semver, and repository landing order grammar.
- [Office Operations](parts/office-operations/README.md): sovereign office posture, operator console route, assistant release invariants, role pairs, office registry, handoff graph, incident re-entry, and multi-office train language.
- [Service Mesh](parts/service-mesh/README.md): service mesh law, service operations, Agon and service release compatibility, service posture, and no-runtime dispatch boundaries.
- [Continuity Context](parts/continuity-context/README.md): context routing grammar, continuity loom, memory weaving, pattern lineage, replayable decision history, dossier governance, rank/reputation candidates, affect economy, and re-entry language.
- [Runtime Boundary](parts/runtime-boundary/README.md): living-workspace runtime boundary language, runtime authority resolver constraints, runtime case queues, kind-safe projection, and auto-rollback stop-lines.
- [Compatibility Bridges](parts/compatibility-bridges/README.md): cross-mechanic compatibility, Agon/Experience seams, ToS candidate boundaries, KAG promotion gates, cross-kind conflict routes, and bridge-only language.

## Distillation law

New waves, bridge packets, and long exploratory surfaces must not become the active route by accumulation. After a packet lands, distill the surviving function into the relevant part `README.md`, `CONTRACT.md`, or `VALIDATION.md`, then update archival accounting through `PROVENANCE.md`.

Schemas, examples, validators, and tests cite older packets or sibling surfaces
through receipt IDs from `provenance-receipts.json`; do not reintroduce direct
source paths into active part artifacts.

A functioning part should make three things clear:

- what does this part own at the center
- what stronger owner keeps operational authority
- which validation or owner route makes the claim reviewable

## Stop-lines

- Do not claim live workspace runtime from Experience center docs.
- Do not claim hidden memory sovereignty.
- Do not claim live router engine authority.
- Do not claim owner-local activation before the owner repository accepts and proves the slice.
- Do not claim operational Experience adoption, KAG/source meaning transfer, or ToS canon from center docs.
- Do not let historical packets become the primary route.

## Validation

```bash
python mechanics/experience/scripts/validate_experience_distillation.py
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
