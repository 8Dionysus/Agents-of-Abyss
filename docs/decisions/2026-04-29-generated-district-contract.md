# Generated District Contract

Status: accepted
Date: 2026-04-29

## Context

The root `generated/` district already carried compact machine-readable center surfaces, generated guardrail indexes, registry summaries, and Questbook read models.
Its README was thin, and its AGENTS card mixed root generated guidance with mechanic part-local Agon generated capsules.

That made the district harder to scale: future contributors could confuse root-published read models, mechanic-local generated companions, and manual registry summaries.

## Options considered

1. Leave the district as-is and rely on individual validators.
2. Move all mechanic-built generated views out of root `generated/`.
3. Keep root `generated/` as the publication district, but classify every root JSON by owner/source, builder, validator, and edit posture.

## Decision

Root `generated/` is the publication district for root-published compact mirrors and indexes.
It now distinguishes root-built surfaces, manual published summaries, and mechanic-built root-published read models.

Questbook read models stay in root `generated/` because they summarize the root `quests/` source store and public Questbook index, while their builder and owner route remain in `mechanics/questbook/`.
Mechanic part-local generated capsules stay under the owning mechanic package.

## Rationale

This preserves stable public paths for low-context agents and root entry surfaces without turning root `generated/` into a mechanic warehouse.
The generated district stays useful as a compact publication layer, and ownership remains visible through source refs, builders, validators, and local AGENTS routes.

## Consequences

- `generated/README.md` indexes every root JSON surface and names its class, source, builder, and validator.
- `generated/AGENTS.md` keeps root generated law concise and routes mechanic-local generated work back to mechanics.
- `tests/test_generated_district.py` rejects orphan root generated JSON and part-local generated drift in root AGENTS guidance.
- The tradeoff is that Questbook read models remain physically root-published, so their mechanic ownership must stay explicit in docs and validators.

## Source surfaces

- `generated/README.md`
- `generated/AGENTS.md`
- `generated/*.json`
- `mechanics/questbook/AGENTS.md`
- `mechanics/questbook/scripts/build_questbook_index.py`
- `config/link_shape_hygiene.json`
- `tests/test_generated_district.py`

## Follow-up route

If a future generated surface becomes machine-consumed as a stronger contract, add or update the owning schema, builder, validator, and source surface in the same change.
If Questbook generated paths move later, update `QUESTBOOK.md`, `quests/README.md`, Questbook builders, freshness config, and generated district tests together.
