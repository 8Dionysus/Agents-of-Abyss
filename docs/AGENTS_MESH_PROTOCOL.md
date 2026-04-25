# AGENTS Mesh Protocol

## Purpose

The AGENTS mesh makes agent guidance local without letting local cards steal authority from source documents. A root card gives route choice and owner boundaries. District cards give local risk and validation. Package cards explain mechanic or thematic intent. Deep cards protect high-friction source surfaces.

## Contract

Every durable district that agents may edit should have a local `AGENTS.md` or an explicit exemption in `config/agents_mesh.json`.

Each card must include:

- `## Applies to`
- `## Role`
- `## Read before editing`
- `## Boundaries`
- `## Validation`
- `## Closeout`

Cards must be readable Markdown, not minified instruction blobs. They should make the next safe action obvious to a low-context agent.

## Precedence

1. Root `AGENTS.md` owns repository identity, route modes, and owner boundaries.
2. Nearer `AGENTS.md` files own local file posture, local checks, and local risks.
3. Source docs, schemas, builders, validators, and owner repositories own their own stronger claims.
4. Generated mirrors reflect source contracts and do not author meaning.

## Growth rule

When a new durable directory appears, choose one of three actions in the same change:

1. add a local `AGENTS.md`;
2. register an explicit exemption in `config/agents_mesh.json` with a reason;
3. prove it is temporary and should not be committed as a durable district.

## Must not claim

The AGENTS mesh must not claim hidden autonomy, memory sovereignty, live runtime authority, proof sovereignty, ToS canon authority, or owner-local acceptance. It gives agents safer roads. It does not become the city charter.

## Validation

```bash
python scripts/validate_agents_md_shape.py
python scripts/validate_agents_mesh.py
python scripts/build_agents_mesh_index.py --check
python scripts/validate_agents_mesh_index.py
python scripts/validate_generated_freshness.py
```
