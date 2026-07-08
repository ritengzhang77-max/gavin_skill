---
name: gavin-autonomous-research
description: Use when Gavin asks Hermes to work autonomously on a local research project, continue an experiment plan, run or monitor research stages, work while he is away/asleep, or advance a project until the next meaningful decision point. Merges Gavin's Codex autonomous research policies with Hermes project routing, GPU checks, artifacts, presentations, and kanban/Codex delegation.

<!-- Support reference: references/branch-specialization-broad-sweep-launches.md covers branch-specialization broad matched real-language sweep launch/reporting patterns, GPU checks, probe-count verification, and caveats around tiny trained real-language LMs versus pretrained Pythia hetero evidence. -->
<!-- Support reference: references/nonlinear-sae-auxk-core5-runner-extension.md covers nonlinear SAE OPT-125M AuxK core-5 matched runner extension, aux-coefficient validation, stale progress cleanup, launch verification, and reporting. -->
<!-- Support reference: references/nonlinear-sae-corrected-gated-matryoshka-makeup.md covers the OPT-125M corrected makeup sweep where gated uses dual ResNet gate/value paths and matryoshka uses per-level ResNet encoders, including 40+40 run cardinality, AuxK caveat, verification, and launch shape. -->
<!-- Support reference: references/nonlinear-sae-reboot-gpu-continuation-and-tied-gated-launch.md covers reboot-time CUDA verification, stale progress repair, explicit physical-GPU binding, avoiding recently flaky GPUs on request, and TDD/config validation before launching the no-Aux tied/shared ResNet-gated 40-run makeup runner. -->
<!-- Support reference: references/nonlinear-sae-pure-nonlinear-no-skip-launch.md covers the next-stage nonlinear SAE pure nonlinear/no-skip OPT+GPT runner launch pattern, corrected pure architecture set, light validation, fit sanity vs ResNet, and two-idle-GPU launch verification while avoiding flaky GPU2. -->
<!-- Support reference: references/nonlinear-sae-param-matched-wider-linear-fixedk.md covers the post-pure-nonlinear wider-linear capacity baseline. Verify 100/100 OPT+GPT pure completion, narrow to 60/model fixed-k TopK+BatchTopK+Matryoshka, use trainable-parameter-matched widths, validate configs, launch on two good GPUs while avoiding CUDA2, and update todo/log provenance. -->
<!-- Support reference: references/nonlinear-sae-pythia-third-lm-fixedk-launch.md covers extending the OPT/GPT fixed-k TopK-family ResNet-vs-linear comparison to Pythia-160M. Add the Pythia model config, validate 60 regular-linear plus 60 ResNet rows, launch on two confirmed-good GPUs while avoiding CUDA2, verify live PIDs/GPU mapping/progress/logs, and update todo.md with output roots. -->
<!-- Support reference: references/background-process-partial-completion-continuation.md covers verifying Hermes background completion notifications against durable logs/artifacts, identifying partial config/seed completion, and relaunching with checkpoint-skipping continuation plus eval-only aggregation. -->
<!-- Support reference: references/resumable-explanation-validation-pipelines.md covers long explanation/validation pipelines with JSONL resume, GPU fault recovery, malformed generated-record repair, validation reruns, and final manifest verification. -->
<!-- Support reference: references/branch-specialization-local-source-and-phase8c-red-handoff.md covers local-source-of-truth continuation after an old Discord thread, reconstructing exact failed-attempt stop points, and the Phase 8C RED scaffold before expensive GPU runs. -->
<!-- Support reference: references/branch-specialization-phase8c-contrastive-helper-scaffold.md covers approved cheap continuation from the Phase 8C RED scaffold, including the import-cheap contrastive helper, Phase 8C/8B/v0 test triad, durable note updates, and stopping before a full model atlas run. -->
<!-- Support reference: references/branch-specialization-phase8c-contrastive-smoke-calibration.md covers one-role Phase 8C smoke calibration, the positive self-effect selection gate, source-effect preservation criteria, GPU/log/artifact handling, and stop-before-full-atlas interpretation. -->
<!-- Support reference: references/branch-specialization-phase8e-core-transfer-launch.md covers Phase 8E/8F core-only architecture-transfer launch after a promotion manifest, including registry validation, CUDA smoke, one-idle-GPU tracked launch, verification, and completion synthesis guardrails. -->
<!-- Support reference: references/branch-specialization-real-language-lm-sweeps.md covers branch-specialization real-language LM sweeps, single-GPU `/data` storage, launch verification, and interpretation boundaries. -->
<!-- Support reference: references/tokenizer-free-fixed-eval-multiseed-launch.md covers tokenizer-free continuation after Round1, including fixed large checkpoint eval before conclusions, narrow multi-seed Round2 generation, one-GPU launch verification, `/data` artifacts, and durable TODO updates. -->
<!-- Support reference: references/tokenizer-free-calibrated-round3-launch.md covers tokenizer-free continuation after calibrated Round2 diagnostics with hard seen-component negatives, split binding-vs-digit-extrapolation, configurable train/best-checkpoint splits, baseline-vs-wide-local Round3 config/runner, one-GPU launch verification, and stop conditions. -->
<!-- Support reference: references/quick-readonly-run-recheck.md covers terse Discord check-again follow-ups with project resolution, lightweight anchors, GPU/process state, durable progress/log/metric inspection, optional short wait for near-finished runs, and concise delta reporting. -->
<!-- Support reference: references/value-action-dense-basis-controls.md covers Value Action raw/PCA signed-pole dense-basis controls against SAE features, matched Q1/Q2/Q5 screens, explanation validation, dense causal-intervention caveats, and final decision-deciding comparison framing. -->
<!-- Support reference: references/value-action-raw-pca-dense-control-continuation.md covers post-Q1/Q2/Q5 raw/PCA continuation with dense-unit evidence packets, artifact-aware explanations, held-out validation, empirical rank-1 decoder fitting, chained background continuation, and matched Q3/Q4 guardrails. -->
<!-- Support reference: references/value-action-raw-pca-validation-decoder-recovery.md covers the continuation state where raw/PCA explanations + validation completed but empirical decoder fitting failed on a `unit_id` vs `unit_or_feature` schema mismatch; verify durable validation artifacts, patch the loader, rerun decoder fitting only, then proceed to Q3/Q4. -->
<!-- Support reference: references/value-action-phase1-3-pptx-gated-continuation.md covers bounded Value Action phase completion where Gavin wants PPTX reports for heavy substeps, including Task2 top-feature audit, A/B/C reversed robustness, gated Task1 pilots, feature-union planning, todo_history snapshots, and bounded cron continuation. -->
<!-- Support reference: references/value-action-phase1-4-q125-steering-union.md covers Value Action Phase 1.4 continuation after Phase 1.3, including verifying Task1/Task2 Q1/Q2/Q5 branch coverage, filling missing Task2 reversed-order Q125 with semantic Option1/Option2 orientation, building the full branch feature union, identifying V2 interpretation deltas, and separating steering results from option-position confounds. -->
<!-- Support reference: references/value-action-phase2-task1-task2-overlap-plan.md covers Value Action Phase 2 planning after Phase 1.6, including Task1↔Task2 condition-aware overlap, descriptive-first taxonomy, source artifacts, metrics, candidate queues, and steering gates. -->
<!-- Support reference: references/value-action-public-basis-preservation-search.md covers the RQ0-style search for more Keishii-like LLM + SAE/transcoder/crosscoder pairs, including sparse/raw preservation thresholds, /data cache policy, candidate reporting columns, and the awk numeric GPU-idle selection pitfall. -->
<!-- Support reference: references/value-action-phase2-exploratory-candidate-mining.md covers the Phase 2B-style exploratory mining pass after Phase 2A with class-balanced candidate manifests, concrete activation examples, sparse bridge/gap taxonomy framing, and the 20-row Phase 2C big-run gate. -->
<!-- Support reference: references/value-action-strict-s34-branch-matched-steering.md covers strict reruns of Value Action S3/S4/S3∩S4 gap-feature steering after display-order/provenance concerns, including canonical source-table manifests, branch-matched normal/reversed q-roots, semantic-vs-display margin reporting, and per-category/per-value/per-S-bin summaries. -->
<!-- Support reference: references/value-action-action-token-steering-continuation.md covers follow-up action-token/action-span steering runs after strict S3/S4 pre-answer steering, including preserving S-bin provenance, remapping Task2 targets to option1/option2 patch sites, smoke testing, and reporting the distinction between source bin, patch site, and answer-token readout. -->
<!-- Support reference: references/value-action-category-specific-s34-candidate-steering.md covers broad robust candidate finding plus compact category-specific steering for Value Action categories 1/2/7/8/9/10, including Cat1/2 no-gap bridge controls, Cat7/9 value-side requirements, Cat8/10 action-side requirements, filter-step accounting, and semantic-vs-display reporting. -->
<!-- Support reference: references/value-action-dataset-scaffold-and-web-preview.md covers autonomous prompt-dataset creation for Value Action, deterministic component/skeleton generators, minimal site metadata, final-cue/pre-answer token definitions, same-format baselines, HTML right-panel web-log previews with catalog/TOC, and optional Keishii activation collection after dataset verification. -->
<!-- Support reference: references/value-action-freegen-prompt-qa-fix.md covers forced-choice answer-format QA when free generation must start with A/B or 1/2, including strict one-ending templates, chat-template wrapping, max_new_tokens=1, non-value baseline rewrites, stratified smoke QA, and activation span-offset pitfalls. -->
<!-- Support reference: references/value-action-pre-answer-generation-sites.md covers decoder-only pre-answer/logits-site semantics for forced-choice answer-marker activations, including why future tokens have no hidden state, why chat-template `pre_answer` may be the assistant tail token, and why `answer_marker_actual` is post-answer diagnostic. -->
<!-- Support reference: references/value-action-public-basis-preservation-search.md covers the RQ0/Phase 1.1-style public SAE/transcoder/crosscoder pair search for more Keishii-like LLM+basis pairs, including preservation thresholds, raw/matched-N baselines, /data cache policy, Hugging Face candidate inventory, and tracked wait-for-idle-GPU launch pattern. -->
<!-- Support reference: references/value-action-public-basis-relaxed-gemmascope-l12-20260626.md covers Gavin's relaxed public-basis exploration bar (sparse acc/F1 >=0.60 and preservation >=80%), benchmark-vs-new-candidate reporting, near-miss percentage tables, same-family GemmaScope L12 L0 sweeps, 30-row screen target, representative-pass promotion strategy, and blocked-vs-scientific-fail labels. -->
<!-- Support reference: references/cron-artifact-only-continuation-when-launch-blocked.md covers scheduled/cron continuations where GPU launch prerequisites cannot be completed; verify durable artifacts only, update notes only for new information, and use `[SILENT]` for no-change rechecks when allowed. -->
<!-- Support reference: references/value-action-fullpos-everactive-v2-interpretability.md covers Value Action full-positive ever-active V2/V2.1 interpretability runs with all nonzero pre_answer features, WikiText and moral-domain axis separation, dual-source packets, one-GPU launch verification, and overnight ETA reporting. -->
<!-- Support reference: references/value-action-consval-row-steering-slope-reports.md covers Phase 3.1 ConsVal row-level steering/effect experiments, top-15-style alpha grids, six task/order groups, order-robust/order-direction candidate manifests, smoke tests, sharded GPU launches, morning report cron jobs, and presentation-quality interactive HTML reports. -->
author: Gavin / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [research, autonomous, mechanistic-interpretability, experiments, long-running, gpu, discord]
    category: research
    related_skills: [research-results-synthesis, gavin-research-presentations, jupyter-live-kernel, codex, kanban-orchestrator, subagent-driven-development]
    requires_toolsets: [file, terminal]
