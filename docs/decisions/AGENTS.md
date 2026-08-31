# AGENTS.md

## Applies to

This card applies to `docs/decisions/` and all descendants unless a nearer `AGENTS.md` narrows the path.

## Role

`docs/decisions/` holds decision records and placement rationales for reviewable choices.

## Read before editing

Select only the source, contract, or owner route that can change the interpretation of the named task.
A nearby human README is on-demand: use it when its explanation, package map, provenance, compatibility, or usage contract is material to the task.
Exact executable checks belong to the applicable `VALIDATION.md`, validated manifest, runner, or stronger owner procedure surface.
## Boundaries

- Do not treat this district as stronger than its source surfaces.
- A decision record should explain a choice, not duplicate every downstream source.
- Keep provenance, dates, and source relationships explicit.
- Route current mechanic doctrine to `mechanics/<slug>/` packages when a package owns the material.
- Route owner-local truth to the owner repository instead of expanding the center.
- Keep `modeled_surfaces` in `docs/decisions/indexes/index_contract.yaml` as a top-level list of normalized repo-relative paths under `docs/decisions/`; do not use it for root non-record Markdown.

## Decision Review Gate

Run this review after meaningful structural, ownership, workflow, route-law,
validator-authority, public-contract, or topology changes.

Record a decision when:

- several plausible paths existed and the rationale will matter later
- future agents may repeat the same debate without a durable "why"
- a source-of-truth boundary, owner route, package topology, validator authority,
  or public contract changed
- a repo-wide convention changed how future work should be closed out

Do not record a decision when the change is tiny, self-evident, purely local, or
already explained by a more specific active source surface. In that case,
closeout should say `Decision review: no record needed` with a short reason.

Decision records must follow [TEMPLATE](TEMPLATE.md). Active records use
canonical `AOA-CENTER-D-####` IDs and full canonical-ID filenames. They explain
why; current source surfaces define what.

## Validation

Use docs and hygiene guardrails:

If thematic district indexes or migration maps changed, run their matching builders and validators too.

## Closeout

Report what moved or changed, whether the file is current law, receipt, trace, audit evidence, or legacy route, and which links or generated mirrors were checked.
