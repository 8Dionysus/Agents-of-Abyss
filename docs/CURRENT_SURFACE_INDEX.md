# Current Surface Index

This index explains which `docs/` surfaces are current and which districts hold historical or supporting material.

## Current docs root surfaces

| Surface | Role | Why it may stay flat |
|---|---|---|
| `docs/README.md` | docs district gate | local human and agent entrypoint |
| `docs/AGENTS.md` | docs-local agent gate | nearest agent instruction surface for docs work |
| `docs/FEDERATION_RULES.md` | source-of-truth law | current center doctrine |
| `docs/LAYERS.md` | layer map | current owner-routing support |
| `docs/REPO_ROLES.md` | repo-role map | current owner-routing support |
| `docs/ROOT_SURFACE_LAW.md` | root placement law | current root and docs cleanup law |
| `docs/START_HERE_ROUTE_CONTRACT.md` | route-mode contract | current entry contract |
| `docs/THEMATIC_DISTRICT_PROTOCOL.md` | docs district law | current docs cleanup law |
| `docs/CURRENT_SURFACE_INDEX.md` | thin current index | routes old material without duplicating it |
| `docs/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md` | hygiene law | current link, shape, status, and freshness guardrail |
| `docs/HYGIENE_GUARDRAIL_INDEX.md` | thin hygiene index | routes hygiene scripts, config, generated mirror, and traces |
| `docs/AGENTS_MESH_PROTOCOL.md` | AGENTS mesh law | current local agent-card coverage and shape guardrail |
| `docs/AGENTS_MESH_INDEX.md` | thin AGENTS mesh index | routes mesh config, generated mirror, validators, and cards |
| `docs/thematic_districts.json` | machine-readable classifier | source for Wave D validators and generated index |

## Thematic districts

| District | Use | Current-law caution |
|---|---|---|
| `docs/agent-lane/` | agent-lane references | root or nearest `AGENTS.md` still wins |
| `docs/audits/` | audit evidence and protocols | evidence is not law until adopted by a canonical surface |
| `docs/landings/` | wave receipts and seed manifests | receipts are not operational proof |
| `docs/registry/` | registry evolution notes | design notes are not generated-capsule truth until builders and validators land |
| `docs/decisions/` | decision records | decisions explain why, current surfaces define what |
| `docs/postmortems/` | repair learning | postmortems do not become current doctrine without promotion |
| `docs/traces/` | move manifests and provenance | traces explain movement, not meaning |
| `docs/agon/` | old or transitional Agon records | current route is `mechanics/agon/README.md` |
| `docs/experience/` | old or transitional Experience records | current route is `mechanics/experience/README.md` |
| `docs/legacy/` | compatibility and superseded flat docs | never cite as current authority when canonical route exists |

## Cleanup command

```bash
python scripts/plan_docs_thematic_cleanup.py --check
python scripts/validate_agents_mesh.py
python scripts/validate_hygiene_suite.py
```
