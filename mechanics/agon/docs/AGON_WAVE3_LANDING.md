# Agon Wave III Landing

## Name

Wave III: Lawful Move Language

## Repository

`Agents-of-Abyss`

## Landing statement

Wave III plants the first center-owned move vocabulary for future Agon sessions.

The wave is landed when:

- `config/agon_lawful_moves.seed.json` exists;
- `generated/agon_lawful_move_registry.min.json` is generated from it;
- every move is explicitly pre-protocol;
- every move has owner handoffs;
- no move claims runtime, verdict, scar, retention, or ToS authority;
- validation passes.

## Commands

```bash
python scripts/build_agon_lawful_move_registry.py --check
python scripts/validate_agon_lawful_moves.py
python -m pytest -q tests/test_agon_lawful_moves.py
```

## Required previous surfaces

The validator expects the center to have at least:

```text
README.md
CHARTER.md
docs/LAYERS.md
mechanics/agon/docs/AGON_PREPARATION_POSTURE.md
```

If Wave 0 was already planted, it should also have:

```text
mechanics/agon/docs/AGON_IMPOSITION_POSTURE.md
generated/agon_imposition_readiness.min.json
```

The validator treats Wave 0 surfaces as strengthening context, not as a blocker for this seed's internal shape. Owner policy may make them required in a later release gate.

## What Wave III enables

Wave III enables later work to ask sharper questions:

- which moves deserve reusable technique canon?
- which moves deserve bounded skills?
- which moves require eval proof?
- which moves need routing gates?
- which moves belong inside early mechanical playbooks?
- which moves require center-owned arena law in the protocol kernel?

## What Wave III does not enable

It does not enable:

- live arena sessions;
- sealed commits;
- session packets;
- contradiction ledger entries;
- verdicts;
- scars;
- retention scheduling;
- runtime services.

## Next wave after this

The natural next wave is not “full arena”.

The next wave should be one of these, depending on owner readiness:

1. `aoa-techniques` and `aoa-skills` bridge for lawful move practice/execution candidates;
2. `aoa-routing` gate preparation for `agon_needed`;
3. center-owned narrow duel kernel.

The cleanest route is usually:

```text
move vocabulary -> technique/skill bridges -> routing gate -> duel kernel
```

Do not let eagerness skip the bridge.
