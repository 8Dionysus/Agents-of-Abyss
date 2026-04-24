# Config District

This directory holds repository-local configuration for center tooling and validation.

It is not a runtime secret store and not the configuration home for `abyss-stack`.

## Rules

- Do not commit secrets.
- Do not store workstation-local paths as public defaults.
- Do not use config files to smuggle owner-local doctrine into the center.
- Prefer explicit names that tell readers which script or validator consumes the config.
- If a config change affects generated surfaces, update the matching documentation, validator, and tests.

## Before editing

1. Identify which script, validator, or generated surface consumes the config.
2. Check whether the setting belongs to runtime infrastructure instead.
3. Keep the default public-safe.
4. Run the nearest validator.
