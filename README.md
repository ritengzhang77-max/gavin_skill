# Gavin Hermes Workflow Skills

> **Open the rendered showcase:** https://ritengzhang77-max.github.io/gavin_skill/  
> GitHub `blob/main/*.html` pages show source code. Use the `github.io` links for interactive demos: [Thread Canvas](https://ritengzhang77-max.github.io/gavin_skill/demos/thread-canvas-demo.html), [Paper plan](https://ritengzhang77-max.github.io/gavin_skill/demos/paper-plan-demo.html), [Value Action feature atlas](https://ritengzhang77-max.github.io/gavin_skill/demos/value-action-feature-atlas-demo.html). For slides, use the direct [pure Hermes-built PDF](https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/hermes-built-research-deck.pdf) / [PPTX](https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/hermes-built-research-deck.pptx).


<p align="center">
  <strong>A public, skill-shaped view of a Discord-first AI research workflow.</strong><br/>
  Hermes skills for research decks, paper planning, Thread Canvas artifacts, and agent operating taste.
</p>

<p align="center">
  <a href="https://ritengzhang77-max.github.io/gavin_skill/"><strong>Open the visual landing page</strong></a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/thread-canvas-demo.html">Thread Canvas sample</a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/paper-plan-demo.html">Paper-plan browser</a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/value-action-feature-atlas-demo.html">Feature atlas</a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/hermes-built-research-deck.pdf">PPTX/PDF package</a>
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

## Visual entrypoint

The designed landing page lives in `docs/index.html` and is suitable for GitHub Pages:

```text
docs/index.html
```

If Pages is enabled for this repo from the `docs/` folder, it should appear at:

```text
https://ritengzhang77-max.github.io/gavin_skill/
```

## Demo artifacts

Public-safe, near-real demos are included so viewers can see the actual artifact shapes these skills produce. Interactive demos are reserved for browser-style artifacts; the slide artifact is linked directly as a PDF/PPTX package rather than wrapped in an unnecessary extra slide viewer.

- [Open the Thread Canvas sample](https://ritengzhang77-max.github.io/gavin_skill/demos/thread-canvas-demo.html) — real Thread Canvas-style clean-chat + promoted-file preview surface.
- [Open the rendered paper-plan browser](https://ritengzhang77-max.github.io/gavin_skill/demos/paper-plan-demo.html) — clickable manuscript hierarchy mapping claims to figures, controls, and next gates.
- [Open the Value Action feature atlas](https://ritengzhang77-max.github.io/gavin_skill/demos/value-action-feature-atlas-demo.html) — searchable public-safe feature/value/evidence browser.
- [Open the pure Hermes-built PDF](https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/hermes-built-research-deck.pdf) / [PPTX](https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/hermes-built-research-deck.pptx) — native deck package with contact-sheet QA.

Preview screenshots:


<p align="center">
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/thread-canvas-demo.html"><img width="420" alt="Thread Canvas sample" src="docs/demos/screenshots/thread-canvas-sample.png"></a>
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/paper-plan-demo.html"><img width="420" alt="Paper plan browser" src="docs/demos/screenshots/paper-plan-browser.png"></a>
</p>
<p align="center">
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/value-action-feature-atlas-demo.html"><img width="420" alt="Value Action feature atlas" src="docs/demos/screenshots/value-action-feature-atlas.png"></a>
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/hermes-built-research-deck.pdf"><img width="420" alt="Pure Hermes-built PPTX/PDF package" src="docs/demos/screenshots/pptx-pdf-package.png"></a>
</p>
These are examples of the artifact style, not private project dumps.

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
│   ├── index.html                         # visual landing page
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