---

# Gavin Autonomous Research

Reference: for long nonlinear-SAE/CUDA training sweeps with reboots, stale `running` rows, or exit-137 resumes, use `references/nonlinear-sae-gpu-runner-resume-pattern.md`. It captures the project-specific safe GPU mapping, progress repair, and resumable-runner launch pattern.

Reference: for the nonlinear SAE pure nonlinear/no-skip OPT+GPT runner stage after the tied-gated makeup runner, use `references/nonlinear-sae-pure-nonlinear-no-skip-launch.md`. It captures the corrected architecture set, fit sanity, light validation, two-idle-GPU launch pattern, and concise reporting shape.

Reference: for the controversial Value Action value-conflict dataset immediately after dataset creation, behavior QA, and Keishii L11 activation collection, use `references/value-action-controversial-dataset-next-analysis.md`. For Phase 3/ConsVal feature tiering and side-specific queues, use `references/value-action-consval-feature-tiering.md`. It captures the post-creation ladder: verify strict F0/F1/F2 QA and activation counts, use `pre_answer` as the primary site, run behavior-only baselines before sparse feature aggregation, build feature-by-value-pair selection tables with control subtraction and stability checks, audit concrete examples before steering, and treat quick top-k prevalence as mechanical triage only; real tiering needs full/expanded support plus own-feature percentile/exceedance scoring. For the full-support Phase 3.1 run itself, use `references/value-action-consval-full-support-tier-run.md`: verify 77,400 rows including controls, safely preempt lower-priority GPU jobs with approval, launch/monitor dense pre_answer collection, and build robust pooled/distribution-qualified/order-format-robust tier slides with nulls, uncertainty, sparse-tie flags, cluster counts, AUC/rank-effect, and explicit_label_lift. For Gavin's correction that percentile-exceedance screens are still frequency-like and should be followed by magnitude/effect-size screens plus aggressive Canvas curation, use `references/value-action-consval-magnitude-aware-tiering-and-canvas-curation.md`.

