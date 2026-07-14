# AGENTS.md

## Applies to

This card applies to `stats/` in `Agents-of-Abyss`.

## Role

This directory owns center-local statistical questions over center-owned
registries and maps. Shared measurement grammar and cross-owner composition
remain owned by `aoa-stats`.

## Read before editing

1. Root `AGENTS.md`, `CHARTER.md`, and `DESIGN.md`.
2. `ECOSYSTEM_MAP.md`, `ROADMAP.md`, and `docs/FEDERATION_RULES.md`.
3. `stats/README.md` and `stats/port.manifest.json`.
4. `generated/ecosystem_registry.min.json`, its schema, and its owner
   validator.
5. The central measurement and packet contracts under `aoa-stats/stats/`.

## Boundaries

- The registry v2 `repos` array defines the exact population. Supporting
  inventories, workspace checkouts, local ports, and runtime surfaces do not
  enter the denominator.
- Only the literal center-authored maturity label `active` enters the
  numerator. Do not reinterpret labels into a quality or progress score.
- A valid complete registry with no `active` rows is an observed zero.
- An unsupported registry version or a malformed, empty, or duplicate
  population is unknown, not zero.
- The reference packet is weaker than the authored ecosystem map and the
  owner-validated registry from which it is derived.
- The ratio does not establish repository health, implementation quality,
  owner acceptance, release readiness, remote freshness, or local stats-port
  coverage.

## Validation

Inspect the registry and packet first. The port validator requires a compatible
`aoa-stats` checkout through `AOA_STATS_ROOT`, `.deps/aoa-stats`, or the sibling
`../aoa-stats` path; CI supplies its pinned checkout explicitly, and an
unavailable central validator is a failed check. Then run:

```bash
python scripts/stats/validate_local_stats_port.py
python -m pytest -q tests/test_local_stats_port.py
```

Use the root route for repository-wide validation.

## Closeout

Report the center-owned question, registry population, manual positive and
negative cases, packet posture, central validation, and repository validation.
