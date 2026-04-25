# Experience Parts

This file is the active map of functioning Experience parts. It replaces the old pattern where many long `EXPERIENCE_*` files in `docs/` acted as the default route.

## Part map

| Part | Center function | Stronger owner route | Raw source families |
|---|---|---|---|
| [Capture Kernel](parts/capture-kernel/README.md) | friction record, candidate packet, owner route, memory gate, and inert projection boundary | `aoa-memo` for memory objects, `aoa-evals` for proof, `aoa-routing` for live route behavior | Wave 1, live session bootstrap, golden cases, cross-repo harvest, downflow, harvest, and first friction surfaces |
| [Certification Proof](parts/certification-proof/README.md) | certification gate, watchtower note, canary route, regression hint, and proof owner handoff | `aoa-evals` owns proof verdicts and regression evidence; center docs only name the contract and stop-lines | Wave 2, certification authority, watchtower authority, canary watch, regression forge, smoke gates, drift alarms, and golden cases |
| [Adoption Federation](parts/adoption-federation/README.md) | owner adoption request, consent boundary, adoption state, rollback route, and retention stop-line | target owner repositories accept or reject landing; `aoa-evals` owns adoption proof | Wave 3, adoption law, federation law, owner consent, rollback, retention, and owner request packet surfaces |
| [Governance Polis](parts/governance-polis/README.md) | decision table, policy registry route, appeal or stay route, precedent index hint, and constitution-runtime stop-line | `Agents-of-Abyss` owns center law; runtime enforcement and proof stay with stronger owners | Wave 4, polis governance, constitution runtime, council, vote, veto, appeal, stay, quarantine, conflict, policy, and precedent files |
| [Release Deployment](parts/release-deployment/README.md) | release gate, installation boundary, rollout ring, rollback trigger, repo landing order, and release ritual route | `mechanics/release-support` owns shared release support; runtime deployment belongs to `abyss-stack` | deployment, installation, release, rollout, rollback, semver, first-release, train, and repo landing order surfaces |
| [Office Operations](parts/office-operations/README.md) | office contour, operator stop-line, role-pair handoff, assistant invariant, and owner-local office request | `aoa-agents` owns actor and handoff posture; future owner-local offices own live behavior | Wave 5, sovereign office, operator, assistant, office registry, handoff graph, multi-office, release train, and sovereign ritual surfaces |
| [Service Mesh](parts/service-mesh/README.md) | service operation drill, service law stop-line, compatibility route, and runtime-owner request | `abyss-stack` owns service runtime; `aoa-routing` owns live dispatch behavior after owner gates | v1.2 service mesh operations, service mesh law, Agon service seams, and service release compatibility |
| [Continuity Context](parts/continuity-context/README.md) | context route hint, continuity weave boundary, replay audit route, memory handoff, and re-entry stop-line | `aoa-memo` owns memory objects; `aoa-routing` owns live context router behavior; `aoa-evals` owns proof | v1.6-v1.9, context routing, memory weaving, replay, canonical dossier, pattern lineage, rank, reputation, affect, and continuity files |
| [Runtime Boundary](parts/runtime-boundary/README.md) | runtime stop-line, authority resolver boundary, case queue handoff, projection boundary, and rollback route | `abyss-stack` owns runtime activation, services, storage, and lifecycle; center docs cannot activate runtime | v2.0 living workspace, runtime authority boundary, runtime queues, authority resolver, kind-safe projection, and auto-rollback policy |
| [Compatibility Bridges](parts/compatibility-bridges/README.md) | compatibility note, bridge stop-line, cross-kind conflict route, ToS or KAG handoff, and owner split reminder | the crossed mechanic or owner repository keeps authority; Experience only records center-side compatibility constraints | Agon compatibility, ToS boundaries, KAG promotion, cross-kind conflicts, migration bridge, and support compatibility surfaces |

## Active part contract

Every part keeps three small surfaces:

- `README.md`: what the part is for and where to start.
- `CONTRACT.md`: owner boundary, stop-lines, and allowed outputs.
- `VALIDATION.md`: commands, tests, and legacy provenance routes.

## Raw source posture

Raw wave and version files are preserved in `legacy/raw/`. They are evidence and provenance, not the primary active route. If a raw file changes the active mechanic, update the relevant part and then update `legacy/INDEX.md` or `legacy/DISTILLATION_LOG.md`.

## Validation

```bash
python scripts/validate_experience_distillation.py
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
