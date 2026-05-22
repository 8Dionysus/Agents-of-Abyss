# AGENTS.md

## Applies to

This card applies to `memo/`.

## Role

`memo/` is the Agents-of-Abyss local memory port. It holds center-local memory
candidates, receipts, exports, and local notes before reviewed landing in
`aoa-memo`.

## Read before editing

1. Root `AGENTS.md`
2. `DESIGN.md`
3. `docs/FEDERATION_RULES.md`
4. This `README.md`
5. `aoa-memo` memory operation contracts when a candidate should move centrally

## Boundaries

Use this port for `write_candidate_only` work. Do not turn local notes into
center doctrine or durable memory without `aoa-memo` review.

Use `PORT.yaml` for the local port contract and `INDEX.md` / `index.min.json`
as generated read models. Use `candidates/` for proposed memory, `receipts/`
for review or handoff traces, `exports/` for packets meant for `aoa-memo`, and
`local/` for center-local memory that should stay here for now.

## Candidate Route

Create center-local candidates through the stack MCP helper from the
`abyss-stack` source checkout:

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli create-candidate \
  --repo Agents-of-Abyss \
  --evidence-ref docs/FEDERATION_RULES.md \
  --claim "Agents-of-Abyss memory should move through reviewed local candidates before aoa-memo landing."
```

Then validate the emitted candidate path:

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli validate-candidate path/to/candidate.json
```

## Reviewed Landing Route

When an export is ready to move from this local port toward durable reviewed
memory, inspect it through the same MCP access plane:

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli pending-exports --repo Agents-of-Abyss
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli landing-plan --repo Agents-of-Abyss --export-ref exports/path.reviewed-intake.json --run-dry-run
```

The landing plan is a readiness/dry-run route. The actual durable memory object
lands only in `aoa-memo` through its reviewed intake script, generated read
models, validators, and review.

## Validation

For local candidate checks through the stack MCP access plane:

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/mcp/services/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli brief --repo Agents-of-Abyss --intent "local memory route"
AOA_MEMO_ROOT="${AOA_MEMO_ROOT:-/srv/AbyssOS/aoa-memo}"
python "$AOA_MEMO_ROOT/scripts/memory/validate_local_memo_port.py" --path memo
python "$AOA_MEMO_ROOT/scripts/memory/build_local_memo_port_index.py" --path memo --check
```

For release-facing center changes, run:

```bash
python scripts/release_check.py
```

## Closeout

Report candidate path, evidence refs, validation result, and whether the item
stayed local, was exported for reviewed intake, or was landed in `aoa-memo`.
