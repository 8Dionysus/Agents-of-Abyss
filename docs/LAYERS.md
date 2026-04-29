# AoA Layers

This document defines the current and emerging conceptual layers of the AoA ecosystem.

## Practice canon

Repository: `aoa-techniques`

Purpose:
- store reusable engineering practice
- preserve contracts, risks, validation paths, and adaptation boundaries

Main question:
- what practice is genuinely reusable?

## Execution canon

Repository: `aoa-skills`

Purpose:
- package techniques into bounded agent-facing workflows
- expose trigger boundaries, procedures, contracts, risks, and verification in operational form

Main question:
- how should an agent execute bounded work?

## Proof canon

Repository: `aoa-evals`

Purpose:
- store bounded proof surfaces for behavior, quality, boundaries, regressions, and growth
- keep claims explicit, comparable, and reviewable

Main question:
- what bounded claim can we honestly support?

## Derived observability layer

Repository: `aoa-stats`

Purpose:
- derive machine-first summary surfaces from owner-local receipts and bounded eval outputs
- keep cross-repo movement legible without turning stats into authority
- publish shared stats event-envelope and bounded summary contracts for derivation

Main question:
- what movement is visible across owner-owned evidence without replacing it?

## Navigation layer

Repository: `aoa-routing`

Purpose:
- route models and humans toward the right next surface
- keep dispatch lightweight and cross-repo
- publish thin federation entry cards and ABI surfaces without becoming authority

Main question:
- where should the next step go?

## Memory layer

Repository: `aoa-memo`

Purpose:
- store memory and recall surfaces
- make retention, retrieval, and provenance legible

Main question:
- what should be remembered, and how should it return?

## Agent layer

Repository: `aoa-agents`

Purpose:
- define role contracts, personas, and handoff posture
- keep explicit who acts and under what constraints

Main question:
- who acts, and under what role contract?

## Scenario-composition layer

Repository: `aoa-playbooks`

Purpose:
- package recurring, cross-layer operational scenarios
- compose techniques, skills, roles, routing, proof, and memory posture into repeatable scenario-level methods

Main question:
- what recurring multi-layer scenario should be packaged?

## Derived knowledge substrate

Repository: `aoa-kag`

Purpose:
- transform authoritative sources into graph-ready or retrieval-ready derived structures
- preserve provenance while remaining clearly downstream of source-owned repositories
- materialize bounded federation-readiness surfaces without claiming source sovereignty

Main question:
- how should authoritative sources be lifted without replacing them?

## Infrastructure substrate

Repository: `abyss-stack`

Purpose:
- run the services, storage, orchestration, and local or hybrid substrate beneath the system

Main question:
- on what body does the system run?

## Source-first knowledge architecture counterpart

Repository: `Tree-of-Sophia`

Purpose:
- own the source-first living knowledge architecture for philosophy and world thought
- keep source-owned tiny-entry seams and authored node law inside ToS rather than downstream layers

Main question:
- what source-linked knowledge world is being cultivated?

## Center mechanics overlay

Repository: `Agents-of-Abyss`

Purpose:
- keep cross-layer mechanics legible without turning this layer map into a mechanic ledger
- route active mechanic law to `mechanics/<slug>/`
- keep mechanic legacy, receipts, generated part artifacts, and owner requests inside the owning mechanic package

Main question:
- which center mechanic shapes the work, and which owner repository must carry the next real implementation or proof?

Current route:
- `mechanics/README.md` for the full mechanics atlas
- `mechanics/registry.json` for machine-checked mechanic package metadata
- `generated/mechanic_card_index.min.json` for compact routing

## Mechanic Selection

Mechanic selection lives in:

- `mechanics/README.md` for the human atlas
- `mechanics/registry.json` for checked package metadata
- `generated/mechanic_card_index.min.json` for compact routing

After selecting a mechanic, continue through the package `README.md`,
`DIRECTION.md`, `PARTS.md`, `LANDING_LOG.md`, `PROVENANCE.md`, and
`OWNER_REQUESTS.md` when those surfaces exist.

This layer map stays at the conceptual layer boundary: it names the mechanics
overlay and routes to the atlas, while package detail stays with the owning
mechanic.
