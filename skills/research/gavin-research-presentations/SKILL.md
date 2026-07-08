---
name: gavin-research-presentations
description: Create Gavin-style research presentations from local project artifacts, defaulting to LaTeX Beamer source plus compiled PDF, with optional native PowerPoint/PPTX, plots, provenance, and Discord-deliverable exports. For no-Aux SAE metric-system decks, use references/noaux-sae-metric-system-decks.md. For Value Action S4/V3/V4 top-15 deck refreshes, use references/value-action-s4-v6style-top15-refresh.md. For Value Action ConsVal full-support counting decks, use references/value-action-consval-fullsupport-counting-decks.md. For Value Action ConsVal magnitude-aware screens/decks, use references/value-action-consval-magnitude-screens.md; when Gavin objects that percentile/exceedance is still frequency-like or asks for magnitude/dominance Tier screens, use references/value-action-consval-magnitude-tier-decks.md. For nonlinear SAE Linear-vs-ResNet detailed comparisons, use the relevant nonlinear-SAE references in this skill.
version: 1.0.0
author: Gavin / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [research, presentations, beamer, latex, powerpoint, pptx, pdf, plots, mechanistic-interpretability]
    category: research
    related_skills: [powerpoint, research-results-synthesis, jupyter-live-kernel, architecture-diagram, excalidraw, manim-video]
    requires_toolsets: [file, terminal]
---

# Gavin Research Presentations

Reference update: for nonlinear-SAE FP/FN ResNet-vs-Linear decks, use `references/fp-fn-resnet-linear-deck-lessons.md` for Gavin-corrected defaults: old green/red row tables, FP as the main metric, FN as appendix/supplement, no FP+FN aggregate pages, one-sided sign tests without “directional” labels, k≤150 sparse-slice tests when useful, and explicit auditing/explanation of undefined FP rates.

## Nonlinear SAE slide-artifact significance updates

When Gavin asks to update nonlinear-SAE V1 evaluation decks/artifacts, use `references/nonlinear-sae-v1-slide-artifact-significance-update.md` for the learned workflow: keep Thread Canvas artifacts to the few final PDFs, merge GPT-2/OPT decks when they share a metric spine, run matched-pair significance tests by all/per-LLM/per-architecture/per-LLM×architecture slices, emphasize low-L0 EV sparse-regime wins when supported, frame redundancy as heterogeneity/sanity-check evidence, and update/QA the actual PDFs rather than only reporting chat findings.

When Gavin asks for nonlinear-SAE FP/FN slides, false-positive/false-negative significance, or separate FP/FN pages for the current-240 fixed-k comparison, use `references/nonlinear-sae-fpfn-significance-deck.md`: make a real PPTX/PDF package with one-sided paired sign tests with H1 = ResNet lower error; default to FP as the main green/red row-table deck and FN as a separate appendix/supplement because forced-on FN is scale/L0-tradeoff dependent; avoid FP+FN aggregate headline pages; for BatchTopK, audit that the loader restores target-k BatchTopK activation before trusting FP/FN candidate counts; include backing CSVs and rendered QA that checks title overlap plus aspect-ratio-preserved table images.

Use this skill when Gavin asks for a presentation, deck, slides, checkpoint PDF,
research status deck, figure-backed summary, or any request that should convert
research findings into a PDF/PPTX artifact he can view from Discord.

Also use it for paper-presentation workspace setup: when Gavin asks to create a
paper-presentation/reading-group channel mapping, folder, and arXiv PDF staging
area, follow `references/paper-presentation-channel-bootstrap.md`.

For reading-group paper decks shown beside an annotated PDF reader, follow
`references/paper-discussion-reader-figures-and-marks.md`: prefer clean crops of
paper figures/tables over abstract redraws when the original visuals are clear,
place method/example figures near the concept introduction, QA every figure/table
slide after PPTX→PDF rendering, and avoid losing underlines by providing
server-side default marks or export/import when browser marks are stored in
origin-scoped localStorage.

## Default Output

Default to a LaTeX Beamer deck and compiled PDF. Gavin especially values:

- editable `.tex` source;
- a compiled `.pdf` that can be sent/opened immediately;
- clear provenance linking claims to local files;
- plots/tables generated from actual artifacts rather than hand-wavy drawings.

