"""Funniest Time Machine Warning Label — make.fun bounty.

One warning label for a time machine.
"""

LINE = (
    "WARNING: Do not meet yourself. If you see yourself, pretend you are "
    "a tourist and walk away slowly."
)

LIMIT = 120
TARGET = "/output/entry.txt"


def check_entry(line):
    """Validate the entry: one non-blank line within the char limit."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("entry must be a non-blank string")
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")
    if len(line) > LIMIT:
        raise ValueError(f"entry is {len(line)} chars, over the {LIMIT} limit")
    if not line.upper().startswith("WARNING"):
        raise ValueError("label must start with WARNING")
    if line.strip() != line:
        raise ValueError("entry must not have leading or trailing whitespace")
    return line


def write_entry(line):
    """Print the line and write it to /output/entry.txt."""
    import os

    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    check_entry(LINE)
    write_entry(LINE)
