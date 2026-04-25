# Constitution Runtime Decision Table

- Missing authority resolution -> block.
- Missing quorum -> block.
- Tampered sealed vote -> invalidate vote and open audit.
- Active material stay -> block owner execution.
- Appeal window open -> hold irreversible execution.
- Sealed decision and clean replay -> allow enforcement.
- Direct ToS runtime write -> block.
