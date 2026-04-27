# Runtime Return

Runtime Return keeps runtime recovery downstream of explicit anchors, owner
gates, context rebuild policy, and return-event evidence.

## Use When

- A runtime wrapper must rebuild bounded context from a valid anchor.
- Return events or recovery summaries need a product-local runtime owner.
- Runtime evidence should travel upward as proof input, not doctrine.

## Do Not Use When

- Runtime is being narrated as self-healing or ambient autonomy.
- The center is asked to define runtime implementation policy.
- A product-local recovery surface is being generalized to the whole federation.

## Route Check

Ask whether runtime has an explicit anchor, allowed re-entry mode, loop limit,
and owner-local policy. If not, safe-stop or route to the runtime owner.

## Active Outputs

- runtime return request
- context rebuild boundary
- return-event evidence route
- safe-stop route
- runtime-owner handoff

## Next Route

Route stack runtime policy to `abyss-stack`, product-local recovery to the
product owner such as `ATM10-Agent`, proof to `aoa-evals`, and memory writeback
to `aoa-memo`.
