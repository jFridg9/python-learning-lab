"""Zybooks exercise: three sequential floor divisions (with teaching notes).

This file keeps the exercise simple and also explains a few concepts
you asked about: `import`, the `sys` module, and what "tokens" are.

Key ideas shown below:
 - `import sys` brings in the `sys` module so we can access `sys.stdin`.
 - `sys.stdin.read()` reads all incoming input (useful when piping).
 - `.split()` turns a string into tokens (chunks separated by whitespace).
 - We validate input (integers) and check for division by zero.

Usage (PowerShell):
    echo "100 3" | python .\\zybooks\\division_three.py

Or run interactively and type the two numbers (either on one line or
two lines):
    python .\\zybooks\\division_three.py
    100 3

The program prints three results, one per line:
    out1 = user_num // div_num
    out2 = out1 // div_num
    out3 = out2 // div_num
"""

import sys


def three_floor_divs(user_num: int, div_num: int) -> tuple[int, int, int]:
    """Return three sequential floor-division results.

    This separates the computation from input/output so it's easier to
    test and reason about.
    """
    r1 = user_num // div_num
    r2 = r1 // div_num
    r3 = r2 // div_num
    return r1, r2, r3


def read_two_integers_from_stdin() -> tuple[int, int]:
    """Read two integers from stdin (supports piping or interactive input).

    Steps:
    1. Read all available stdin with `sys.stdin.read()`.
    2. `.split()` produces tokens (strings) separated by whitespace.
    3. Convert the first two tokens to integers.

    Raises ValueError if conversion fails or not enough tokens are present.
    """
    # If stdin is a terminal (interactive), use input() so the program
    # prompts the user immediately instead of waiting for EOF.
    if sys.stdin.isatty():
        a = input()
        b = input()
        data = [a, b]
    else:
        data = sys.stdin.read().split()

    if len(data) < 2:
        raise ValueError("Not enough input tokens")

    return int(data[0]), int(data[1])


def main() -> None:
    try:
        user_num, div_num = read_two_integers_from_stdin()
    except ValueError:
        # Friendly message for the learner: invalid or missing input.
        print("Invalid input", file=sys.stderr)
        return

    if div_num == 0:
        print("Error: division by zero", file=sys.stderr)
        return

    out1, out2, out3 = three_floor_divs(user_num, div_num)

    # Print each result on its own line (common exercise requirement).
    print(out1)
    print(out2)
    print(out3)


if __name__ == "__main__":
    main()
