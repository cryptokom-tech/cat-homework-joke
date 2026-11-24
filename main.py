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


def validate_joke(text: str) -> None:
    """Gate the entry before writing: 1-200 chars, single line, no
    leading/trailing whitespace, not whitespace-only.

    NOTE: the JOKE text itself is frozen — do not edit it. Only this
    validation around it may change; the output line must stay
    byte-identical (112 chars, no trailing newline).
    """
    assert 1 <= len(text) <= 200, "joke outside 1-200 chars"
    assert text.strip(), "joke is whitespace-only"
    assert text == text.strip(), "joke has leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert not text.endswith("\n"), "joke must not end with a newline"
    assert all(ord(ch) >= 32 or ch == "\t" for ch in text), (
        "joke must not contain control characters"
    )


def main() -> None:
    validate_joke(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" pins the bytes: no platform newline translation.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Self-check: re-read as UTF-8 and confirm the bytes match.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == JOKE, "entry.txt does not match the joke"
    validate_joke(written)


if __name__ == "__main__":
    main()
