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

## Active mechanic packages

| Mechanic | Use when | Route |
|---|---|---|
| method-growth | repeated patterns need reviewable growth, lineage, method capture, or pruning | `mechanics/method-growth/README.md` |
| distillation | raw packets, waves, or legacy material must become light active form | `mechanics/distillation/README.md` |
| growth-cycle | harvest, progression, self-diagnosis, or repair loops need bounded routing | `mechanics/growth-cycle/README.md` |
| recurrence | return, continuity, re-entry, or durable boundedness is at stake | `mechanics/recurrence/README.md` |
| checkpoint | an intermediate state must be captured without becoming final authority | `mechanics/checkpoint/README.md` |
| experience | staged contracts, office/service posture, continuity, and runtime boundaries are involved | `mechanics/experience/README.md` |
| agon | pressure, lawful move language, arena readiness, verdict contour, owner binding, or trial handoff is involved | `mechanics/agon/README.md` |
| antifragility | subtraction, degraded mode, via negativa, or authority inflation must be checked | `mechanics/antifragility/README.md` |
| questbook | obligations should survive as public, reviewable game objects rather than TODO noise | `mechanics/questbook/README.md` |
| rpg | game-language overlay helps route quests, progression, proof, and handoff without becoming a toy layer | `mechanics/rpg/README.md` |
| boundary-bridge | cross-owner transition needs support without ownership collapse | `mechanics/boundary-bridge/README.md` |
| release-support | public claims, internal releases, and transition proof need one support route | `mechanics/release-support/README.md` |

Mechanic detail belongs in package `DIRECTION.md`, `PARTS.md`, `LANDING_LOG.md`, `PROVENANCE.md`, and `OWNER_REQUESTS.md`, not in this layer map.
