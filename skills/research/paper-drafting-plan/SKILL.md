---
name: paper-drafting-plan
description: Use when a research phase/result finishes and Gavin wants to decide where each new result, analysis component, figure, table, control, limitation, or planned experiment belongs in the main paper and appendices.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [research, paper-writing, manuscript-planning, appendix-organization, phase-handoff]
    category: research
    related_skills: [research-paper-writing, research-results-synthesis]
    requires_toolsets: [file, terminal]
---

# Paper Drafting Plan

## Overview

Use this skill after a research phase, result checkpoint, deck, audit, or major analysis completes. The goal is **not** to immediately write polished prose. The goal is to keep a durable map from research artifacts to manuscript locations so that valuable work is not lost:

- what belongs in the main paper;
- what belongs in appendices;
- what is only a control/limitation/caveat;
- what is not paper-ready yet but may become useful;
- what remains blocked or planned.

For Gavin's projects, update a project-local planning document each time, rather than relying on Discord history. Prefer concise section/appendix ledgers with artifact paths and claim boundaries.

When Gavin asks whether a mature research project is ready to become a conference paper and uploads an older draft plus a venue author kit, do not only give a strategic yes/no. Create a paper-specific workspace, import the old draft as a theory/source seed, import the venue template into a manuscript directory, and produce the markdown + HTML paper-plan dashboard in the same pass. For the July 2026 nonlinear SAE / AAAI pattern, see `references/nonlinear-sae-aaai-paper-planning-2026-07.md`.

## When to Use

Use when the user says or implies:

- "phase is done; update the paper plan"
- "where should these results go in the paper?"
- "organize main paper and appendix"
- "keep track of everything we have done"
- "what have we got for the manuscript so far?"
- "after this phase, call/update the paper drafting plan"

Do **not** use for a pure literature review, full manuscript drafting, or venue formatting unless the user asks; use `research-paper-writing` for those broader tasks.

## Required Inputs To Inspect

1. Resolve the project root from the Discord channel / router / user message.
2. Read the project status anchors first:
   - `handbook.md`
   - `todo.md`
   - `RECENT_CHAT.md` or equivalent handoff file
   - existing paper workspace (`paper/...`) if present
3. Read any project-local naming or terminology notes before updating the plan. For Value Action, inspect `/home/<user>/value_action/docs/VALUE_ACTION_S_AND_V_METRIC_RENAMING.md` and use S1/S2/S3 + V1/V2 naming rather than old Q1-Q5 names. For nonlinear SAE plans that extend EV/L0 comparisons into auto-interpretability, dominance, or redundancy, use `references/nonlinear-sae-dominance-aware-metric-plan.md`: keep fixed-`k` sparse-regime wins separate from interpretability claims until dominance-stratified auto-interp and high-dominance redundancy checks are planned/run.
4. Read the phase result summary files before raw tables:
   - `RUN_SUMMARY.md`, `*_SYNTHESIS.md`, `*_RESULTS.md`, `*_PLAN.md`
   - presentation `README.md` files
   - paper `README.md`, `main.tex`, section files, appendix files, provenance ledgers
5. Only inspect raw CSV/JSON when counts, denominators, or artifact coverage need verification.

## Durable Output Files

Create or update a project-local markdown source file named one of:

```text
paper/<paper-name>/PAPER_DRAFTING_PLAN.md
paper/PAPER_DRAFTING_PLAN.md
PAPER_DRAFTING_PLAN.md
```

Also create or update an adjacent static HTML companion:

```text
paper/<paper-name>/PAPER_DRAFTING_PLAN.html
paper/PAPER_DRAFTING_PLAN.html
PAPER_DRAFTING_PLAN.html
```

Choose the paper-specific location if a paper workspace exists. Treat the markdown as the durable text source and the HTML as Gavin's always-readable planning dashboard. Both files should carry the same `Last updated`, project root, paper root, and source-plan metadata.

The markdown file should include:

```markdown
# Paper Drafting Plan

Last updated: YYYY-MM-DD
Project root: ...
Paper root: ...
HTML companion: ...

## Current Paper Thesis
## Main Paper Section Plan
## Appendix Plan
## Result-to-Section Ledger
## Result-to-Code / Artifact Links
## Planned / Not Yet Ready
## Open Claim Hygiene Questions
## Next Update Trigger
```

