# Root Surface Law

This document decides what may live in the root of `Agents-of-Abyss` and what may stay flat under `docs/`.

The root is not a warehouse. It is the civic front of the polis: a small set of surfaces that let humans, agents, contributors, validators, and neighboring repositories orient without digging.

## Root principle

A root surface is allowed only when it serves at least one durable role:

1. **Civic law**: it names, governs, or maps the AoA center.
2. **Public governance**: platforms and contributors expect it at root.
3. **Thin civic index**: it routes to deeper districts without duplicating them.
4. **Machine/developer district**: it is a top-level technical directory expected by tooling.
5. **Agent lane**: it belongs to the agent-facing lane and is governed by that lane.

A surface that is merely interesting, historical, local to one package, generated, experimental, or future-looking must not sit in root by default.

## Docs-root principle

`docs/` root has its own smaller version of the same law.

A file may remain flat under `docs/` only when it is current center doctrine, current route law, owner map support, or a compatibility route that protects a known public entrypoint.

Historical receipts, audit evidence, decisions, traces, mechanic-specific legacy records, and superseded aliases need named homes. Registry contract changes must land through schemas, generated capsules, validators, and aligned source docs rather than parked design-note doors. Empty route doors are not homes.

The docs thematic cleanup guardrails are defined by:

- [`guardrails/THEMATIC_DISTRICT_PROTOCOL`](guardrails/THEMATIC_DISTRICT_PROTOCOL.md)
- [`guardrails/CURRENT_SURFACE_INDEX`](guardrails/CURRENT_SURFACE_INDEX.md)
- [`guardrails/thematic_districts.json`](guardrails/thematic_districts.json)
- [`generated/docs_thematic_index.min.json`](../generated/docs_thematic_index.min.json)

## Allowed root surfaces

| Class | Allowed examples | Why root is justified | Guardrail |
|---|---|---|---|
| Civic law and public map | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md` | they define the center's identity, contour, and direction | must stay aligned with generated capsules and validators |
| Public governance and legal | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` | GitHub and contributors expect them there | must not become doctrine catalogs |
| Thin civic indexes | `GLOSSARY.md`, `QUESTBOOK.md`, `ECOSYSTEM_AUDIT_INDEX.md`, `FRAGILITY_BLACKLIST.md` | they help humans and agents route quickly | must stay compact and link to deeper canonical docs |
| Agent lane | `AGENTS.md`, `.agents/`, `Spark/` | agent-facing work needs a stable local lane | must not become a substitute for civic docs |
| Tooling and machine districts | `.github/`, `scripts/`, `schemas/`, `generated/`, `tests/`, `config/`, `examples/`, `manifests/`, `quests/`, `docs/`, `mechanics/` | tooling and repo structure expect stable directories | each district needs a local gate; generated objects stay generated; quests stay tracked obligations, not roadmap copies |
| Development requirements | `.gitignore`, `requirements-dev.txt` | development hygiene | must stay technical and small |

## Surfaces that should not live in root

| Surface kind | Better home | Reason |
|---|---|---|
| One-mechanic seed manifest or landing receipt | `mechanics/<slug>/legacy/raw/` plus that mechanic `PROVENANCE.md` | useful receipt, not civic law |
| Owner-bound release retrospective | `mechanics/release-support/legacy/raw/` plus release-support `PROVENANCE.md` | release repair learning belongs to the release-support mechanic |
| Generic move manifest or link rewrite trace | `docs/traces/` | traces explain movement, not meaning |
| Registry contract change | `schemas/`, `generated/`, validators, and a decision record when the route changes | registry evolution becomes real only when the machine contract and source docs move together |
| Audit candidate list | `mechanics/audit/legacy/raw/` plus `mechanics/audit/PROVENANCE.md` | review evidence should be inspectable but not displayed as a civic front-door peer |
| Generated artifact | `generated/` | generated surfaces must remain machine-facing and reproducible |
| Experiment or scratchpad | owner repo, mechanic legacy, or untracked local notes | the root must not preserve every thought as public law |
| Repo-local semantic change | owner repository | the center must not absorb layer truth |
| Duplicate platform file | one canonical platform file | duplicate names with different casing create review and platform ambiguity |

