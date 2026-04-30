# Root Tests District Contract

Status: accepted
Date: 2026-04-30

## Context

Root `tests/` had become the center regression surface for entry routes,
district registries, generated surfaces, documentation guardrails, mechanics
topology, owner request queues, and ecosystem contracts. Mechanic-owned tests
now live in mechanic packages and parts, but root tests still lacked a
machine-readable map that kept new tests attached to a visible contract family.

## Options considered

1. Keep `tests/README.md` and `tests/AGENTS.md` as prose-only guidance.
2. Move root tests into each district directory.
3. Keep root tests for root-owned center contracts and add a registry-backed
   tests district contract.

## Decision

Root `tests/` keeps root-owned center tests and is governed by
`tests/registry.json`. Mechanic-owned tests stay in their owning mechanic or
part. The tests district validator checks that every root test file is
registered in exactly one family and that mechanic test-home routes stay
visible.

## Rationale

Root tests still provide the shortest reliable proof path for release-facing
center contracts. Moving them into every source district would scatter the
release proof surface, while prose-only guidance would let orphan tests grow
quietly. A family registry keeps the test surface legible without turning test
assertions into source authority.

## Consequences

- New root test files must be registered before they are relied on.
- `release_check.py` now runs the tests district validator.
- `tests/README.md` and `tests/AGENTS.md` can stay compact and route-led.
- The registry names test families, not detailed proof semantics.
- Mechanic-local tests remain in `mechanics/<slug>/.../tests/`.

## Source surfaces

- `tests/README.md`
- `tests/AGENTS.md`
- `tests/registry.json`
- `scripts/validate_tests_district.py`
- `tests/test_tests_district.py`
- `scripts/release_check.py`

## Follow-up route

When a root test becomes mechanic-specific, move it to the owning mechanic or
part and update `tests/registry.json`. When a new root test family appears,
add it to the registry before relying on it from `release_check.py`.
