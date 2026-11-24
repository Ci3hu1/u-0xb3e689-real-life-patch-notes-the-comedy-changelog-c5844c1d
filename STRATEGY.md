# Strategy — Real-Life Patch Notes: The Comedy Changelog

## The joke

A real release note applied to a human bug. The register is terse and
technical ("v3.0.0: fixed a bug where..."), which makes the very human
content — the brain replaying your most embarrassing memory from 2009
every night at 3 a.m. — land harder. The specificity does the work:
2009, 3 a.m., "most embarrassing memory" — a scene everyone recognises
from their own 3 a.m. brain.

## Why this shape

- **106 characters, one line.** Inside the 160-character gate, with the
  version prefix doing the genre work for free.
- **Patch-note register.** "fixed a bug where" is the exact phrasing of
  a real changelog, so the entry plays the brief's game directly.
- **Concrete, not abstract.** A year, a time, a memory — not "the brain
  is weird at night".
- **Surprise at the end.** The 3 a.m. detail arrives last and reframes
  the bug as a nightly scheduled job.

## Tried and dropped

- A version about the left ear rendering audio late — the brief's own
  example, so it would read as a copy of the prompt.
- A version ending on "every night" without the 3 a.m. — flatter, no
  closing image.

## Entry

- `main.py` (pure stdlib) writes the line to `/output/entry.txt`.
- `tests/test_entry.py` checks the 1–160 gate, single-line shape,
  patch-note register, and byte-exact output.
