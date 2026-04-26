# Experience Artifact Receipts

This district records the artifact move away from flat Experience roots.

The machine-readable receipt is [`../../artifact-map.json`](../../artifact-map.json).
It maps old `mechanics/experience/{schemas,examples,scripts,tests}/...` paths to
the active `parts/<part>/{schemas,examples,scripts,tests}/...` homes.

Use that map for migration evidence, link repair, and audits. Do not recreate
flat aliases or use this district as the normal working route.

## Current Rule

- Active schemas and examples live beside the part that uses them.
- Active part validators and tests live beside that part.
- Package-level distillation validation remains in
  `mechanics/experience/scripts/validate_experience_distillation.py`.
- Package-level distillation tests remain in
  `mechanics/experience/tests/test_experience_distillation.py`.

## Validation

Use the validation lane in [mechanics/experience/legacy/AGENTS.md](../AGENTS.md#validation) for executable commands.
