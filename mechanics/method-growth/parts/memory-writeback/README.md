# Memory Writeback

Memory Writeback routes lessons and retention reasons without turning center
prose into memory canon.

## Use When

- A growth route produced a durable lesson.
- A prune, merge, defer, or drop decision should remain recallable.
- A future agent needs a bounded memory route rather than raw history.

## Do Not Use When

- The output is only a landing receipt.
- The object owner should retain the fact locally.
- The route has no clear retention reason.

## Route Check

Name the lesson, why it should be retained, what provenance supports it, and
which memory owner should carry it.

## Active Outputs

- Memory request.
- Retention reason.
- Recall route hint.
- Provenance pointer.

## Next Route

Route memory objects, recall contracts, and retention policy to `aoa-memo`.
Route proof of memory integrity to `aoa-evals` when claims harden.
