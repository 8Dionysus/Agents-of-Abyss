# Scripts District

`scripts/` holds root-owned builders, validators, release checks, and shared
helper modules for the AoA center. Mechanic-owned tooling lives with the
owning mechanic or part.

Scripts may build or validate compact surfaces. They do not create
constitutional authority by themselves.

## Current Surface

| Surface | Role |
|---|---|
| [`registry.json`](registry.json) | canonical map of root script families, root Python files, and mechanic script-home routes |

## Script Families

| Family | Role |
|---|---|
| `release-gate` | public release check orchestration |
| `center-entry` | center entry map building, route parity, and validation |
| `root-registries` | root config, schema, manifest, technical district, and ecosystem registry validation |
| `docs-districts` | root docs district cleanup, indexes, decisions, and trace receipts |
| `hygiene` | link, Markdown, status vocabulary, generated freshness, and known-repair guardrails |
| `agents-mesh` | AGENTS-card shape, coverage, and compact mesh indexes |
| `mechanics-topology` | mechanics package topology, cards, artifact homes, and landing logs |
| `owner-requests` | center-side owner request queue building and validation |

## Script Homes

| Home | Role |
|---|---|
| `scripts/*.py` | root-owned center tooling registered in `scripts/registry.json` |
| `mechanics/<slug>/scripts/` | mechanic-level tooling |
| `mechanics/<slug>/parts/<part>/scripts/` | part-local mechanic tooling |
| `Spark/scripts/` | Spark agent-lane validation |

## Source Order

When a script and another surface disagree, read authority in this order:

1. owner source document, mechanic package, or root district README
2. schema, registry, config, or generated source map that defines the shape
3. script implementation
4. generated or derived consumer surface

## Editing Route

- Add root scripts here only for root-owned center tooling.
- Add mechanic scripts under the owning mechanic or part.
- Update `registry.json` when a root script or mechanic script-home route
  changes.
- Keep builders deterministic and validators explicit about the surface they
  check.
- Keep release-facing changes aligned with `release_check.py`.

## Validation

Use the validation lane in [`AGENTS.md`](AGENTS.md#validation).