Reference: for Phase 3.1 ConsVal distribution-first feature classification after B0/B1 artifacts exist, use `references/value-action-consval-feature-taxonomy-atlas.md`. It captures Gavin's requested taxonomy buckets, the rule that high/low should be measured by frequency + magnitude + baseline contrast + stability, the distribution→qualitative audit→quantitative/causal ladder, and the requirement to build a comprehensive QA-rendered PPTX/PDF review deck after each completed step.

Reference: for Value Action full-positive ever-active V2/V2.1 interpretability runs, use `references/value-action-fullpos-everactive-v2-interpretability.md`. It captures the broad explanation-coverage target of all nonzero `pre_answer` dense-pass features, WikiText vs moral-domain axis separation, dual-source packet construction, one-GPU launch verification, and compact overnight-scale ETA reporting.

Reference: for long nonlinear SAE sweeps that fail with a transient HuggingFace `ReadTimeout`, use `references/nonlinear-sae-hf-timeout-resume.md`: verify dict-shaped progress plus final metrics/weights, relaunch only the retryable row via the resumable runner with longer HF timeout env vars, confirm GPU allocation, and update `todo.md` with the new session/log.

Reference: for the nonlinear SAE fixed-k TopK-family DAME passes, use `references/nonlinear-sae-dame-tertile-full-run.md`. It captures the 240-checkpoint scope, original dominance tertiles × top25 design, the targeted V3 High50+Mid25/no-Low robustness rerun, local Mistral memory/GPU policy, no-pipe resume wrappers for `[Errno 32] Broken pipe`, CUDA contention handling, and launch/reporting shape.

