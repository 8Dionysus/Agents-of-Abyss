# Root Surface Law

This document decides what may live in the root of `Agents-of-Abyss`.

The root is not a warehouse. It is the civic front of the polis: a small set of surfaces that let humans, agents, contributors, validators, and neighboring repositories orient without digging.

## Root principle

A root surface is allowed only when it serves at least one of these durable roles:

1. **Civic law**: it names, governs, or maps the AoA center.
2. **Public governance**: platforms and contributors expect it at root.
3. **Thin civic index**: it routes to deeper districts without duplicating them.
4. **Machine/developer district**: it is a top-level technical directory expected by tooling.
5. **Agent lane**: it belongs to the agent-facing lane and is governed by that lane.

A surface that is merely interesting, historical, local to one wave, generated, experimental, or future-looking must not sit in root by default.

## Allowed root surfaces

| Class | Allowed examples | Why root is justified | Guardrail |
|---|---|---|---|
| Civic law and public map | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md` | they define the center's identity, contour, and direction | must stay aligned with generated capsules and validators |
| Public governance and legal | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` | GitHub and contributors expect them there | must not become doctrine catalogs |
| Thin civic indexes | `GLOSSARY.md`, `QUESTBOOK.md`, `ECOSYSTEM_AUDIT_INDEX.md`, `FRAGILITY_BLACKLIST.md` | they help humans and agents route quickly | must stay compact and link to deeper canonical docs |
| Agent lane | `AGENTS.md`, `.agents/`, `Spark/` | agent-facing work needs a stable local lane | must not become a substitute for civic docs |
| Tooling and machine districts | `.github/`, `scripts/`, `schemas/`, `generated/`, `tests/`, `config/`, `examples/`, `manifests/`, `quests/`, `docs/` | tooling and repo structure expect stable directories | generated objects stay generated; quests stay tracked obligations, not roadmap copies |
| Development requirements | `.gitignore`, `requirements-dev.txt` | development hygiene | must stay technical and small |

## Surfaces that should not live in root

| Surface kind | Better home | Reason |
|---|---|---|
| One-wave seed manifest | `docs/landings/` or nearest specific docs district | useful receipt, not civic law |
| Future registry design note | `docs/registry/` | design evolution belongs beside registry law, not beside the constitution |
| Audit candidate list | `docs/audits/` | review evidence should be inspectable but not displayed as a civic front-door peer |
| Generated artifact | `generated/` | generated surfaces must remain machine-facing and reproducible |
| Experiment or scratchpad | `docs/audits/`, `docs/experiments/`, owner repo, or untracked local notes | the root must not preserve every thought as public law |
| Repo-local semantic change | owner repository | the center must not absorb layer truth |
| Duplicate platform file | one canonical platform file | duplicate names with different casing create review and platform ambiguity |

## Decision procedure before adding a root file

Ask these questions in order:

1. Does the file define center identity, map, governance, public platform posture, or a thin index?
2. Would a human reasonably expect to find this file at the repository root before entering `docs/`?
3. Would an agent make safer decisions because this file is at root rather than in a deeper district?
4. Does a generated, audit, registry, quest, landing, or owner-local home already fit better?
5. Can the file stay compact over time without becoming a duplicate doctrine surface?

If the answer to any of questions 1-3 is no, or question 4 is yes, do not place the file at root.

## Current root cleanup decisions

| Existing surface | Decision | New home or status | Why |
|---|---|---|---|
| `SEED_MANIFEST.md` | move | `docs/landings/AGON_WAVE3_SEED_MANIFEST.md` | it is an Agon Wave III receipt, not a root manifest for the whole repository |
| `registry-v2-notes.md` | move | `docs/registry/REGISTRY_V2_NOTES.md` | it is a future registry design note and belongs near registry evolution |
| `DELETION_CANDIDATES.json` | move | `docs/audits/DELETION_CANDIDATES.json` | it is an inspect-first audit artifact, not a civic root surface |
| `.github/pull_request_template.md` | remove | keep `.github/PULL_REQUEST_TEMPLATE.md` | duplicate PR templates with different casing create template ambiguity |
| `FRAGILITY_BLACKLIST.md` | keep, narrow | root index to `docs/VIA_NEGATIVA.md` and `docs/audits/DELETION_CANDIDATES.json` | useful root pattern index if compact |
| `QUESTBOOK.md` | keep, narrow | root quest index | useful only while it stays federation-level and does not become a second roadmap |
| `ECOSYSTEM_AUDIT_INDEX.md` | keep, clean | root audit router | useful root index if it routes rather than storing every audit detail |
| `GLOSSARY.md` | keep | root vocabulary companion | useful compact vocabulary if aligned with center docs |

## Long-term next step

This law intentionally opens deeper cleanup instead of hiding the problem.

After the first root cleanup lands, run a second pass over `docs/` to decide whether wave landing receipts should remain flat under `docs/` or migrate into thematic districts such as `docs/landings/`, `docs/agon/`, `docs/experience/`, and `docs/registry/`. Do not perform that migration casually. It touches many links, generated surfaces, tests, and agent expectations.

## Final rule

The root is healthy when every file there can explain why it is visible before the reader enters the districts. If the explanation sounds like "it was created during a wave," move it.
