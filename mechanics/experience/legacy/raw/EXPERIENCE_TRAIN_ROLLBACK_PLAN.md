# Experience Train Rollback Plan

This v1.1 surface belongs to the **AoA Experience Live Office Expansion and Multi-Release Train**.

## Purpose

Defines train rollback and office quarantine.

## Boundary

This surface does not create a new `aoa-experience` repository. It does not give Codex approval authority. It does not allow assistants to self-release, self-enroll, self-certify, or drift into agonic contestants. It does not allow direct runtime writes into `Tree-of-Sophia`.

## Shape

`notary.assistant` remains the first receipt-bearing anchor. `concierge.assistant`, `courier.assistant`, and `monitor.assistant` join through a governed train with compatibility checks, handoff graph, smoke gates, rollback, replay audit, and operator go/no-go.