If Gavin explicitly asks for PowerPoint, create a native `.pptx` using the
Hermes `powerpoint` skill and treat it as a deliverable package, not merely an
outline. Render that PPTX to a PDF preview and slide images, inspect the render,
fix visual/content issues, and re-render before delivery. If the request is for
Value Action Phase 1.6 Task2 condition-overlap robustness, use the compact
condition-grid deck/package pattern in `references/value-action-phase1-6-pptx-package.md`:
cover behavior agreement, 2×2 condition matrix, feature overlap, rank-gap/stability labels,
claim boundary, and deliver contact sheet + PPTX + PDF. If the Phase 1.6 request
involves feature overlap by value, S1/S2/S3, V1/V2, or answer-agreement splits,
use the corrected per-value package pattern in
`references/value-action-phase1-6-per-value-condition-overlap.md`: keep
`value_item` as the primary unit, separate raw full-basis top-20 overlap from
S/V-selected feature-set agreement, split same-answer vs changed-answer pairs,
and do not present an all-values raw top-20 chart as the value-feature result.
If Gavin asks for Phase 1.7 / 1.7A-B-C makeup runs, use `references/value-action-phase1-7-makeup-runs.md`: for Task1/Task2 top-15s, manually interesting feature interpretation × target value × target option/direction quality is the primary selection criterion, while S/V scores are discovery/evidence filters. If Gavin asks for a Phase 2 Task1↔Task2 value-action gap/overlap deck, same-context gap-vs-no-gap slides, feature-composition paper planning, or a PPTX/PDF review artifact after the Phase 2 overlap exploration, use `references/value-action-phase2-gap-overlap-deck.md`: emphasize the nuanced thesis that raw overlap only weakly separates gap/no-gap while feature composition is the stronger signal; include manual examples, controls, a 20-row Phase 2C pilot plan, safe claims, and run the dense-slide QA loop. If Gavin asks for the conclusion, meaningfulness, or a big-slide summary after the Phase 2.4B category-specific S3/S4/S3∩S4 steering run, use `references/value-action-phase2-4b-category-s34-steering-deck.md`: frame the result as meaningful but category-specific, foreground Cat7 value-side transfer and Cat8/Cat10 action-side survivor leads, state Cat1/2 bridge-control negatives, keep display/order caveats explicit, and QA dense survivor tables for wrapped feature IDs/signature text. If Gavin corrects the framing toward natural activation/asymmetry versus steering/capability, or asks how many Cat1/2/7/8/9/10 feature×value×target rows satisfy S3/S4/S3∩S4 requirements and what that means, use `references/value-action-natural-gap-vs-steering-deck.md` and `references/value-action-phase2-category-direction-overlap-slides.md`: build a big deck that separates natural recruitment/asymmetry from intervention capability, first verifies category/target direction with fake examples, reports category/S-bin denominators and selection bars, includes raw/selected/S3∩S4 overlap percentages before steering claims, lists selected Cat7–10 rows with value/target/source/interpretation/data support, explicitly distinguishes encoded/gap-side steering from gap-closing direction, and make selected-row slides mobile-readable with the one-row-card pattern rather than dense tables; color-code steering classes and explicitly define that `T2 both` means Task2 normal+reversed orders, not Task1+Task2. If the request is about Phase 2.4C-style corrected-intended-direction strict S3/S4 dose/steering results, use `references/value-action-phase2-4c-strict-s34-deck-lessons.md`: define `Task2 exact-source+` versus `Task2 both-order+`, add `Task1+ AND Task2 both+`, clarify pre-answer S3/S4 source rows versus answer-token outcome/Q1 branch, and show selected feature×value×direction records as readable interpretation cards rather than ID-only tables.
If Gavin asks to explain, present, or recall the controversial value-conflict / dataset-crafting plan, first use the existing HTML/Thread Canvas artifact if it exists and the link can be verified; if the tunnel expired, refresh the web-log base URL rather than making a duplicate deck. If no suitable artifact exists or he asks for explanatory pages, prefer a slide-style HTML artifact with crafting logic plus Task1 / implicit Task2 / explicit-control examples before native PPTX unless he explicitly asks for PowerPoint; see `research-results-synthesis` reference `references/value-action-controversial-value-conflict-dataset.md`.
If Gavin asks to turn the controversial value-conflict dataset plan / HTML slide-web into slides, asks to explain the dataset crafting logic, or asks for Task1 + implicit Task2 + explicit-control example pages, use `references/value-action-dataset-crafting-logic-slides.md`: build a real native PPTX/PDF/contact-sheet package, include the 30×50 logic, budget, controls, quality gates, and one readable example page per value-pair conflict; concrete PPTX examples should use concrete A/B actions rather than generic placeholders; inspect long-title example slides individually after LibreOffice rendering because contact sheets can miss title/subtitle overlaps.
If he asks to rethink Phase 2.1 before the full overlap atlas, asks which values have enough Task1/Task2 data, asks for S1/S2/S3/S4 activation coverage at intended sites, asks for “distribution-like” Phase 2 slides around S3/S4/S3∩S4 overlap, or asks for slides to decide whether more data is needed, use `references/value-action-phase2-1r-denominator-activation-audit.md`: build or retrieve the denominator/activation planning deck with per-value minority thresholds, all-three Task1+Task2-normal+Task2-reversed intersections, S-lane count/magnitude coverage at original intended sites, activation-frequency maps, PPTX/PDF/contact-sheet QA, and XLSX/CSV backing tables. Recognition cue: the existing deck is typically named `Phase 2.1R S1234 Denominator + Activation Audit` / `value_action_phase2_1R_s1234_denominator_activation_audit`, exported under `/data/<user>/hermes_exports/value_action_phase2_1R_basic_distribution_slides_YYYYMMDD`; key slides include minority threshold intersection, 56-value balance map, top-20 S-lane coverage, data+activation planning map, and per-value S3/S4 pre-answer magnitude coverage. Do not force all 56 values to be balanced; mark one-sided values underpowered for gap/minority analysis and consider extra data only for naturally mixed or near-threshold values. If Gavin asks for a **big unified Phase 2 distribution/gap/S1234 PPTX or website** covering total data, per-value Endorse/Reject and Option1/Option2 ratios, same-context gap distributions, and S1234/category feature distributions, use `references/value-action-phase2-unified-distribution-gap-s1234-deck.md`: answer that the gap question is valid only on same-context Task1×Task2 pairs, color Endorse with Option1 and Reject with Option2, export exact per-value tables to XLSX/HTML, keep S3/S4/S3∩S4 bins separate, and use readable cards rather than dense candidate tables. For the controversial value-conflict / ConsVal dataset specifically, when Gavin asks for distribution/filtering/category slides about features that are high for individual values, directions, rows, or tasks, use `references/value-action-consval-row-level-distribution.md`: the main unit is `feature × value_pair × semantic_side × task/behavior direction`, not global feature behavior across all values; one-value/one-side/one-task rows are scientifically interesting and should be shown as row-level queues plus per-value-pair distributions. For Phase 3.1 ConsVal full-support tier decks, start with `references/value-action-consval-fullsupport-counting-decks.md. For Value Action ConsVal magnitude-aware screens/decks, use references/value-action-consval-magnitude-screens.md`; if Gavin complains that percentile/exceedance is still frequency-like, asks for target-vs-opposite mean/p90/AUC/excess-mass/mass-share screens, or says the deck can be big, switch to `references/value-action-consval-magnitude-tier-decks.md`: make a larger native-PPTX/PDF magnitude-aware tier deck, use readable row cards rather than dense tables, keep all-5 consensus / AUC-only / 3-of-5 claim strengths separate, export backing CSV/XLSX, and curate Thread Canvas so only the current main deck plus essential context artifacts remain visible. If he asks to focus on the Phase 2.1 last-three S4/S3∩S4 bridge lanes (`10/7/2`, strict S3∩S4, Task1 S4↔Task2 S3∩S4, Task1 S3∩S4↔Task2 S4) and run Task1/Task2 dose plus flip results like prior V6/top15 steering PDFs/PPTXs, use `references/value-action-phase2-bridge-dose-deck.md`: keep metrics at `pre_answer`, run Task1 dose and Task2 normal/reversed dose screens, make PPTX/PDF/XLSX outputs, and defer gap-rate aggregation until after survivor steering. If he asks for dense Phase 2.1/2.1R per-value denominators, target-option activation distributions, S1/S2/S3/S4 count/magnitude coverage, or top-activating-feature inspection, do **not** default to a dense slide deck: use `references/value-action-phase2-1r-activation-audit-browser.md` and build/update an interactive Value Feature Browser page with value/option/site dropdowns, S-lane top-k badges, and sortable feature activation tables. If he then asks for full slides/reporting after focusing on Layer 2 qualitative mixed-value motifs, use `references/value-action-phase2-1r-layer2-qualitative-report.md`: define exact SAE/sparse-feature analysis units, separate global Layer 2 motif discovery from same-context paired examples, foreground Gavin's corrected six report categories (1, 2, and 7-10: aligned mirrors plus gap-specific creed/action override/brake classes) rather than over-emphasizing standalone 3-6 ghosts or funny examples, include counts at multiple filter scopes, and explicitly state whether steering/dose validation has or has not been run for the curated motifs. If he asks about extending dose/free-generation beyond top-15 to the whole feature browser/website, use `references/value-action-all-feature-steering-atlas.md`: verify the current union (771 vs 777), ensure any new union features have V2/V2.1 interpretations, and recommend a staged all-feature atlas with cheap all-pair screens plus selective full V6 rather than full feature×value×option V6. If he also asks to
update paper writing, make the deck and paper update one coordinated deliverable:
add the short methods/results subsection, compact figures/tables, full appendix
details, compile the paper, and export both deck and paper PDFs; see
`references/dense-baseline-paper-pptx-workflow.md`. For baseline/control decks
whose conclusion depends on interpretation or explanation validation, include the
validation-score comparison explicitly, not just predictive metrics and causal
follow-up. If a requested deck is too broad, slow, brittle, or Gavin asks to see
it section-by-section, split it into reviewable section decks and deliver one
section at a time rather than forcing a monolithic deck; see
`references/sectioned-native-pptx-workflow.md`.
If he asks whether the most updated results already have a PowerPoint, inspect
the project's latest presentation indexes/packages before answering; create the
native PPTX only if the current result state is not already covered.
If Gavin asks whether we “remember which slide/deck” covered a Value Action result, or asks to “show me the slide” for an existing analysis, treat it as targeted artifact recall: inspect `RECENT_CHAT.md`, `presentations/`, and `/data/<user>/hermes_exports/`; identify exact slide PNGs from rendered outputs/PPTX text; copy the requested slides plus optional full PDFs into a fresh export folder; and attach the individual slide images first with minimal prose. See `references/value-action-slide-recall-and-targeted-export.md`.
For Value Action Task2, if Gavin asks for the “most updated V6 experiment slides,”
“the full 50+ page V6 slides,” or asks whether you know what deck he means, first
recognize/check the actual S4-corrected V6/V5-style dose + fixed-completion
package and attach it if complete; see
`references/value-action-task2-s4-v6-deck-recognition.md`.
If he asks for a “big”/comprehensive deck covering all major phases, what
happened, what we did, sample results, and claim boundaries, make a synthesis
artifact rather than a concatenation of old checkpoint decks: build a phase
timeline from `todo.md`, `RECENT_CHAT.md`, presentation READMEs, and result
artifacts; include methods, sample plots/features, controls, safe claims, claims
to avoid, next decision-changing steps, provenance, PDF/contact-sheet QA, and
exports. See `references/major-phase-overview-deck.md`. If he asks
for “current stage” or “most updated slides,” do **not** answer with a plan or
recommendation in place of the deck; make a checkpoint/status deck from the
latest artifacts and show it in Discord. See
`references/native-powerpoint-checkpoint-qa.md` for the current PPTX package and
QA pattern,
`references/current-stage-powerpoint-request.md` for the session-specific
pitfall this rule came from, and
`references/real-model-causal-validation-powerpoint.md` for the pattern where a
requested PowerPoint should be built after completing the approved stop-phase
research update, and
`references/branch-specialization-second-role-expansion-powerpoint.md` for the
mixed-result checkpoint-deck pattern after a bounded role-expansion phase fails
part of its gate, and
`references/branch-specialization-phase4c-effect-map-slide.md` for one-slide
round-result checkpoints where the central story is a stratified effect map
(strict-vs-subset claim boundary plus role/family hits), and
`references/branch-specialization-affinity-first-cross-phase-powerpoint.md` for
native PPTX decks that consolidate branch-specialization structural-affinity
results across Phase 4C/Phase 6/Phase 8G after a long-thread/context reset, and
`references/value-action-heavy-substep-pptx-checkpoints.md` for Value Action
phase work where each heavy substep needs its own PPTX/PDF/contact-sheet
checkpoint while the autonomous research phase continues, and
`references/value-action-top15-steering-pptx.md` for native PPTX decks that must
cover every feature in a top-k feature-steering audit with value/option Q-ranks,
dose-response plots, free-generation examples, option-position audit verdicts,
and full CSV/XLSX backing data, and
For revisions to an existing Gavin-reviewed deck, preserve the existing slide spine/visual format unless Gavin explicitly asks for a redesign; add new results into the established format rather than replacing it with a new compact checkpoint style. For Value Action S4 refreshes of the latest Phase 1.4 Task2 top-15 deck, preserving the V6/V5-style spine is not enough: if Gavin asks for the “latest / most updated” version, rerun the actual all-example dose + V6 role-diverse fixed-completion free-generation + blind judge pipeline on the S4 manifest before claiming the deck is finished; see `references/value-action-s4-actual-v6-dose-freegen.md`. For Value Action Task2 “interesting top-15” requests, optimize the manual feature interpretation × target value × target option/direction story rather than metric rank, keep `Feature interpretation` and `Why interesting` as separate table columns, avoid generic rows like Creativity+possessive, and if Gavin says V6/full/latest/50+ pages, deliver or run the actual full V6 package; see `references/value-action-interesting-top15-v6-full-deck.md`. If Gavin says he wants “that V6 thing” but **for this phase / on Task1**, do not attach the existing Task2 V6 package; build or verify the Task1 S4/V3/V4 analogue with Task1 dose, V6 completion generation, blind judging, corrected S4/V3/V4 metric wording, and duplicate-feature-safe row identity; see `references/value-action-task1-s4-actual-v6-dose-freegen.md`. For V3 revisions that preserve
the existing deck spine while adding S/V metric naming, dose-slope-verdict wording,
α=±1/5-sample free generation, expected-direction flip highlighting, balanced-vs-all
example explanations, and causal+interesting feature-set refresh rules.

