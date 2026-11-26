"""Print the Snooze Button Roast entry line exactly as written."""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    # write(), not print(): print() would append a newline and the
    # output would no longer be byte-identical to entry.txt.
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