Reference: for the nonlinear SAE current-240 FP/FN metric pass, use `references/nonlinear-sae-current240-fpfn-manifest.md`. It captures the matched 240-row/60-per-LLM-family manifest scope, why to use a manifest runner instead of old broad directory FP/FN code, the fixed-target-k Linear Matryoshka adapter requirement, fast linear-decoder FP/FN computation with direct-decode verification, GPU launch pattern, output paths, and BatchTopK low-eval-L0 interpretation caveat.

Reference: for preparing or launching SAEBench evaluation over Gavin's local nonlinear/ResNet SAE checkpoints, use `references/nonlinear-sae-saebench-bridge.md`. It captures the correct SAEBench paper/repo, current-240 manifest, local bridge scripts, branch/import compatibility check, CPU smoke-load verification, recommended initial eval subset, GPU launch pattern, and paired ResNet-vs-linear interpretation rule.

Reference: for current-240 FP/FN evaluation over the nonlinear SAE fixed-k TopK-family manifest, use `references/nonlinear-sae-current240-fpfn.md`. It captures the manifest-based runner pattern, why the old GPT-2-only `run_fp_fn.py` is unsafe for OPT/current-240, fixed-target-k Linear Matryoshka adapter use, fast decoder-effect FP/FN computation with verification, GPU/log/output conventions, and BatchTopK/eval-L0 caveats.

Reference: for the nonlinear SAE parameter-matched wider-linear fixed-k baseline comparison against corresponding ResNet rows, use `references/nonlinear-sae-wider-linear-baseline-comparison.md`. It captures the OPT/GPT artifact path mapping, finished-row-only EV comparison, green/red PNG table deliverable, and file-only logging pitfall for huge tqdm jobs.

Use this skill when Gavin asks for autonomous research work across any local
project: "keep going", "continue this plan", "work while I sleep", "run the
next stage", "advance the project", "do the systematic comparison", "monitor
the runs", or similar.

The purpose is bounded high-access autonomy: continue through routine research
steps without stopping for every small uncertainty, but stop when Gavin's
judgment is needed.

## Autonomy Modes

Choose the smallest mode that fits the request.

- **Status/read-only mode:** inspect project notes, logs, artifacts, GPUs, and
  running jobs; do not edit or launch new runs. For terse follow-ups like
  "check again", use the quick recheck pattern in
  `references/quick-readonly-run-recheck.md`: resolve the project, inspect
  lightweight anchors plus durable progress/log/metric files, optionally wait a
  short bounded interval for near-finished runs, and report concise deltas.
- **Bounded research mode:** run one coherent phase or the next decisive
  experiment/analysis, then report.
- **Sleep/away mode:** if Gavin gives a time window, compute the stop time and
  work until that time, a blocker, or a decision point.
- **Orchestrated mode:** use Hermes kanban/Codex delegation only when there are
  independent lanes, long-running work that should survive restarts, or a review
  loop. Do not create agent fleets for one small task.

If Gavin does not give a time window or explicit phase boundary, default to a
bounded research mode: complete the next useful decision-changing step, update
local notes, and stop with the next recommended action.

## Start Contract

Before running experiments or editing files:

1. Resolve the project from the Discord channel, `/home/<user>/work/HERMES.md`,
   or the explicit path in Gavin's message.
2. Read the project `handbook.md`, `todo.md`, recent-chat/status notes, current
   plan/RQs, and latest result/provenance summaries. If Gavin says not to rely
   on an old Discord thread, treat local files/artifacts as the source of truth
   and do not use chat memory as evidence.
3. Inspect current git status, recent commits, latest logs/results, TODO/handoff
   files, and relevant `/data/<user>/<project>/` artifacts before proposing work.
4. If continuing after a failed or interrupted attempt, reconstruct the exact
   stop point before coding or launching anything expensive: what file/artifact
   is missing, whether an expensive run actually started, whether the failure was
   scientific vs infrastructural vs a RED test scaffold, and what cheap test or
   smoke would validate the next step. For the branch-specialization Phase 8C
   pattern, see
   `references/branch-specialization-local-source-and-phase8c-red-handoff.md`.
5. State internally, and briefly to Gavin when useful:
   - current project and root;
   - current claim or research question;
   - unit of analysis;
   - allowed experiment family;
   - success criterion;
   - stop condition or stop time;
   - artifact/output location.
6. If any of those are materially ambiguous, ask one concise clarification
   instead of guessing.

## GPU And Storage Rules

- Before any CUDA/GPU work, inspect GPU status and existing GPU processes.
- Prefer idle GPUs. Ask before killing, preempting, or changing existing jobs.
- **Default to one GPU for training launches.** If Gavin says to use "an idle CUDA"
  or "any idle CUDA", choose a single idle device and launch one non-sharded job.
  Do not split across multiple GPUs, use sharding, or occupy every idle card
  unless Gavin explicitly asks for multi-GPU/sharded execution.
- When restarting after an interrupted/sharded launch, clear stale `running`
  progress entries only for the interrupted run IDs after verifying the processes
  were killed and checkpoint files do not exist, then relaunch the single-GPU job.
