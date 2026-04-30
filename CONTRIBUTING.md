# Contributing to Agents of Abyss

Thank you for helping shape AoA.

`Agents-of-Abyss` is the constitutional polis of AoA. It names, maps, governs,
audits, and routes the federation without becoming the default home for every
technique, skill, proof bundle, memory object, role, playbook, graph projection,
runtime service, or ToS-authored meaning.

A good contribution here makes the federation easier to read and safer to grow.

## Contribution Promise

Contributions to this repository should improve at least one center-owned route:

- the AoA charter, ecosystem map, federation rules, or layer model
- root surface governance and cleanup
- repository-role and owner-boundary routing
- center mechanics, mechanic cards, owner requests, and landing routes
- compact public indexes such as glossary, questbook, audit, or fragility routes
- generated center capsules, schemas, validators, or tests that protect center
  claims

When the stronger truth belongs to a sibling repository, route the work there
and keep the center contribution narrow.

## Choose the Owner First

Before editing, decide which surface owns the meaning:

- `Agents-of-Abyss` owns ecosystem-level truth, center mechanics, and root
  surface law.
- Specialized AoA repositories own their object classes, such as techniques,
  skills, evals, roles, playbooks, memory, routing, KAG, stats, and SDK helpers.
- `Tree-of-Sophia` owns ToS-authored knowledge meaning.
- `abyss-stack` owns runtime infrastructure and service behavior.
- `8Dionysus` owns public profile orientation and shared-root projection
  sources.

Use [docs/REPO_ROLES](docs/REPO_ROLES.md) and
[docs/FEDERATION_RULES](docs/FEDERATION_RULES.md) when ownership is unclear.

## Entry Routes

Use the canonical route contract before widening a center claim or moving
material into this repository:
[docs/START_HERE_ROUTE_CONTRACT.md](docs/START_HERE_ROUTE_CONTRACT.md).

| Route mode | Contributor use |
|---|---|
| `first-reading` | understand the center before expanding a claim |
| `root-editing` | add, move, delete, rename, or rewrite root surfaces |
| `direction-change` | change roadmap, horizon posture, maturity, owner-route pressure, future trigger, transition, or release contour |
| `ownership-routing` | decide which repository owns a change |
| `mechanic-change` | edit a center mechanic package, process route, stop-line, owner split, or mechanic-facing validation lane |
| `public-claim-validation` | check whether public language is honest and supportable |
| `low-context-agent` | use a compact machine route before full reading |
| `district-work` | follow local README gates inside technical districts |

For root files, also read
[docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md). For mechanic work, start at
[mechanics/README](mechanics/README.md) and then read the package-local
`AGENTS.md`.

## Root and District Changes

Root files stay visible because they help humans, agents, contributors,
validators, and neighboring repositories orient before entering deeper
districts.

Use root for:

- civic law and public maps
- public governance files expected by GitHub or contributors
- thin civic indexes that route to deeper source surfaces
- stable technical districts expected by tooling
- agent-facing route law

Use the owning district or mechanic package for:

- historical receipts and raw source packets
- mechanic-specific doctrine, examples, schemas, generated companions, scripts,
  and tests
- audit evidence, traces, decisions, and legacy material
- owner-local semantic truth

Technical districts such as `generated/`, `scripts/`, `schemas/`, `tests/`,
`config/`, `examples/`, `manifests/`, and `quests/` have local README or
`AGENTS.md` gates. Read those before changing files there.

## Pull Request Shape

A strong pull request says:

- what center surface changed
- why the change belongs in `Agents-of-Abyss`
- which root surface class, mechanic package, or technical district is involved
- which owner boundary stayed outside the change
- which generated surfaces, schemas, scripts, tests, or local validators moved
- whether direction, public release history, durable obligations, mechanic
  landing surfaces, generated companions, or decision records need follow-up
- which checks ran, which checks were skipped, and what risk remains

Agent-facing branch, closeout, and merge law lives in [AGENTS](AGENTS.md). This
file keeps the contributor route readable.

## Validation

Run the smallest relevant check first, then widen when a generated surface,
schema, public route, or release-facing surface changes.

Center entry surfaces may point to the current baseline instead of repeating the
full command list:
[docs/guardrails/ENTRY_SURFACE_VALIDATION_BASELINE.md](docs/guardrails/ENTRY_SURFACE_VALIDATION_BASELINE.md).

For release-facing or repo-wide changes, use the broad gate:

```bash
python scripts/release_check.py
```

For local work, prefer the nearest `AGENTS.md`, README, builder, validator, or
test named by the touched surface.

## Style

Prefer:

- compact routes over catalogs
- explicit owner boundaries over vague ambition
- readable maps over abstract slogans
- one source surface over duplicate meaning
- reviewable receipts over hidden mutation
- future routes over inert placeholders

Route away when:

- the change mainly authors a specialized object class
- a generated or derived surface starts acting like source truth
- an example starts carrying proof authority
- a root file would become a warehouse rather than a civic entrance

## Unsure?

Choose the narrower change.

If the work feels like a new layer, mechanic, or owner-local doctrine, name the
possibility and route it. A small honest route is better than a large confused
landing.