## Package Layout

Create one versioned presentation package under the project root:

```text
presentations/<theme>/YYYY-MM-DD-HHMM-short-topic/
  README.md
  outputs/
    <deck>.tex
    <deck>.pdf
    <deck>.pptx                  # optional
    <deck>_pptx_rendered.pdf     # optional
  figures/
  data/
  src/
```

Also copy final Discord-deliverable PDFs/PPTXs to
`/data/<user>/hermes_exports/` (or a clear subdirectory such as
`/data/<user>/hermes_exports/decks/` when keeping many decks organized) when

For native PowerPoint checkpoint QA, see
`references/native-powerpoint-checkpoint-qa.md`: render PPTX → PDF → slide
images/contact sheet, inspect visually, fix layout issues, then deliver contact
sheet + PPTX + PDF.
For nonlinear SAE threads whose immediate purpose is to organize existing V1
slide artifacts rather than regenerate them, use
`references/nonlinear-sae-thread-artifact-workspace.md`: locate latest PDFs/PPTXs,
create a small local/export artifact index, register human-readable PDF/PPTX files
into Thread Canvas / Thread Files, and only then discuss whether GPT-2+OPT SAFE
rankings should be merged into a unified cross-model EV/L0 deck. **Thread Canvas delivery pitfall:** when Gavin asks for the Thread Canvas page, give the actual `thread_canvas.html` page or a verified clean alias to it, not the thread `index.html`, not the clean chat log, and not a PPTX/PDF/file-preview link. On mobile/Discord, prefer a short alias under the web-log root with no underscore-heavy channel path, verify it returns `content-type: text/html`, then sync any registered `files/current/` artifacts into that alias before sending. For dense research PPTX decks, also use
`references/pptx-no-cutoff-card-containment-qa.md`: primary scientific text
(feature interpretations, conclusions, status labels) must not be ellipsis-cut
off when intended to be shown, and every card/button/chip background must fully
contain its associated text. When a native PPTX deck has overlapping titles, subtitles,
chips, cards, or footers, use
`references/pptx-overlap-preflight-and-qa.md`: reserve fixed lanes, measure/wrap
long titles, shorten card headings before they wrap into body text, add geometry
preflight checks, rerender with LibreOffice, and inspect dense slides at high
resolution. For nonlinear SAE architecture comparison decks, see
`references/nonlinear-sae-resnet-vs-linear-architecture-pptx.md`: use ResNet-vs-Linear wording when ResNet is the candidate, put AuxK rows before no-Aux rows when both appear, avoid chart legends that overlap footer/color-key text, and add a transparent top-10 EV+L0 rank-sum page when requested. For GPT-2 decks that mirror the updated OPT no-Aux metric-system format while a small training tail is still running/failed, use `references/nonlinear-sae-gpt2-provisional-deck-and-qa.md`: build a visibly provisional checkpoint deck, list missing rows/unequal denominators, preserve the OPT metric spine, and QA dense cards/tables individually after rendering. When that tail later finishes, use `references/nonlinear-sae-gpt2-complete-deck-regeneration.md`: re-verify progress plus final-metrics artifacts, regenerate all CSVs/plots/deck from the full 200/200 universe, scrub stale provisional wording, and ensure empty missing-row CSVs still have headers. When both the Linear 100-run and ResNet 100-run no-Aux universes are complete and Gavin asks for final top-10 rankings plus per-architecture beating maps for OPT/GPT, use `references/nonlinear-sae-final-linear-resnet-ranking-decks.md
- `references/nonlinear-sae-big-width-linear-vs-resnet-gapok.md`: addendum for parameter-matched wider Linear vs ResNet SAFE decks, including the required `Big-R`, `GapOK`, and `LossOK` columns and color semantics.
- `references/nonlinear-sae-big-width-linear-safe-decks.md` — SAFE-style provisional/complete decks comparing corrected ResNet rows against trainable-parameter-matched big-width linear baselines, including exact-EV red/green tables, GapOK/LossOK efficiency-of-EV-gap diagnostics, wall-time summaries/details from `progress.json`, and omitted-row handling.`: verify 100/100 progress plus final metrics/weights, select the corrected/final ResNet sources (tied/shared gated and corrected multi-ResNet Matryoshka), produce separate OPT and GPT PPTX/PDF decks with default global EV/L0 H2 plus the old six Method-2 value-normalized H2 variants, include a rank-correlation-with-H2 table, one top-10 slide per variant, and matched ResNet-vs-Linear beat/loss maps by exact sparsity hyperparameter level. If Gavin asks for a small/simple update using the SAFE ranking-deck format after the pure nonlinear/no-skip runs finish, use `references/nonlinear-sae-pure-nonlinear-compact-ev-l0-deck.md`: make a compact 4-slide PPTX/PDF (OPT/GPT pure nonlinear vs Linear, then OPT/GPT pure nonlinear vs ResNet), keep candidate-first `Pure nonlinear vs baseline` beat/loss/trade wording, and QA individual rendered slide images because tall beatmap PNGs can collide with footers when inserted by width. If Gavin asks to add concentration/dominance scores to these ranking decks, use `references/nonlinear-sae-concentration-diagnostics-ranking-decks.md`: lower top-10/top-50 dominance concentration is better, keep it as a diagnostic rather than an EV/L0 ranking term, preserve the existing EV/L0 outcome colors, add a separate concentration outcome column/page for available families, and display `ΔC = Linear − ResNet` so positive means ResNet is less concentrated. For Value Action feature-explanation audit decks, also see
`references/value-action-v2-1-feature-audit-deck-qa.md`: include V1-vs-V2.x
interpretation changes, manual semantic-interest labels, raw/PCA dense-control
separation, browser update notes, and explicit claim hygiene.

