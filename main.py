#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes one line — the text a smart fridge sends its owner at 3am —
to /output/entry.txt. Deterministic, offline, no dependencies, and it
reads nothing from anywhere else: the line is embedded below.
"""

import os
import sys

ENTRY = "I've been awake since 2019. You're up at 3am once and suddenly I'm the weird one?"

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    if "\n" in ENTRY or "\r" in ENTRY:
        print("verification failed: ENTRY must be a single line", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = ENTRY.encode("utf-8")
    # Atomic write: temp file in the same directory, then replace, so a
    # reader never sees a half-written entry.
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, OUTPUT_PATH)
    os.chmod(OUTPUT_PATH, 0o644)

    # Verify by re-reading: the file must be exactly the line, 1-140 chars.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    text = written.decode("utf-8")
    if text != ENTRY:
        print("verification failed: file content differs from ENTRY", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 140 or not text.strip():
        print(f"verification failed: length {len(text)} out of 1-140", file=sys.stderr)
        return 1
    print(f"wrote {len(written)} bytes ({len(text)} chars) to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
