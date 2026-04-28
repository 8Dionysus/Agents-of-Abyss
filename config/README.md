# Config District

`config/` holds repository-local source configuration for AoA center tooling.
It is not a runtime secret store, not an `abyss-stack` configuration home, and
not a place to smuggle mechanic-owned seed contracts back into the root.

Use this district when a setting governs repo-wide validators, generated
mirrors, hygiene suites, release checks, or local guardrails. Mechanic-owned
seed config belongs under the owning mechanic or part, such as
`mechanics/<slug>/parts/<part>/config/`.

## Source Map

`config/registry.json` is the active map for this district. It lists each root
config JSON file, its owner, source protocol, generated mirror, consumers, and
validation route.

Every `config/*.json` file must be registered there. Do not add convenience
aliases or workstation-local defaults.

## Current Configs

| Surface | Consumed by | Role |
|---|---|---|
| `config/registry.json` | `scripts/validate_config_registry.py`, `tests/test_config_registry.py` | root config inventory and add-change contract |
| `config/link_shape_hygiene.json` | hygiene validators and `generated/link_shape_hygiene.min.json` | local link repair rules, Markdown shape targets, status vocabularies, and generated freshness checks |
| `config/agents_mesh.json` | AGENTS mesh validators and `generated/agents_mesh.min.json` | required local AGENTS-card coverage, shape headings, exemptions, and compact mesh metadata |

## Rules

- Do not commit secrets, tokens, credentials, private host paths, or local-only
  operator defaults.
- Keep root config repo-wide. If a config only makes sense for one mechanic,
  move it to that mechanic's home.
- When a config change affects generated surfaces, update the config, generated
  mirror, docs, validator, and tests together.
- When adding a new root config JSON file, add it to `config/registry.json`
  before relying on it from scripts or release checks.
- Config may drive checks; it must not silently become constitutional law.

## Add Or Change Route

1. Identify the consumer script, validator, generated surface, or release check.
2. Confirm the setting belongs in root `config/`, not in `abyss-stack`,
   `mechanics/<slug>/`, or a sibling owner repo.
3. Update `config/registry.json` with source refs, consumers, generated refs,
   validation commands, and `must_not_claim` boundaries.
4. Update the human protocol or index named by the registry entry.
5. Rebuild generated mirrors when the config feeds generated output.
6. Run the narrow validators first, then the release gate if the change is
   release-facing.

## Validation

Use the validation lane in [`config/AGENTS.md`](AGENTS.md#validation).
