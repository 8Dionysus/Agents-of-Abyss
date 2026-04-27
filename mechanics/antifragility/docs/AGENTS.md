# AGENTS.md

## Applies to

This card applies to `mechanics/antifragility/docs/` and all descendant source documents.

## Role

`mechanics/antifragility/docs/` holds detailed center-source doctrine and
stop-lines for the `Antifragility` mechanic. The package `README.md` remains
the entry card; active operation routes through package `PARTS.md`.

## Read before editing

Read root `AGENTS.md`, `mechanics/AGENTS.md`, `mechanics/antifragility/AGENTS.md`,
`mechanics/antifragility/README.md`, and the specific source document you are changing. If a
generated surface mirrors this document, read the builder and validator before editing.

## Boundaries

- Keep detailed doctrine package-local and linked from the package README when it becomes an entry path.
- Do not create owner-local activation claims, runtime claims, proof verdicts, memory objects, role contracts, playbook choreography, KAG canon, or ToS-authored meaning here.
- If this document becomes historical, route it through landing, trace, or legacy posture instead of deleting provenance.
- If this document creates a request to a stronger owner, update
  `mechanics/antifragility/OWNER_REQUESTS.md` and the owner-request queue rather
  than pretending the owner accepted it.

## Validation

Use the validation lane in
[`mechanics/antifragility/AGENTS.md`](../AGENTS.md#validation).

<!-- centralized-child-validation:start -->

### Centralized Child Validation

Executable validation commands from child docs live here. Child docs should
route to this section instead of carrying command blocks.

#### `mechanics/antifragility/docs/ANTIFRAGILITY_OWNER_REPO_REQUESTS.md`

```bash
python mechanics/antifragility/scripts/validate_antifragility_distillation.py
python scripts/validate_owner_request_queue.py --mechanic antifragility
python scripts/build_owner_request_queue.py --check
python scripts/validate_generated_owner_request_queue.py
python scripts/validate_owner_request_docs.py --mechanic antifragility
python scripts/validate_mechanics_topology.py --mechanic antifragility
```

<!-- centralized-child-validation:end -->

## Closeout

Report source docs changed, package README or registry updates needed,
generated mirrors rebuilt or not rebuilt, owner-request status affected, and
checks run or skipped.
