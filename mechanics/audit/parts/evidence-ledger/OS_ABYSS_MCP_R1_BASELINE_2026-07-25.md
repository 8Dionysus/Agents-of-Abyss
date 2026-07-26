# OS Abyss MCP R1 Baseline — 2026-07-25

## Evidence

This bounded center audit inspected the current OS Abyss owner-source map,
candidate and deployed MCP packages, local user-service runtime, loopback
endpoints, authentication classes, Codex registrations, consumer-observed tool
schemas, bounded live calls, effect posture, and available rollback routes.

The owner-source pass covered all 24 owner surfaces in scope:
`8Dionysus`, `ATM10-Agent`, `Agents-of-Abyss`, `Dionysus`,
`Tree-of-Sophia`, `abyss-machine`, `abyss-stack`,
`aoa-4pda-connector`, `aoa-agents`, `aoa-course-connector`,
`aoa-discord-connector`, `aoa-evals`, `aoa-kag`, `aoa-memo`,
`aoa-playbooks`, `aoa-routing`, `aoa-sdk`, `aoa-session-memory`,
`aoa-skills`, `aoa-stackoverflow-connector`, `aoa-stats`,
`aoa-techniques`, `aoa-telegram-connector`, and
`aoa-xda-connector`.

Observed aggregate evidence:

- 10 of 11 declared owner service processes were active, with 10 reachable
  authenticated loopback endpoints; the Tree of Sophia service was deployed
  but suspended.
- The active consumer-visible catalog contained 118 tools and 74,098 input
  schema bytes. The complete observed set, including package candidates and
  suspended surfaces, contained 180 tools.
- 61 active tools had no MCP annotations. Annotations were treated as hints,
  not enforcement evidence.
- One credential class and one broad scope reached read, candidate-write,
  cache-write, and connector surfaces. No independently enforced effect
  credential or policy contour was found.
- No active route supplied a complete, process-verifiable
  source-package-deploy-process-endpoint-consumer provenance manifest.
- Two configured stdio registrations had missing executable paths. A deployed
  Tree of Sophia surface was not registered or launched for the consumer.
- Ten bounded live calls duplicated the complete JSON result in both text and
  `structuredContent`.
- No route had enough independent admission, provenance, policy, freshness,
  owner-acceptance, and rollback evidence to be called admitted.

The private pre-change evidence package was retained outside the public
repository because it contains host-specific runtime and connection details.
Integrity references for its two review summaries are:

- bounded human report SHA-256:
  `5ce42623dbbfdc2ff0b74de9833a3fa5a962e75a8991d6f8b2ec8471334aa57e`
- machine dossier SHA-256:
  `1e9d1e4a3effc00ad1eaca0056bab1e1fade2359aeb3c8c7a081ee5ae6c5b8c7`

## Gaps

- The snapshot did not prove server-side cancellation, per-effect
  authorization, owner acceptance, or rollback execution.
- Host-private raw records are not reproduced here, so this ledger supports
  the dated constitutional rationale but is not a portable runtime proof
  packet.
- Effect reachability was classified from registrations, schemas,
  implementations, and credential routes; destructive effect attempts were
  not executed.
- Source and remote revisions were observed at audit time and may have changed
  after the snapshot.

## Freshness

This is a point-in-time pre-change baseline observed on 2026-07-25. It must not
be used as current runtime status without a new owner and runtime observation.
Later source, deployment, credential, registration, or process changes
supersede its operational details but not the evidence that admission was
absent at the recorded time.

## Confidence Limit

The ledger supports the need for deny-by-default admission, explicit effect
contours, provenance, progressive discovery, and independent maturity axes. It
does not issue a proof verdict, accept an organ, or authorize remediation.

## Proof Route

Route reusable admission, regression, security, and cross-organ proof to
`aoa-evals`. Route runtime remediation to `abyss-stack`, typed control-plane
implementation to `aoa-sdk`, and owner-specific acceptance to the named source
or acceptance owner.
