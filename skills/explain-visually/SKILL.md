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

### When to animate

- Animate flows in architecture diagrams and workflows only when the steps reveal something the static diagram can't show at once (state that changes, messages that replace each other, branches that differ per run). If the full diagram already shows the order, keep it static.
- This applies equally to workflows and to execution flows through an architecture: a numbered flow is not by itself a reason to animate. Numbered labels, ordered edges and a legend usually convey the order at once — prefer that.
- Links between elements in an architecture get no flowing dots and no dash animation under the rule above.
- Switching between variants of an architecture (layout changes in the diagram) is instant — no morph, no lerp.

### Reduced motion

- Disregard local reduced-motion settings entirely. No `prefers-reduced-motion` branches, no frozen frames, no instant jumps, no shortened durations. The user runs macOS "Reduce motion" on, and such shortcuts hide the explanation.

### Controls

- Every animation gets play/stop buttons. The play button acts as a real stop while running.
- Any step-through player (prev / next / play) also gets a back-to-start (double left arrow, ⏮) and a fast-forward-to-end (double right arrow, ⏭).
- The default state is the completed diagram at its last step. Switching variants or rounds also lands on the last step.
- Never autoplay — not the hero, not simulators; every animation waits for its play/run button.
- Never loop. An animation plays once and rests on its final frame; play after the end restarts it.

### Side panels

- Sequence and trace side panels carry no code snippets: title, description and control badge only.

## Export

If the user wants a PDF or PNG, hand the finished file to the `export-explain-visually` skill.