## Decision procedure before adding a root file

Ask these questions in order:

1. Does the file define center identity, map, governance, public platform posture, or a thin index?
2. Would a human reasonably expect to find this file at the repository root before entering `docs/` or `mechanics/`?
3. Would an agent make safer decisions because this file is at root rather than in a deeper district?
4. Does a generated, audit, registry, quest, trace, mechanic, or owner-local home already fit better?
5. Can the file stay compact over time without becoming a duplicate doctrine surface?

If the answer to any of questions 1-3 is no, or question 4 is yes, do not place the file at root.

## Current root cleanup decisions

| Existing surface | Decision | New home or status | Why |
|---|---|---|---|
| `SEED_MANIFEST.md` | move | `mechanics/agon/legacy/raw/AGON_WAVE3_SEED_MANIFEST.md` | it is an Agon Wave III receipt, not a root manifest for the whole repository |
| `DELETION_CANDIDATES.json` | move | `mechanics/audit/legacy/raw/DELETION_CANDIDATES.json` | it is an inspect-first audit artifact, not a civic root surface |
| `.github/pull_request_template.md` | remove | keep `.github/PULL_REQUEST_TEMPLATE.md` | duplicate PR templates with different casing create template ambiguity |
| `FRAGILITY_BLACKLIST.md` | keep, narrow | root index to `mechanics/antifragility/docs/VIA_NEGATIVA.md` and `mechanics/audit/legacy/raw/DELETION_CANDIDATES.json` | useful root pattern index if compact |
| `QUESTBOOK.md` | keep, narrow | root quest index | useful only while it stays federation-level and does not become a second roadmap |
| `ECOSYSTEM_AUDIT_INDEX.md` | keep, clean | root audit router | useful root index if it routes rather than storing every audit detail |
| `GLOSSARY.md` | keep | root vocabulary companion | useful compact vocabulary if aligned with center docs |

## Docs thematic cleanup decisions

| Existing docs surface kind | Decision | New home or status | Why |
|---|---|---|---|
| current center doctrine | keep flat under `docs/` | `FEDERATION_RULES`, `LAYERS`, `REPO_ROLES`, `ROOT_SURFACE_LAW`, `START_HERE_ROUTE_CONTRACT` | these are current orientation surfaces |
| mechanic compatibility route | keep flat and narrow | `docs/MECHANICS.md` | existing entrypoint that routes to `mechanics/README.md` |
| guardrail law and classifier | keep under | `docs/guardrails/` | validator law, hygiene law, mesh law, and classifier config belong together |
| active agent guidance | promote into owner `AGENTS.md`, validator, mechanic card, or audit protocol | agent rules should not sit in a preserved reference cache |
| audit protocol/evidence | move or keep under | `mechanics/audit/` or `mechanics/audit/legacy/raw/` | review surfaces belong with the audit mechanic |
| registry contract change | land through | schema, generated capsule, validator, source docs, and decision record when needed | registry evolution should not live as an unexecuted docs tail |
| decision record | keep or move into | `docs/decisions/` | decisions explain why; current surfaces define what |
| owner-bound retrospective | move into owner legacy | `mechanics/<slug>/legacy/raw/` plus `PROVENANCE.md` | repair learning should live with the process that can act on it |
| generic review retrospective | move into | `mechanics/audit/legacy/raw/` plus `PROVENANCE.md` when distilled | center-generic review learning is audit evidence, not a standing docs district |
| move manifest/provenance log | move into | `docs/traces/` | traces explain movement, not meaning |
| mechanic-specific legacy docs | move into | `mechanics/<slug>/legacy/raw/` | current mechanic doctrine routes through the owning mechanic package |
| superseded aliases | avoid by default | surviving canonical home plus provenance note | do not create empty docs doors for compatibility alone |

## Docs cleanup validation

Use `docs/AGENTS.md` and `docs/guardrails/AGENTS.md` for the current validation lane.

## Final rule

The root is healthy when every file there can explain why it is visible before the reader enters the districts. If the explanation sounds like "it was created during a package," move it.

The docs root is healthy when every flat docs file can explain why it is current rather than historical, evidential, transitional, mechanic-owned, or legacy.
