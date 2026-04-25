# RPG Owner-repo Requests

This is the center-side request packet list for `rpg`.

It names the stronger owner slices that must land outside `Agents-of-Abyss` before `rpg` may be treated as operational beyond center doctrine, routes, and stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance. It may be copied into an owner-local issue, document, branch, or receipt, but it remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../../../mechanics/owner-request-queue.json)

Generated companion: [`generated/owner_request_queue.min.json`](../../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-RPG-AGENTS-001` | `aoa-agents` | `requested` | `P1` | Role, actor, and persona truth behind RPG reflection | Role contracts and actor-seat definitions that RPG reflection may reference without mutating. | Role claims route to `aoa-evals` where needed. |
| `ORQ-RPG-SKILLS-001` | `aoa-skills` | `requested` | `P1` | Skill and feat truth behind progression labels | Skill-owned object truth for feats, capability labels, triggers, and verification. | Skill claim proof routes to `aoa-evals`. |
| `ORQ-RPG-PLAYBOOKS-001` | `aoa-playbooks` | `requested` | `P1` | Campaign, scenario, and questline choreography | Playbook-owned campaign route, scenario sequence, fallback posture, and expected evidence. | Scenario progress proof routes to `aoa-evals`. |
| `ORQ-RPG-EVALS-001` | `aoa-evals` | `requested` | `P1` | Progression proof and evidence-backed advancement | Eval surface for whether advancement, capability, or progress claims are defensible. | Proof lives in `aoa-evals`. |
| `ORQ-RPG-STACK-001` | `abyss-stack` | `requested` | `P3` | Runtime ledger or session-state support after gates | Runtime ledger or state surface only after role, proof, and scenario owners have landed boundaries. | Runtime evidence routes through infrastructure receipts and evals. |
| `ORQ-RPG-STATS-001` | `aoa-stats` | `requested` | `P2` | Derived progression summaries | Derived summary windows over owner-local proof, role, skill, and quest receipts. | Stats claims cite evals and owner receipts. |

## Center sources

- [README.md](../../../mechanics/rpg/README.md)
- [RPG_LAYER_MODEL.md](../../../mechanics/rpg/docs/RPG_LAYER_MODEL.md)
- [RPG_BOUNDARY_MAP.md](../../../mechanics/rpg/docs/RPG_BOUNDARY_MAP.md)
- [RPG_ARCHITECTURE_RFC.md](../../../mechanics/rpg/docs/RPG_ARCHITECTURE_RFC.md)

## Stop-lines

- `ORQ-RPG-AGENTS-001`: RPG reflection must not mutate role canon.
- `ORQ-RPG-SKILLS-001`: RPG labels must not become skill canon.
- `ORQ-RPG-PLAYBOOKS-001`: The center must not own campaign execution truth.
- `ORQ-RPG-EVALS-001`: The center must not treat RPG progression as proof.
- `ORQ-RPG-STACK-001`: RPG must not become a runtime ledger inside the center.
- `ORQ-RPG-STATS-001`: Stats must not become progress authority.

## Validation

```bash
python scripts/validate_owner_request_queue.py --mechanic rpg
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic rpg
python scripts/validate_mechanics_topology.py --mechanic rpg
```

## Next route

Carry the request ID into the owner repository. Do not promote center language to owner-local truth without owner acceptance, owner landing, and proof where proof is required.
