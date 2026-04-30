# Ecosystem Audit Index

This file is the compact root audit router for Codex and human reviewers.

Use it with `AGENTS.md`, [docs/REPO_ROLES](docs/REPO_ROLES.md),
[audit mechanic](mechanics/audit/README.md),
[audit provenance](mechanics/audit/PROVENANCE.md), and
[docs/ROOT_SURFACE_LAW](docs/ROOT_SURFACE_LAW.md).

It exists to answer four questions fast:

1. What does this repository own?
2. What kind of drift is most dangerous here?
3. Which source surface should be checked first?
4. Where should the finding be routed next?

## Use when

Use this root index when you need to classify a review, choose an owner, or
route a finding before entering a deeper audit.

Active audit method, evidence ledgers, finding lifecycle, campaign routes, and
owner handoffs live in [mechanics/audit](mechanics/audit/README.md). This root
index keeps the first route compact.

This file does not replace [docs/REPO_ROLES](docs/REPO_ROLES.md) or the target
repository `AGENTS.md` and `README.md`. Use it to choose the first audit lens,
then move to the owner surface.

## Audit classes

| Class | Looks for |
|---|---|
| constitutional | identity, ownership, routing, root surface, and federation drift |
| runtime | services, ports, secrets, bootstrap, deployment, recoverability, and hidden mutation |
| workflow | runnable entrypoints, dry-run safety, automation contracts, dependency drift, and service drift |
| meaning | provenance, source layering, interpretation boundaries, lineage, and authored-vs-derived drift |
| proof | bounded claims, caveats, verdict shape, comparison posture, and overclaiming drift |

## Repository audit routes

This table is a triage lens, not an ownership contract. For exact ownership, use
[docs/REPO_ROLES](docs/REPO_ROLES.md) and the target repository route card.

| Route | Audit class | First check | Watch for | Next route |
|---|---|---|---|---|
| `Agents-of-Abyss` | constitutional | `AGENTS.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `ROADMAP.md` | center absorbing owner-local truth, public promises without release support, root-surface sprawl | nearest center validator, then `python scripts/release_check.py` for repo-wide claims |
| `Tree-of-Sophia` | meaning | ToS README and review route | provenance loss, canon flattening, derived text outranking authored source | ToS-owned docs |
| `abyss-stack` | runtime | stack `AGENTS.md`, README, security/runbook surfaces | ports, secrets, lifecycle, profile, preset, deployment, or self-healing drift | runtime-owner checks in `abyss-stack` |
| `aoa-techniques` | workflow | repo `AGENTS.md`, README, technique docs | shallow practice copies, missing evidence, technique/skill blur | `aoa-techniques` owner route |
| `aoa-skills` | workflow | repo `AGENTS.md`, README, target `SKILL.md` | workflow widening, technique truth copied into skills, proof posture overreach | `aoa-skills`, or route back to techniques/evals |
| `aoa-evals` | proof | repo `AGENTS.md`, README, eval bundle docs | overclaiming, verdict mismatch, comparison drift, scoring as authority | `aoa-evals` proof route |
| `aoa-routing` | constitutional | repo `AGENTS.md`, README | route hint promoted into source authority | `aoa-routing`, then source owner |
| `aoa-memo` | meaning | repo `AGENTS.md`, README | memory speaking as proof, recall without provenance | `aoa-memo`, or `aoa-evals` for proof |
| `aoa-agents` | constitutional | repo `AGENTS.md`, README, role docs | role blur, persona inflation, agent layer swallowing skills/playbooks/evals | `aoa-agents` owner route |
| `aoa-playbooks` | workflow | repo `AGENTS.md`, README | scenario as hidden orchestration or proof, playbook swallowing skill canon | `aoa-playbooks`, or route to skills/evals |
| `aoa-kag` | meaning | repo `AGENTS.md`, README | derived projection acting as source replacement | `aoa-kag`, then authored source owner |
| `aoa-stats` | proof | repo `AGENTS.md`, README, generated stats surfaces | summary as authority, score drift, quest or proof status overclaim | `aoa-stats`, then proof/source owner |
| `aoa-sdk` | workflow | repo `AGENTS.md`, README, typed helper surfaces | helper convenience becoming policy, activation, or owner acceptance | `aoa-sdk`, then owning source/runtime repo |
| `Dionysus` | workflow | repo `AGENTS.md`, README, seed/staging surfaces | seed receipt promoted to final truth | final owner repository |
| `8Dionysus` | constitutional | profile README, profile glossary, workspace projection docs | public mirror outrunning center, projection source confusion | `8Dionysus` for profile/projection; AoA or owner repo for truth |

## Root-surface audit route

Use this route when the question is not only "is the claim true?" but "should this file live in root?"

| Surface kind | Canonical home |
|---|---|
| civic law or public map | root |
| contributor, security, conduct, or license surface | root |
| compact civic index | root only while compact |
| historical seed or package receipt | owning `mechanics/<slug>/legacy/raw/` for mechanic-specific receipts, or `docs/traces/` for generic movement evidence |
| audit candidate list or cleanup evidence | `mechanics/audit/` and `mechanics/audit/legacy/raw/` |
| registry contract change | `schemas/`, `generated/`, validators, aligned source docs, and `docs/decisions/` when the route changes |
| generated compact machine surface | `generated/` |
| owner-local semantic change | owning repository |

Current root-surface cleanup evidence is preserved through
[audit provenance](mechanics/audit/PROVENANCE.md) and the raw receipt
[ROOT_SURFACE_AUDIT_2026_04_24](mechanics/audit/legacy/raw/ROOT_SURFACE_AUDIT_2026_04_24.md).

## Drift signatures worth flagging immediately

### Documentation shape drift

- a key README or civic surface collapses into a few long lines
- tables, code fences, or numbered paths become hard for humans or agents to parse
- a technical district gains many files without a local README or `AGENTS.md` gate
- a root file keeps material whose better home is a mechanic package,
  `docs/traces/`, `docs/decisions/`, schemas/generated validators, or owner
  legacy/provenance

### Constitutional drift

- a center or routing surface starts owning layer detail
- a summary or mirror states stronger ownership than the source repository
- neighboring repositories are described inconsistently
- generated registry or index surfaces change without source docs changing
- a root file appears without a root-surface role
- owner-request, decision, trace, quest, or landing-log routes become
  interchangeable

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
- helper or SDK language implies owner acceptance without owner evidence

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
