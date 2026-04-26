# Agon Trial Playbook Stop-Lines

Wave VI is a pre-protocol choreography wave. It must keep these stop-lines intact:

- no_arena_session_creation
- no_sealed_commit_runtime
- no_live_move_execution
- no_verdict_authority
- no_scar_write
- no_retention_schedule
- no_rank_mutation
- no_tos_promotion
- no_hidden_assistant_contestant
- no_runtime_substrate_claim

## Assistant boundary

Assistant service actors may prepare receipts, preserve context, flag boundaries, and hand off to agonic actors.

They may not receive:

- contestant_seat
- judge_seat
- closer_jurisdiction
- summon_initiator_jurisdiction
- scar_writer
- rank_mutator
- tos_promoter

## Playbook boundary

If a trial starts deciding who won, it is becoming eval or arena protocol.

If a trial starts storing consequences, it is becoming memo.

If a trial starts choosing routes dynamically, it is becoming routing.

If a trial starts running durable sessions, it is becoming runtime substrate.

`aoa-playbooks` keeps the choreography. It does not seize the throne.
