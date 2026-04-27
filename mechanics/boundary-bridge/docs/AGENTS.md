# AGENTS.md

## Applies to

This card applies to `mechanics/boundary-bridge/docs/` and all descendant
source documents.

## Role

`docs/` holds detailed center-source doctrine and ToS-support source notes for
the `boundary-bridge` mechanic. The package `README.md` and active `parts/`
remain the default operating route.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`,
`mechanics/boundary-bridge/AGENTS.md`,
`mechanics/boundary-bridge/README.md`, and the specific source document you are
changing.

## Boundaries

- Keep detailed doctrine package-local and linked through `PROVENANCE.md` when
  it becomes source context for active parts.
- Do not create owner-local activation claims, runtime claims, proof verdicts,
  memory objects, role contracts, playbook choreography, KAG canon, or
  ToS-authored meaning here.
- If this document becomes historical, route it through landing, trace, or
  legacy posture instead of deleting provenance.
- If this document creates a request to a stronger owner, update
  `../OWNER_REQUESTS.md` and the owner-request queue rather than pretending the
  owner accepted it.

## Validation

Use the validation lane in [../AGENTS.md](../AGENTS.md#validation).

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/boundary-bridge/docs/TOS_BRIDGE_OWNER_REPO_REQUESTS.md`

```bash
python scripts/validate_owner_request_queue.py --mechanic boundary-bridge
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic boundary-bridge
python scripts/validate_mechanics_topology.py --mechanic boundary-bridge
```

<!-- centralized-child-validation:end -->

## Closeout

Report source docs changed, package README or registry updates needed,
generated mirrors rebuilt or not rebuilt, owner-request status affected, and
checks run or skipped.
