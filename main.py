"""
Simple Python 3 script that prints the interpreter version.
"""

import sys


def main() -> None:
    """Print the running Python interpreter version in a friendly format."""
    major, minor, micro = sys.version_info[:3]
    print(f"Running on Python {major}.{minor}.{micro}")


if __name__ == "__main__":
    main()
