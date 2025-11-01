import subprocess
import sys
from pathlib import Path


def run_madlib_with_input(inputs: str) -> str:
    """Run the madlib script with given stdin and return stdout text."""
    script = Path(__file__).resolve().parents[1] / "madlib.py"
    proc = subprocess.run([sys.executable, str(script)], input=inputs.encode(), capture_output=True)
    return proc.stdout.decode().strip()


def test_madlib_basic():
    # Provide the four interactive inputs separated by newlines
    out = run_madlib_with_input("Alice\n5\ncookies\npark\n")
    assert "Alice buys 5 different types of cookies at park" in out
