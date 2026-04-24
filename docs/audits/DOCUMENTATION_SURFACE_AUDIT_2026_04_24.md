# Documentation Surface Audit - 2026-04-24

This audit records the second documentation-order pass after the root-surface rebuild.

It is an audit artifact, not constitutional law. Canonical placement law lives in `docs/ROOT_SURFACE_LAW.md`. Mechanic routing lives in `docs/MECHANICS.md`.

## Method

The pass read the repository from the top down and then back up from the lower districts:

1. Start at root identity and civic surfaces.
2. Check the center claim verification path.
3. Inspect docs entrypoints and mechanics routing.
4. Inspect audit, registry, and landing districts.
5. Inspect lower technical districts: `generated/`, `scripts/`, `schemas/`, `tests/`, `config/`, `examples/`, `manifests/`, and `quests/`.
6. Return to root and decide what must be reformatted, moved, deleted, narrowed, or given a local gate.

## Findings

| Finding | Severity | Decision |
|---|---|---|
| Key Markdown surfaces were semantically stronger but collapsed into long lines. | P0 | Re-copy formatted Markdown files and add `scripts/validate_markdown_shape.py`. |
| Root cleanup was planted but old root copies still remained. | P0 | Remove root `SEED_MANIFEST.md`, `registry-v2-notes.md`, `DELETION_CANDIDATES.json`, and lowercase duplicate PR template after preserving or verifying their better homes. |
| `CONTRIBUTING.md` still spoke in the older "ecosystem-center" voice. | P1 | Rewrite it around constitutional polis, root surface law, mechanics atlas, district gates, and owner split. |
| `GLOSSARY.md` lacked new stable vocabulary for polis, root surfaces, civic indexes, districts, landing receipts, audit artifacts, supporting consumers, and mechanics. | P1 | Synchronize vocabulary without turning the glossary into a new mechanics atlas. |
| Technical districts had many machine-facing files but no local gates. | P1 | Add durable local README files for technical districts. |
| Future deeper docs migration remains too risky for a casual sweep. | P2 | Leave a clear next step in `docs/ROOT_SURFACE_LAW.md` instead of moving Agon/Experience docs blindly. |

## Package actions

The v4 documentation-order package performs these actions:

- reformat and update root civic surfaces
- reformat and update `docs/README.md`, `docs/MECHANICS.md`, and `docs/ROOT_SURFACE_LAW.md`
- update `CONTRIBUTING.md`, `GLOSSARY.md`, and `.github/PULL_REQUEST_TEMPLATE.md`
- add a Markdown shape validator
- add local README gates for root-adjacent technical districts
- remove root leak artifacts after their better homes exist
- remove duplicate lowercase PR template
- leave deeper thematic migration as a future deliberate pass

## Non-goals

This pass does not:

- restructure all Agon documents into a new `docs/agon/` district
- restructure all Experience documents into a new `docs/experience/` district
- rewrite generated registry semantics
- grant live runtime authority
- change owner-local truth in sibling repositories
- alter the parallel AGENTS front

## Follow-up path

After this package lands and validates, the next deep documentation pass should decide whether `docs/` needs thematic subdistricts for Agon, Experience, ToS support, and recurrence.

That pass must be link-aware and validator-aware. It should not move files merely because the directory looks crowded.
