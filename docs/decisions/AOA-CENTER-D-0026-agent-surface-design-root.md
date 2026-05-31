# Decision Note: Agent Surface Design Root

- Decision ID: AOA-CENTER-D-0026

## Status

Accepted.

## Index Metadata

- Original date: 2026-05-13
- Surface classes: root surface, agent lane, center doctrine
- Center facets: agent guidance, design surface
- Mechanic parents: none
- Guard families: AGENTS/mesh, center route law
- Posture: accepted rationale

## Context

AoA already had a root `AGENTS.md` route law and an AGENTS mesh protocol, but it
did not have a root design surface that named the desired form of agent-facing
guidance itself.

The candidate `DESIGN.AGENTS.md` describes the design shape of the agent-facing
layer: root and local cards, source surfaces, validators, generated companions,
closeout expectations, negative boundaries, and portability to projects that
explicitly adopt the form.

The placement question mattered because this content is stronger than a
guardrail note but weaker than executable route law. It should shape future
agent-surface work without becoming another instruction wall.

## Options considered

1. Keep the text outside the repository as local source material.
2. Place it under `docs/guardrails/` as part of the AGENTS mesh guardrail lane.
3. Merge the design language into root `AGENTS.md`.
4. Land `DESIGN.AGENTS.md` at repository root as the agent-surface design form
   and wire it to the AGENTS mesh and root-surface law.

## Decision

`DESIGN.AGENTS.md` is a root agent-lane design surface for `Agents-of-Abyss`.

It describes what kind of agent-facing form the repository preserves when
`AGENTS.md` cards, AGENTS mesh contracts, generated mesh companions, or portable
agent guidance change.

## Rationale

Root placement is justified because the file answers a durable repository-wide
design question: what shape should agent-facing guidance take so agents can act
locally without losing owner truth, evidence, reviewability, or return routes?

Keeping the surface separate from root `AGENTS.md` prevents route law from
absorbing design doctrine and becoming too large. Keeping it outside
`docs/guardrails/` prevents a prose-only design note from masquerading as a
checkable guardrail contract.

The root surface makes the design discoverable next to `DESIGN.md` while still
preserving the authority split: `AGENTS.md` routes work, local cards narrow
scope, `docs/guardrails/AGENTS_MESH_PROTOCOL.md` defines the checkable mesh
contract, `config/agents_mesh.json` registers required cards, and generated
mirrors remain derived.

## Consequences

- Agents and maintainers get a stable source for card-shape and mesh-form
  design without inflating root `AGENTS.md`.
- AGENTS mesh changes must consider whether `DESIGN.AGENTS.md` still matches the
  checkable protocol, config, validators, and generated mirror.
- `DESIGN.AGENTS.md` must not override local owner truth, source surfaces,
  validators, or generated-source boundaries.
- Public root docs now have one more root design surface, so root-surface law
  and Markdown shape validation must keep it visible and bounded.

## Source surfaces

- `DESIGN.AGENTS.md`
- `AGENTS.md`
- `DESIGN.md`
- `README.md`
- `docs/ROOT_SURFACE_LAW.md`
- `docs/guardrails/AGENTS_MESH_PROTOCOL.md`
- `docs/guardrails/AGENTS_MESH_INDEX.md`
- `config/link_shape_hygiene.json`
- `generated/link_shape_hygiene.min.json`

## Follow-up route

Revisit this decision if `DESIGN.AGENTS.md` starts duplicating root `AGENTS.md`,
weakening the AGENTS mesh protocol, or absorbing owner-local skill, technique,
eval, memory, runtime, role, playbook, routing, KAG, or ToS truth.
