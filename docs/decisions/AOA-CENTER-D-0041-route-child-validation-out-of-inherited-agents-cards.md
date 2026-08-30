# Route Child Validation Out of Inherited AGENTS Cards

- Decision ID: AOA-CENTER-D-0041

## Status

Accepted.

## Index Metadata

- Original date: 2026-08-30
- Surface classes: agent lane, validation guard, mechanic package, decision record
- Center facets: agent guidance, mechanic validation
- Mechanic parents: cross-mechanic
- Guard families: AGENTS/mesh, mechanic topology, link/shape hygiene
- Posture: accepted routed validation law; commands remain owner-local and do not imply proof or acceptance

## Context

Mechanic child documents route executable checks away from `README.md` and
`VALIDATION.md`, but the resulting command matrices were copied into twenty
inherited `AGENTS.md` cards. On the current source tree those blocks described
64 entries for 63 unique child surfaces and 405 commands. They pushed five
unique inherited AGENTS chains, covering 27 registered scopes, above the
32-KiB low-context budget; the largest chain was 40,883 bytes.

The commands are useful owner-local procedure. Their repetition inside every
descendant prompt is not useful authority. One route was duplicated between a
package card and its nearer docs card, and the RPG owner-request route was
described under a docs card that did not own the target surface.

## Options considered

1. Keep the full child command matrices inside inherited `AGENTS.md` cards.
2. Move the command blocks back into each child `README.md` or `VALIDATION.md`.
3. Keep concise executable entrypoints in the nearest `AGENTS.md`, move exact
   child command argv into one validated mechanics manifest, and expose a
   no-shell runner for exact surface lookup and execution.

## Decision

Choose option 3.

`mechanics/validation-routes.json` is the source manifest for exact
child-surface command routes. The nearest owner card retains local boundaries,
the package-level validation lane, and a compact route to
`scripts/mechanics_topology/run_validation_route.py`. The runner requires one
exact repository-relative surface, supports inspection without execution, and
passes argv directly to subprocesses without a shell.

The manifest validator must reject missing surfaces, missing command files,
unsafe repository refs, empty argv, non-Python entrypoints, non-nearest owner
cards, stale legacy block markers, and owner cards that do not point back to
the manifest.

The AGENTS mesh source config owns a 32-KiB inherited-chain budget. Its
validator and generated read model must expose and reject over-budget
registered chains. This budget is a navigation and context guard, not a claim
that shorter guidance is semantically better by itself.

## Rationale

Option 3 preserves the original separation between human entry maps and
executable procedure without forcing all procedure into prompt-visible cards.
It also makes each command route addressable, machine-checkable, and safe to
inspect before execution. Nearest-card validation removes ambiguous ownership,
while the chain budget prevents the same form of prompt inflation from
silently returning.

## Consequences

- Child `README.md` and `VALIDATION.md` files remain concise route surfaces.
- `AGENTS.md` retains role, boundaries, local checks, and one route into exact
  child procedure instead of inheriting hundreds of unrelated commands.
- All migrated command argv remain explicit in an authored, reviewed manifest.
- A green routed command proves only its declared check; it does not prove
  runtime state, proof strength, release readiness, or owner acceptance.
- Adding or moving a route now requires manifest validation and nearest-card
  review.
- The remaining cost is one additional lookup when a child-specific command
  set is actually needed.

## Source surfaces

- `DESIGN.AGENTS.md`
- `AGENTS.md`
- `mechanics/AGENTS.md`
- `mechanics/README.md`
- `mechanics/validation-routes.json`
- `docs/guardrails/AGENTS_MESH_PROTOCOL.md`
- `config/agents_mesh.json`

## Follow-up route

Use `scripts/mechanics_topology/validate_validation_routes.py` for route
integrity and the AGENTS mesh validators for inherited-chain pressure. Future
owners should add a route only for a real child-specific procedure and should
keep broadly applicable package checks in the nearest package card. The
cross-repository README/AGENTS corpus ledger remains the integration surface
for comparing this owner-local result with other AbyssOS repositories.
