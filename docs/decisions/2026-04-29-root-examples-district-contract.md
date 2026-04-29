# Root Examples District Contract

Status: accepted
Date: 2026-04-29

## Context

The root `examples/` district was present as a top-level technical district, but it only carried a README and local AGENTS card.
That made the path legal but thin: future contributors could either leave it as an empty door or use it as a general warehouse for mechanic examples, proof fixtures, or sibling-repository usage.

AoA already keeps mechanic examples inside mechanic packages and proof fixtures under the relevant test, schema, generated, or owner proof surfaces.
The missing decision was what the root examples district should demonstrate.

## Options considered

1. Keep `examples/` as a thin placeholder with only README and AGENTS guidance.
2. Move all examples into mechanic packages and remove the root district.
3. Keep root `examples/` as a small center-owned worked-example district for route, placement, owner-routing, and public-entry walkthroughs.

## Decision

Root `examples/` stays as a small center-owned worked-example district.
It carries public-safe examples that demonstrate how to apply center route contracts and placement rules.
Mechanic behavior examples stay in the owning mechanic package, sibling implementation examples stay in the owning repository, and proof fixtures stay with tests, schemas, generated validators, or owner proof surfaces.

## Rationale

The center benefits from at least one concrete example of how a reader or agent enters AoA, selects a route mode, checks owner boundaries, and closes with bounded verification.
Keeping that example at root makes the center route easier to learn without forcing every mechanic package to repeat entry guidance.

At the same time, the root examples district must stay light.
If it absorbs mechanic behavior, runtime usage, or proof fixtures, it weakens the owner boundaries that the mechanics topology was created to protect.

## Consequences

- Future root examples must name source surfaces, demonstrate the route or placement decision, state their boundary, and point to local validation.
- `examples/README.md` indexes root examples and explains placement.
- `examples/AGENTS.md` owns the required shape and validation route for the district.
- `tests/test_examples_district.py` prevents orphan Markdown examples and unshaped root examples.
- The tradeoff is that mechanic examples require one extra placement decision before landing, but that keeps root `examples/` readable.

## Source surfaces

- `examples/README.md`
- `examples/AGENTS.md`
- `examples/center-entry-route.md`
- `tests/test_examples_district.py`
- `docs/START_HERE_ROUTE_CONTRACT.md`
- `generated/center_entry_map.min.json`

## Follow-up route

If a future example teaches a mechanic behavior, move it to the owning mechanic package and update that package's local README or examples index.
If root examples become machine-consumed, add a schema and validator in the owning root technical districts before treating them as contract fixtures.