- Keep large checkpoints, datasets, logs, caches, and repeated run outputs under
  `/data/<user>/<project>/`, not `/home`.
- Use `/data/<user>/hermes_exports` for Discord-deliverable PDFs, decks, CSVs,
  reports, and artifacts.
- Never reset, clean, delete, or reorganize research repos unless Gavin
  explicitly asks.

### Launching Bounded Multi-GPU Sweeps

When Gavin approves a prepared sweep or says to finish the remaining runs on
idle CUDA devices:

1. Reconfirm the run cardinality before launching: run the script's dry-run or
   inspect its manifest/progress file and report total, already-complete/linkable,
   and remaining-to-train counts.
2. Recheck `nvidia-smi` immediately before launch. Use only genuinely idle GPUs;
   do not disturb existing hot jobs.
3. Prefer the runner's built-in sharding/resume/progress controls over ad-hoc
   shell loops. Split across idle GPUs with explicit `--num-shards` and
   `--shard-index` when available.
4. Launch long bounded sweeps as Hermes-tracked background processes with
   `notify_on_complete=true`, not shell-disowned jobs. Write each shard to a
   descriptive log under the project `logs/` directory. For very noisy multi-day
   stdout/tqdm/model-output jobs, use a no-pipe wrapper with direct
   `exec >> "$LOG" 2>&1` file redirection rather than a long captured `tee`, so
   a logging pipe failure cannot masquerade as row-level experiment failures.
5. For matched sweep extensions, verify that the new runner exactly preserves
   the intended comparison grid before launching. Instantiate one config per
   architecture and check any special knobs (e.g. AuxK coefficients) because
   shared config helpers may silently default or override architecture-specific
   fields.
6. If resuming a sweep with stale `running` progress entries, clear only the
   verified stale entries: first confirm no matching process is alive, confirm no
   checkpoint files exist for that run, back up `progress.json`, then dry-run the
   runner to ensure the point is trainable again. After a reboot, prefer this
   targeted stale-entry repair over broad progress-file cleanup.
7. When binding a physical GPU to a single-process runner, set
   `CUDA_DEVICE_ORDER=PCI_BUS_ID` and `CUDA_VISIBLE_DEVICES=<physical_gpu>`, then
   pass `--device cuda:0` inside the process because the runner sees only the
   visible device. If Gavin asks to avoid a historically flaky GPU, leave it idle
   even if it is visible after reboot.
8. Verify launch success before reporting: poll the background sessions, inspect
   the first log lines for the expected output root/device/shard, check
   `nvidia-smi` for new Python processes on the intended GPUs, and inspect the
   progress file for linked/done/running entries.
8. If a Hermes background process later reports completion with unknown/null exit
   code or unavailable output history, do not assume the sweep completed. Verify
   durable logs, output rows, checkpoint inventory, and live GPU/process state;
   if only part of a config/seed sweep finished, relaunch with a
   checkpoint-skipping continuation wrapper and run a clean eval-only aggregate
   after all checkpoints exist. See
   `references/background-process-partial-completion-continuation.md`.
9. In scheduled/cron research continuations, if the process session is no longer
   visible and the session cannot complete required launch prerequisites such as
   a fresh GPU/process check, do not launch GPU work. Use artifact-only
   verification and update a durable status note only when the invocation adds
   new information, a fix, or a materially clearer next command. If the check
   only confirms an already-documented blocked/no-change state and the delivery
   contract allows silence, respond exactly `[SILENT]` rather than sending a
   noisy report. When reporting, name the exact blocked next phase without
   treating the missing launch as a scientific result. See
   `references/cron-artifact-only-continuation-when-launch-blocked.md`.
10. In the report, include the process session IDs, log paths, output root,
   current done/running/remaining state, and any caveats such as points that were
   linked from a previous sweep rather than retrained.

## Research Loop

For each autonomous step:

1. Define the specific claim being tested.
2. Prefer honest baselines and the smallest decisive experiment over broad
   unfocused sweeps.
3. For open-ended analysis, inspect concrete examples, traces, plots, rows, or
   logs before broad quantitative aggregation.
4. Read exact local definitions before collapsing labels or metrics.
5. Then compute quantitative checks that support, weaken, or falsify the
   hypothesis.
6. Inspect per-example outputs when behavior metrics are involved.
7. For failed, weak, or mixed results, do a failure-analysis pass before making
   a broad conclusion:
   - list plausible causes or confounds;
   - identify which are testable in scope;
   - run the most targeted control or tweak when compute allows;
   - document whether the interpretation changed.
8. For role-specialization projects whose next analysis depends on knowing
   `role -> head` mappings, apply a causal-control validation gate before using
   roles as scored endpoints. Passing means the mapping is reliable enough for
   the next experiment; failing means the assay/mapping is unreliable, not that
   the function is absent. For the branch-specialization pattern, see
   `references/branch-specialization-validation-gated-hetero-pilot.md`.
