# Root Scripts Family Topology

- Decision ID: AOA-CENTER-D-0029

## Status

Accepted.

## Index Metadata

- Original date: 2026-06-03
- Surface classes: root district, validation guard, root surface
- Center facets: root district
- Mechanic parents: none
- Guard families: release/tooling, docs hygiene
- Posture: accepted rationale

## Context

`AOA-CENTER-D-0022` kept root `scripts/*.py` as a flat, registry-backed
release-facing seam. That was useful while the center needed a compact map of
root-owned validators, builders, release checks, and helper modules.

The district then grew to dozens of root Python files. The registry still named
families, but the filesystem no longer showed them. Agents had to read JSON
before seeing whether a script belonged to center entry, docs districts,
hygiene, AGENTS mesh, mechanics topology, owner requests, root registries,
organ contract, or release gate. Shared helper modules and CLI entrypoints also
sat in the same flat namespace.

## Options considered

1. Keep the D-0022 shape and rely on `scripts/registry.json` only.
2. Keep root compatibility wrappers and move implementations under family
   directories.
3. Move root-owned Python files into family directories, remove root-level
   command aliases, and teach the registry validator to enforce the new shape.

## Decision

Move root-owned center Python tooling from `scripts/*.py` to
`scripts/<family>/*.py`.

The family directories are:

- `scripts/agents_mesh/`
- `scripts/center_entry/`
- `scripts/docs_districts/`
- `scripts/hygiene/`
- `scripts/mechanics_topology/`
- `scripts/organ_contract/`
- `scripts/owner_requests/`
- `scripts/release_gate/`
- `scripts/root_registries/`

`scripts/registry.json` now records each `family_dir`. The scripts district
validator rejects root-level Python command files, discovers family-scoped
Python files, and requires every discovered family file to be registered in
exactly one family.

Root `scripts/` remains the top-level technical district, but it is no longer a
flat Python command home.

## Rationale

The center still needs a visible release-facing tooling district, but it should
not require agents to mentally reconstruct a tree from a JSON registry before
they can act. A family topology makes the owner lane visible in the path name
while preserving the registry-backed proof that no root script appears
unowned.

Leaving root wrappers would preserve old commands but would keep two command
surfaces alive. That would make future route-law weaker: an agent could follow
the wrapper instead of the owner family. Removing the wrappers makes the new
topology real.

## Consequences

- Root-owned script commands now use paths such as
  `python scripts/hygiene/validate_links.py`.
- `python scripts/release_check.py` is replaced by
  `python scripts/release_gate/release_check.py`.
- Root-level `scripts/*.py` command files are invalid, except package markers.
- Generated route capsules, validation baselines, tests, and registries must
  reference the family-scoped paths.
- Historical legacy receipts may preserve old command text when they describe a
  past landing rather than a current route.

## Source surfaces

- `scripts/README.md`
- `scripts/AGENTS.md`
- `scripts/registry.json`
- `scripts/root_registries/validate_scripts_district.py`
- `tests/test_scripts_district.py`
- `scripts/release_gate/release_check.py`
- `docs/guardrails/ENTRY_SURFACE_VALIDATION_BASELINE.md`
- `generated/center_entry_map.min.json`

## Follow-up route

When a root script becomes mechanic-specific, move it to the owning mechanic or
part and update `scripts/registry.json`. When a new root script family appears,
create a named family directory, add the family to `scripts/registry.json`, and
wire the nearest validator before relying on it from the release gate.
