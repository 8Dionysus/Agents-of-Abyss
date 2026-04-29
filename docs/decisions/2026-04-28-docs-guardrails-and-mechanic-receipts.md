# ADR: Docs Guardrails and Mechanic Receipts

Status: accepted
Date: 2026-04-28

## Context

`docs/` had begun carrying three different kinds of material in one flat neighborhood:

- current center doctrine and route maps;
- validation and cleanup guardrails;
- mechanic-specific historical receipts and empty compatibility districts.

That made the docs surface harder for agents to read. It also created weak doors such as `docs/agon/`, `docs/experience/`, `docs/legacy/`, and `docs/landings/` after active mechanics had already moved to `mechanics/<slug>/`.

## Options considered

1. Keep flat `docs/` districts and rely on reader discipline.
2. Move guardrail law into `docs/guardrails/` and route mechanic receipts to
   owning mechanic legacy/provenance surfaces.
3. Move all docs cleanup evidence into one generic archive.

## Decision

Create `docs/guardrails/` as the home for docs cleanup, hygiene, generated freshness, and AGENTS mesh guardrail law.

Remove empty mechanic and legacy docs districts. Mechanic-specific receipts move to the owning mechanic legacy route, starting with the Agon Wave III seed manifest under `mechanics/agon/legacy/raw/`.

Keep `docs/README.md` as a route map and keep validation command lanes in `AGENTS.md` surfaces.

Do not keep a generic `docs/postmortems/` shelf for one owner-bound release
retrospective. Release repair learning belongs under the release-support
mechanic legacy/provenance route unless it belongs in the Audit mechanic.

Do not keep a generic `docs/agent-lane/` shelf for a preserved root
`AGENTS.md` snapshot. Active agent rules must live in root or nearest owner
`AGENTS.md`, a validator, or a mechanic package.

## Rationale

The docs root is safest when it behaves like a route map and law surface rather
than a storage shelf. Guardrails are still center-owned, but they need their own
district because they govern placement, hygiene, and generated freshness across
many docs surfaces.

Mechanic receipts stay more useful when they live near the mechanic that can
distill or act on them. That keeps historical evidence reachable without making
flat docs directories look like active authority.

## Consequences

- `docs/` root stays focused on current center doctrine and route law.
- Guardrail source files are grouped with their classifier and local AGENTS card.
- Mechanics do not gain duplicate docs-root legacy doors.
- Release-support retrospectives stay close to the mechanic that can act on
  them.
- The old root-agent reference cache is removed after its surviving boundary,
  review, and Agon validation rules are promoted into active owner surfaces.
- Historical audit documents may keep old path references as evidence, but active configs, validators, generated mirrors, and maps must use the new homes.
- Future mechanic receipts should land under `mechanics/<slug>/legacy/` with provenance, not under generic docs receipt folders.

## Source surfaces

- `docs/guardrails/`
- `docs/README.md`
- `docs/ROOT_SURFACE_LAW.md`
- `mechanics/<slug>/legacy/`
- `mechanics/<slug>/PROVENANCE.md`
- `mechanics/audit/`

## Follow-up route

Route future docs placement disputes through `docs/ROOT_SURFACE_LAW.md`,
`docs/guardrails/`, and owner mechanic provenance before creating new docs
districts.
