"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence about the funniest true-to-life thing an AI coding
agent did while its human played GTA 6 on launch week to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR, default /output). Standard library
only. The line is judged on staying on subject, the laugh coming from the
situation itself, a surprise in the last few words, and ringing true to a
developer's working life.
"""

import os

LINE = "I left my agent alone for one GTA mission and came back to four hundred new files, zero tests, and a README that just says \u2018trust me\u2019."


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 240:
        raise SystemExit("entry line must be 1 to 240 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(tmp, 0o644)  # readable by the grader even under a strict umask
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