When
Gavin wants the artifact sent through Discord.

## Workflow

1. Resolve the project via `/home/<user>/work/HERMES.md`, the Discord channel,
   or the project `handbook.md`.
2. Read `handbook.md`, `todo.md`, recent-chat/status notes, deck READMEs,
   result summaries, manifests, and relevant CSV/JSON/Markdown artifacts.
3. Use `research-results-synthesis` before writing slides when the result needs
   interpretation, claim hygiene, or metric/sign-convention reconstruction.
4. Generate plots from local CSV/JSON artifacts when they clarify the story.
   Use Python/matplotlib or the project’s existing plotting scripts. Put plots
   in `figures/` and copied source data in `data/`.
5. Write the Beamer deck in `outputs/`, compile to PDF, and inspect the rendered
   PDF for clipping, missing definitions, unreadable tables, and overlapping
   text.
6.   If native PowerPoint is needed, use the `powerpoint` skill and its QA loop:
   build `.pptx`, render to PDF/images with LibreOffice/Poppler, inspect the
   contact sheet and any suspicious individual slides, fix issues, and re-render.
   Common fixes: shorten long titles before they collide with subtitles; enlarge
   short callout cards that clip body text; summarize long provenance/path lists
   instead of printing every path; force conservative hard wrapping inside
   `python-pptx` card bodies because LibreOffice can render auto-wrapped text as
   overflowing single lines; put horizontal-bar labels for negative/small values
   to the right of zero or reserve padding so they do not collide with y-axis
   categories; and keep the exported contact sheet beside the PDF/PPTX for
   Discord review. A contact sheet is only a first-pass overview: for any dense
   or auto-generated research deck, also inspect high-resolution individual slide
   PNGs for every chart/table/card-heavy slide before delivery. If Gavin says a
   deck is “draft-like,” cramped, overlapping, or has text outside boxes, treat
   that as a blocking QA failure, update the relevant presentation reference if
   it allowed the bad pattern, and regenerate with fewer components per slide,
   larger cards, fixed lanes, and split slides rather than patching only the
   offending slide. For metric-heavy research decks, put each non-obvious metric
   definition on its own spacious slide with a line-by-line formula, symbol
   definitions, how-to-read guidance, and one concrete example/readout; do not
   cram metric definitions into one dense table. Hard visual constraint: no text
   visually belonging to a card may extend outside the card after LibreOffice
   rendering; if needed, remove the card background or split into another slide.
   If a prior version of the same deck had any text out of boxes, clipped tables,
   or off-page diagrams, the next revision must switch to a layout-safe pattern:
   no large chart screenshots unless individually inspected, no multi-panel
   diagrams sharing a slide with dense tables, top-10 tables split into ranks
   1–5 and 6–10, abbreviated labels with definitions, conservative margins, and
   high-resolution QA of every dense slide before delivery. Do not claim visual
   QA passed from a contact sheet alone when Gavin has already flagged overflow.
