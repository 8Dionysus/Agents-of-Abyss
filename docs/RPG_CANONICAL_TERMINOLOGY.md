# RPG Canonical Terminology

This note fixes the canonical machine vocabulary for the runtime/frontend RPG contour.

The rule is simple:

- the machine vocabulary stays stable
- the frontend may theme it
- the themed label never replaces the canonical key

## Identity terms

| Canonical key | Meaning | Primary owner | Presentation note |
|---|---|---|---|
| `class_archetype` | RPG-facing reflection of an agent role profile | `aoa-agents` upstream, runtime snapshot downstream | theme as class / vocation / path |
| `execution_origin` | runtime-side origin of execution, wrapper, and model posture | `abyss-stack` | theme as origin / lineage / vessel |
| `rank` | reviewed progression label summarizing evidence-backed mastery posture | `aoa-agents` progression overlay, runtime snapshot downstream | theme as rank / tier / standing |

## Mastery axes

| Canonical key | Meaning | Primary owner | Presentation note |
|---|---|---|---|
| `boundary_integrity` | respect for repo ownership and contract seams | `aoa-agents` progression overlay | theme as boundary / discipline / guard |
| `execution_reliability` | bounded changes that survive verification | `aoa-agents` progression overlay | theme as craft / execution / force |
| `change_legibility` | readable diffs, handoffs, summaries, state deltas | `aoa-agents` progression overlay | theme as clarity / legibility / signal |
| `review_sharpness` | finding drift, contradiction, and regression | `aoa-agents` progression overlay | theme as review / judgment / vigilance |
| `proof_discipline` | claim-to-evidence coherence | `aoa-agents` progression overlay plus `aoa-evals` evidence | theme as proof / rigor / oath |
| `provenance_hygiene` | source-of-truth, lineage, and traceability hygiene | `aoa-agents` progression overlay and `aoa-memo` witness posture | theme as lineage / provenance / memory-cleanliness |
| `deep_readiness` | capacity for high-ambiguity or arbitration routes when truly needed | `aoa-agents` progression overlay | theme as depth / arcana / abyssal readiness |

## Derived gameplay stats

| Canonical key | Meaning | Runtime owner | Presentation note |
|---|---|---|---|
| `difficulty_ceiling` | highest safe difficulty class currently unlocked | `abyss-stack` snapshot from progression evidence | theme as level cap / expedition tier |
| `risk_ceiling` | highest safe risk class currently unlocked | `abyss-stack` snapshot from progression evidence | theme as risk tolerance / hazard lane |
| `allowed_control_modes` | control postures currently permitted for this build | `abyss-stack` | theme as leash / command posture / autonomy gates |
| `handoff_accuracy` | derived confidence in clean handoff behavior | `abyss-stack` | theme as relay / baton discipline |
| `reanchor_resilience` | derived resilience when governed return is needed | `abyss-stack` | theme as recovery / return strength |
| `campaign_stability` | derived fit for long-horizon scenario work | `abyss-stack` | theme as campaign fitness / endurance |

## Runtime resources

| Canonical key | Meaning | Runtime owner | Presentation note |
|---|---|---|---|
| `integrity_budget` | current and max budget for safe operational integrity | `abyss-stack` | theme as health / integrity |
| `focus_budget` | current and max budget for bounded concentrated work | `abyss-stack` | theme as stamina / focus |
| `deep_budget` | current and max budget for rare high-cost deep routes | `abyss-stack` | theme as mana / depth |
| `recall_budget` | current and max budget for recall-heavy routes | `abyss-stack` | theme as memory / recall |
| `autonomy_budget` | current and max budget for self-driven action under current control posture | `abyss-stack` | theme as autonomy / resolve |

## Loadout and equipment terms

| Canonical key | Meaning | Primary owner | Presentation note |
|---|---|---|---|
| `equipped_ability_ids` | active bounded workflows currently loaded | runtime snapshot from `aoa-skills` reflections | theme as active skills / hotbar |
| `passive_feat_ids` | passive reusable-practice modifiers currently loaded | runtime snapshot from `aoa-techniques` reflections | theme as passives / feats / perks |
| `artifact_ids` | durable runtime-side modifiers or tokens | runtime only for now | theme as artifacts / relics |
| `toolset_refs` | runtime tool bundles and wrappers | `abyss-stack` | theme as gear / kit |
| `pack_profiles` | packaged execution posture hints from skill layer | `aoa-skills` upstream, runtime snapshot downstream | theme as loadout set / kit profile |
| `adapter_posture` | portability vs local-adapter posture | `aoa-skills` upstream, runtime snapshot downstream | theme as attunement / portability stance |

## Quest and campaign terms

| Canonical key | Meaning | Primary owner | Presentation note |
|---|---|---|---|
| `quest_ref` | stable quest object reference | source quest owner | theme as quest / mission |
| `quest_state_hint` | non-authoritative runtime hint about likely next quest state | `abyss-stack` | theme as state omen / likely status |
| `campaign_ref` | playbook-owned questline or campaign reference | `aoa-playbooks` | theme as campaign lane / saga |
| `party` | current group of agents engaged in one run | `abyss-stack` runtime envelope | theme as party / cohort |
| `orchestrator_kind` | explicit orchestrator type | `abyss-stack` | theme as conductor / orchestrator |

## Reputation axes

| Canonical key | Meaning | Runtime owner | Presentation note |
|---|---|---|---|
| `proof_trust` | trust in proof-linked output | `abyss-stack` ledger from eval evidence | theme as proof reputation |
| `handoff_trust` | trust in clean handoff and relay behavior | `abyss-stack` ledger | theme as relay reputation |
| `provenance_trust` | trust in traceability and source hygiene | `abyss-stack` ledger | theme as lineage reputation |
| `campaign_discipline` | trust in long-horizon scenario discipline | `abyss-stack` ledger | theme as campaign reputation |
| `boundary_trust` | trust in ownership and authority adherence | `abyss-stack` ledger | theme as boundary reputation |
| `review_trust` | trust in review quality and caution posture | `abyss-stack` ledger | theme as review reputation |

## Required keys for the first frontend minimum

The first stable frontend minimum SHOULD support labels for:

- `class_archetype`
- `execution_origin`
- `rank`
- all seven mastery axes
- all five runtime resources
- `inspect`
- `expand`
- `handoff`
- `verify`
- `reanchor`
- all six reputation axes

These keys are required by `dual_vocabulary_overlay_v1`.

## Final rule

The frontend may sing.

The canonical keys keep the score.
