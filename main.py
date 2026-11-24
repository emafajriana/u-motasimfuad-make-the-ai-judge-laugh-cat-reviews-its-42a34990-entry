"""Cat Reviews Its Human — make.fun entry (Python 3.13, stdlib only).

Writes one deadpan one-star review from a house cat about its human
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the
grader). The gate: UTF-8 text of 1 to 200 characters, not only
whitespace. Verified below by a read-back check.
"""

import os
from pathlib import Path

ENTRY = (
    "One star. I sat on his keyboard to help with his deadline; "
    "he moved me off, finished it himself, and still expects a cuddle."
)


def output_path() -> Path:
    """Where the grader reads the entry."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_gate(text: str) -> None:
    """The comp gate: UTF-8 text of 1 to 200 characters, not whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate needs 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")


def write_entry() -> Path:
    """Write the review, then read it back and verify it in full."""
    check_gate(ENTRY)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != ENTRY:
        raise IOError("read-back text differs from the entry")
    check_gate(written)
    return target


def main() -> None:
    target = write_entry()
    print(f"wrote {target} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
