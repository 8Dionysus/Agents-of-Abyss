## Summary

Describe the ecosystem-level change in a few sentences.

## Why this belongs in `Agents-of-Abyss`

Explain why this change belongs in the constitutional polis rather than in a specialized AoA repository.

## Surface changed

Mark the primary surface changed by this PR:

- [ ] charter or principles
- [ ] ecosystem map
- [ ] layer model or repository-role map
- [ ] federation rules
- [ ] root surface governance
- [ ] glossary
- [ ] questbook
- [ ] audit surface
- [ ] roadmap or direction surface
- [ ] mechanics atlas or center-level process surface
- [ ] machine-readable registry, schema, generated capsule, validator, or test
- [ ] technical district README
- [ ] contributor or entrypoint guidance
- [ ] other ecosystem-center surface

## Root placement check

If this PR adds, moves, removes, or renames a root file:

- [ ] I checked `docs/ROOT_SURFACE_LAW.md`.
- [ ] I named the root surface class.
- [ ] The file has a root-allowed role, or it was moved to a better district.
- [ ] Historical receipts, audit artifacts, registry notes, and generated files are not being promoted into root by convenience.

## Mechanic or district check

If this PR touches a center mechanic or technical district:

- [ ] I checked `docs/MECHANICS.md` for the relevant mechanic.
- [ ] I checked the local district README for `generated/`, `scripts/`, `schemas/`, `tests/`, `config/`, `examples/`, `manifests/`, or `quests/` when applicable.
- [ ] I confirmed the change does not grant live runtime authority, hidden memory sovereignty, proof authority, rank mutation, ToS canon write authority, or owner-local truth outside the proper owner repository.

## Neighboring repositories affected

List any neighboring repositories whose meaning, role description, route, or entrypoint expectations are affected:

- none

## Intentionally not included here

State what was deliberately left to specialized repositories instead of being absorbed into this one.

## Validation

Describe how you checked the change. Examples:

- read for consistency with `CHARTER.md`
- checked `ECOSYSTEM_MAP.md` and `docs/LAYERS.md` for alignment
- checked `docs/ROOT_SURFACE_LAW.md` for root placement
- checked `docs/MECHANICS.md` for mechanic routing
- checked the relevant technical district README
- ran `python scripts/validate_markdown_shape.py`
- ran `python scripts/validate_ecosystem.py`
- ran the nearest Agon, Experience, schema, generated, or release validator
- ran `python -m pytest -q tests`

## Risk / follow-ups

Name remaining ambiguity, owner-local follow-through, or a future migration path.

Prefer opening a clear next step over planting a placeholder.