The HTML companion should be a standalone, dependency-free file with inline CSS/JS and should include:

- a compact paper thesis / current drafting decision panel;
- a clickable hierarchy for main-paper sections, subsections/subsubsections/paragraph nodes, appendix sections/subsections, and planned-but-undrafted nodes;
- a preview panel for each hierarchy node:
  - if a `.tex` source exists, show rough rendered draft text for that section/subsection;
  - if the node is only planned, show the writing intent, claim boundary, gate, and supporting artifact/code paths;
  - for section-level nodes, include child subsection buttons and a drawer with full text including children; that full-node drawer must also include the rendered tables, figures, and diagrams referenced anywhere in those child subsections;
- main-section cards or tree nodes showing section, claim role, draft status, and linked `.tex` file when present;
- appendix cards/tree nodes with stable appendix letters/subsections;
- table/figure previews where possible: surface linked `\input{tables/...}` files as preview/source blocks and available figures/images as browser previews, while clearly noting that browser rendering is not final paper rendering;
- a result-to-section ledger with status chips (`draft-ready`, `needs writeup`, `planned`, `exploratory`, etc.);
- a result-to-code/artifact ledger linking local paths for scripts, analysis folders, tables, decks, browsers, and provenance files;
- open claim-hygiene questions and next drafting gates;
- filter/search controls if the ledger is large;
- a collapsible left-hand hierarchy for main sections, subsections, appendix sections, and planned-but-undrafted nodes; default view should show only first-level nodes, with per-node expand/collapse buttons plus a show-all/collapse-all control;
- a right-hand preview panel: if a `.tex` source exists, show rough rendered draft text; if not drafted, show the plan/claim boundary; parent section previews should expose child subsection links and a full-node preview option;
- citations and references styled as distinct colored inline chips rather than raw LaTeX;
- formula/math notation rendered as readable browser math (inline math chips and display-math blocks with subscripts/superscripts/fractions/symbols) rather than showing raw LaTeX commands like `\mathbb`, `\frac`, `\begin{align}`, or `\[...\]`;
- basic manuscript typography preserved in previews: section/subsection/subsubsection/paragraph headings should render as headings, `\textbf{}` as bold, `\emph{}` as italics, list items as browser lists, and blockquotes/other simple markdown-like structure where feasible;
- for the Value Action-style implementation details and pitfalls Gavin corrected in June 2026, consult `references/value-action-html-dashboard-2026-06.md`;
- table inputs rendered as readable HTML tables when possible, and figures/diagrams embedded as image previews when available; do not show raw LaTeX table source as the primary preview;
- print-friendly styling so Gavin can export it to PDF or screenshot it.

Detailed implementation pattern: `references/html-preview-dashboard.md`. For Discord-thread delivery and Value Action-style preview artifacts, also consult `references/discord-thread-artifact-paper-preview.md`. Prefer a reproducible builder script under the paper workspace (for example `scripts/build_paper_planning_dashboard.py` or `scripts/build_paper_preview_mode.py`) over hand-editing large static HTML dashboards.

Update these files after each completed phase. If the update is large, preserve important prior decisions in an archive section rather than deleting them.

## Main Paper Planning Rules

For each new result/component, decide whether it is:

1. **Main claim** — belongs in a main Results section, with a short table/figure and tight claim.
2. **Method standard** — belongs in Methods or Experimental Setup.
3. **Control baseline** — may belong in main Results if it changes interpretation; full details go appendix.
4. **Case study** — one or two representative examples in main; full inventory in appendix.
5. **Diagnostic / caveat** — Discussion or Limitations; detailed evidence appendix.
6. **Infrastructure / browser / tooling** — Reproducibility or appendix unless central to the paper.
7. **Planned but incomplete** — keep in `Planned / Not Yet Ready`; do not write as a result.

For every main-paper placement, record:

```text
section/subsection:
claim role:
artifact paths:
code / generating scripts:
source data paths:
canonical tables/figures:
claim boundary:
status: draft-ready | needs table | needs figure | needs verification | planned
```

