# Method-growth Owner-repo Requests

This is the center-side request packet list for `method-growth`.

It names the stronger owner slices that must land outside `Agents-of-Abyss` before `method-growth` may be treated as operational beyond center doctrine, routes, and stop-lines.

## Owner request packet

Each request is a handoff candidate. A request packet is not owner acceptance. It may be copied into an owner-local issue, document, branch, or receipt, but it remains center-side until the owner repository accepts it.

Source queue: [`mechanics/owner-request-queue.json`](../../../mechanics/owner-request-queue.json)

Generated companion: [`generated/owner_request_queue.min.json`](../../../generated/owner_request_queue.min.json)

## Requests

| Request | Owner | Status | Priority | Slice | Required owner landing | Proof route |
|---|---|---|---|---|---|---|
| `ORQ-METHOD-SKILLS-001` | `aoa-skills` | `requested` | `P1` | Candidate skill identity and bounded execution shape | Owner-local candidate or skill-shaped object with trigger, procedure, risks, and verification boundaries. | Route proof to `aoa-evals` before promotion or public quality claims. |
| `ORQ-METHOD-SDK-001` | `aoa-sdk` | `requested` | `P2` | Provisional carry and typed helper hints | Typed helper seam or local-first carrier that can support candidate movement without owning meaning. | Compatibility evidence may route through `aoa-evals` when claims become public. |
| `ORQ-METHOD-DIONYSUS-001` | `Dionysus` | `requested` | `P1` | Seed staging for candidate objects before owner landing | Seed packet or staging trace that preserves origin, source context, and intended owner without declaring final truth. | Closure evidence should point back to owner landing and pruning receipts. |
| `ORQ-METHOD-EVALS-001` | `aoa-evals` | `requested` | `P1` | Proof route for promoted candidates and reusable method claims | Eval surface that states claim, evidence, blind spots, regression posture, and verdict boundary. | Proof itself is the owner-local landing route in `aoa-evals`. |
| `ORQ-METHOD-PLAYBOOKS-001` | `aoa-playbooks` | `requested` | `P1` | Recurring method choreography after repeated work stabilizes | Playbook-owned recurring route with decision points, fallback posture, and expected evidence. | Scenario outcomes should route to `aoa-evals` for claim discipline. |
| `ORQ-METHOD-MEMO-001` | `aoa-memo` | `requested` | `P2` | Lessons, memory, and pruning receipts after owner landing | Bounded memory object or lesson surface that records provenance, retention reason, and recall route. | Memory integrity and retention claims may route to `aoa-evals`. |

## Center sources

- [README.md](../../../mechanics/method-growth/README.md)
- [METHOD_SPINE.md](../../../mechanics/method-growth/docs/METHOD_SPINE.md)
- [REVIEWABLE_GROWTH_REFINERY.md](../../../mechanics/method-growth/docs/REVIEWABLE_GROWTH_REFINERY.md)
- [OWNER_LANDING_AND_PRUNING.md](../../../mechanics/method-growth/docs/OWNER_LANDING_AND_PRUNING.md)

## Stop-lines

- `ORQ-METHOD-SKILLS-001`: The center must not claim final skill truth or executable workflow activation.
- `ORQ-METHOD-SDK-001`: SDK helpers must not become constitutional authority or final object truth.
- `ORQ-METHOD-DIONYSUS-001`: `Dionysus` staging must not be read as final owner truth.
- `ORQ-METHOD-EVALS-001`: The center must not defend promotion claims without proof surfaces.
- `ORQ-METHOD-PLAYBOOKS-001`: The center must not become the scenario-method corpus.
- `ORQ-METHOD-MEMO-001`: The center must not hold primary memory truth.

## Validation

```bash
python scripts/validate_owner_request_queue.py --mechanic method-growth
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic method-growth
python scripts/validate_mechanics_topology.py --mechanic method-growth
```

## Next route

Carry the request ID into the owner repository. Do not promote center language to owner-local truth without owner acceptance, owner landing, and proof where proof is required.
