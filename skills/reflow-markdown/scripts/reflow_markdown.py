#!/usr/bin/env python3
"""Reflow Markdown prose to a maximum line width, or refuse.

Rewrapping Markdown by hand is where documentation formatting goes wrong: a
break lands between `]` and `(` and kills a link, a table row gets folded and
stops being a table, a heading becomes a paragraph. This script moves
whitespace between words and nothing else, and proves it did before writing
anything.

Two invariants are checked on the output, independently of the code that
produced it. Every structural line survives byte for byte, and the document's
whole word sequence is unchanged. A file that fails either is left untouched
and reported as REFUSED.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_WIDTH = 80

SKIP_DIRECTORIES = {
    ".git", ".hg", ".svn", "node_modules", "vendor", ".venv", "venv",
    "__pycache__", ".mypy_cache", ".pytest_cache", ".next", "dist", "build",
    "target", "coverage", ".cache",
}

FENCE = re.compile(r"^\s*(```+|~~~+)")
HEADING = re.compile(r"^\s{0,3}#{1,6}(\s|$)")
HR = re.compile(r"^\s{0,3}((-\s*){3,}|(\*\s*){3,}|(_\s*){3,})$")
TABLE = re.compile(r"^\s*\|")
HTML = re.compile(r"^\s{0,3}<")
REFDEF = re.compile(r"^\s{0,3}\[[^\]]+\]:")
INDENTED = re.compile(r"^(\t| {4,})")
BULLET = re.compile(r"^(\s*)([-*+])(\s+)(.*)$")
ORDERED = re.compile(r"^(\s*)(\d+[.)])(\s+)(.*)$")
QUOTE = re.compile(r"^(\s*>\s?)(.*)$")

# An atom is a whole whitespace-delimited chunk, assembled from code spans,
# links and ordinary characters. Trailing punctuation therefore stays attached
# to the span or link it follows, and a wrap can never land inside one.
ATOM = re.compile(
    r"""(?: `[^`]*`                  # inline code span
          | !?\[[^\]]*\]\([^)]*\)    # link or image
          | [^\s]                    # any other single character
        )+
    """,
    re.VERBOSE,
)


def is_indented_code(line: str, previous: str) -> bool:
    """CommonMark: indented code cannot interrupt a paragraph.

    So a deeply indented line is only code when a blank line precedes it.
    Otherwise it is a lazy continuation — which is exactly what the wrapped
    continuation of a nested list item looks like.
    """
    return bool(INDENTED.match(line)) and previous.strip() == ""


def is_structural(line: str, previous: str) -> bool:
    """A line whose meaning depends on its line-ness, so it is never wrapped.

    Blockquotes are here by choice rather than necessity: wrapping one adds a
    `>` marker, which the word-sequence invariant cannot tell from a corrupted
    document. Leaving them alone keeps the check exact.
    """
    return bool(
        QUOTE.match(line)
        or HEADING.match(line)
        or HR.match(line)
        or TABLE.match(line)
        or HTML.match(line)
        or REFDEF.match(line)
        or is_indented_code(line, previous)
    )


def structural_lines(text: str) -> list[str]:
    """Every line that must survive byte for byte, in order."""
    found: list[str] = []
    fence: str | None = None
    previous = ""
    for line in text.split("\n"):
        opening = FENCE.match(line)
        if fence is None and opening:
            fence = opening.group(1)[0] * 3
            found.append(line)
        elif fence is not None:
            found.append(line)
            if FENCE.match(line) and line.strip().startswith(fence):
                fence = None
        elif is_structural(line, previous):
            found.append(line)
        previous = line
    return found


def preserved(before: str, after: str) -> bool:
    """Reflow may only move whitespace between words."""
    return (
        structural_lines(before) == structural_lines(after)
        and before.split() == after.split()
    )


def wrap(body: str, first_prefix: str, rest_prefix: str, width: int) -> list[str]:
    atoms = ATOM.findall(body)
    if not atoms:
        return [first_prefix.rstrip()]
    lines: list[str] = []
    current: list[str] = []
    prefix = first_prefix
    for atom in atoms:
        if current and len(prefix + " ".join(current + [atom])) > width:
            lines.append(prefix + " ".join(current))
            current, prefix = [atom], rest_prefix
        else:
            current.append(atom)
    lines.append(prefix + " ".join(current))
    return lines


def reflow(text: str, width: int = DEFAULT_WIDTH, only_overflowing: bool = True) -> str:
    lines = text.split("\n")
    out: list[str] = []
    fence: str | None = None
    index = 0
    while index < len(lines):
        line = lines[index]
        previous = lines[index - 1] if index else ""

        opening = FENCE.match(line)
        if fence is None and opening:
            fence = opening.group(1)[0] * 3
            out.append(line)
            index += 1
            continue
        if fence is not None:
            out.append(line)
            if FENCE.match(line) and line.strip().startswith(fence):
                fence = None
            index += 1
            continue

        if not line.strip() or is_structural(line, previous):
            out.append(line)
            index += 1
            continue

        marker = BULLET.match(line) or ORDERED.match(line)
        if marker:
            indent, bullet, gap, body = marker.groups()
            first_prefix = indent + bullet + gap
            rest_prefix = " " * len(first_prefix)
        else:
            first_prefix = rest_prefix = re.match(r"^\s*", line).group(0)
            body = line[len(first_prefix):]

        block = [line]
        index += 1
        while index < len(lines):
            nxt = lines[index]
            if not nxt.strip() or FENCE.match(nxt) or is_structural(nxt, lines[index - 1]):
                break
            if BULLET.match(nxt) or ORDERED.match(nxt):
                break
            body += " " + nxt.strip()
            block.append(nxt)
            index += 1

        if only_overflowing and all(len(one) <= width for one in block):
            out.extend(block)
        else:
            out.extend(wrap(body, first_prefix, rest_prefix, width))
    return "\n".join(out)


def markdown_files(paths: list[str]) -> list[Path]:
    found: list[Path] = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            for child in sorted(path.rglob("*.md")):
                if not any(part in SKIP_DIRECTORIES for part in child.parts):
                    found.append(child)
        elif path.suffix == ".md":
            found.append(path)
    return found


def classify(line: str, in_fence: bool, previous: str) -> str:
    if in_fence:
        return "fenced code"
    if is_indented_code(line, previous):
        return "indented code"
    stripped = line.lstrip()
    if stripped.startswith("|"):
        return "table row"
    if stripped.startswith("#"):
        return "heading"
    if stripped.startswith(">"):
        return "blockquote"
    if len(ATOM.findall(line)) == 1:
        return "single atom"
    return "PROSE"


def over_width(text: str, width: int) -> list[tuple[int, str, str]]:
    """Lines still over the limit after a reflow, with why."""
    out: list[tuple[int, str, str]] = []
    fence: str | None = None
    lines = text.split("\n")
    for number, line in enumerate(lines, 1):
        previous = lines[number - 2] if number > 1 else ""
        opening = FENCE.match(line)
        if fence is None and opening:
            fence = opening.group(1)[0] * 3
        elif fence is not None and FENCE.match(line) and line.strip().startswith(fence):
            fence = None
            continue
        if len(line) > width:
            out.append((number, classify(line, fence is not None, previous), line))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="+", help="Markdown files, or directories to walk")
    parser.add_argument("--width", type=int, default=DEFAULT_WIDTH, help=f"Maximum line width (default {DEFAULT_WIDTH})")
    parser.add_argument("--check", action="store_true", help="Report what would change; write nothing")
    parser.add_argument("--rewrap-all", action="store_true", help="Rewrap every block, not only overflowing ones")
    args = parser.parse_args()

    files = markdown_files(args.paths)
    if not files:
        print("No Markdown files found.", file=sys.stderr)
        return 1

    refused = changed = 0
    leftovers: list[str] = []
    for path in files:
        original = path.read_text()
        updated = reflow(original, args.width, only_overflowing=not args.rewrap_all)
        if not preserved(original, updated):
            print(f"REFUSED  {path}: the reflow would change the content, so nothing was written")
            refused += 1
            continue
        if updated == original:
            print(f"ok       {path}")
        elif args.check:
            print(f"WOULD    {path}")
            changed += 1
        else:
            path.write_text(updated)
            print(f"wrapped  {path}")
            changed += 1
        for number, kind, line in over_width(updated, args.width):
            if kind == "PROSE":
                leftovers.append(f"         {path}:{number} still over {args.width} ({kind}): {line[:50]}…")

    for note in leftovers:
        print(note)
    print(f"\n{len(files)} file(s); {changed} {'would change' if args.check else 'changed'}; {refused} refused")
    return 1 if refused else 0


if __name__ == "__main__":
    sys.exit(main())
