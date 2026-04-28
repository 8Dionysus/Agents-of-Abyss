# ADR: Docs Guardrails and Mechanic Receipts

Date: 2026-04-28

## Status

Accepted

## Context

`docs/` had begun carrying three different kinds of material in one flat neighborhood:

- current center doctrine and route maps;
- validation and cleanup guardrails;
- mechanic-specific historical receipts and empty compatibility districts.

That made the docs surface harder for agents to read. It also created weak doors such as `docs/agon/`, `docs/experience/`, `docs/legacy/`, and `docs/landings/` after active mechanics had already moved to `mechanics/<slug>/`.

## Decision

Create `docs/guardrails/` as the home for docs cleanup, hygiene, generated freshness, and AGENTS mesh guardrail law.

Remove empty mechanic and legacy docs districts. Mechanic-specific receipts move to the owning mechanic legacy route, starting with the Agon Wave III seed manifest under `mechanics/agon/legacy/raw/`.

Keep `docs/README.md` as a route map and keep validation command lanes in `AGENTS.md` surfaces.

Do not keep a generic `docs/postmortems/` shelf for one owner-bound release
retrospective. Release repair learning belongs under the release-support
mechanic legacy/provenance route unless it is center-generic audit evidence.

Do not keep a generic `docs/agent-lane/` shelf for a preserved root
`AGENTS.md` snapshot. Active agent rules must live in root or nearest owner
`AGENTS.md`, a validator, a mechanic package, or the audit protocol.

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
