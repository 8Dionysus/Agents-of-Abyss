# Experience Parts

This file is the active map of functioning Experience parts. Each part owns a real slice of the mechanic: purpose, boundary, validation, and next route. Long historical packets stay outside the working path.

## Part map

| Part | Center function | Stronger owner route |
|---|---|---|
| [Capture Kernel](parts/capture-kernel/README.md) | friction record, candidate packet, owner route, memory gate, and inert projection boundary | `aoa-memo` for memory objects, `aoa-evals` for proof, `aoa-routing` for live route behavior |
| [Certification Proof](parts/certification-proof/README.md) | certification gate, watchtower note, canary route, regression hint, and proof owner handoff | `aoa-evals` owns proof verdicts and regression evidence; center docs only name the contract and stop-lines |
| [Adoption Federation](parts/adoption-federation/README.md) | owner adoption request, consent boundary, adoption state, rollback route, and retention stop-line | target owner repositories accept or reject landing; `aoa-evals` owns adoption proof |
| [Governance Polis](parts/governance-polis/README.md) | decision table, policy registry route, appeal or stay route, precedent index hint, and constitution-runtime stop-line | `Agents-of-Abyss` owns center law; runtime enforcement and proof stay with stronger owners |
| [Release Deployment](parts/release-deployment/README.md) | release gate, installation boundary, rollout ring, rollback trigger, repo landing order, and release ritual route | `mechanics/release-support` owns shared release support; runtime deployment belongs to `abyss-stack` |
| [Office Operations](parts/office-operations/README.md) | office contour, operator stop-line, role-pair handoff, assistant invariant, and owner-local office request | `aoa-agents` owns actor and handoff posture; future owner-local offices own live behavior |
| [Service Mesh](parts/service-mesh/README.md) | service operation drill, service law stop-line, compatibility route, and runtime-owner request | `abyss-stack` owns service runtime; `aoa-routing` owns live dispatch behavior after owner gates |
| [Continuity Context](parts/continuity-context/README.md) | context route hint, continuity weave boundary, replay audit route, memory handoff, and re-entry stop-line | `aoa-memo` owns memory objects; `aoa-routing` owns live context router behavior; `aoa-evals` owns proof |
| [Runtime Boundary](parts/runtime-boundary/README.md) | runtime stop-line, authority resolver boundary, case queue handoff, projection boundary, and rollback route | `abyss-stack` owns runtime activation, services, storage, and lifecycle; center docs cannot activate runtime |
| [Compatibility Bridges](parts/compatibility-bridges/README.md) | compatibility note, bridge stop-line, cross-kind conflict route, ToS or KAG handoff, and owner split reminder | the crossed mechanic or owner repository keeps authority; Experience only records center-side compatibility constraints |

## Active part contract

Every part keeps three working surfaces:

- `README.md`: what the part is for and where to start.
- `CONTRACT.md`: owner boundary, stop-lines, and allowed outputs.
- `VALIDATION.md`: commands and tests.

A part may grow, split, merge, shrink, or retire when that improves its function and keeps the route cleaner. The move should leave the active path easier to follow, not merely smaller.

## Provenance bridge

Historical source accounting is deliberately outside part docs. Use
[PROVENANCE](PROVENANCE.md) when a task must audit where older packets landed.

## Validation

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
