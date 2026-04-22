# Rollback Trigger Decision Table

| Signal | Required verdict | Action |
| --- | --- | --- |
| critical scope drift | deployment integrity verdict | rollback or quarantine |
| repeated false closure | post-release regression verdict | pause ring, route incident |
| authority breach | authority policy check | immediate pause |
| canary failure only | canary verdict | block promotion |
| noisy low severity alarm | suppression rule | keep watching |
