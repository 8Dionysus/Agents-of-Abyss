# Ecosystem Audit Index

This file is the compact audit routing surface for Codex and human reviewers.

Use it with `AGENTS.md`, [docs/audits/CODEX_AUDIT_PROTOCOL](docs/audits/CODEX_AUDIT_PROTOCOL.md), [docs/audits/CODEX_SKILL_PROOF_AUDIT_BRIDGE](docs/audits/CODEX_SKILL_PROOF_AUDIT_BRIDGE.md), and [docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md).

It exists to answer five questions fast:

1. What does this repository own?
2. Which documents are the source of truth?
3. What kind of drift is most dangerous here?
4. What validation must be run before claiming the work is done?
5. When should work be routed to a neighboring repository instead?

## Audit classes

| Class | Looks for |
|---|---|
| constitutional | identity, ownership, routing, root surface, and federation drift |
| runtime | services, ports, secrets, bootstrap, deployment, recoverability, and hidden mutation |
| workflow | runnable entrypoints, dry-run safety, automation contracts, dependency drift, and service drift |
| meaning | provenance, source layering, interpretation boundaries, lineage, and authored-vs-derived drift |
| proof | bounded claims, caveats, verdict shape, comparison posture, and overclaiming drift |

## Repository index

| Repository | Audit class | Owns | Primary source-of-truth docs | Mandatory verification before "done" | Default audit focus | Route away when |
|---|---|---|---|---|---|---|
| `Agents-of-Abyss` | constitutional | ecosystem identity, layer map, federation rules, program-level direction, center mechanics, root surface law | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md`, `docs/ROOT_SURFACE_LAW.md`, `ROADMAP.md`, generated registry capsules | `python scripts/validate_ecosystem.py`, `python scripts/validate_markdown_shape.py`, plus nearest center validator for touched generated surfaces | ownership drift, routing drift, root-surface inflation, silent absorption of layer-owned meaning | the task mainly changes a layer-owned object rather than the center |
| `Tree-of-Sophia` | meaning | source-first knowledge architecture, node layering, lineage logic, authored meaning discipline | ToS README, ToS review checklist, and ToS architecture notes | manual review route in ToS-owned docs | provenance loss, authored-vs-derived drift, flattened interpretation | the task mainly concerns runtime, routing, or derived substrate mechanics |
| `abyss-stack` | runtime | runtime body, deployment, storage, profiles, presets, secrets bootstrap, lifecycle, and security posture | stack README, charter, boundaries, architecture, service catalog, deployment, runbook, and security docs | repo-local stack validator and touched runtime checks | port exposure, secret-bearing drift, profile/preset/module drift, path mapping drift | the task mainly changes authored meaning or AoA layer truth |
| `aoa-techniques` | workflow | reusable engineering practice canon | repo `AGENTS.md`, `README.md`, and technique docs | repo-local validation documented there | technique duplication, shallow donor copying, missing evidence or checks | the task mainly packages execution rather than reusable practice |
| `aoa-skills` | workflow | bounded execution canon, trigger boundaries, invocation posture, and generated skill surfaces | `README.md`, architecture docs, target `skills/*/SKILL.md`, target `skills/*/techniques.yaml`, `AUDIT.md` | repo-local validation; re-read skill/proof audit bridge when proof posture changes | workflow widening, technique-truth duplication, overlay authority drift | the task mainly changes upstream technique truth or bounded proof doctrine |
| `aoa-evals` | proof | bounded proof canon, portable eval bundles, claim framing, verdict wording, comparison posture, shared proof infra, generated eval surfaces | `README.md`, eval philosophy, eval index, target bundle docs, `AUDIT.md` | `python scripts/validate_repo.py`; rebuild catalog when manifests or generated surfaces change | overclaiming, verdict/claim mismatch, baseline-by-association drift, chooser/routing overreach | the task mainly changes execution workflow meaning |
| `aoa-routing` | constitutional | thin navigation and dispatch surfaces | repo `AGENTS.md`, `README.md` | repo-local validation documented there | route-to-wrong-owner drift, routing promoted into authority | the task requires authoring primary truth |
| `aoa-memo` | meaning | explicit memory objects and recall posture | repo `AGENTS.md`, `README.md` | repo-local validation documented there | provenance drift, authored/core memory confused with derived substrate | the task mainly belongs to KAG or evals |
| `aoa-agents` | constitutional | role contracts, persona boundaries, handoff posture, and memory/evaluation posture at agent layer | `README.md`, target role docs, generated registry surfaces, `AGENTS.md` | repo-local validation documented there | role blur, handoff drift, agent layer swallowing skills/playbooks/evals | the task mainly changes workflows or proof doctrine |
| `aoa-playbooks` | workflow | scenario-level composition and recurring operational routes | repo `AGENTS.md`, `README.md` | repo-local validation documented there | playbook swallowing skill canon, scenario ambiguity, unclear evidence posture | the task is still only a bounded single workflow |
| `aoa-kag` | meaning | derived provenance-aware substrate, graph-ready and retrieval-ready projections | repo `AGENTS.md`, `README.md` | repo-local validation documented there | derived layer claiming authored source authority | the task mainly changes authored source meaning |
| profile repo `8Dionysus/README.md` | constitutional | public entry surface and orientation only | profile `README.md`, profile `GLOSSARY.md`, AoA center docs | manual consistency review against center docs | mirror drift, summary outrunning the center | the task changes core definitions rather than public orientation |

## Root-surface audit route

Use this route when the question is not only "is the claim true?" but "should this file live in root?"

| Surface kind | Canonical home |
|---|---|
| civic law or public map | root |
| contributor, security, conduct, or license surface | root |
| compact civic index | root only while compact |
| historical seed or package receipt | owning `mechanics/<slug>/legacy/raw/` for mechanic-specific receipts, or `docs/traces/` for generic movement evidence |
| audit candidate list or cleanup evidence | `docs/audits/` |
| future registry design note | `docs/registry/` |
| generated compact machine surface | `generated/` |
| owner-local semantic change | owning repository |

Current root-surface cleanup evidence lives in [docs/audits/ROOT_SURFACE_AUDIT_2026_04_24](docs/audits/ROOT_SURFACE_AUDIT_2026_04_24.md).

## Drift signatures worth flagging immediately

### Documentation shape drift

- a key README or civic surface collapses into a few long lines
- tables, code fences, or numbered paths become hard for humans or agents to parse
- a technical district gains many files without a local README gate
- a root file remains after its better home is planted in `docs/audits/`, `docs/registry/`, `docs/traces/`, or `mechanics/<slug>/legacy/raw/`

### Constitutional drift

- a center or routing surface starts owning layer detail
- a summary or mirror states stronger ownership than the source repository
- neighboring repositories are described inconsistently
- generated registry or index surfaces change without source docs changing
- a root file appears without a root-surface role

### Runtime drift

- localhost binds change to wider exposure
- public-safe examples drift toward live runtime secrets
- repair or resume loops mutate state without receipts
- profile, preset, or module edits are not reflected in render/bootstrap checks

### Workflow drift

- runnable entrypoints change without smoke validation
- dry-run defaults quietly weaken
- a skill mostly copies a technique or owner runbook without adding bounded execution semantics
- public docs leak workstation-specific paths, tokens, or local state

### Meaning drift

- source, extraction, interpretation, and synthesis get flattened together
- derived substrate starts reading like authored source truth
- provenance, lineage, or context disappears
- memory starts speaking as proof

### Proof drift

- an eval implies more than its evidence carries
- verdict shape no longer matches the bounded claim
- caveats disappear while metrics stay
- a single composite score starts acting like standing, rank, or authority

## Routing rule

When in doubt, do not patch across repository boundaries. Instead:

1. name the owning repository,
2. state the boundary clearly,
3. make the smallest local routing fix if needed,
4. leave the owned semantic change to the correct repository.
