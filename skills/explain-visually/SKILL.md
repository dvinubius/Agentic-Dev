---
name: explain-visually
description: Use when the user asks for a visual explainer of a concept, system, or architecture. Produces a single self-contained HTML file with diagrams and optional animation.
---

# Explain Visually

Build a visual explainer of the given subject matter.

## Output

- A single, self-contained HTML file: Tailwind CSS plus a canvas script, no build step, no external assets beyond the CDN.
- Put it outside the code repo, filename starting with today's date: e.g. `/tmp/2026-01-12-explainer-<slug>.html`.
- Make generous use of the features and flexibility the medium gives us, to optimally convey the concepts.

## Diagrams

- Existing diagrams in the source material can be reused or remixed. Add more if it helps — you have full freedom for the purpose of creating an optimal visual explainer.
- No ASCII diagrams.

## Animation

- Disregard local reduced-motion settings; if you need to animate, do so.
- Do not animate for its own sake. Links between elements in an architecture are not animated unless their individual motion conveys a sequence of steps.
- Switches between variants of an architecture (layout changes in the diagram) need not be animated either.
- A multi-step process shown as a sequence diagram gets a back-to-start (double left arrow) and a fast-forward-to-end (double right arrow). The default state is the completed sequence diagram, at its last step.
- Every animation gets play/stop buttons. Never autoplay, never loop.

## Export

If the user wants a PDF or PNG, hand the finished file to the `export-explain-visually` skill.
