"""One-line cat joke for make.fun bounty
u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.

Writes exactly one joke (one line, under 200 characters) to
/output/entry.txt. Stdlib only, no network, deterministic.
"""

import os

JOKE = (
    "My cat sat on my homework when she was a kitten. "
    "Twelve years later, she's still sitting on my homework. "
    "I'm 34."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Self-check: the gate requires 1-200 chars, not whitespace-only.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "entry.txt does not match the joke"
    assert 1 <= len(written) <= 200, "joke outside 1-200 chars"
    assert written.strip(), "joke is whitespace-only"
    assert "\n" not in written, "joke must be a single line"


if __name__ == "__main__":
    main()
