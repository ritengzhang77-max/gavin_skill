# Gavin Hermes Workflow Skills

> **Open the rendered showcase:** https://ritengzhang77-max.github.io/gavin_skill/  
> GitHub `blob/main/*.html` pages show source code. Use the `github.io` links for rendered demos: [Thread Canvas](https://ritengzhang77-max.github.io/gavin_skill/demos/thread-canvas-demo.html), [Paper plan](https://ritengzhang77-max.github.io/gavin_skill/demos/paper-plan-demo.html), [Real deck browser](https://ritengzhang77-max.github.io/gavin_skill/demos/research-deck-demo.html), [Value Action feature atlas](https://ritengzhang77-max.github.io/gavin_skill/demos/value-action-feature-atlas-demo.html), [real GPT-2 SAFE PDF deck](https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/gpt2_corrected_final_linear_resnet_ranking_SAFE.pdf), [PPTX](https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/gpt2_corrected_final_linear_resnet_ranking_SAFE.pptx).


<p align="center">
  <strong>A public, skill-shaped view of a Discord-first AI research workflow.</strong><br/>
  Hermes skills for research decks, paper planning, autonomous handoffs, Thread Canvas artifacts, and agent operating taste.
</p>

<p align="center">
  <a href="https://ritengzhang77-max.github.io/gavin_skill/"><strong>Open the visual landing page</strong></a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/research-deck-demo.html">Real deck browser</a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/thread-canvas-demo.html">Thread Canvas demo</a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/paper-plan-demo.html">Paper-plan browser</a>
  ·
  <a href="https://ritengzhang77-max.github.io/gavin_skill/demos/value-action-feature-atlas-demo.html">Feature atlas</a>
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

Public-safe, near-real demos are included so viewers can see the actual artifact shapes these skills produce: artifact-rich Thread Canvas pages, manuscript-browser paper dashboards with near-real research questions, and rendered HTML/PDF/PPTX deck/contact-sheet QA packages:

- [Open the real deck browser](https://ritengzhang77-max.github.io/gavin_skill/demos/research-deck-demo.html) — actual GPT-2 nonlinear-SAE SAFE ranking deck with slide images, PDF, PPTX, and contact-sheet QA.
- [Open the rendered Thread Canvas demo](https://ritengzhang77-max.github.io/gavin_skill/demos/thread-canvas-demo.html) — clean-chat artifact surface with clickable promoted files and right-side previews.
- [Open the rendered paper-plan browser](https://ritengzhang77-max.github.io/gavin_skill/demos/paper-plan-demo.html) — clickable manuscript hierarchy mapping claims to figures, controls, and next gates.
- [Open the Value Action feature atlas](https://ritengzhang77-max.github.io/gavin_skill/demos/value-action-feature-atlas-demo.html) — searchable public-safe feature/value/evidence browser.
- [Open the real GPT-2 SAFE PDF deck](https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/gpt2_corrected_final_linear_resnet_ranking_SAFE.pdf) / [PPTX](https://ritengzhang77-max.github.io/gavin_skill/demos/artifacts/gpt2_corrected_final_linear_resnet_ranking_SAFE.pptx) — actual nonlinear-SAE artifact package.

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
