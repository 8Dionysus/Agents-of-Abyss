# Ecosystem Audit Index

This file is the compact audit routing surface for Codex and human reviewers.

It exists to answer five questions fast:

1. What does this repository own?
2. Which documents are the source of truth?
3. What kind of drift is most dangerous here?
4. What validation must be run before claiming the work is done?
5. When should work be routed to a neighboring repository instead?

Use this file together with `AGENTS.md`, `docs/CODEX_AUDIT_PROTOCOL.md`, and `docs/CODEX_SKILL_PROOF_AUDIT_BRIDGE.md`.

## Audit classes

- **constitutional**: identity, ownership, routing, and federation drift
- **runtime**: services, ports, secrets, bootstrap, deployment, and recoverability
- **workflow**: runnable entrypoints, dry-run safety, automation contracts, dependency and service drift
- **meaning**: provenance, source layering, interpretation boundaries, lineage, and authored-vs-derived drift
- **proof**: bounded claims, caveats, verdict shape, comparison posture, and overclaiming drift

## Repository index

| repository | audit class | owns | primary source-of-truth docs | mandatory verification before "done" | default audit focus | route away when |
|---|---|---|---|---|---|---|
| `Agents-of-Abyss` | constitutional | ecosystem identity, layer map, federation rules, program-level direction | `README.md`, `CHARTER.md`, `ECOSYSTEM_MAP.md`, `docs/LAYERS.md`, `docs/FEDERATION_RULES.md`, `ROADMAP.md`, `generated/ecosystem_registry.min.json`, `ECOSYSTEM_AUDIT_INDEX.md`, `docs/CODEX_AUDIT_PROTOCOL.md` | `python scripts/validate_ecosystem.py` | ownership drift, routing drift, silent absorption of layer-owned meaning | the task mainly changes a layer-owned object rather than the center |
| `ATM10-Agent` | workflow | local-first companion runtime, perception/HUD, retrieval, KAG, gateway/operator surface, dry-run automation flows | `README.md`, `MANIFEST.md`, `ROADMAP.md`, `docs/RUNBOOK.md`, `docs/SOURCE_OF_TRUTH.md`, `AUDIT.md` | `python -m pytest`, plus nearest smoke path for touched runnable entrypoints | dry-run safety, runnable contract drift, public-safe docs, dependency/service drift | the task mainly belongs to AoA center, ToS, or infra substrate |
| `abyss-stack` | runtime | runtime body, deployment, storage, profiles, presets, secrets bootstrap, lifecycle and security posture | `README.md`, `CHARTER.md`, `BOUNDARIES.md`, `docs/ARCHITECTURE.md`, `docs/SERVICE_CATALOG.md`, `docs/PROFILES.md`, `docs/PRESETS.md`, `docs/PROFILE_RECIPES.md`, `docs/RENDER_TRUTH.md`, `docs/INTERNAL_PROBES.md`, `docs/PATHS.md`, `docs/STORAGE_LAYOUT.md`, `docs/DEPLOYMENT.md`, `docs/FIRST_RUN.md`, `docs/DOCTOR.md`, `docs/SECRETS_BOOTSTRAP.md`, `docs/LIFECYCLE.md`, `docs/RUNBOOK.md`, `docs/SECURITY.md`, `AUDIT.md` | `python scripts/validate_stack.py`, plus relevant render/bootstrap checks from `AUDIT.md` | port exposure, secret-bearing drift, profile/preset/module drift, path mapping drift | the task mainly changes authored meaning or a layer-owned object |
| `Tree-of-Sophia` | meaning | source-first knowledge architecture, node layering, lineage logic, authored meaning discipline | `README.md`, `AGENTS.md`, `docs/REVIEW_CHECKLIST.md`, architecture notes referenced by the README | manual review route in `docs/REVIEW_CHECKLIST.md` | provenance loss, authored-vs-derived drift, flattened interpretation | the task mainly concerns runtime, routing, or derived substrate mechanics |
| `aoa-techniques` | workflow | reusable engineering practice canon | repo `AGENTS.md`, `README.md`, architecture/docs referenced there | repo-local validation documented in the repo | technique duplication, shallow donor copying, missing evidence or checks | the task mainly packages execution rather than reusable practice |
| `aoa-skills` | workflow | bounded execution canon, trigger boundaries, invocation posture, technique traceability, thin overlays, generated skill surfaces | `README.md`, `docs/ARCHITECTURE.md`, `docs/LAYER_POSITION.md`, `docs/BRIDGE_SPEC.md`, `docs/RUNTIME_PATH.md`, `docs/EVALUATION_PATH.md`, `docs/PUBLIC_SURFACE.md`, `docs/OVERLAY_SPEC.md`, `SKILL_INDEX.md`, target `skills/*/SKILL.md`, target `skills/*/techniques.yaml`, `AUDIT.md` | `python scripts/release_check.py`; when canonical skill semantics or evaluation/public surfaces change also run `python scripts/report_skill_evaluation.py --fail-on-canonical-gaps`; when technique dependencies change also run `python scripts/report_technique_drift.py --techniques-repo ../aoa-techniques` | workflow widening, technique-truth duplication, overlay authority drift, generated-surface drift | the task mainly changes upstream technique truth or bounded proof doctrine |
| `aoa-evals` | proof | bounded proof canon, portable eval bundles, claim framing, verdict wording, comparison posture, shared proof infra, generated eval surfaces | `README.md`, `docs/ARCHITECTURE.md`, `docs/EVAL_PHILOSOPHY.md`, `EVAL_INDEX.md`, `EVAL_SELECTION.md`, `docs/COMPARISON_SPINE_GUIDE.md`, `docs/ARTIFACT_PROCESS_SEPARATION_GUIDE.md`, `docs/REPEATED_WINDOW_DISCIPLINE_GUIDE.md`, `docs/SHARED_PROOF_INFRA_GUIDE.md`, `docs/TRACE_EVAL_BRIDGE.md`, target `bundles/*/EVAL.md`, target `bundles/*/eval.yaml`, `AUDIT.md` | `python scripts/validate_repo.py`; when manifests, generated surfaces, or public chooser wording change also run `python scripts/build_catalog.py`; for comparison-spine changes also re-read `generated/comparison_spine.json` against the changed bundle and public docs | overclaiming, verdict/claim mismatch, baseline-by-association drift, chooser/routing overreach, shared-infra overstatement | the task mainly changes execution workflow meaning rather than proof posture |
| `aoa-routing` | constitutional | thin navigation and dispatch surfaces | repo `AGENTS.md`, `README.md` | repo-local validation documented in the repo | route-to-wrong-owner drift, routing promoted into authority | the task requires authoring primary truth |
| `aoa-memo` | meaning | explicit memory objects and recall posture | repo `AGENTS.md`, `README.md` | repo-local validation documented in the repo | provenance drift, authored/core memory confused with derived substrate | the task mainly belongs to KAG or evals |
| `aoa-agents` | constitutional | role contracts, persona boundaries, handoff posture, memory/evaluation posture at agent layer | `README.md`, target role docs, generated registry surfaces, `AGENTS.md` | repo-local validation documented in the repo | role blur, handoff drift, agent layer swallowing skills/playbooks/evals | the task mainly changes workflows or proof doctrine |
| `aoa-playbooks` | workflow | scenario-level composition and recurring operational routes | repo `AGENTS.md`, `README.md` | repo-local validation documented in the repo | playbook swallowing skill canon, scenario ambiguity, unclear evidence posture | the task is still only a bounded single workflow |
| `aoa-kag` | meaning | derived provenance-aware substrate, graph-ready and retrieval-ready projections | repo `AGENTS.md`, `README.md` | repo-local validation documented in the repo | derived layer claiming authored source authority | the task mainly changes authored source meaning |
| profile repo (`8Dionysus/README.md`) | constitutional | public entry surface and orientation only | profile `README.md`, `GLOSSARY.md`, `Agents-of-Abyss` | manual consistency review against center docs | mirror drift, summary outrunning the center | the task changes core definitions rather than public orientation |

## Drift signatures worth flagging immediately

### Constitutional drift

- a center or routing surface starts owning layer detail
- a summary or mirror states stronger ownership than the source repository
- neighboring repositories are described inconsistently
- generated registry or index surfaces change without source docs changing

### Runtime drift

- localhost binds change to wider exposure
- public-safe examples drift toward live runtime secrets
- profile, preset, or module edits are not reflected in render/bootstrap checks
- Fedora runtime root and Windows source path assumptions get confused

### Workflow drift

- runnable entrypoints change without smoke validation
- dry-run defaults quietly weaken
- new dependencies, services, or auth paths appear without explicit review
- public docs leak workstation-specific paths, tokens, or local state

### Meaning drift

- source, extraction, interpretation, and synthesis get flattened together
- derived substrate starts reading like authored source truth
- provenance, lineage, or context disappears

### Proof drift

- an eval implies more than its evidence carries
- verdict shape no longer matches the bounded claim
- caveats disappear while metrics stay

## Routing rule

When in doubt, do not patch across repository boundaries.

Instead:

1. name the owning repository,
2. state the boundary clearly,
3. make the smallest local routing fix if needed,
4. leave the owned semantic change to the correct repository.