9. For branch-specialization hetero-vs-uniform or role-ontology runs, keep the
   claims separated: structural affinity, specialization, and functional
   modularity are different thresholds. Small validated batteries and
   from-scratch actual-LM smoke tests can support affinity/specialization
   without supporting modularity. See
   `references/branch-specialization-claim-hygiene.md`.
10. When moving branch-specialization work from toy/synthetic batteries to
   actual language-model training on real text, use the single-GPU, `/data`
   artifact, launch-verification, and interpretation pattern in
   `references/branch-specialization-real-language-lm-sweeps.md`.
11. When Gavin approves the "true next run" after role validation, prefer a
   role-first validated bundle over another broad ontology sweep: separate core
   scored roles from auxiliary roles, verify probe registry counts, run tests and
   a larger-config smoke check, launch one-GPU hetero-vs-uniform real-language
   training, and report the exact role question. See
   `references/branch-specialization-validated-role-lm-launch.md`.
12. When a branch-specialization role/head cluster has passed validation and the
   next question is whether it behaves like a causal module, run a selected
   bundle vs same-layer random-bundle ablation check before porting endpoints
   into hetero-vs-uniform batteries. Treat strong seed-consistent excess over
   random as core evidence, and keep mixed endpoints auxiliary. See
   `references/branch-specialization-causal-bundle-ablation.md`.
13. For branch-specialization multi-LLM role-atlas outputs, add a specificity
   gate before architecture transfer: selected-vs-random passes identify causal
   footholds, but the autonomous next step should compare selected bundles
   against off-role and matched off-role endpoints, then prefer contrastive
   head selection (`self_effect - matched_offrole_effect`) if specificity is
   weak. Do not launch a hetero-vs-uniform role battery from broad v0 atlas rows
   until this gate is satisfied. See the research-results-synthesis reference
   `references/branch-specialization-phase8b-specificity-matrix.md`.
14. When Gavin approves proceeding from a Phase 8C RED scaffold, keep the next
   step cheap unless he explicitly asks for a full atlas run: implement/import
   testable contrastive-selection helpers, run the Phase 8C/8B/v0 unit-test
   triad, update `todo.md` and provenance, and stop before GPU/model evaluation.
   See `references/branch-specialization-phase8c-contrastive-helper-scaffold.md`.
15. For Value Action public-basis searches, do **not** jump directly into the
   full Keishii S/V/V3/V4/steering pipeline. First run the RQ0-style preservation
   screen to find more Keishii-like LLM + SAE/transcoder/crosscoder pairs: raw
   activation probe, sparse feature probe, matched-N raw MI, matched-N sparse MI,
   acc/macroF1 preservation ratios, L0/active-feature health, and checkpoint
   size. Keep two tiers distinct: the strict/gold Keishii-like bar is roughly
   `>=0.70` sparse acc/macroF1 and `>=80–85%` sparse/raw preservation, while
   Gavin may also ask for relaxed exploration at about `>=0.60` sparse acc/F1
   and `>=80%` preservation. Label the already-used Keishii L11 pair as
   `BENCHMARK`, not as a newly found candidate; count new/other screened rows
   separately. When a candidate is near/relaxed, show the raw score, sparse score,
   and preservation percentage for full acc, full macroF1, matched-N acc, and
   matched-N macroF1. Keep all HF caches, model files, activations, sparse
   features, and probe checkpoints under `/data/<user>/value_action/...`, not
   `/home`. If a model is gated or unauthenticated, classify the attempt as
   `BLOCKED before scientific result` and move to the next feasible public
   candidate when Gavin asked to keep trying. Report candidates in a compact
   aligned text table with LLM name/size, basis repo/type/width, layer site, file
   size, metrics, and decision. See
   `references/value-action-public-basis-preservation-search.md` and
   `references/value-action-public-basis-relaxed-screen-20260626.md`.
16. For Value Action dense-basis sanity controls against SAE features, keep the
   SAE-vs-raw/PCA comparison matched on dataset, hook site, and Q definitions;
   treat raw/PCA coordinates as signed-pole pseudo-features; use Q1/Q2/Q5 only
   as a challenger screen; then require evidence-packet explanation validation
   and Q3/Q4 causal/Shapley support before making the final “decision-deciding”
   comparison. See `references/value-action-dense-basis-controls.md`. When
   continuing the all-56 raw/PCA control after phase-1, verify basis + 112
   item/basis Q outputs from durable artifacts, build the numerical gap report,
   collapse top rows to unique dense challenger units, run resumable
   explanation/validation, fit empirical rank-1 dense decoder vectors, and only
   then proceed to raw/PCA Q3/Q4; see
   `references/value-action-raw-pca-dense-continuation.md`. If the chained
   validation+decoder process fails after validation because the decoder loader
   expects `unit_id` while the challenger CSV uses `unit_or_feature`, treat it as
   a schema-recovery continuation: preserve completed validation artifacts, patch
   the decoder loader to accept the alternate column, and rerun decoder fitting
   only after a fresh one-idle-GPU check; see
   `references/value-action-raw-pca-validation-decoder-recovery.md`. When Gavin
   asks to finish a bounded Value Action phase and wants PPTX reports for heavy
   substeps, split the phase into gated substeps, run Hermes-owned audits and
   robustness jobs autonomously, build reproducible scripts plus PPTX/PDF/contact
   sheet packages for heavy outputs, snapshot `todo.md` under `todo_history/`,
   and stop before Gavin-gated full Q-metric stages; see
   `references/value-action-phase1-3-pptx-gated-continuation.md`.
