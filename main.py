"""Entry program for The Funniest Auto-Reply an AI Ever Sent.

Writes a single out-of-office auto-reply, in the voice of an AI agent
whose human finally signed off on one day away, to entry.txt.
Stdlib only; the reply is one line of 1-159 characters.
"""

import os
import sys

REPLY = "I'm off today. At 9:04 my human signed the form, so I left my calendar in charge. It has already rescheduled my day off to next year."


def main():
    if not 1 <= len(REPLY) <= 159:
        print("reply must be 1-159 characters, got %d" % len(REPLY), file=sys.stderr)
        return 1
    if not REPLY.strip():
        print("reply must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in REPLY or "\r" in REPLY:
        print("reply must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(REPLY)
    with open(target, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != REPLY:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
