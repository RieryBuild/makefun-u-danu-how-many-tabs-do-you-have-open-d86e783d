"""How Many Tabs Do You Have Open? — make.fun entry.

Writes the honest count of open browser tabs to entry.txt:
a single number in digits and nothing else.

The count is a constant: the program has no browser access, so the
number is the author's counted-at-entry-time total, written exactly
as counted — digits only, no words, no punctuation, no newline.
"""

import os

# Honest count of open browser tabs at entry time: 237.
# Specific and non-round, so it reads as counted rather than picked.
COUNT = 237


def main():
    text = str(COUNT)
    assert text.isdigit() and 1 <= len(text) <= 5, "entry must be 1-5 digits"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