If a result already has a provenance entry, link the HTML and markdown ledger to that provenance file rather than duplicating every command inline. If provenance is missing, add a short `needs provenance` gate in the result-to-code/artifact ledger.

## Appendix Organization Rules

Use appendices as lettered top-level buckets and numbered subsections within each bucket:

```text
Appendix A — Metric definitions and formulas
  A1 S1 answer-site association screen
  A2 S2 content/action-span association screen
  A3 S3 pre-decision contrast-contribution screen
  A4 V1 singleton causal decisiveness validation
  A5 V2 small-bundle Shapley causal decisiveness validation
  A6 P0 whole-probe quality diagnostic

Appendix B — Feature pools and feature identity
  B1 pool definitions
  B2 manifest/union accounting
  B3 explanation/validation pipeline

Appendix C — Dataset/task/value distribution
  C1 prompt/task variants
  C2 answer-format variants
  C3 value/family/item balance

Appendix D — Artifact index and reproducibility
  D1 scripts
  D2 data roots
  D3 browser/deck/export paths
```

When new experimental phases accumulate, add later appendix letters rather than overloading A-D. Keep experimental appendices separate from non-experimental/method appendices unless Gavin asks otherwise.

## HTML Companion Dashboard Rules

The HTML file is for planning and discussion, not for replacing provenance ledgers or manuscript source. Build it so Gavin can open it directly in a browser from the project checkout.

If Gavin asks for a “paper preview mode,” “web-like paper preview,” or says it should be “like the Value Action one,” build a separate `PAPER_PREVIEW_MODE.html` when useful: a manuscript-browser interface with a collapsible hierarchy, right-side reading pane, planned nodes for undrafted result sections, and rough-rendered seed text only where real source text exists. Do **not** invent final paper prose for planned sections; show plan, claim boundary, gates, and artifact paths instead. If he asks to attach it to the Discord thread, register it as a Thread File via `scripts/manage_discord_web_log.py add-file` and verify the Cloudflare URL. See `references/discord-thread-artifact-paper-preview.md`.

If Gavin asks for an HTML link he can open while away from the server, expose the dashboard through the existing project browser/Cloudflare pattern rather than only returning a local file path. See `references/public-paper-planning-link.md` for the reusable quick-tunnel + served-entrypoint pattern.

Minimum structure:

```text
<header> title, last updated, source markdown path, project/paper roots
<nav> jump links to preview browser, result ledger, artifact links, gates
<section id="browser"> two-pane hierarchy + preview panel
  <aside> searchable/filterable tree for main sections/subsections and appendices
  <main> selected-node preview: drafted text or planned intent/gate
<section id="ledger"> filterable result-to-section table/cards
<section id="artifacts"> result-to-code/artifact links, or per-node artifact cards
<section id="gates"> planned work, claim hygiene questions, next trigger
```

Implementation rules:

- Keep it standalone: no remote CSS, JS, fonts, or CDN dependencies.
- Use normal local path text (`/home/<user>/...`) rather than `file://` links unless Gavin asks; browsers often block file links differently across contexts.
- Make status visually scannable with small colored chips, but keep all information readable as text.
- Add a visible "source generated from" note if the HTML was generated from an existing markdown plan whose date differs from today's date.
- Include enough artifact/code paths for each result that Gavin can jump from "what section do I write?" to "what script/table/report supports it?".
- If you cannot verify a code path, mark it `needs provenance` instead of inventing one.
- Prefer a hierarchy + preview layout over one giant dense table when the user is discussing manuscript organization.
- If a public/openable link is needed away from the server, serve the static dashboard through the existing project browser/http-server + Cloudflare tunnel pattern and verify the public URL. Explicitly mention that Cloudflare quick-tunnel URLs are temporary unless a named tunnel is configured.

## Result-to-Section Ledger Template

For Gavin-facing chat responses from this skill, show the plan as **monospace aligned tables inside plain triple-backtick code blocks**, not Markdown pipe tables. Discord shows Markdown pipe tables as raw text with unaligned columns, which Gavin cannot read.

