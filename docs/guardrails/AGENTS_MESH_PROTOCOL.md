# AGENTS Mesh Protocol

## Purpose

The AGENTS mesh makes agent guidance local without letting local cards steal authority from source documents. A root card gives route choice and owner boundaries. District cards give local risk and validation. Package cards explain mechanic or thematic intent. Deep cards protect high-friction source surfaces.

`DESIGN.AGENTS.md` describes the design form of this agent-facing layer. This
protocol defines the current checkable mesh contract.

`README_AGENTS_CORPUS_PROTOCOL.md` defines the role boundary between inherited
agent routes and on-demand human README surfaces, including the evidence needed
before a file is merged, moved, generated, or removed.

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

`Read before editing` is a conditional owner-route section, not a standing
reading list. A card may name a README when its human explanation, package map,
provenance, or compatibility route is material to the task. It must not require
the nearest README only because the file exists.

Registered inherited card chains must fit the byte budget declared in
`config/agents_mesh.json`. The budget measures prompt pressure, not semantic
quality: a necessary stop-line stays in the nearest card until a stronger
source surface can carry it.

## Precedence

1. Root `AGENTS.md` owns repository identity, route modes, and owner boundaries.
2. Nearer `AGENTS.md` files own local file posture, local checks, and local risks.
3. Source docs, schemas, builders, validators, and owner repositories own their own stronger claims.
4. Generated mirrors reflect source contracts and do not author meaning.
5. `DESIGN.AGENTS.md` shapes the agent-surface form; it does not replace the
   root card, local cards, this protocol, config, validators, or generated
   mirrors.

## Growth rule

When a new durable directory appears, choose one of three actions in the same change:

1. add a local `AGENTS.md`;
2. register an explicit exemption in `config/agents_mesh.json` with a reason;
3. prove it is temporary and should not be committed as a durable district.

When child-specific executable procedure would repeat across descendants or
push a registered inherited chain over budget, keep only a compact validation
route in the nearest card and route exact argv through its single owner
procedure. For mechanics, that source is `mechanics/validation-routes.json` and
its no-shell runner. Other validation surfaces name the route or manifest key
instead of copying the command. Do not move command catalogs into README entry
maps merely to make AGENTS shorter.

Do not move human overview or usage prose into AGENTS to reduce the README
count. Do not move local stop-lines into README to reduce inherited bytes. Apply
the dispositions and review evidence from
`README_AGENTS_CORPUS_PROTOCOL.md` before merging, moving, generating, or
removing either surface class.

## Must not claim

The AGENTS mesh must not claim hidden autonomy, memory sovereignty, live runtime authority, proof sovereignty, ToS canon authority, or owner-local acceptance. It gives agents safer roads. It does not become the city charter.

## Validation

Use the repository `VALIDATION.md` map for the current command route.
