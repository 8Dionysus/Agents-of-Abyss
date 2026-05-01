# Organ Contract Center Law

Status: accepted
Date: 2026-04-30

## Context

AoA now has enough center structure to describe how sibling repositories should
meet the center without turning AoA into their implementation owner.

The repeated fork is whether this belongs only in public README language, in a
future SDK/control surface, or in a small AoA law district that route surfaces
and validators can cite before downstream repository work begins.

## Options considered

1. Leave organ alignment implicit in `CHARTER.md`, `ECOSYSTEM_MAP.md`, and
   `ROADMAP.md`.
2. Add downstream-specific instructions inside each future `aoa-*` repository
   first.
3. Plant a compact `docs/organ-contract/` district in AoA that defines the
   center law and first cycle while leaving downstream implementation local.

## Decision

AoA owns a compact `docs/organ-contract/` district as center law for AbyssOS
organ alignment.

The district defines organ contract boundaries, surface states, events, and the
first cycle. It does not own downstream implementation, runtime behavior, SDK
control panels, or owner-local proof.

## Rationale

This gives future agents a durable route before they descend into sibling
repositories. AoA can state the shared contract, route mode, validation shape,
and stop-lines once, while each downstream owner keeps its own local truth.

Making this explicit now also prevents two weaker outcomes: public README text
that sounds promising but is not validated, and downstream copies that diverge
before the center law is stable.

## Consequences

- The `organ-alignment` route mode now has a canonical center surface and schema
  coverage.
- Root docs can refer to organ alignment without absorbing sibling repository
  ownership.
- Release checks now include `scripts/validate_organ_contract.py`.
- A machine-readable organ registry remains a future trigger after real
  downstream descent proves the needed fields.

## Source surfaces

- `docs/organ-contract/README.md`
- `docs/organ-contract/ORGAN_CONTRACT.md`
- `docs/organ-contract/SURFACE_STATES.md`
- `docs/organ-contract/FIRST_CYCLE.md`
- `docs/organ-contract/EVENTS.md`
- `docs/START_HERE_ROUTE_CONTRACT.md`
- `generated/center_entry_map.min.json`
- `scripts/validate_organ_contract.py`

## Follow-up route

When the first downstream organ pass begins, use `organ-alignment` to compare
the target repository against `docs/organ-contract/FIRST_CYCLE.md`, then record
owner-local decisions in that repository. Return to AoA only for center law,
route mode, validation, or cross-organ contract changes.
