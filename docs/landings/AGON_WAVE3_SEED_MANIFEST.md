# Agon Wave III Seed Manifest - Lawful Move Language

Moved from root `SEED_MANIFEST.md` during the root-surface cleanup pass. This is a wave receipt, not a root manifest for the entire repository.

Target repository: `Agents-of-Abyss`.

This seed lands the third Agon wave as a center-owned **pre-protocol lawful move vocabulary**.

It does not:

- open arena sessions
- create runtime packets
- define verdict logic
- write scars
- promote anything into `Tree-of-Sophia`

Wave III gives future Agon a first legal language: a compact registry of move names, classes, actor-seat eligibility, preconditions, stop-lines, and owner handoffs.

## Why this belongs in `Agents-of-Abyss`

The center owns Agon law, session lifecycle, lawful moves, contradiction ledger, terminal forms, and promotion discipline as constitutional protocol posture.

Neighboring repositories keep their own truths:

- `aoa-agents` owns actor form.
- `aoa-techniques` owns reusable practice meaning.
- `aoa-skills` owns bounded execution workflow meaning.
- `aoa-routing` owns arena entry hints and dispatch.
- `aoa-evals` owns proof and verdict surfaces.
- `aoa-memo` owns scars, delta history, and retention memory.
- `aoa-playbooks` owns repeated trial choreography.
- `Tree-of-Sophia` owns slow source-first canonization.

## Files planted

```text
docs/
  AGON_LAWFUL_MOVE_LANGUAGE.md
  AGON_MOVE_REGISTRY_MODEL.md
  AGON_MOVE_OWNER_HANDOFFS.md
  AGON_WAVE3_LANDING.md
schemas/
  agon-lawful-move.schema.json
  agon-lawful-move-registry.schema.json
config/
  agon_lawful_moves.seed.json
generated/
  agon_lawful_move_registry.min.json
scripts/
  build_agon_lawful_move_registry.py
  validate_agon_lawful_moves.py
tests/
  test_agon_lawful_moves.py
examples/
  agon_lawful_move.example.json
quests/
  AOA-Q-AGON-0010-lawful-move-language.md
  AOA-Q-AGON-0011-owner-handoff-followthrough.md
  AOA-Q-AGON-0012-technique-skill-bridge-prep.md
```

## Validation

After merging the wave into the root of `Agents-of-Abyss`:

```bash
python mechanics/agon/parts/lawful-move-grammar/scripts/build_agon_lawful_move_registry.py --check
python mechanics/agon/parts/lawful-move-grammar/scripts/validate_agon_lawful_moves.py
python -m pytest -q mechanics/agon/parts/lawful-move-grammar/tests/test_agon_lawful_moves.py
```

## Landing rule

This wave is valid only if the generated move registry stays pre-protocol. Every move must say:

```json
{
  "live_protocol": false,
  "runtime_effect": "none"
}
```

Any future patch that turns these moves into live session packets belongs to a later center-owned protocol-kernel wave and must preserve owner boundaries.
