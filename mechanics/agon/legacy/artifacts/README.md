# Agon Artifact Receipts

This district records the artifact move away from flat Agon technical roots.

The machine-readable receipt is [`../../artifact-map.json`](../../artifact-map.json).
It maps old `mechanics/agon/{config,generated,schemas,examples,scripts,tests}/...`
paths to active `parts/<part>/{config,generated,schemas,examples,scripts,tests}/...`
homes.

Use that map for migration evidence, link repair, and audits. Do not recreate
flat aliases or use this district as the normal working route.

## Current Rule

- Active Agon schemas, examples, config seeds, generated capsules, validators,
  and tests live beside the part that uses them.
- Package-level distillation validation remains in
  `mechanics/agon/scripts/validate_agon_distillation.py`.
- Package-level distillation tests remain in
  `mechanics/agon/tests/test_agon_distillation.py`.

## Validation

Use the validation lane in [mechanics/agon/legacy/AGENTS.md](../AGENTS.md#validation) for executable commands.