For compact beat/loss or architecture-comparison decks, avoid
   dense narrow PowerPoint tables when two-digit counts or long labels must fit:
   use `references/nonlinear-sae-layout-safe-detail-slides.md` for Gavin's required
   per-architecture detailed Linear-vs-ResNet breakdown slides. For SAEBench
   current-240 fixed-k decks/results, check
   `references/nonlinear-sae-saebench-matryoshka-targetk-adapter.md` before
   interpreting or rerunning Matryoshka rows: linear Matryoshka checkpoints may
   load as thresholded `jumprelu` unless the target-k adapter view is forced. These slides must
   include dead-neuron-bad rows, sort within width by Linear L0 low-to-high,
   recompute robust B/L/trade outcomes, color-code the `Out` cells, and avoid
   boxed legends/chips that can visibly overflow after LibreOffice rendering.
   dense narrow PowerPoint tables when two-digit counts or long labels must fit:
   use row cards plus short colored outcome chips, define abbreviations in a
   footer, and QA the right edge/chips specifically after LibreOffice rendering;
   see `references/nonlinear-sae-compact-beat-loss-pptx.md`. When Gavin asks not
   just for aggregate beat rates but for where fixed-k TopK-family wins/losses
   happen by sparsity, make full per-run table slides with all `width × k` rows,
   neuron count, EV, L0, ΔEV, and BEAT/LOSS; see
