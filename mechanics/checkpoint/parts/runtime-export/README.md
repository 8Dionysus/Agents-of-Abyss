# Runtime Export

Runtime Export keeps checkpoint exports, runtime receipts, and closeout
plumbing subordinate to runtime gates and owner-local writeback contracts.

## Use When

- Runtime state may need a bounded export.
- A runtime closeout receipt should become evidence for later review.
- A checkpoint export may feed memo writeback after review.

## Do Not Use When

- The center is being asked to implement runtime behavior.
- A checkpoint export is being treated as memory canon.
- Runtime wants to bypass proof or owner gates.

## Route Check

Ask whether the runtime owner has the gate, receipt, and export contract. If
not, keep the center output as a stop-line or owner request.

## Active Outputs

- runtime export stop-line
- runtime owner request
- memo writeback route
- eval proof route
- closeout receipt route

## Next Route

Route runtime plumbing to `abyss-stack`, writeback targets to `aoa-memo`, and
runtime claims to `aoa-evals` when proof is required.
