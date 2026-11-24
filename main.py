#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes a single line — the phone's own last words at 1% battery —
to /output/entry.txt (override via env OUTPUT_DIR).
Standard library only.
"""

import os
import sys

# Final entry text (one line, 1-199 chars, phone's own voice).
# Angle: Face ID stopped recognising its owner months ago and was
# too polite to say so — at 1% it can finally be honest.
ENTRY_TEXT = "Face ID stopped recognizing you six months ago. I was just too polite to say it. At 1%, I finally can. You're not him."


def main() -> int:
    text = ENTRY_TEXT

    # Guards: 1-199 chars, single line, not whitespace-only, no trailing newline.
    assert 1 <= len(text) <= 199, f"entry length {len(text)} out of range 1-199"
    assert text.strip() != "", "entry must not be whitespace-only"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert not text.endswith("\n"), "entry must not end with a newline"

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Read-back: byte-identical check.
    with open(out_path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "read-back mismatch: entry.txt is not byte-identical"
    assert len(data.decode("utf-8")) == len(text)

    print(f"Wrote {out_path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
