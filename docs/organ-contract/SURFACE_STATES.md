# Surface States

Surface states tell an agent how to treat a file, capsule, trace, or public
claim before trusting it.

Use the strongest state that actually applies. A surface may reference another
state, but it should not silently inherit that authority.

## State table

| State | Meaning | Stronger route |
|---|---|---|
| `source` | authored meaning or law for the owning surface | owner repository, mechanic, or district `AGENTS.md` |
| `generated` | deterministic or compact output derived from stronger source | builder, schema, validator, and source doc |
| `trace` | movement evidence, migration record, link repair, or apply receipt | `docs/traces/` or owning mechanic provenance |
| `legacy` | preserved raw or superseded material retained for provenance | owning `legacy/`, `legacy/raw/`, `PROVENANCE.md`, or index |
| `runtime` | deployed service, state, worker, storage, daemon, or execution body | `abyss-stack` unless another owner explicitly owns it |
| `public` | claim intended for outside readers or GitHub-facing surfaces | release-support posture and owner evidence |
| `projection` | transported or displayed view of stronger source | projection owner and source owner together |
| `receipt` | evidence that a move, review, release, or owner acceptance happened | receipt owner, decision route, trace route, or landing log |
| `cache` | local, temporary, reproducible, or disposable support artifact | rebuild route or ignore rule |

## Reading order

When two surfaces disagree, read in this order:

1. source owner law
2. owner-local `AGENTS.md`, README, contract, or protocol
3. schema, builder, validator, or generated-source map
4. receipt, trace, landing log, or decision record
5. generated, projected, cached, or displayed output

## Alignment rule

An organ alignment should label or route each important surface state before
asking another repository to accept it.

The center may name the state vocabulary. The stronger owner decides whether a
surface becomes operational truth.