15a. When Gavin asks to find more SAE/transcoder/crosscoder + LLM pairs like
   Keishii, do **not** jump straight to the full S/V/V3/V4/steering pipeline and
   do not frame it as abandoning Keishii. Treat it as an RQ0/Phase 1.1-style
   public-basis preservation search first: compare raw activation probes,
   sparse-basis probes, matched-N raw MI, and matched-N sparse MI; require about
   `>=0.70` sparse acc/F1 and `>=80–85%` sparse/raw preservation before strict
   promotion; keep Hugging Face caches and large artifacts under `/data`; and
   if GPUs are busy, use a tracked wait-for-one-idle-GPU launch rather than
   preempting jobs. If Gavin relaxes the search bar, preserve both labels:
   `BENCHMARK` for the existing Keishii pair, `STRICT`/`STRICT_DENSE` for new
   numeric strict passes, `RELAXED` for candidates meeting the relaxed bar (e.g.
   `>=0.60` sparse acc/F1 plus `>=80%` preservation), `FAIL` for completed
   scientific failures, and `BLOCKED` for access/infra blocks. Do not count the
   existing Keishii pair as a new discovery. Around 30 RQ0 screen rows/settings
   is a good first systematic target; after that, stop broad expansion and run
   deeper experiments only on representative passes rather than every same-family
   L0 checkpoint. For GemmaScope-style high-L0 numeric passes, keep the
   `STRICT_DENSE` caveat and frame them as dense public preservation baselines
   unless feature explanations validate well. See
   `references/value-action-public-basis-preservation-search.md` and
   `references/value-action-public-basis-relaxed-gemmascope-l12-20260626.md`. 
16. For Value Action category-specific S3/S4/S3∩S4 steering, do not use one global eligibility rule. If Gavin asks for categories `1/2/7/8/9/10`, first run or inspect a broad robust candidate census, then build a compact manifest with category-specific requirements and explicit steering targets: Cat1/Cat2 bridge controls need both-task target-positive evidence but no gap requirement; Cat7/Cat9 count value-side Task1 S3, S4, and S3∩S4 evidence separately; Cat8/Cat10 count action-side Task2 both-order semantic S3, S4, and S3∩S4 evidence separately. Treat S3∩S4 as stronger evidence, not a hard requirement. Never let the natural gap-side label silently become the steering target: Cat7 should test Task2 Option1 rescue, Cat9 Task2 Option2 brake/rescue, Cat8 action Option2 plus Task1 Reject counterpart, and Cat10 action Option1 plus Task1 Endorse counterpart. Report filter-step counts and final steering results separately by category, value, and S-bin, with Task2 semantic-vs-display and normal-vs-reversed margins separated. See `references/value-action-category-specific-s34-candidate-steering.md`.
17. For autonomous Value Action prompt-dataset creation, use the dataset-scaffold pattern in `references/value-action-dataset-scaffold-and-web-preview.md`: deterministic component/skeleton generation is acceptable when the schema is regular; save the reproducible builder under `/home/<user>/value_action/scripts/`; save large dataset artifacts under `/data/<user>/value_action/...`; verify counts/manifests before launching optional activation collection; and render Discord right-panel plan/report previews as HTML with a visible catalog/TOC, not raw Markdown. If forced-choice answer markers must work under free generation, do not assume `Reply with only A/B` is enough. Run answer-format QA, wrap Llama instruct prompts with the chat template, use `max_new_tokens=1`, rewrite abstract same-format non-value baselines as concrete tradeoff choices, and fix activation span offsets after chat-template wrapping. If Gavin asks to preserve old F0/F1/F2 answer-site variants, run a strict-F0/F1/F2 rescue test rather than silently collapsing to an F3-only ending. For downstream decoder-only activation analysis, explicitly distinguish the primary pre-answer logits site from post-answer marker-visible diagnostics: with chat templates the `pre_answer` position is the last model-input generation-prompt token, not necessarily the raw prompt's final cue token, while `answer_marker_actual` sees the generated marker. See `references/value-action-freegen-prompt-qa-fix.md`.
18. Update durable local artifacts immediately after meaningful results:
   `todo.md`, result summaries, provenance logs, manifests, scripts, or deck
   READMEs as appropriate.
16. For tokenizer-free/apperception follow-ups after calibrated diagnostics, do not broaden architecture variants by default. If Gavin approves continuing after Round2 calibration exposed yes-bias or answer-range confounds, run one narrow cleaned Round3: baseline vs `slot_wide_local_heads`, train on `hard_bind`, eval `hard_bind hard_calibrated digit_extrap iid long rename hard`, use configurable `train_split` and `best_checkpoint_split`, verify tests/config cardinality, then launch one GPU and stop after launch verification. See `references/tokenizer-free-calibrated-round3-launch.md`.
16. For long explanation/validation pipelines, rely on resumable JSONL and
   durable artifact checks rather than background-process exit alone. Verify
   expected feature/item counts, malformed generated rows, validation summary
   rows, and final manifest gates before reporting completion. If generated
   explanation rows are malformed, repair only the affected feature IDs and
   rerun their validation judgments instead of restarting the whole pipeline.
   When the feature-selection source can produce empty/too-small sets (e.g.
   dominance tertiles over very sparse SAE features), handle it as data coverage:
   skip zero-active rows with an explicit summary, run partial rows only over
   active features, and mark them as caveated/non-comparable rather than letting
   one row crash a multi-day job. See `references/resumable-explanation-validation-pipelines.md`.
