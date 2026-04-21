#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REG = ROOT / "generated" / "agon_duel_kernel_model_registry.min.json"
REQUIRED_EVENTS = [
    "kernel.draft_created",
    "kernel.charter_bound",
    "kernel.seats_bound",
    "kernel.commit_phase_opened",
    "kernel.sealed_commit_recorded",
    "kernel.commit_phase_closed",
    "kernel.reveal_view_recorded",
    "kernel.engagement_window_opened",
    "kernel.move_declaration_recorded",
    "kernel.revision_statement_recorded",
    "kernel.adjudication_request_recorded",
    "kernel.closeout_candidate_recorded",
]
FORBIDDEN_STOP_LINE_GAPS = [
    "no_live_verdict_authority",
    "no_durable_scar_write",
    "no_rank_or_trust_mutation",
    "no_tree_of_sophia_promotion",
    "no_assistant_contestant_drift",
]


def fail(msg):
    print(msg, file=sys.stderr)
    return 1


def main():
    if not REG.exists():
        return fail(f"missing {REG}")

    reg = json.loads(REG.read_text(encoding="utf-8"))
    kernels = reg.get("kernels", [])
    if reg.get("count") != len(kernels):
        return fail("count mismatch")

    seen_ids = set()
    for kernel in kernels:
        kernel_id = kernel.get("id")
        if not isinstance(kernel_id, str) or not kernel_id:
            return fail("kernel id must be a non-empty string")
        if kernel_id in seen_ids:
            return fail(f"duplicate kernel id: {kernel_id}")
        seen_ids.add(kernel_id)

        if kernel.get("live_protocol") is not False:
            return fail(f"{kernel_id} must be live_protocol=false")

        seats = kernel.get("minimum_seats", {})
        if seats.get("contestants", {}).get("count") != 2:
            return fail(f"{kernel_id} must require exactly two contestants")
        if seats.get("contestants", {}).get("kind_required") != "agonic":
            return fail(f"{kernel_id} contestants must be agonic")

        assistant_forbidden = set(kernel.get("assistant_boundary", {}).get("forbidden", []))
        if "contestant_seat" not in assistant_forbidden:
            return fail(f"{kernel_id} must forbid assistant contestant seat")

        events = kernel.get("event_sequence", [])
        last_position = -1
        for event in REQUIRED_EVENTS:
            if event not in events:
                return fail(f"{kernel_id} missing event {event}")
            current_position = events.index(event)
            if current_position <= last_position:
                return fail(f"{kernel_id} event order is invalid at {event}")
            last_position = current_position

        stop_lines = set(kernel.get("stop_lines", []))
        for item in FORBIDDEN_STOP_LINE_GAPS:
            if item not in stop_lines:
                return fail(f"{kernel_id} missing stop-line {item}")

    print("agon duel kernel model registry ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
