# Gavin Hermes Workflow Skills

<p align="center">
  <strong>A public, skill-shaped view of a Discord-first AI research workflow.</strong><br/>
  Hermes skills for research decks, paper planning, autonomous handoffs, Thread Canvas artifacts, and agent operating taste.
</p>

<p align="center">
  <a href="https://ritengzhang77-max.github.io/gavin_skill/"><strong>Open the visual landing page</strong></a>
  ·
  <a href="docs/demos/research-deck-demo.html">Slide demo</a>
  ·
  <a href="docs/demos/thread-canvas-demo.html">Thread Canvas demo</a>
  ·
  <a href="docs/demos/paper-plan-demo.html">Paper-plan demo</a>
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
Discord thread → project context → loaded skill → local artifacts → QA → handoff / Thread Canvas
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

Synthetic demos are included so viewers can see the kinds of artifacts these skills are designed to produce:

- [`docs/demos/research-deck-demo.html`](docs/demos/research-deck-demo.html) — slide-style research checkpoint deck.
- [`docs/demos/thread-canvas-demo.html`](docs/demos/thread-canvas-demo.html) — Thread Canvas / clean-chat artifact surface.
- [`docs/demos/paper-plan-demo.html`](docs/demos/paper-plan-demo.html) — paper-planning board mapping claims to figures, controls, and next actions.

These are examples of the artifact style, not private project dumps.

## Skill groups

### Research and writing

- `skills/research/gavin-research-presentations/` — research decks, rendered QA, PPTX/PDF packaging.
- `skills/research/paper-drafting-plan/` — where each result belongs in a paper and what controls/figures it needs.
- `skills/research/gavin-autonomous-research/` — bounded autonomous work until the next decision point.
- `skills/research/research-results-synthesis/` — grounded interpretation of local computational artifacts.
- `skills/research/paper-translation-web-reader/` — side-by-side reading and memorable translation workflow.

### Productivity and deliverables

- `skills/productivity/powerpoint/` — native PPTX authoring/editing.
- `skills/productivity/felix-translation/` — bilingual historical-document translation package workflow.
- `skills/productivity/teams-meeting-pipeline/` — Teams meeting summary operations.

### Hermes / Discord / infrastructure

- `skills/software-development/hermes-gateway-troubleshooting/` — debugging stuck/silent gateway turns.
- `skills/software-development/debugging-hermes-tui-commands/` — TUI/slash command debugging.
- `skills/software-development/hermes-s6-container-supervision/` — container supervision internals.
- `skills/devops/remote-hpc-slurm/` — remote Slurm/HPC control from Hermes.
- `skills/devops/webhook-subscriptions/` — event-driven agent runs.

## What makes the workflow different

- **Skill-encoded taste**: layout rules, claim boundaries, QA expectations, and stop points are stored as reusable procedures.
- **Durable local state**: project handbooks, TODOs, handoffs, manifests, and artifacts keep long-running work coherent across threads.
- **Artifact-first delivery**: decks, HTML dashboards, PDFs, and Thread Canvas pages are treated as first-class deliverables.
- **Bounded autonomy**: the agent can continue work, but stops at decision-changing results, failed prerequisites, or resource conflicts.
- **Public-safe examples**: demos here are synthetic and manually staged; private logs and runtime state are excluded.

## Repository layout

```text
.
├── docs/
│   ├── index.html                         # visual landing page
│   ├── demos/                             # synthetic artifact examples
│   ├── workflow-architecture.md
│   ├── thread-canvas-discord-workflow.md
│   └── PRIVACY_REVIEW.md
├── examples/                              # prompt/output-shape examples
├── templates/                             # project handbook + handoff templates
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
