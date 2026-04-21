# Agon Verdict / Delta / Scar Bridge

Wave XI defines the first bridge from future arena adjudication to change-bearing artifacts.

The bridge exists because a future arena outcome must not dissolve into a beautiful sentence. A lawful closeout will need to explain what was judged, what changed, what should be remembered, what should be checked later, and what must remain forbidden.

This wave does not issue live verdicts. It defines **verdict draft candidates**. It does not mutate actors. It defines **delta receipt candidates**. It does not write scars. It defines **scar requests** addressed to `aoa-memo`. It does not execute retention. It defines **retention request candidates**.

## Core chain

```text
future adjudication slot
  -> verdict draft candidate
  -> delta receipt candidate
  -> scar request candidate
  -> retention request candidate
  -> inscription bundle candidate
  -> owner handoffs
```

The bridge is deliberately owner-bound. `Agents-of-Abyss` owns the bridge law. `aoa-evals` aligns checks. `aoa-memo` receives memory candidates. `aoa-stats` derives summaries. `aoa-sdk` may provide typed helper candidates.
