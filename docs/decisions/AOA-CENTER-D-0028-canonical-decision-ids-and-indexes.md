# Canonical Decision IDs And Indexes

- Decision ID: AOA-CENTER-D-0028

## Status

Accepted.

## Index Metadata

- Original date: 2026-05-31
- Surface classes: decision record, generated capsule, validation guard
- Center facets: decision index
- Mechanic parents: cross-mechanic
- Guard families: decision index/read-model, docs hygiene, release/tooling
- Posture: accepted rationale

## Context

`Agents-of-Abyss` already used `docs/decisions/` as the center rationale lane
for route choices, owner splits, placement law, validation authority, and public
contract decisions. The lane was still addressed by date-prefixed filenames and
a hand-maintained README table.

That shape was workable while the center held only a few decision records. It
became weaker after the center gained docs districts, mechanics, generated
capsules, AGENTS mesh validation, organ alignment, release-support routes, and
local memory-port expectations. Future agents need stable handles that survive
renames and generated lookup paths that answer which decision explains a center
surface, mechanic family, route facet, or guard family.

Sibling AoA repositories now use canonical decision IDs and generated indexes,
but the center must adapt that pattern to constitutional and federation-route
authority rather than importing skill, eval, memo, technique, or role-layer
truth.

## Options considered

1. Keep date-prefixed filenames and continue maintaining the README list by
   hand.
2. Add generated indexes while preserving date-prefixed source filenames.
3. Rename records to canonical `AOA-CENTER-D-####` IDs and generate lookup
   indexes from explicit metadata.

## Decision

Use canonical `AOA-CENTER-D-####` decision IDs and full canonical-ID filenames
as the active addresses for center decision records.

Each decision record owns an `## Index Metadata` block naming original date,
surface classes, center facets, mechanic parents, guard families, and posture.
Generated indexes under `docs/decisions/indexes/` are read models derived from
that metadata.

The center-facet index uses center-local categories such as federation contour,
release contract, growth lineage, questbook, mechanic validation, docs
guardrail, registry contract, root district, trace receipt, entry surface,
GitHub landing, organ alignment, roadmap horizon, Spark lane, design surface,
agent guidance, and decision index.

Previous date-prefixed paths are retired as live files. They remain available
through git and PR history only.

## Rationale

Stable decision IDs make cross-surface references durable when files move or
when many decisions share a date. Metadata-backed read models keep lookup cheap
without loading every crosswalk back into the README.

The generated indexes are deliberately weaker than both the decision notes and
the source surfaces they describe. They summarize center-route evidence; they
do not create sibling-owner truth, proof verdicts, memory authority, runtime
state, role contracts, or implementation promises.

## Consequences

- Decision records are now addressed as
  `docs/decisions/AOA-CENTER-D-####-*.md`.
- Generated indexes support lookup by number, date, source surface class,
  center facet, mechanic parent, and guard family.
- `scripts/generate_decision_indexes.py --check` becomes part of release
  validation.
- Live refs inside center schemas, tests, and decision records point at
  canonical decision paths.
- Old date-prefixed decision paths should not be recreated as compatibility
  aliases or lookup maps.

## Source surfaces

- `docs/decisions/`
- `docs/decisions/indexes/`
- `scripts/decision_indexes.py`
- `scripts/generate_decision_indexes.py`
- `scripts/validate_decision_records.py`
- `tests/test_decision_indexes.py`
- `tests/test_decision_records.py`
- `scripts/release_check.py`

## Follow-up route

For future decision records, start from `docs/decisions/TEMPLATE.md`, choose
the next contiguous `AOA-CENTER-D-####` ID, regenerate indexes, and run the
decision index check before closeout.
