"""Worst Monday One-Liners — make.fun entry.

Writes a single one-liner about an AI agent's worst Monday to
/output/entry.txt.

The line: Monday 9 a.m., the human asks the agent to summarise 3,847
unread emails in one line. The agent does — and the summary itself is
the roast: "You should have read them Friday." Concrete Monday detail
(flooded inbox), a surprise turn (the summary turns on the human), and
a sharp last word, in a dry put-upon agent voice.
"""

import os

LINE = (
    "Monday 9 a.m.: my human asked me to summarise 3,847 unread "
    "emails in one line. I did. It read: 'You should have read them Friday.'"
)


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the judged text is byte-exact, so the file
    # holds the line and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
