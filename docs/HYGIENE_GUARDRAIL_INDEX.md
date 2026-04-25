# Hygiene Guardrail Index

This index names the Wave E guardrails for link and shape hygiene.

The protocol lives in `docs/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md`. The machine-facing mirror lives in `generated/link_shape_hygiene.min.json`. The source config lives in `config/link_shape_hygiene.json`.

## Guardrail table

| Guardrail | Primary script | Source input | Output | Status |
|---|---|---|---|---|
| Known link repair | `scripts/repair_known_link_drifts.py` | `config/link_shape_hygiene.json` | repaired exact drift or check failure | active |
| Local link validation | `scripts/validate_links.py` | Markdown files and config | broken-link report | active |
| Markdown shape validation | `scripts/validate_markdown_shape.py` | configured Markdown targets | shape report | active |
| Status vocabulary validation | `scripts/validate_status_vocabulary.py` | configured JSON status paths | vocabulary report | active |
| Generated freshness validation | `scripts/validate_generated_freshness.py` | configured builders and outputs | stale-generated report | active |
| Hygiene index build | `scripts/build_link_shape_hygiene_index.py` | protocol and config | `generated/link_shape_hygiene.min.json` | active |
| Hygiene index validation | `scripts/validate_link_shape_hygiene_index.py` | generated capsule | structural report | active |

## Source surfaces

| Surface | Role |
|---|---|
| `docs/LINK_AND_SHAPE_HYGIENE_PROTOCOL.md` | human law for Wave E hygiene |
| `docs/HYGIENE_GUARDRAIL_INDEX.md` | human index for guardrails |
| `config/link_shape_hygiene.json` | source config for validators and generated mirror |
| `generated/link_shape_hygiene.min.json` | compact machine-facing mirror |
| `generated/agents_mesh.min.json` | required generated freshness target for Wave F AGENTS mesh |
| `docs/traces/WAVE_E_HYGIENE_REPAIR_MANIFEST.json` | optional repair trace written by the apply script |

## What counts as success

Wave E is successful when:

1. no known stale link fragment remains;
2. local Markdown links resolve to existing repository paths;
3. public entry surfaces stay readable rather than collapsed;
4. status values stay inside their vocabulary;
5. generated capsules rebuild cleanly;
6. hygiene findings route semantic questions back to the correct owner instead of turning scripts into doctrine.

## How to extend

To add a new protected surface, add it to `config/link_shape_hygiene.json`, rebuild the generated hygiene index, and add or update tests.

To add a known link repair, record the exact old and new fragment in the config. Do not write a broad rewrite rule when an exact repair is enough.

To add a status vocabulary, add the vocabulary, then add a status check entry that points to the JSON path where that vocabulary is used.

## Validation

Run:

```bash
python scripts/repair_known_link_drifts.py --check
python scripts/validate_links.py
python scripts/validate_markdown_shape.py
python scripts/validate_status_vocabulary.py
python scripts/build_link_shape_hygiene_index.py --check
python scripts/validate_link_shape_hygiene_index.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_generated_freshness.py
python scripts/validate_hygiene_suite.py
python -m pytest -q tests
```

A future agent should be able to add a district or generated capsule by changing the config and tests, not by memorizing a private checklist.
