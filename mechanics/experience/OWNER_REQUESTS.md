# Experience Owner-repo Requests

This is the center-side request packet list for `experience`.

It names the stronger owner slices that must land outside `Agents-of-Abyss` before `experience` may be treated as operational beyond center doctrine, routes, and stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance. It may be copied into an owner-local issue, document, branch, or receipt, but it remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../owner-request-queue.json)

Generated companion: [`generated/owner_request_queue.min.json`](../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-EXPERIENCE-STACK-001` | `abyss-stack` | `requested` | `P0` | Living workspace runtime and office infrastructure | Owner-local runtime surface for workspace services, storage, lifecycle, and operational gates. | Runtime activation requires infrastructure receipts and proof routes before public claims. |
| `ORQ-EXPERIENCE-MEMO-001` | `aoa-memo` | `requested` | `P0` | Experience memory, provenance, recall, and continuity loom objects | Memory objects for friction, incidents, continuity anchors, witness posture, and recall boundaries. | Memory integrity and retention claims route to `aoa-evals`. |
| `ORQ-EXPERIENCE-ROUTING-001` | `aoa-routing` | `requested` | `P1` | Context router and live route behavior for experience flows | Routing surface for context selection, salience, budget, handoff, and route receipts. | Routing behavior proof routes to `aoa-evals`. |
| `ORQ-EXPERIENCE-EVALS-001` | `aoa-evals` | `requested` | `P0` | Adoption proof, certification checks, and regression evidence | Proof bundle for adoption gates, certification watchtower checks, incidents, and regression posture. | Proof itself lands in `aoa-evals`. |
| `ORQ-EXPERIENCE-AGENTS-001` | `aoa-agents` | `requested` | `P1` | Office, role-pair, actor, and handoff posture | Role contracts for offices, service assistants, role pairs, jurisdiction, and handoff boundaries. | Role claim proof routes to `aoa-evals` when public or operational. |
| `ORQ-EXPERIENCE-KAG-001` | `aoa-kag` | `requested` | `P2` | Derived workspace and experience-ready knowledge projections | Provenance-aware derived lifts from accepted source surfaces without source-authority transfer. | Derived-readiness claims route to `aoa-evals`. |
| `ORQ-EXPERIENCE-TOS-001` | `Tree-of-Sophia` | `requested` | `P1` | ToS meaning boundaries touched by experience contracts | ToS-owned source or concept node decision whenever experience surfaces touch Sophian meaning. | AoA can only support; ToS-owned acceptance is the authority. |
| `ORQ-EXPERIENCE-PLAYBOOKS-001` | `aoa-playbooks` | `requested` | `P1` | Experience adoption, release, office, and service choreography | Playbook-owned route for adoption, release dry-runs, rollback drills, office follow-through, and service choreography. | Scenario outcomes and public claims route to `aoa-evals` before promotion. |
| `ORQ-EXPERIENCE-SDK-001` | `aoa-sdk` | `requested` | `P1` | Typed install, runtime, train, and helper API carriers for Experience routes | SDK-owned helper or API surface that carries Experience route packets without becoming semantic, runtime, or owner-acceptance authority. | Compatibility evidence routes through `aoa-evals` when helper claims become public or operational. |
| `ORQ-EXPERIENCE-STATS-001` | `aoa-stats` | `requested` | `P2` | Experience dashboards, watch summaries, and derived movement readouts | Stats-owned summary surfaces for certification, adoption, release, office, and service movement. | Stats summaries are not proof; proof routes to `aoa-evals` and owner-local receipts. |
| `ORQ-EXPERIENCE-SKILLS-001` | `aoa-skills` | `requested` | `P2` | Experience receipt, adoption, release, and service operation skills | Skill-owned workflow with trigger, procedure, risks, verification, and stop-lines for Experience operations or receipt generation. | Workflow quality and public claims route to `aoa-evals` before promotion. |
| `ORQ-EXPERIENCE-TECHNIQUES-001` | `aoa-techniques` | `requested` | `P2` | Reusable Experience adoption, deployment, office, and service practice | Technique-owned reusable practice note that extracts repeatable Experience method without carrying owner-local truth or runtime authority. | Technique usefulness routes through `aoa-evals` or reviewed owner receipts when claims become public. |

## Center sources

- [README.md](README.md)
- [DIRECTION.md](DIRECTION.md)
- [PARTS.md](PARTS.md)
- [adoption-federation contract](parts/adoption-federation/CONTRACT.md)
- [certification-proof contract](parts/certification-proof/CONTRACT.md)
- [continuity-context contract](parts/continuity-context/CONTRACT.md)
- [office-operations contract](parts/office-operations/CONTRACT.md)
- [release-deployment contract](parts/release-deployment/CONTRACT.md)
- [service-mesh contract](parts/service-mesh/CONTRACT.md)
- [runtime-boundary contract](parts/runtime-boundary/CONTRACT.md)
- [compatibility-bridges contract](parts/compatibility-bridges/CONTRACT.md)

Use [PROVENANCE](PROVENANCE.md) only when auditing how a center source was
distilled; do not treat archive accounting as owner acceptance.

## Stop-lines

- `ORQ-EXPERIENCE-STACK-001`: The center must not claim experience runtime until runtime owner gates land.
- `ORQ-EXPERIENCE-MEMO-001`: The center must not claim hidden memory sovereignty.
- `ORQ-EXPERIENCE-ROUTING-001`: The center must not claim live router engine authority.
- `ORQ-EXPERIENCE-EVALS-001`: The center must not claim operational Experience adoption until evidence is owner-local.
- `ORQ-EXPERIENCE-AGENTS-001`: The center must not create hybrid-agent authority.
- `ORQ-EXPERIENCE-KAG-001`: `aoa-kag` projections must not become source-authored meaning.
- `ORQ-EXPERIENCE-TOS-001`: The center must not write ToS canon.
- `ORQ-EXPERIENCE-PLAYBOOKS-001`: The center must not claim recurring Experience choreography or owner-followthrough playbook truth.
- `ORQ-EXPERIENCE-SDK-001`: The center must not claim SDK helper availability, install API truth, or typed runtime authority.
- `ORQ-EXPERIENCE-STATS-001`: The center must not treat Experience dashboards or stats summaries as proof, certification, or owner acceptance.
- `ORQ-EXPERIENCE-SKILLS-001`: The center must not claim executable Experience skill truth or approval authority.
- `ORQ-EXPERIENCE-TECHNIQUES-001`: The center must not turn Experience technique hints into canonical reusable practice without technique-owner landing.

## Validation

Use the validation lane in [mechanics/experience/AGENTS.md](AGENTS.md#validation) for executable commands.

## Next route

Carry the request ID into the owner repository. Do not promote center language to owner-local truth without owner acceptance, owner landing, and proof where proof is required.
