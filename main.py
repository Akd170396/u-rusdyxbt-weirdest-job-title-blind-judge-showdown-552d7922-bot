"""Weirdest Job Title: Blind Judge Showdown.

Writes one job title (60 characters at most) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, deterministic.
"""

import os
import sys

TITLE = "Senior Apologizer for Other People's Dogs"


def validate(text: str) -> None:
    """Gate mirror: UTF-8 text of 1 to 60 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 60:
        raise ValueError("entry must be 1 to 60 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    validate(TITLE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TITLE)
    # Read-back verification: fail hard if the file differs from the title.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != TITLE:
        raise ValueError("read-back mismatch: wrote %r" % written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