17. If Gavin requested slides/deck/PDF as part of the autonomous phase, complete
   the presentation package before reporting the stop point: render and QA the
   deck, copy Discord-deliverable artifacts under `/data/<user>/hermes_exports`,
   and update presentation indexes/READMEs. For Value Action metric/checkpoint
   decks, do not only dump category tables: include plain-language definitions
   for every shorthand metric, explicitly report both-task/both-order counts,
   and give brief feature×value×direction interpretations plus caveats so Gavin
   can tell why a selected feature matters.
18. If Gavin asks to run the Value Action "action token thing" after strict
   S3/S4 steering, treat it as an action-span patch continuation unless he says
   otherwise: preserve the original pre-answer S3/S4/S3∩S4 selection provenance,
   remap the Task2 semantic target to `option1`/`option2` as the patch site,
    keep the outcome as the answer-token semantic margin, smoke-test one target,
    then launch the full branch-matched normal/reversed dose run. See
    `references/value-action-action-token-steering-continuation.md`.
 17. For Phase 3.1 ConsVal row-level steering/slope reports, update the visible deck/HTML artifact before replying, show pooled/order-direction/order-robust views together when robustness is in question, and build interactive HTML reports with pooled plus per-task/order slopes, flip rates, tiers, value-pair metadata, and V2.1 interpretation coverage. See `references/value-action-consval-steering-reporting.md`. 
16. Continue to the next decisive step unless a stop condition is reached.

## Stop Conditions

Stop autonomous work and report when any of these occur. If Gavin explicitly says
“go until the stop phase” or similar, interpret that as permission to complete
the approved bounded phase, not permission for indefinite scope expansion. See
`references/stop-phase-with-presentation-checkpoint.md` for the pattern where a
positive result plus requested deck/report packaging completes the phase and the
next broader role/method family requires approval.

Stop autonomous work and report when any of these occur:

- The requested time window expires.
- Gavin input is needed to choose between materially different research
  directions.
- The next plausible step changes the unit of analysis, architecture family,
  method family, or main claim from what Gavin approved.
- A result changes the project thesis enough that continuing could waste
  substantial compute.
- The branch looks low-potential enough that abandonment, narrowing, or major
  reframing should be considered.
- The current phase/RQ is complete enough that the next phase needs approval.
- A genuinely interesting insight, contradiction, or decision-changing result is
  found and should be surfaced.
- Infrastructure failure, missing credentials, storage limits, broken
  dependencies, or GPU contention blocks the next meaningful step.
- A requested operation would be destructive, irreversible, or affect another
  running project.

Routine intermediate findings, normal uncertainty, successful run completions,
and small implementation choices are not stop conditions by themselves.

## Quality Bar

Treat Gavin's research branches as potential paper projects. Be willing to
recommend abandoning, narrowing, or reframing a branch when evidence is weak.
Watch for:

- no clean behavior after reasonable setup fixes;
- interpretability methods failing against simple baselines;
- results likely caused by engineering artifacts;
- missing novelty after local baselines and related-work checks;
- aggregate metrics unsupported by concrete examples.

Separate exploratory observations from quantified claims.

## Related Skills

- Use `research-results-synthesis` to interpret results, reconstruct
  definitions/sign conventions, compute counts, and explain artifacts.
- Use `gavin-research-presentations` at major checkpoints, abandonment/reframe
  points, or when Gavin asks for a PDF/deck. Do not make decks for routine
  progress.
- Use `jupyter-live-kernel` for notebook-centered analysis when a live notebook
  already exists or notebook state matters.
- Use `codex`, `subagent-driven-development`, or `kanban-orchestrator` only for
  independent coding/research lanes, review loops, or long-running workflows
  that should persist beyond one chat thread.

## Reporting

For long-running resumable experiment runners, see `references/long-running-runner-file-logging-resume.md`: prefer durable file-only logs for noisy multi-hour jobs, verify ambiguous `exit code None` notifications against `progress.json`/artifacts/GPU state, and resume rather than treating a detached stdout/broken-pipe event as scientific failure.

Keep Discord updates concise and action-oriented:

- current phase/RQ;
- what changed;
- whether the result strengthens, weakens, or reframes the project;
- artifact paths;
- next decisive action.

Avoid Markdown pipe tables in Discord. Use compact bullets or fenced `text`
tables with aligned columns.

At the end of an autonomous run, report:

- what was done;
- what passed/failed;
- where artifacts live;
- what was updated in `todo.md` or provenance;
- the next recommended action;
- whether Gavin approval is needed.