Use this shape in replies:

```
Phase / result                  Main placement          Appx   Status
------------------------------  ----------------------  -----  ------------
S/V metric standard             Methods                 A      draft-ready
all-56 S/V item sweep           Results                 E      draft-ready
raw/PCA dense controls          Results                 F      draft-ready
Task2 prompt reversal           Results / Limits        G      needs writeup
Task1 clean-option branch       Methods / Results       H      needs writeup
```

Formatting rules:

- Use a plain code block: start with ``` only, not ```text.
- Pad columns with spaces so headers and row values line up visually.
- Split wide ledgers into multiple small aligned tables by status/topic.
- Keep columns short: `Item`, `Main`, `Appx`, `Status`, `Gate`.
- Wrap long cells onto continuation lines under the same column instead of letting any row push horizontally past the visible page/chat width.

## Claim Hygiene Checklist

Before assigning a result to the main paper, answer:

- What exactly is the unit of analysis? (`feature`, `value_item`, `prompt cell`, `branch`, etc.)
- Is the result descriptive/probe-only, causal, Shapley over a small bundle, or free-generation steering?
- Are answer-token, action-span, pre-answer, and reason-token sites kept separate?
- Are normal/reversed option order and answer-format variants kept branch-labeled?
- Are controls and dense baselines represented?
- Is there a clear limitation if scaffold/position/syntax features dominate?
- Are counts/denominators verified from artifacts rather than memory?
- Does the result need a figure/table before it is draft-ready?

## Reporting Back To Gavin

After updating the plan, report:

1. Where the durable markdown plan file is.
2. Where the HTML companion dashboard is.
3. The current main-paper skeleton.
4. The appendix A/B/C... organization.
5. A result-to-section ledger for completed and planned phases.
6. The biggest not-yet-written or not-yet-done pieces.

Formatting rule for Gavin-facing replies:

- Use monospace aligned tables in plain triple-backtick code blocks.
- Start code blocks with ``` only; do not use a visible language label like ```text.
- Do not use Markdown pipe tables for this skill, because Discord shows them raw and unaligned.
- Split wide tables into several smaller aligned tables.
- Keep columns short: `Item`, `Main`, `Appx`, `Status`, `Gate`.
- If a cell is too long, continue it on a new line under the same column. Never let long cells push into the next column or off the PDF/chat page.

## Common Pitfalls

1. **Dumping every result into Results.** Main paper needs a small number of claim-bearing results; appendices can hold the full audit trail.
2. **Mixing evidence classes.** S1/S2/S3 screens, V1/V2 causal validations, small-bundle Shapley, and free-generation steering are different evidence types. During transition, mention old Q names only parenthetically when needed.
3. **Forgetting completed controls.** Negative/control results often shape the central claim and should be planned explicitly.
4. **Treating planned work as done.** Keep incomplete phases in a planned section with explicit gates.
5. **Using appendix letters inconsistently.** Once Appendix E is all-56 audit, do not later reuse E for prompt robustness.
6. **Relying on chat memory.** Always ground placements in local artifacts and write the durable plan file.
7. **Returning only a local path when Gavin asks for an anywhere-openable link.** For Discord/mobile access, publish or link the HTML through a served browser directory and Cloudflare tunnel, verify the public URL, and state the quick-tunnel persistence caveat.

## Verification Checklist

- [ ] Project root and paper root resolved.
- [ ] Existing paper `main.tex` / section files inspected if present.
- [ ] Latest project `todo.md` and handoff/recent-chat notes inspected.
- [ ] Every completed phase has a proposed main and appendix location.
- [ ] Appendix letters and subsection IDs are unique and stable.
- [ ] Planned/incomplete work is clearly separated from completed results.
- [ ] Claim boundaries and evidence class are recorded.
- [ ] Durable `PAPER_DRAFTING_PLAN.md` updated.
- [ ] Static `PAPER_DRAFTING_PLAN.html` companion updated and opens without external dependencies.
- [ ] Result-to-code/artifact links are recorded or explicitly marked `needs provenance`.
- [ ] Response includes the markdown plan path, HTML path, and compact section ledger.
