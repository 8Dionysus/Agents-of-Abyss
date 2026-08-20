# Keep Training And Model Memory Disabled

- Decision ID: AOA-CENTER-D-0037

## Status

Accepted.

## Index Metadata

- Original date: 2026-07-29
- Surface classes: organ contract, federation boundary, decision record
- Center facets: organ alignment, owner descent
- Mechanic parents: organ-contract
- Guard families: owner boundary, operator authority, sibling-owner boundary
- Posture: accepted training stop line

## Context

The active-organ program includes a possible future route from reviewed
experience and outcomes into a de-identified training candidate, candidate
model, offline and shadow evaluation, operator canary, and model promotion.
That route is materially different from nonparametric memory: it changes model
weights or model behavior, introduces dataset and checkpoint retention, and
creates purge or unlearning obligations.

The current program evidence does not establish natural operator benefit for
the nonparametric organ. Public benchmark and deterministic lifecycle evidence
remain bounded; reviewed OS outcome replay and the real 7/30-day soak are not
complete. More importantly, no repository has been admitted as the
training/model owner.

Without a durable stop line, a future agent could mistake a useful memory
benchmark, outcome receipt, operator usage, or learned memory-management paper
for permission to export private material, fine-tune a model, or assign model
authority to an existing memory, SDK, runtime, host, or eval owner.

## Options considered

1. Assign training/model ownership temporarily to `aoa-memo` because it owns
   reviewed memory meaning.
2. Assign it to `abyss-machine` or `abyss-stack` because they can host models,
   datasets, runtimes, and jobs.
3. Treat training as an `aoa-evals` extension after a benchmark improvement.
4. Keep the entire training/model-memory contour at consumer-zero until
   nonparametric natural benefit is proven and a separate owner is admitted by
   a new operator decision.

## Decision

Choose option 4.

Training and model memory remain disabled. No current repository inherits
training, model editing, model promotion, dataset retention, checkpoint purge,
or unlearning authority.

Reviewed memory, outcome receipts, access counts, benchmark records, private
session evidence, host evidence, and derived projections may not be exported
into a training dataset or model-editing route. Model-backed evaluation remains
read-only evidence about a pinned model; it is not a training candidate or
promotion.

The disabled contour has explicit consumer-zero: no input reader, dataset
writer, export, storage root, scheduler, service, candidate checkpoint, model
mutation, promotion route, or hidden fallback.

A future route requires all of the following before its first artifact:

- positive natural net benefit for the nonparametric organ against frozen
  no-memory and reviewed-pull baselines;
- completed 30-day soak within foreground, storage, backlog, resource, and
  operator-attention budgets;
- a separately admitted training/model owner and owner-local contracts;
- dataset lineage, consent, privacy, retention, access, purge, and unlearning
  obligations;
- a frozen predecessor, independent adversarial/offline/shadow proof, and
  exact rollback;
- a new hash-bound decision by the sole human operator.

Meeting those conditions permits a new research phase only. It does not
authorize training or model promotion.

## Rationale

Memory objects can be retracted, superseded, or erased through explicit owner
surfaces. Model weights create a different and often weaker erasure boundary.
Assigning that boundary to a convenient existing repository would silently
expand its authority and leave private-data residue without a qualified owner.

The smaller nonparametric form is independently useful and reversible. Keeping
training at consumer-zero preserves the ability to learn through reviewed
external memory, policies, and evals without making model mutation a hidden
dependency of the organ.

## Consequences

- `aoa-memo` may own reviewed memory and a future de-identified proposal shape
  but cannot emit a training dataset or mutate a model.
- `aoa-evals` may compare pinned models but cannot train, promote, or become
  the final judge of a model it changes.
- `abyss-machine` may report hardware and admit bounded model work but cannot
  acquire model or training semantics.
- `abyss-stack` may host a separately admitted runtime in the future but cannot
  create training authority through deployment capability.
- `aoa-sdk`, `aoa-kag`, `aoa-stats`, `.aoa`, and `aoa-agents` retain their
  existing boundaries and do not become training sources by composition.
- An erase manifest that names a training/model surface without an admitted
  owner remains `pending/residue`; it cannot be reported plain-complete.
- The immediate tradeoff is that possible model-level adaptation is excluded,
  even if a public benchmark suggests it could improve recall.

## Source surfaces

- `CHARTER.md`
- `DESIGN.md`
- `docs/FEDERATION_RULES.md`
- `docs/REPO_ROLES.md`
- `docs/decisions/AOA-CENTER-D-0032-organ-access-admission-law.md`
- `docs/decisions/AOA-CENTER-D-0036-hash-bound-operator-decision-envelope.md`

## Follow-up route

Keep the nonparametric active-organ evaluation with the named memory, SDK,
runtime, host, proof, statistics, graph, session, and agent owners. Revisit
this decision only through a new center decision after the entry conditions
are evidenced and the sole operator has admitted a separate training/model
owner. A sibling owner must then define dataset, checkpoint, purge, unlearning,
validation, and rollback truth locally.
