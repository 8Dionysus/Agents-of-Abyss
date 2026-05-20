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

Use `candidates/` for proposed memory, `receipts/` for review or handoff traces,
`exports/` for packets meant for `aoa-memo`, and `local/` for center-local
memory that should stay here for now.

## Validation

For local candidate checks through the stack MCP access plane:

```bash
AOA_ABYSS_STACK_ROOT="${AOA_ABYSS_STACK_ROOT:-$HOME/src/abyss-stack}"
PYTHONPATH="$AOA_ABYSS_STACK_ROOT/MCP/aoa-memo-mcp/src" python -m aoa_memo_mcp.cli brief --repo Agents-of-Abyss --intent "local memory route"
```

For release-facing center changes, run:

```bash
python scripts/release_check.py
```

## Closeout

Report candidate path, evidence refs, validation result, and whether the item
stayed local or was exported for reviewed intake.
