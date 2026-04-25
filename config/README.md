# Config District

This directory holds repository-local configuration for center tooling and validation.

It is not a runtime secret store and not the configuration home for `abyss-stack`.

Mechanic-owned seed config belongs in `mechanics/<slug>/config/`. Root config
stays for repo-wide validators, hygiene, and release gates.

## Rules

- Do not commit secrets.
- Do not store workstation-local paths as public defaults.
- Do not use config files to smuggle owner-local doctrine into the center.
- Prefer explicit names that tell readers which script or validator consumes the config.
- If a config change affects generated surfaces, update the matching documentation, validator, and tests.

## Current configs

| Surface | Consumed by | Role |
|---|---|---|
| `link_shape_hygiene.json` | Wave E hygiene validators and `generated/link_shape_hygiene.min.json` | local link repair rules, Markdown shape targets, status vocabularies, and generated freshness checks |
| `agents_mesh.json` | Wave F AGENTS mesh validators and `generated/agents_mesh.min.json` | required local AGENTS-card coverage, shape headings, and compact mesh metadata |

## Before editing

1. Identify which script, validator, or generated surface consumes the config.
2. Check whether the setting belongs to runtime infrastructure instead.
3. Keep the default public-safe.
4. Run the nearest validator.

For `link_shape_hygiene.json`, the nearest validator is:

```bash
python scripts/validate_hygiene_suite.py
```

For `agents_mesh.json`, the nearest validators are:

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
```
