# Tests District

`tests/` holds root-owned regression and contract tests for the AoA center.
Mechanic-owned tests live with the owning mechanic or part.

Tests protect bounded claims. They do not replace proof canon in `aoa-evals`
and do not grant authority beyond the claims they check.

## Current Surface

| Surface | Role |
|---|---|
| [`registry.json`](registry.json) | canonical map of root test families, root test files, and mechanic test-home routes |
| [`../pytest.ini`](../pytest.ini) | root-level pytest collection contract for active root, mechanic, and Spark test homes |

## Test Families

| Family | Role |
|---|---|
| `agents-mesh` | AGENTS-card shape, coverage, and generated mesh tests |
| `entry-and-roadmap` | center entry, route sync, roadmap, and public route tests |
| `root-districts` | config, schemas, scripts, manifests, examples, and generated district tests |
| `docs-districts` | docs migration, thematic indexes, decisions, and trace district tests |
| `organ-contract` | AbyssOS repo-organ contract and route-mode tests |
| `hygiene` | link, Markdown shape, status vocabulary, generated freshness, and known repair tests |
| `mechanics-topology` | mechanic registry, cards, artifact homes, and landing ledger tests |
| `owner-requests` | owner request queue and owner request document tests |
| `ecosystem-contract` | ecosystem registry, Questbook center surface, and cross-mechanic route tests |
| `tests-district` | tests district registry and route-shape tests |

## Test Homes

| Home | Role |
|---|---|
| `tests/test*.py` | root-owned center tests registered in `tests/registry.json` |
| `mechanics/<slug>/tests/` | mechanic-level tests |
| `mechanics/<slug>/parts/<part>/tests/` | part-local mechanic tests |
| `Spark/tests/` | Spark agent-lane tests |

Root `pytest.ini` keeps `python -m pytest -q` broad enough to collect active
test homes while excluding legacy, cache, and build directories from default
collection.

## Source Order

When a test and another surface disagree, read authority in this order:

1. owner source document, mechanic package, or root district README
2. schema, registry, config, builder, or validator that defines the contract
3. test assertion
4. generated or derived consumer surface

## Editing Route

- Add root tests here only for root-owned center contracts.
- Add mechanic tests under the owning mechanic or part.
- Update `registry.json` when a root test or mechanic test-home route changes.
- Keep assertions close to the claim they protect.
- Keep fixtures compact and clearly non-authoritative.

## Validation

Use the validation lane in [`AGENTS.md`](AGENTS.md#validation).
