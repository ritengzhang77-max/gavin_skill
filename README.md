# Gavin Hermes Workflow Skills

> Working artifacts from Gavin's Discord-first Hermes research workflow. Use the `github.io` links below for rendered interfaces and native presentation files; GitHub `blob/main/*.html` shows source code instead of rendering.


<p align="center">
  <strong>A public, skill-shaped view of a Discord-first AI research workflow.</strong><br/>
  Hermes skills for research decks, paper planning, Thread Canvas artifacts, and agent operating taste.
</p>

<p align="center">
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/thread-canvas-demo.html">Thread Canvas workflow</a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/paper-plan-demo.html">Paper-plan browser</a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/value-action-feature-atlas-demo.html">Feature atlas</a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/value-mechanism-evidence-deck.pdf">PPTX/PDF package</a>
</p>

<p align="center">
  <img alt="Hermes skills" src="https://img.shields.io/badge/Hermes-Agent-7170ff?style=for-the-badge">
  <img alt="Workflow" src="https://img.shields.io/badge/workflow-Discord%20%E2%86%92%20Files%20%E2%86%92%20Artifacts-23252a?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-f7f8f8?style=for-the-badge">
</p>

---

## What this repo is

This repository is a public-safe package of Gavin's Hermes Agent workflows. It is meant to show the **operating system around the research**, not just individual prompts:

```text
Discord thread → project context → loaded skill → local artifacts → QA → Thread Canvas
```

The central idea is that a strong agent workflow should be inspectable. Skills encode the things that otherwise live only in repeated chat corrections: deck taste, evidence hygiene, stop rules, artifact routing, readable layout standards, and what counts as “done.”

## Workflow artifacts

Each artifact shows a different part of the working research process: academic discussion, manuscript planning, result exploration, and native presentation delivery.

- [Open the Thread Canvas workflow](https://ritengzhang77-max.github.io/gavin_skill/demos/thread-canvas-demo.html) — a substantive mechanistic-interpretability discussion beside a restrained academic slide in a natural PDF viewer.
- [Open the rendered paper-plan browser](https://ritengzhang77-max.github.io/gavin_skill/demos/paper-plan-demo.html) — section and subsection hierarchy beside a manuscript preview with a formula, definitions, and evidence table.
- [Open the Value Action feature atlas](https://ritengzhang77-max.github.io/gavin_skill/demos/value-action-feature-atlas-demo.html) — a searchable value, feature, evidence, and explanation interface.
- [Open the rendered PDF](https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/value-mechanism-evidence-deck.pdf) / [PPTX](https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/value-mechanism-evidence-deck.pptx) — a four-page academic methods deck in native presentation and document formats.

Preview screenshots are shown one per row so the labels and UI details are readable.

### 1. Thread Canvas workflow

<a href="https://ritengzhang77-max.github.io/gavin_skill/demos/thread-canvas-demo.html">
  <img width="1000" alt="Thread Canvas workflow" src="https://ritengzhang77-max.github.io/gavin_skill/demos/screenshots/thread-canvas-workflow.png">
</a>

### 2. Paper-plan browser

<a href="https://ritengzhang77-max.github.io/gavin_skill/demos/paper-plan-demo.html">
  <img width="1000" alt="Paper-plan browser" src="https://ritengzhang77-max.github.io/gavin_skill/demos/screenshots/paper-plan-browser.png">
</a>

### 3. Value Feature Browser

<a href="https://ritengzhang77-max.github.io/gavin_skill/demos/value-action-feature-atlas-demo.html">
  <img width="1000" alt="Value Action feature atlas" src="https://ritengzhang77-max.github.io/gavin_skill/demos/screenshots/value-action-feature-atlas.png">
</a>

### 4. Native PPTX + PDF delivery

<a href="https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/value-mechanism-evidence-deck.pdf">
  <img width="1000" alt="Native PPTX and PDF academic methods deck" src="https://ritengzhang77-max.github.io/gavin_skill/demos/screenshots/pptx-pdf-package.png">
</a>

These artifacts are staged from real workflow structures while excluding private project logs and runtime state.

## Skill groups

This showcase is intentionally narrow: it includes Gavin/Hermes workflow skills we built or substantially customized together. Generic Hermes package skills and friend-specific workflows are not showcased here.

### Research workflow skills

- `skills/research/gavin-research-presentations/` — Gavin-style research decks, rendered QA, PPTX/PDF packaging, and slide evidence hygiene.
- `skills/research/paper-drafting-plan/` — paper-section/appendix planning dashboards and manuscript preview browsers.
- `skills/research/research-results-synthesis/` — Gavin/Hermes local research interpretation workflow for reading result artifacts, claim boundaries, and project status. This is not presented as a stock Hermes package skill.

### Hermes / project operations skills

- `skills/software-development/hermes-gateway-troubleshooting/` — debugging Gavin's Discord/Hermes gateway workflow.
- `skills/software-development/debugging-hermes-tui-commands/` — debugging Hermes TUI/slash-command behavior in this environment.
- `skills/devops/remote-hpc-slurm/` — Gavin's remote HPC/Slurm workflow conventions.

### Attribution note

Removed from the public showcase: friend-specific workflows and generic upstream/helper skills that should not be implied as Gavin-built. If a future page needs a stock Hermes package skill, it should be marked as upstream/stock.

## What makes the workflow different

- **Skill-encoded taste**: layout rules, claim boundaries, QA expectations, and stop points are stored as reusable procedures.
- **Durable local state**: project handbooks, TODOs, handoffs, manifests, and artifacts keep long-running work coherent across threads.
- **Artifact-first delivery**: decks, HTML dashboards, PDFs, and Thread Canvas pages are treated as first-class deliverables.
- **Public-safe demos**: demos here are near-real, artifact-backed, and manually staged; private logs and runtime state are excluded.

## Repository layout

```text
.
├── docs/
│   ├── index.html                         # simple GitHub Pages index for separate examples
│   ├── demos/                             # near-real public-safe artifact examples
│   ├── workflow-architecture.md
│   ├── thread-canvas-discord-workflow.md
│   └── PRIVACY_REVIEW.md
├── examples/                              # prompt/output-shape examples
├── templates/                             # project handbook templates
├── code-comparisons/                      # before/after workflow comparison scaffold
├── skills/                                # curated Hermes SKILL.md workflows
└── scripts/privacy_scan.py                # lightweight pre-public scan
```

## Privacy stance

This is not a dump of `~/.hermes`. It deliberately excludes credentials, logs, raw sessions, memories, and private project artifacts. Supporting per-project reference files from live skills were omitted from the public tree and archived separately for private review.

Before public release or major updates, run:

```bash
python scripts/privacy_scan.py
```

Then complete `docs/PRIVACY_REVIEW.md` manually.
