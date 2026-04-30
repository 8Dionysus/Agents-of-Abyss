# Root Schema District Contract

Status: accepted
Date: 2026-04-30

## Context

Root `schemas/` had already been reduced to a small set of center-owned schema
contracts, while mechanic schemas lived under mechanic and part homes. The
remaining problem was discoverability: local guidance still carried old
mechanic-era contract lists, and there was no machine-readable registry tying
each root schema to its owner surface, generated consumer, validator, and test.

## Options considered

1. Keep `schemas/` as a tiny folder with only README/AGENTS guidance.
2. Move the remaining root schemas into generated or mechanic packages.
3. Keep root `schemas/` for root-owned contracts and add a compact registry plus
   validation.

## Decision

Root `schemas/` keeps only root-owned center schema contracts and
`schemas/registry.json`. Mechanic-owned schemas remain in their owning mechanic
or part homes. The schema registry names each root schema's owner surface,
generated consumer, validators, tests, and schema-home route globs.

## Rationale

The center needs stable shape contracts for center entry and ecosystem registry
surfaces. It does not need to warehouse mechanic schemas or manually repeat old
mechanic histories in `schemas/AGENTS.md`. A registry makes the root contract
auditable without turning `schemas/` into another index of every mechanic file.

## Consequences

- Root schema changes now have a district validator and targeted test.
- Future root schemas must be registered with their owner, consumers, and proof
  route.
- Mechanic schema growth stays local to mechanics and parts.
- `schemas/AGENTS.md` can stay short and validation-focused instead of listing
  historical contract families.

## Source surfaces

- `schemas/README.md`
- `schemas/AGENTS.md`
- `schemas/registry.json`
- `scripts/validate_schema_registry.py`
- `tests/test_schema_district.py`
- `scripts/release_check.py`

## Follow-up route

When a mechanic introduces or reorganizes schemas, update the owning mechanic
package first. Update root `schemas/registry.json` only when the root schema
contract or schema-home routing convention changes.
