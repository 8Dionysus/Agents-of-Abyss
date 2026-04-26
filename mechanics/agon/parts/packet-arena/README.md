# Packet Arena

This part keeps packets, seats, session grammar, and arena boundaries legible
without opening a live arena.

## Start here

- [CONTRACT](CONTRACT.md)
- [VALIDATION](VALIDATION.md)

## Center function

- name state packet and session model boundaries
- keep charter and seat grammar separate from actor authority
- keep runtime session bodies outside the center

## Next route

Route actor seats to `aoa-agents`, live route behavior to `aoa-routing`, and
runtime session bodies to `abyss-stack`.