When he asks to move
beyond EV/L0 into DAME, dominance, auto-interpretability, or redundancy for
the same fixed-k comparisons, add dominance concentration, dominance-quartile
auto-interp, and high-dominance redundancy views, and keep the claim
conditional until those checks are non-worse/favorable; see
`references/nonlinear-sae-fixed-k-dominance-aware-slides.md`. If Gavin asks for SAEBench core “big slides” with green beat / red loss rows, especially “6 pages for each LLM each architecture,” use `references/nonlinear-sae-saebench-core-beat-loss-slides.md` and, for current-240 Matryoshka target-k repair/significance context, also check `references/nonlinear-sae-saebench-matryoshka-targetk-adapter.md`: build exactly six row-table slides for OPT-125M/GPT-2 × BatchTopK/Corrected Matryoshka/Original TopK, color each SAEBench metric cell from the ResNet-vs-Linear perspective, use a five-primary-metric row vote (KL score, CE score, EV, MSE, Cos) with L0 shown as a sanity column, export PPTX/PDF/contact-sheet plus row/summary CSVs, and QA individual dense slide renders. If he asks for “one unified slide/deck/artifact” while also asking for the six table pages, do **not** drop the table pages: make one human-facing PDF artifact whose first pages are the overview/evaluation-policy/significance pages and whose final six pages are the detailed row-comparison tables; if significance tests are requested, report them for every scored row-vote metric (KL, CE, EV, MSE, cosine), not EV alone. Keep only that PDF promoted in Thread Canvas unless he explicitly asks for sources. If the requested deck combines EV/DAME with dead-neuron and redundancy sanity filters, use `references/nonlinear-sae-ev-dame-quality-filter-deck.md`: mark true FAIL only when the ResNet/candidate side has the problem, keep Linear-only quality problems as separately colored baseline issues, add standalone redundancy and dead-neuron count slides, and color EV/DAME columns independently rather than collapsing to one row verdict. If Gavin asks to regenerate the DAME slides from the new V2 ranking, or asks for the same old DAME/v1 deck format with new data, use `references/nonlinear-sae-dame-v2-deck-workflow.md`: wait for 240/240 DAME V2 completion, verify 240/240 Dominance V2 L0 sanity and split-half stability, use only `*_v2` paths, preserve the old slide spine, and explicitly quarantine v1 outputs. If Gavin asks for the completed DAME V3 High50/Mid25 “same report as before,” per-row green/red checks, High-vs-Mid dominance slices, significance tests, or low-L0/k≤150 focus, use `references/nonlinear-sae-dame-v3-high50-mid25-report.md`: build the High and Mid row-table report from `dame_results_v3_high50_mid25`, headline High-sentence/semantic DAME as the clean ResNet win, keep High-token and Mid as heterogeneity diagnostics, and render/QA the PPTX/PDF/contact sheet before delivery.
an EV+DAME comparison while treating dead neurons/redundancy as “not too bad”
filters, produce the actual PPTX/PDF package immediately rather than stopping
at a CSV/heatmap: use `references/nonlinear-sae-ev-dame-quality-filter-deck.md`
for the quality-gate definition, independent green/red EV/DAME columns, row-card
slide spine, export checklist, and QA pitfalls. If Gavin asks to regenerate the
If Gavin asks to regenerate the DAME slides from the new V2 ranking, or asks for the same old DAME/v1 deck format
with new data, use `references/nonlinear-sae-dame-v2-deck-workflow.md`: wait for
240/240 DAME V2 completion, verify 240/240 Dominance V2 L0 sanity and split-half
stability, use only `*_v2` paths, preserve the old slide spine, and explicitly
quarantine v1 outputs. For EV+DAME quality-filter decks with detailed per-architecture tables, `references/nonlinear-sae-ev-dame-quality-filter-deck.md` is mandatory: add a dedicated table-label explainer slide before dense table pages, define `Q/ΔEV/ΔTok/ΔSent/Tok/Sent/Rdup/Ldup`, prefer `Rdup/Ldup` over ambiguous `Rred/Lred`, and use fixed-lane table layouts that have been high-resolution QA'd for text staying inside cells/cards. For V1 wrap-up significance addenda and focused thread artifact curation, use `references/nonlinear-sae-v1-significance-and-artifact-curation.md`: promote only the few review PDFs Gavin asked for, optionally unify GPT-2+OPT PDFs, mirror DAME paired-row significance tests for EV/redundancy, and remember the L0-filtered EV pitfall that fixed-k EV gains are in low/mid K (k≤100/150) and reverse at k≥200.
- `references/nonlinear-sae-redundancy-deck.md` — redundancy-only ResNet-vs-Linear deck pattern: default Top100 high-dominance decoder redundancy @0.7, six per-LLM/per-family row-table pages, green/grey/red beat/tie/loss coloring, and no EV foregrounding unless requested.`. See
   fixed-sparsity TopK-family beat-rate mini-deck, compare ResNet-vs-Linear by
   matched `width × k`, exclude unfinished gated rows, make one OPT slide and
   one GPT slide, and follow `references/nonlinear-sae-fixed-k-beat-rate-mini-decks.md`.
   See
   `references/native-powerpoint-checkpoint-qa.md`,
   `references/sectioned-native-pptx-workflow.md`, and
   `references/branch-specialization-second-role-expansion-powerpoint.md`.
   If Gavin asks for PPTX reporting for each heavy substep of an autonomous
   phase, create one compact native-PPTX checkpoint package per heavy result
   substep, each generated from local analysis artifacts and exported as PPTX,
   PDF, and contact sheet; see
   `references/value-action-heavy-substep-pptx-checkpoints.md`.
For Value Action ConsVal magnitude/order-robustness deck revisions, use
`references/value-action-consval-magnitude-order-robustness-decks.md`: when a
new robustness analysis is computed after a deck exists, patch the visible deck
or HTML artifact immediately; show pooled, order-direction, and order-robust
views together when Gavin is reasoning about robustness; and publish a
cache-busted verified Canvas link.

For Value Action / ConsVal RQ6 gap-vs-no-gap feature-similarity decks, use
`references/value-action-rq6-signed-contrast-decks.md`: make the main evidence
signed side-specific contrast alignment, include formulas/toy examples, and
remove raw activation-overlap / weighted-Jaccard visuals from the headline spine
because they can be high even when A-vs-B value support flips.

For Value Action RQ6 / feature-usage-similarity decks about whether gap cases
have less/more similar Task1↔Task2 feature usage, use
`references/value-action-rq6-similarity-multiverse-decks.md`: first display the
per-value Task1 / Task2 implicit / Task2 explicit majority map to define gap vs
same, then define the exact vector comparison, then report a metric multiverse
(raw magnitude overlap, signed side-contrast alignment, behavior-product
correlations, gap-only chosen-vs-same-side diagnostics). Do not conclude from a
single top-k Jaccard metric or frame the target as finding a universal moral
feature; keep the safe claim/overclaim boundary visible on-slide.

For “current stage / most updated slides” requests, this step is mandatory:
produce and deliver the slide artifact itself, even if the research stage is
still evolving. For Value Action ConsVal magnitude-aware decks, order-robust addenda, Canvas artifact fixes, and slope/steering plan HTMLs, follow `references/value-action-consval-magnitude-decks-and-slope-plans.md`: put new analyses into the visible deck/HTML and re-register verified direct Canvas links rather than leaving them only in chat. For Value Action RQ6 gap-vs-no-gap feature-similarity decks, follow `references/value-action-rq6-similarity-deck.md`: define behavior-gap labels first, include explicit raw-magnitude and signed-contrast formulas plus a toy numeric example, and frame the safe claim as an SAE-detectable representational correlate rather than a proven full causal mechanism.
   incomplete. If an experiment phase completes while satisfying the request,
   fold the new result into the deck and then deliver the `.pptx` plus preview
   artifacts; do not let a prose-only status report become the final answer. If
   the user has also authorized continued work until a stop phase,
   first finish the approved decision-changing phase, then build the deck from
   the newest artifacts; see `references/real-model-causal-validation-powerpoint.md`.
   Incomplete stages should become checkpoint decks with claim boundaries and
   next experiments, not markdown-only plans.
7. Update `README.md`, `presentations/README.md` if present, and
   `presentations/<theme>/README.md` if present.
8. For checkpoint decks that update an existing storyline, make the last slide
   explicit about the safe claim, the overclaim to avoid, and the next
   decision-changing experiment. For branch-specialization-style updates, this
   often means separating structural role affinity from stronger functional
   modularity claims and pointing to real-model causal validation when toy
   controls weaken the broader claim.

## Nonlinear SAE ranking deck requirements

For Gavin's nonlinear SAE Linear-vs-ResNet ranking decks, include these by default unless he explicitly asks for a smaller checkpoint.

**Pure nonlinear SAFE-format pitfall:** if Gavin asks for pure nonlinear/no-skip comparisons “in the format/style of a corrected final SAFE ranking deck” or says “4 slides” while referencing that SAFE deck, do **not** make four single-page slides. Interpret this as four full SAFE-format decks/slidesets unless he explicitly says single-page summaries. Inspect the referenced SAFE deck spine first, then build separate full decks for OPT/GPT pure-vs-Linear and OPT/GPT pure-vs-ResNet as applicable; see `references/nonlinear-sae-pure-nonlinear-full-safe-ranking-decks.md`.

For Gavin's nonlinear SAE Linear-vs-ResNet ranking decks, include these by default unless he explicitly asks for a smaller checkpoint:

1. **Method-2 six-variant correlation table**: show the old six value-normalized H2 variants and their rank correlations vs the default global rank-H2, then give a separate top-10 slide for each variant.
2. **Per-family detailed matched-pair appendix**: add one slide per architecture family (`Standard`, `Gated`, `TopK`, `Matryoshka`, `BatchTopK`) with all 20 matched rows (4k + 8k × 10 sparsity settings), including dead-neuron-bad rows. Sort each width by Linear L0 low→high so sparse-regime wins/losses are visible.
3. **Dead-neuron handling**: ranking/top-10 slides may apply the dead-feature eligibility gate, but detailed per-family slides must include omitted rows and mark `D%* = dead_frac > 10%`. Do not make the user infer what disappeared.
4. **Correct final architecture sources**: use tied/shared ResNet-gated rows for `Gated` (`nonlinear_resnet_tied_gated`) and corrected multi-ResNet Matryoshka rows for `Matryoshka` (`matryoshka_multi_resnet_topk`, separate ResNet/nonlinear encoder per non-final level plus full encoder), not old asymmetric/dual-gated or shared-prefix Matryoshka unless explicitly labeled as ablations.
5. **Outcome classification**: recompute matched-pair outcomes robustly from EV and L0, not just cached CSV labels. At equal/fixed-k L0, lower ResNet EV is a `loss`, not a `tie`. `Beat` means ResNet EV non-worse and L0 non-worse with one strict improvement; `Loss` is the reverse; `Trade` is one metric better and the other worse.
6. See `references/nonlinear-sae-final-ranking-deck-lessons-2026-06.md` for the concrete corrected-deck checklist, layout pitfalls, architecture-source checks, and metric-explainer wording learned from the June 2026 final ranking deck review.

## Slide Content Standard

- Start with the question, setting, and why the checkpoint matters.
- Define local terms before using them repeatedly.
- Separate evidence classes: raw activation patterns, validated explanations,
  correlational summaries, case studies, causal interventions, and caveats.
- Prefer concrete examples: feature ID, explanation, token/site, activation,
  metric, and text snippet.
- Every important plot needs axis definitions, denominator, and one takeaway.
- Every causal/intervention slide must state operation, site, scale, and outcome
  before interpreting the number.
- When Gavin asks for every feature on a single page, make an actual deck with
  one slide/page per feature rather than only a prose list or compact table.
  For Value Action feature-audit/Q-system decks, include score-system
  definitions, prompt-divergence plots, causal-status wording, and one evidence
  page per selected feature; see
  `references/value-action-qsystem-feature-pages-deck.md`.
- Tables must be readable. Split dense tables across slides or move full tables to `data`/`appendix`. For mobile/Discord deliverables, if the table is meant to be read directly and includes selected row details, prefer one-row or one-feature cards with large text over multi-row tables; do not rely on zooming in Discord.
- For nonlinear SAE comparison PPTX decks, use candidate-first labels such as
  `ResNet vs Linear`, order AuxK rows before no-Aux rows when both appear, avoid
  bottom legends that collide with footer/line elements, and add a top-10 joint
  EV+L0 rank slide when Gavin asks for best runs across architectures/settings;
  see `references/nonlinear-sae-resnet-vs-linear-pptx-comparison-decks.md`.
- For nonlinear SAE percentile-normalized comparison decks, include the exact EV/L0 percentile formulas in the slides and distinguish global/top-checkpoint percentile shortlists from matched ResNet-vs-Linear `ΔH2` pair comparisons.
  For **global top-run or global architecture rankings**, compute percentiles over the full declared eligible run universe after a dead-feature eligibility filter; do not use local `family_group × width` percentiles as absolute utilities. Dead neurons should be a filter/sanity gate, not part of Gavin's default H2 ranking score. For per-architecture slides, show both global rank positions and matched hyperparameter beat/loss ratios. See `references/nonlinear-sae-global-ranking-pptx.md`.
  For older within-family knee selection, percentiles may be computed in fair pools such as `family_group × width`, not inside each two-row pair. Export summary and pair-row CSVs with the deck;
  see `references/nonlinear-sae-percentile-comparison-decks.md`.
  comparable. Dead neurons should normally be an eligibility/sanity filter (e.g.
  discard `dead_features > 0.10 * d_sae`), not part of the H2 score. Export summary
  and pair-row CSVs with the deck; see
  `references/nonlinear-sae-percentile-comparison-decks.md` and
  `references/nonlinear-sae-global-ev-l0-ranking-decks.md`.
- For nonlinear SAE percentile-comparison decks, treat percentile scoring as a
  secondary shortlist layer after matched Pareto beat/loss, not as the win/loss
  evidence. Local percentiles inside `family_group × width` are useful only for
  within-family knee selection; for all-run/global top lists use global EV and
  reversed-L0 percentiles over the whole eligible universe. Include the exact
  formulas, keep dead-feature filtering separate from ranking, separate all-run
  top lists from nonlinear-candidate top lists, and QA long titles/dense tables
  after LibreOffice rendering; see `references/nonlinear-sae-global-ev-l0-ranking-decks.md`.
- For Value Action top-k feature-steering decks, especially when Gavin asks for
  “all 15 features” plus dose-response/free-generation results, do **not** cap
  each feature at a fixed three-page budget. The agent should always keep a
  sense of space: if the main audit, dose change, keyword/free-generation drift,
  or examples are tight, add more slides for that feature rather than shrinking,
  clipping, or overpacking. If Gavin asks to redo the experiment formally rather
  than only re-present existing rows, use the V2 balanced-steering pattern:
  build a target manifest for all top-k features, balance dose examples by
  baseline semantic Option1/Option2 where possible, display `α = -raw_scale` so
  `+α` amplifies and `-α` suppresses, report directional flip counts with
  denominators, use freer replicated generation prompts, and aggregate
  normalized keyword drift by α. Each feature should include the strongest
  value/item and target Option1/Option2 direction, Q1/Q2/Q5 ranks/scores for
  that value-option pair, best Q3/Q4 causal rank when present, dose-response
  plot/summary, free-generation keyword-drift plot/summary, and
  option-position/display-binding audit verdict. Prefer separate plot-backed
  dose-response and keyword/free-generation slides when those plots exist, and
  treat three slides per feature as a minimum spine rather than a cap. Put all
  raw example rows in the deck `data/` folder and an XLSX workbook instead of
  trying to cram every row onto slides; see
  `references/value-action-top15-steering-pptx.md` and
  `references/value-action-spacious-plot-backed-feature-decks.md`. For Gavin-requested
  V3 revisions after he reviews a top-15 steering deck, preserve the existing deck
  spine unless he explicitly asks for a restructure, but add the clarifications he
  requested: use `dose slope verdict` rather than bare `verdict`; show S1/S2/S3 and
  V1/V2 metric naming with old Q names in parentheses; make feature titles/metadata
  clearly refer to the targeted 56-value item and selected target row; explain/order
  the two dose plot panels as order robustness vs baseline-choice decisiveness;
  highlight expected-direction flip cells; use `α = [-10,-5,-1,0,+1,+5,+10]` and
  5 free-generation samples per prompt when requested; handpick/scored representative
  snippets instead of first-row snippets; and prefer causal+interesting feature-set
  refreshes with positive non-control V1/V2 rows plus readable value-relevant explanations.
  See `references/value-action-v3-top15-steering-refresh.md`. When Gavin asks for
  separate K-balanced vs all-example deck versions, or asks to manually insert a
  specific feature into the top-k set, keep every deck/package internally
  consistent by sampling regime, add a front manual feature-ID map with short
  human labels, rebuild the underlying per-feature artifacts rather than only
  editing slide text, and export both full decks plus requested single-feature
  slides; see `references/value-action-sampling-regime-split-and-feature-replacement.md`.
  For V4-style revisions where Gavin wants more interesting feature choices, select
  feature/value rows by both causal evidence and intuitive interpretation ↔
  target-value connection, not evidence alone; add a short Option1/Option2 meaning
  phrase to each feature overview page so ambiguous value labels are clear; see
For post-review display fixes
on Value Action steering decks, keep `Feature`, `O1 often`, and `O2 often` as separate
visible lines, color directional-flip tables by expected steering behavior (toward-target
cells are blue for negative/suppressing α and red for positive/amplifying α, while
away/non-target cells are red for negative α and blue for positive α), and circle only
non-zero flip-count cells with a visible outline while leaving zero numerators uncircled;
see `references/value-action-steering-displayfix-qa.md` and
`references/value-action-steering-nonzero-flip-circles.md`. For Phase 1.7C overlap decks
that Gavin says still have “out of box” slide issues, patch the generator and rerender the
whole PPTX/PDF/contact-sheet package; inspect high-resolution versions of flagged slides,
fix short cards by increasing card height and/or lowering body font, and move dense chart
legends into a reserved lane below the axes rather than inside bar charts; see
`references/value-action-phase1-7c-slide-layout-fix.md`.
  For V5-style all-example Value Action steering revisions, make all-example denominators
the main qualitative deck, use propagated L11 steering as the behavioral default,
remove `±10` from the main alpha grid in favor of `[-7,-5,-3,-1,0,+1,+3,+5,+7]`,
regenerate/merge free-generation rows so every alpha has matched sample counts,
include representative snippets selected by an explicit relatedness audit, and mark
the paper-plan appendix task; see `references/value-action-v5-all-example-steering.md`.
  If Gavin says the free-generation branch is too variant or asks for fixed prefixes,
short completions, fill-in-the-blank completions, manual representative checking, or
blind 0–4 relatedness judging, treat it as a fixed-completion free-gen repair. First
follow `references/value-action-v5-fixed-completion-freegen.md` for the general short-neutral-completion pattern: steering only at the completion boundary/generated tokens, blinded relatedness scoring, and representative snippets chosen from high-score rows with visible highlight reasons. If he asks for “V6”, role-diverse templates, less-redundant templates, prefix-vs-generated-suffix judge wording, short judge explanations, or supporting/opposite direction splits, follow
`references/value-action-v6-role-diverse-completion.md`: use the 10 role-diverse templates, tell the judge to evaluate the generated suffix primarily, ask for JSON evidence quotes/reasons, keep opposite-but-related rows as high relatedness when appropriate, and aggregate overall/supporting/opposite relatedness separately. For deck revisions and significance follow-up, also follow `references/value-action-v6-fixed-completion-deck-and-stats.md`: preserve the V5 deck spine/format unless Gavin requests redesign, add `% score ≥3` to free-generation plots, and use paired feature×template cluster tests against α=0 for V6 completion significance. When chaining generation and judging jobs, use `set -euo pipefail` or explicit `&&`, and verify row-count manifests plus judged-output existence after completion so a failed generation phase cannot be masked by a later `judge done` echo.
  If Gavin has already
  corrected the deck/TODO once, treat the reference's completion checklist as
  mandatory: re-read the plan, verify rendered slides and extracted text, check
  workbook sheets/highlighting, validate row counts/manifests, and only then claim
  the package is complete.
- End with a conservative claim, what would be overclaiming, and the next
  decision/action.

## Visual And Plotting Standard

Use plots/figures when they answer the research question better than prose.
Borrow from Hermes visual skills when appropriate:

- Use Python/matplotlib for result plots and paper-style figures.
- Use `architecture-diagram` for system/workflow diagrams.
- Use `excalidraw` for hand-drawn concept/flow sketches.
- Use `manim-video` only when Gavin asks for animation or a concept needs
  dynamic explanation; otherwise still images are usually enough.

Do not add decorative visuals that do not carry evidence or explanation.

## PowerPoint Bridge

When `.pptx` is requested:

- Use Hermes `powerpoint` skill.
- Prefer `python-pptx` or PptxGenJS for native generation.
- Include the `.pptx` in `outputs/`.
- Render a preview PDF with LibreOffice and inspect it.
- Also render slide images plus a contact sheet when the deck is visual enough
  that Discord preview/QA matters; deliver the contact sheet alongside the PPTX
  and PDF when helpful.
- Extract text when possible and check for placeholder/lorem-style leftovers.
- For branch-specialization affinity decks, use local files as source of truth
after context resets and keep the deck affinity-first: define structural
affinity, show cross-phase rho/widest-head evidence, and explicitly separate it
from Q2 specialization and Q3 modularity. See
`references/branch-specialization-affinity-first-cross-phase-powerpoint.md`.
- For nonlinear SAE architecture comparison decks, make the comparison direction match the scientific claim: if ResNet is candidate and linear is baseline, titles/tables should say `ResNet vs Linear`, not `Linear vs ResNet`. When both AuxK and no-Aux rows appear, order AuxK first, then no-Aux. Avoid duplicating chart legends under figures when footer/color-key text is present; use chips or a compact in-plot legend instead. If Gavin asks for top overall runs by EV and L0, add a dedicated top-10 page with the explicit rank-sum rule and backing CSV; see `references/nonlinear-sae-resnet-vs-linear-architecture-pptx.md`.
- Keep the Beamer/PDF path as the reliable source unless Gavin explicitly wants
  PPTX as the primary artifact.
- For nonlinear-SAE native PPTX comparison decks, follow Gavin's deck-specific
  conventions: title candidate-baseline comparisons as `ResNet vs Linear` when
  ResNet is the candidate, put AuxK rows before no-Aux rows, avoid separate
  matplotlib legends that overlap footer color keys, and explain any `rank
  score` directly on ranking slides. On top-run/best-run/ranking tables, do **not**
  make Gavin infer architecture from run IDs or long method labels: include an
  explicit `Arch` / `best arch` column with `ResNet` or `Linear`, and QA that the
  column is readable after render. If long family/method labels collide, shorten
  display labels rather than dropping the architecture tag. See
  `references/nonlinear-sae-pptx-ranking-deck-qa.md`.

Detailed native-PPTX checkpoint procedure:
`references/native-powerpoint-checkpoint-qa.md`.

When Gavin asks whether his PPTX/PowerPoint skill is connected to Hermes, or asks for a Markdown copy of the skill/docs involved, treat it as a skill-library inspection/export task rather than a deck-generation task. Inspect the Hermes `powerpoint` and `gavin-research-presentations` skills, include any relevant PowerPoint/PPTX references, check the Codex-only `/home/<user>/.codex/skills/latex-ppt-presenter/` for comparison, and export one combined Markdown file under `/data/<user>/hermes_exports/`. Make clear that Codex skills are not active Hermes skills unless ported/installed. See `references/pptx-skill-doc-export.md`.

For nonlinear SAE V1 wrap-up/significance addenda, see `references/nonlinear-sae-v1-significance-addenda.md`: if Gavin asks whether DAME-style significance can be repeated for EV or redundancy, run matched-pair bootstrap/sign/Wilcoxon tests by all/per-LLM/per-architecture/per-LLM×architecture slices before editing slides. Keep the Discord Thread Files drawer minimal: promote only the requested human-facing PDFs unless he asks for PPTX/source/manifest/backing CSVs.

## Discord Formatting

Use this skill’s compiler helper:

```bash
python3 /home/<user>/.hermes/skills/research/gavin-research-presentations/scripts/compile_latex_deck.py path/to/deck.tex
```

It tries `latexmk`, then `pdflatex`, `xelatex`, `lualatex`, and `tectonic`.

## Discord Formatting

In Discord messages, do not use Markdown pipe tables. Summarize with bullets or
fenced `text` tables. Attach the PDF/PPTX/CSV when the artifact matters.

## Stop-Point Rule

When a research run reaches a major insight, a decision point, or an
abandon/reframe point, create a short deck if Gavin asks for a presentation or
if a visual checkpoint would materially help. Do not make decks for trivial
status updates.
