# RPG Owner-repo Requests

This is the center-side request packet list for `rpg`.

It names the stronger owner slices that must land outside `Agents-of-Abyss` before `rpg` may be treated as operational beyond center doctrine, routes, and stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance. It may be copied into an owner-local issue, document, branch, or receipt, but it remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../owner-request-queue.json)

Generated companion: [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-RPG-AGENTS-001` | `aoa-agents` | `requested` | `P1` | Role, actor, and persona truth behind RPG reflection | Role contracts and actor-seat definitions that RPG reflection may reference without mutating. | Role claims route to `aoa-evals` where needed. |
| `ORQ-RPG-SKILLS-001` | `aoa-skills` | `requested` | `P1` | Skill and feat truth behind progression labels | Skill-owned object truth for feats, capability labels, triggers, and verification. | Skill claim proof routes to `aoa-evals`. |
| `ORQ-RPG-PLAYBOOKS-001` | `aoa-playbooks` | `requested` | `P1` | Campaign, scenario, and questline choreography | Playbook-owned campaign route, scenario sequence, fallback posture, and expected evidence. | Scenario progress proof routes to `aoa-evals`. |
| `ORQ-RPG-EVALS-001` | `aoa-evals` | `requested` | `P1` | Progression proof and evidence-backed advancement | Eval surface for whether advancement, capability, or progress claims are defensible. | Proof lives in `aoa-evals`. |
| `ORQ-RPG-STACK-001` | `abyss-stack` | `requested` | `P3` | Runtime ledger or session-state support after gates | Runtime ledger or state surface only after role, proof, and scenario owners have landed boundaries. | Runtime evidence routes through infrastructure receipts and evals. |
| `ORQ-RPG-STATS-001` | `aoa-stats` | `requested` | `P2` | Derived progression summaries | Derived summary windows over owner-local proof, role, skill, and quest receipts. | Stats claims cite evals and owner receipts. |

## Ready-to-carry packets

These cards are portable handoff maps. They may be copied into an owner-local issue, document, branch, or receipt with the request ID intact. They do not mark the request accepted, landed, proved, or activated.

### ORQ-RPG-AGENTS-001

Carry to: `aoa-agents`

Status: `requested`, not accepted.

Center asks for: owner-local role, actor-seat, and persona contract language that RPG may reference as reflection without rewriting role truth.

Why this owner: `aoa-agents` owns role contracts, actor posture, persona boundaries, and handoff behavior; RPG can only read them.

Center sources:

- `mechanics/rpg/README.md`
- `mechanics/rpg/PARTS.md`
- `mechanics/rpg/parts/source-boundary/README.md`
- `mechanics/rpg/parts/progression-unlocks/README.md`
- `mechanics/rpg/parts/owner-handoffs/README.md`

Owner landing should decide: which role, class, origin, party-seat, or persona labels are safe to expose as RPG reflection and which remain owner-private or unsupported.

Acceptance signal: an `aoa-agents` issue, document, branch, or receipt names `ORQ-RPG-AGENTS-001`, accepts the bounded slice, and states the role-canon boundary.

Proof route: role claims route to `aoa-evals` where evidence or public advancement claims are needed.

Stop-lines:

- RPG reflection must not mutate role canon.
- Center docs must not assign classes, origins, party seats, or personas as accepted role truth.
- Acceptance must not imply progression proof.

Do not carry as: a request for RPG to own roles, personas, actor status, or agent progression.

Return receipt: update `mechanics/owner-request-queue.json` `owner_landing_ref` or `owner_proof_ref` only after an owner-local receipt exists, then rebuild `generated/owner_request_queue.min.json`.

### ORQ-RPG-SKILLS-001

Carry to: `aoa-skills`

Status: `requested`, not accepted.

Center asks for: skill-owned ability and feat truth that RPG may display as capability reflection without creating skill objects in the center.

Why this owner: `aoa-skills` owns bounded execution workflows and skill-shaped objects; RPG may only name a readable ability layer around accepted skill truth.

Center sources:

- `mechanics/rpg/README.md`
- `mechanics/rpg/USAGE.md`
- `mechanics/rpg/parts/progression-unlocks/README.md`
- `mechanics/rpg/parts/vocabulary-overlay/TERMINOLOGY.md`
- `mechanics/rpg/parts/owner-handoffs/README.md`

Owner landing should decide: which skill objects, triggers, verification rules, ability labels, or feat reflections can be referenced by RPG without widening skill canon.

Acceptance signal: an `aoa-skills` issue, document, branch, or receipt names `ORQ-RPG-SKILLS-001`, accepts the bounded slice, and states how skill truth remains owner-local.

Proof route: skill claim proof routes to `aoa-evals` before public capability, unlock, or readiness claims.

Stop-lines:

- RPG labels must not become skill canon.
- Center docs must not declare abilities, feats, equipped skills, or reusable workflows accepted.
- Pack, loadout, and ability language must not become runtime inventory.

Do not carry as: a request for RPG to define skills, promote techniques, or activate workflows.

Return receipt: update `mechanics/owner-request-queue.json` `owner_landing_ref` or `owner_proof_ref` only after an owner-local receipt exists, then rebuild `generated/owner_request_queue.min.json`.

### ORQ-RPG-PLAYBOOKS-001

Carry to: `aoa-playbooks`

Status: `requested`, not accepted.

Center asks for: playbook-owned campaign, scenario, questline, and party choreography surfaces that RPG may read as campaign structure.

Why this owner: `aoa-playbooks` owns recurring scenario composition and route choreography; RPG can make that work legible as campaign but cannot own execution truth.

Center sources:

- `mechanics/rpg/README.md`
- `mechanics/rpg/USAGE.md`
- `mechanics/rpg/parts/quest-campaign/README.md`
- `mechanics/rpg/parts/quest-campaign/PLAYABLE_OBLIGATION.md`
- `mechanics/rpg/parts/owner-handoffs/README.md`

Owner landing should decide: which campaign routes, scenario sequences, fallback postures, party patterns, and expected evidence can receive RPG readings.

Acceptance signal: an `aoa-playbooks` issue, document, branch, or receipt names `ORQ-RPG-PLAYBOOKS-001`, accepts the bounded slice, and states the campaign choreography boundary.

Proof route: scenario progress proof routes to `aoa-evals` before progress, unlock, or public campaign claims.

Stop-lines:

- The center must not own campaign execution truth.
- RPG questline language must not close quests or reorder playbook-owned choreography.
- Campaign labels must not imply runtime session state.

Do not carry as: a request for RPG to own playbooks, scenario order, quest closure, or long-running campaign execution.

Return receipt: update `mechanics/owner-request-queue.json` `owner_landing_ref` or `owner_proof_ref` only after an owner-local receipt exists, then rebuild `generated/owner_request_queue.min.json`.

### ORQ-RPG-EVALS-001

Carry to: `aoa-evals`

Status: `requested`, not accepted.

Center asks for: eval-owned proof surfaces for RPG progression, advancement, unlock, readiness, and capability claims.

Why this owner: `aoa-evals` owns proof, verdict, regression, and claim discipline; RPG may frame a trial or unlock question but cannot issue proof.

Center sources:

- `mechanics/rpg/README.md`
- `mechanics/rpg/USAGE.md`
- `mechanics/rpg/parts/source-boundary/README.md`
- `mechanics/rpg/parts/progression-unlocks/README.md`
- `mechanics/rpg/parts/quest-campaign/examples/playable-obligation-route.md`

Owner landing should decide: what evidence, regression posture, verdict boundary, and claim language can support RPG-facing progression or unlock readings.

Acceptance signal: an `aoa-evals` issue, document, branch, or receipt names `ORQ-RPG-EVALS-001`, accepts the bounded slice, and states how eval verdicts constrain RPG claims.

Proof route: proof lives in `aoa-evals`; RPG references proof routes and does not defend verdicts itself.

Stop-lines:

- The center must not treat RPG progression as proof.
- RPG must not claim rank, unlock, reputation, capability, or trial success without owner proof.
- A request status is not evidence.

Do not carry as: a request for RPG to create proof authority, verdicts, regression judgment, or public claim backing.

Return receipt: update `mechanics/owner-request-queue.json` `owner_landing_ref` or `owner_proof_ref` only after an owner-local receipt exists, then rebuild `generated/owner_request_queue.min.json`.

### ORQ-RPG-STACK-001

Carry to: `abyss-stack`

Status: `requested`, not accepted.

Center asks for: runtime-owned RPG projection, session-state, or ledger surfaces only after role, proof, and scenario boundaries are accepted by their owners.

Why this owner: `abyss-stack` owns runtime, services, storage, lifecycle, and frontend projection; center RPG docs can only state projection needs.

Center sources:

- `mechanics/rpg/README.md`
- `mechanics/rpg/USAGE.md`
- `mechanics/rpg/parts/runtime-projection/README.md`
- `mechanics/rpg/parts/vocabulary-overlay/TERMINOLOGY.md`
- `mechanics/rpg/parts/owner-handoffs/README.md`

Owner landing should decide: whether any runtime read model, session state, display bundle, ledger, or frontend projection can exist and which source/proof/runtime precedence it must preserve.

Acceptance signal: an `abyss-stack` issue, document, branch, or receipt names `ORQ-RPG-STACK-001`, accepts the bounded slice, and states runtime state, storage, service, and projection boundaries.

Proof route: runtime evidence routes through infrastructure receipts and evals before public claims or activation language.

Stop-lines:

- RPG must not become a runtime ledger inside the center.
- Center docs must not claim live RPG runtime, session state, equipped loadout, or frontend activation.
- Runtime projection must preserve canonical keys and source/proof/runtime/presentation precedence.

Do not carry as: a request for center docs to run services, store state, own ledgers, or activate UI behavior.

Return receipt: update `mechanics/owner-request-queue.json` `owner_landing_ref` or `owner_proof_ref` only after an owner-local receipt exists, then rebuild `generated/owner_request_queue.min.json`.

### ORQ-RPG-STATS-001

Carry to: `aoa-stats`

Status: `requested`, not accepted.

Center asks for: stats-owned derived RPG progression summaries over owner-local proof, role, skill, quest, and runtime receipts.

Why this owner: `aoa-stats` owns derived observability and movement summaries; RPG can read summaries but cannot turn them into authority.

Center sources:

- `mechanics/rpg/README.md`
- `mechanics/rpg/USAGE.md`
- `mechanics/rpg/parts/progression-unlocks/README.md`
- `mechanics/rpg/parts/vocabulary-overlay/TERMINOLOGY.md`
- `mechanics/rpg/parts/owner-handoffs/README.md`

Owner landing should decide: which derived windows, source inputs, proof refs, rollup labels, and disclaimers keep RPG progression summaries non-authoritative.

Acceptance signal: an `aoa-stats` issue, document, branch, or receipt names `ORQ-RPG-STATS-001`, accepts the bounded slice, and states the derived-summary boundary.

Proof route: stats claims cite evals and owner receipts; stats do not become proof or progression authority.

Stop-lines:

- Stats must not become progress authority.
- RPG must not collapse proof, memory, runtime, role, skill, or quest signals into a single power score.
- Derived summaries must stay source-linked and reversible.

Do not carry as: a request for stats to judge advancement, issue verdicts, own reputation truth, or replace evals.

Return receipt: update `mechanics/owner-request-queue.json` `owner_landing_ref` or `owner_proof_ref` only after an owner-local receipt exists, then rebuild `generated/owner_request_queue.min.json`.

## Center sources

- [README.md](README.md)
- [PARTS.md](PARTS.md)
- [source-boundary](parts/source-boundary/README.md)
- [progression-unlocks](parts/progression-unlocks/README.md)
- [quest-campaign](parts/quest-campaign/README.md)
- [runtime-projection](parts/runtime-projection/README.md)
- [owner-handoffs](parts/owner-handoffs/README.md)

## Stop-lines

- `ORQ-RPG-AGENTS-001`: RPG reflection must not mutate role canon.
- `ORQ-RPG-SKILLS-001`: RPG labels must not become skill canon.
- `ORQ-RPG-PLAYBOOKS-001`: The center must not own campaign execution truth.
- `ORQ-RPG-EVALS-001`: The center must not treat RPG progression as proof.
- `ORQ-RPG-STACK-001`: RPG must not become a runtime ledger inside the center.
- `ORQ-RPG-STATS-001`: Stats must not become progress authority.

## Validation

Use the validation lane in [mechanics/rpg/AGENTS.md](AGENTS.md#validation) for executable commands.

## Next route

Carry the request ID into the owner repository. Do not promote center language to owner-local truth without owner acceptance, owner landing, and proof where proof is required.
