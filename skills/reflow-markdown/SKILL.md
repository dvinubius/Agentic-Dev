---
name: reflow-markdown
description: Reflow Markdown prose to a maximum line width with a bundled Python script that proves it moved only whitespace, or refuses and writes nothing. Use when Markdown lines exceed a width limit, when a repository needs one consistent wrap width, or when checking width compliance without changing files.
---

# Reflow Markdown

Rewrapping Markdown by hand is where documentation formatting goes wrong, and
the damage is quiet: a break lands between `]` and `(` and the link dies, a
table row gets folded and stops being a table, a heading becomes a paragraph.
Use the bundled script rather than rewrapping by hand or writing a one-off.

## Quick start

Substitute this skill's base directory for `<skill-dir>`. Paths are files, or
directories to walk (vendor and build directories are skipped).

```bash
python3 <skill-dir>/scripts/reflow_markdown.py README.md docs .agents
```

Report what would change without writing:

```bash
python3 <skill-dir>/scripts/reflow_markdown.py --check --width 100 docs
```

## Why the output can be trusted

The script checks two invariants on its own output, classified independently of
the code that produced it:

- every structural line survives byte for byte
- the document's whole word sequence is unchanged

Together these catch a dropped, added or reordered word, a folded table row, a
broken link, and a paragraph that became a heading or a code block. A file
failing either is **refused**: reported, and left exactly as it was.

A refusal is the script working. Do not hand-edit the file to get past one, and
do not relax the check — find what the reflow would have changed, fix the cause,
and rerun.

## What it never wraps

Table rows, headings, horizontal rules, fenced and indented code, blockquotes,
reference definitions, and HTML blocks. Also any single atom longer than the
width — a link or code span with no legal break inside it. These stay long on
purpose, and the run reports them so you can see there is nothing to do.

## Choosing the width

Measure the repository before imposing a number, because most already have one:

```bash
awk 'length > 0 {print length}' $(git ls-files '*.md') | sort -rn | uniq -c | head
```

A cluster at 78–80 means 80. Pass `--width` to match what you find.

## Only what overflows

By default a block is rewrapped only if one of its lines exceeds the width, so
paragraphs already inside the limit keep the breaks their author chose. Prefer
this: refilling compliant files rewrites documents that were never wrong, and
buries the real change in diff noise. `--rewrap-all` overrides it when the goal
really is to normalise every paragraph.

## Done when

The run prints no `REFUSED` lines, and every remaining over-width line is one of
the kinds listed above rather than prose. Pair with
[`validate-markdown-repo`](../validate-markdown-repo/SKILL.md) to confirm links
still resolve afterwards.
