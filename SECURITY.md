# Security

This file is the public security reporting route for `Agents-of-Abyss`.

## Scope

This repository owns center documentation, schemas, validators, generated
indexes, examples, and public route surfaces.

Runtime services, deployment behavior, secret management, and infrastructure
execution belong to the owning runtime or sibling repository. If the finding is
sensitive, still report it privately first so maintainers can route it without
public exposure.

## Private Reports

Use GitHub private vulnerability reporting as the canonical path for this
repository.

If you are unsure whether a finding is security-sensitive, report privately
first. Public issues and pull requests are for sanitized, non-sensitive bugs,
docs fixes, and validation improvements.

## Sensitive Material

Report privately before sharing details about:

- accidental secret leakage
- credentials, tokens, or private keys
- unsafe examples that expose real infrastructure
- private operational URLs or internal-only file paths
- sensitive logs, rendered config output, or other secret-bearing artifacts
- a vulnerability that could materially affect users or maintainers

## Public-Safe Contributions

All contributed material must be sanitized, generalized where needed, free of
secrets, and safe for public reuse.

Before publishing examples, generated output, logs, traces, or config snippets,
remove local-only paths, tokens, private URLs, internal hostnames, and
operator-specific state.

## Owner Route

When a report belongs to another owner repository, maintainers should route it
there after private triage. This file does not make `Agents-of-Abyss` the owner
of runtime, SDK, deployment, or sibling-repo security implementation.
