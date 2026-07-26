# Release Leaf Command Ownership

- Decision ID: AOA-CENTER-D-0034

## Status

Accepted.

## Index Metadata

- Original date: 2026-07-26
- Surface classes: validation guard, release workflow, root script
- Center facets: release
- Mechanic parents: none
- Guard families: release/tooling, docs hygiene, generated freshness
- Posture: accepted rationale

## Context

The root release gate called both the generated-freshness and hygiene-suite
wrappers after already calling their leaf checks directly. The two wrappers
also nested: hygiene called generated freshness again. With the current stats
port check included, 61 top-level release commands expanded to 88 process
nodes, 85 leaf occurrences, and only 59 unique leaf commands.

The repeated execution was old construction scaffolding rather than additional
proof. Exact-command mutations found no distinct state or failure route
protected by rerunning those leaves.

## Options considered

1. Keep the nested wrappers in the broad release and accept repeated execution.
2. Put all hygiene leaves behind one wrapper and shorten the direct release
   list.
3. Let the broad release own each leaf command directly once while retaining
   both wrappers as standalone aggregate routes.

## Decision

The root release gate owns its 59 distinct leaf commands directly and executes
each exact command once.

`validate_hygiene_suite.py` and `validate_generated_freshness.py` remain
standalone public routes. The broad release does not invoke either wrapper.
Generated freshness groups outputs by exact builder argv and runs each group
once; different argv remain different commands, and a grouped failure names
every covered output.

## Rationale

Direct leaf ownership preserves fail-fast labels and the docs-district
requirement that its builder remain visible in the release script. Moving all
leaves behind the hygiene wrapper was tested and rejected by that owner
validator.

Keeping the standalone wrappers preserves focused and failure-aggregating
operator routes without charging their internal command graphs to every broad
release. Exact-argv grouping removes execution duplication without assuming
that two different builder invocations are equivalent.

## Consequences

- The broad release process graph contracts from 88 nodes to 59 without
  removing a distinct check.
- Standalone hygiene still runs later checks after a failure.
- One builder may protect several generated outputs, and one failure reports
  all of them.
- The direct release list remains intentionally explicit. A genuinely new leaf
  requires an owner-reviewed release edit and an updated leaf-count invariant.
- Wrapper source, registries, documentation, and public commands remain; this
  is execution contraction, not raw source-volume contraction.

## Source surfaces

- `scripts/release_gate/release_check.py`
- `scripts/hygiene/validate_generated_freshness.py`
- `scripts/hygiene/validate_hygiene_suite.py`
- `config/link_shape_hygiene.json`
- `tests/test_generated_freshness.py`

## Follow-up route

Revisit this decision when a leaf has a witnessed reason to run twice, when the
docs-district direct-builder contract changes, or when release command
authority moves to a stronger source-owned manifest without recreating wrapper
re-entry.
