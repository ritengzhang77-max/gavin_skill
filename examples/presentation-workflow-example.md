# Example: Research Presentation Workflow

Synthetic prompt:

> Create a checkpoint deck from the latest local experiment artifacts. Explain the setup, show the formulas, include one toy example, summarize the strongest result, and QA the rendered PDF for overflow.

Expected workflow:

1. Load the presentation skill.
2. Resolve project root and artifact root.
3. Read handbook/TODO/handoff and relevant result files.
4. Draft slide plan before rendering.
5. Build LaTeX Beamer or PPTX.
6. Render to PDF/images.
7. Inspect rendered slides for overflow, tiny tables, and off-page elements.
8. Export final deck to a human-facing location.
9. Answer with concise bullets plus direct file links.

Quality bar:

- Literal grounded titles.
- Pedagogical order.
- Formula/setup slides before result slides.
- Dense tables moved to appendix or XLSX.
- No link-only reply.
