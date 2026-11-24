"""One-Line Roast: The Gadget You Use Every Day.

Writes exactly one roast line to /output/entry.txt (<=200 chars).
Standard library only. No network, no secrets, no environment reads.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# The roast line, authored for this entry. Punchier verb, tighter tail.
ROAST_LINE = (
    "My phone flatlines at 4pm sharp like it clocked out, and I can't even be mad - "
    "it's the only thing I own with a healthier work-life balance than me."
)


def build_line() -> str:
    """Return the single roast line to submit, trimmed to the 200-char gate."""
    return ROAST_LINE.strip()


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    line = build_line()
    assert 1 <= len(line) <= 200, f"line out of gate range: {len(line)}"
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
