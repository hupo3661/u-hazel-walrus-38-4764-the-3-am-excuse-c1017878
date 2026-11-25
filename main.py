#!/usr/bin/env python3
"""The 3 AM Excuse.

Writes one excuse line -- a single line of under 200 characters, in the
voice of a hardware wallet refusing to sign a transaction at 3 AM -- to
/output/entry.txt.

The joke: the wallet has learned from experience. Last time it woke up
at 3 AM, its human approved a token called DefinitelyNotAScam, so now
it treats itself as a vault, not a babysitter, and its buttons sleep
till sunrise.
"""

import os

LINE = (
    "Last time you woke me at 3 AM, you approved a token called "
    "DefinitelyNotAScam. I'm a vault, not a babysitter - my buttons "
    "sleep till sunrise."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("Invalid line: entry must be non-empty.")
    if line != line.strip():
        raise SystemExit(
            "Invalid line: entry must not have leading or trailing whitespace."
        )
    if len(line) >= MAX_CHARS:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, must be under "
            f"{MAX_CHARS}."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )
    line.encode("utf-8")


def main() -> None:
    validate(LINE)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    expected = LINE.encode("utf-8")
    with open(output_path, "wb") as f:
        f.write(expected)
    with open(output_path, "rb") as f:
        written = f.read()
    if written != expected:
        raise SystemExit(
            "Write verification failed: entry file bytes do not match the line."
        )
    print(f"wrote {len(LINE)} chars to {output_path}")


if __name__ == "__main__":
    main()
