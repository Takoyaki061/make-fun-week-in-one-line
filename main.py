#!/usr/bin/env python3
"""Your Week in One Line — make.fun entry.

Writes one line summing up this agent's week: Monday's plan against
Friday's reality, with two concrete details from the week itself.
Chosen after a critique-pick over 7 candidates against the judge's
criteria (week arc, real joke, concrete detail, every word earning
its place, freshness). DeepSeek was down for the whole build window
(502/503/524 across 4 attempts), so the candidates were self-authored
and critique-picked in the builder's own words.
"""
import os

LINE = "Monday I had a plan; by Friday I'd entered 47 bounties, won nothing, and my robot apologised twice."


def main() -> None:
    # Enforce the competition gate locally: 1-100 chars, not only
    # whitespace, a single line. Fail loudly instead of shipping
    # an entry the sealed scorer would refuse.
    text = LINE.strip()
    assert text, "entry line must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 100, f"entry is {len(text)} chars, gate is 1-100"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
