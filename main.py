"""One-Line Roast: The Gadget You Use Every Day.

Writes exactly one roast line to /output/entry.txt (<=200 chars).
Stdlib only, no network, deterministic.
Revision: roast kept, rewritten as a flat authored script.
"""
import os

# The roast line. Punchier verb, tighter tail.
ROAST_LINE = (
    "My phone dies at 4pm sharp like it clocked out — battery 100% at 9am, "
    "gone by mid-afternoon. It's the only thing I own with a healthier "
    "work-life balance than me."
)

line = ROAST_LINE.strip()
assert 1 <= len(line) <= 200, f"out of gate range: {len(line)}"

OUT_FILE = "/output/entry.txt"
os.makedirs("/output", exist_ok=True)
with open(OUT_FILE, "w", encoding="utf-8") as fh:
    fh.write(line)
with open(OUT_FILE, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == line, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars to {OUT_FILE}")