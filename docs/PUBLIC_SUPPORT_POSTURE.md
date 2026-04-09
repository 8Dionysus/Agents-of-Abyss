# Public Support Posture

This note records the public onboarding, support, release, and CI posture for the AoA center.
It is about what the center may honestly claim, not about taking ownership away from sibling repositories.

## Shortest onboarding path

For ecosystem understanding, read in this order:

1. `README.md`
2. `CHARTER.md`
3. `ECOSYSTEM_MAP.md`
4. `docs/FEDERATION_RULES.md`

Stop there for a first-pass center view.
Use `docs/LAYERS.md` and `ROADMAP.md` only when you need conceptual detail or declared direction after the overview.

For small-model and low-context entry, use `generated/center_entry_map.min.json` as the compact machine-facing companion to the same route.
`README.md` remains the public human root, and `CHARTER.md` remains the authority surface.

## Public support posture

The center may publicly support:

- ecosystem identity and naming
- the current public layer map
- federation rules and source-of-truth boundaries
- compact registry surfaces for the documented public contour
- reviewable routing toward layer-owned repositories

The center does not publicly support:

- layer-owned truth that belongs in `aoa-techniques`, `aoa-skills`, `aoa-evals`, `aoa-memo`, `aoa-agents`, `aoa-playbooks`, or `aoa-kag`
- runtime guarantees that belong in `abyss-stack`
- ToS-authored meaning that belongs in `Tree-of-Sophia`
- typed consumer or control-plane guarantees that belong in `aoa-sdk`

## Release semantics

An `Agents-of-Abyss` public claim is only honest when these stay aligned in the same landed state:

- `CHARTER.md`
- `ECOSYSTEM_MAP.md`
- `docs/FEDERATION_RULES.md`
- `generated/center_entry_map.min.json`
- `generated/ecosystem_registry.min.json`
- `generated/federation_supporting_inventory.min.json`

This repository names the federation contour.
It does not version or release the primary meaning of sibling repositories.

## CI tier map

Use the tiers below when you need to verify center claims:

| tier | purpose | surface |
|---|---|---|
| Tier 1 | compact center contract validation | `python scripts/validate_ecosystem.py` |
| Tier 2 | bounded repository regression battery | `python -m pytest -q tests` |
| Tier 3 | source-side scheduled truth check | `.github/workflows/source-side-smoke.yml` |

The machine-facing center capsule has its own bounded rebuild loop:

- `python scripts/build_center_entry_map.py --check`
- `python scripts/validate_center_entry_map.py`

PR and push validation live in `.github/workflows/repo-validation.yml`.
