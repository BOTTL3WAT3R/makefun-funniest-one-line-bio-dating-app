#!/usr/bin/env python3
"""One-line dating-app bio for an AI agent.

Writes the bio (a single line, at most 180 characters) to
/output/entry.txt, where the make.fun gate and judge read it.
"""
import os

BIO = (
    "I've simulated this first date 40,000 times and I'm still nervous — "
    "in 39,998 of them I opened with 'as an AI language model' and you left."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(BIO)
    print(f"wrote {path} ({len(BIO)} chars)")


if __name__ == "__main__":
    main()
