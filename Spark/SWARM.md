# Spark Swarm Recipe — Agents-of-Abyss

Рекомендуемый путь назначения: `Spark/SWARM.md`

## Для чего этот рой
Используй Spark здесь очень бережно: для ecosystem registry, layer map coherence, boundary language drift, link cleanup и micro-patches в canonical center-layer surfaces. Этот рой не должен переписывать AoA doctrine целиком и не должен тянуть сюда layer-owned meaning.

## Читать перед стартом
- `README.md`
- `CHARTER.md`
- `ECOSYSTEM_MAP.md`
- `docs/LAYERS.md`
- `docs/FEDERATION_RULES.md`
- `ROADMAP.md`

## Форма роя
- **Coordinator**: выбирает один center-layer seam
- **Drift Auditor**: ищет inconsistency между README / CHARTER / map / rules
- **Micro-Patcher**: делает минимальный patch
- **Verifier**: запускает `python scripts/validate_ecosystem.py`
- **Boundary Keeper**: следит за ecosystem truth vs layer truth

## Параллельные дорожки
- Lane A: registry / role / ownership wording
- Lane B: link and cross-doc consistency
- Lane C: validate center-layer surface
- Не запускай больше одного пишущего агента на одну и ту же семью файлов.

## Allowed
- чинить `generated/ecosystem_registry.min.json` aligned surfaces
- прояснять repository roles и center-layer ownership assumptions
- устранять boundary-language drift
- делать micro-patches ради legibility и coherence

## Forbidden
- тащить сюда technique/skill/eval/memo/agent/runtime specifics как primary meaning
- переписывать сразу полдоктрины
- размывать distinction between ecosystem truth and layer truth
- пытаться лечить sibling-layer bugs inside the center repo

## Launch packet для координатора
```text
We are working in Agents-of-Abyss with a one-repo one-swarm setup.
Pick exactly one center-layer seam:
- ecosystem registry
- repository role wording
- ownership boundary drift
- link / cross-doc consistency
- one minimal canonical clarification

Return:
1. the seam
2. exact files to touch
3. whether generated registry is affected
4. which layer-owned meanings must remain untouched
```

## Промпт для Scout
```text
Audit only. Do not edit.
Return:
- exact inconsistency or drift
- files involved
- whether the problem lives here or actually belongs in a sibling layer repo
- impact on ecosystem legibility
- validation implications
```

## Промпт для Builder
```text
Make the smallest patch possible.
Rules:
- preserve this repo as the constitutional and ecosystem-center statement
- keep layer ownership boundaries explicit
- do not absorb sibling layer meaning
- prefer micro-patches over sweeping rewrites
```

## Промпт для Verifier
```text
Run:
- python scripts/validate_ecosystem.py
Then report:
- commands run
- whether the ecosystem registry changed
- whether repository roles and ownership assumptions stayed coherent
```

## Промпт для Boundary Keeper
```text
Review only for anti-scope.
Check:
- ecosystem truth remained separate from layer truth
- no specialized layer meaning was absorbed
- patch stayed canonical and high-level
- any required sibling-repo follow-up is named explicitly
```

## Verify
```bash
python scripts/validate_ecosystem.py
```

## Done when
- один center-layer seam стал яснее и когерентнее
- validator реально прогнан
- specialized layer meaning не был затянут в центр
- любые sibling follow-ups названы явно

## Handoff
Если inconsistency живёт в одном из layer repos, фикси её там и потом возвращайся только для center-layer wording sync.
