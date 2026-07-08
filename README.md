# Gavin Hermes Workflow Skills

A public-facing package of Gavin's Hermes Agent workflows: research presentation generation, paper planning, autonomous research handoffs, Thread Canvas / Discord artifact practice, and project-oriented agent operating patterns.

This repository is staged locally first. It is intended to be pushed to a GitHub repository later after a final privacy review. Supporting per-project reference files from the live skills have been omitted from the public tree and archived separately for private review.

## What this is

This is not a full dump of `~/.hermes` and not a backup of private projects. It is a curated workflow showcase:

- **Skills**: reusable Hermes `SKILL.md` workflows that encode how Gavin runs research, creates decks, plans papers, translates documents, troubleshoots Hermes/Discord, and manages long-running jobs.
- **Examples/templates**: public-safe placeholders for showing how a workflow is invoked and what artifacts it produces.
- **Code-comparison notes**: space for comparing naive scripts/prompts vs the workflow-enhanced version.
- **Privacy review docs**: explicit checklist before pushing public.

## Core skill groups

### Research and writing

- `skills/research/gavin-research-presentations/` — Gavin-style research deck generation and rendered QA.
- `skills/research/paper-drafting-plan/` — paper-planning and result-to-section mapping.
- `skills/research/gavin-autonomous-research/` — autonomous local research phases, handoffs, TODO updates.
- `skills/research/research-results-synthesis/` — explain and validate computational research artifacts.
- `skills/research/paper-translation-web-reader/` — side-by-side paper/PDF reading and memorable translation workflow.

### Productivity / artifacts

- `skills/productivity/powerpoint/` — PPTX creation/editing workflow.
- `skills/productivity/felix-translation/` — bilingual historical-document translation deliverable workflow.
- `skills/productivity/teams-meeting-pipeline/` — Teams meeting summary pipeline operations.

### Hermes / Discord / infrastructure

- `skills/software-development/hermes-gateway-troubleshooting/` — stuck/silent Discord gateway debugging.
- `skills/software-development/debugging-hermes-tui-commands/` — TUI/slash command debugging.
- `skills/software-development/hermes-s6-container-supervision/` — container service supervision.
- `skills/devops/remote-hpc-slurm/` — remote Slurm/HPC cluster control from Hermes.
- `skills/devops/webhook-subscriptions/` — event-driven Hermes runs.

## Intended public story

The repo should show three layers of Gavin's workflow:

1. **Operating system for research** — Discord/Hermes as a project control plane, local project roots, durable TODOs/handoffs, and Thread Canvas artifacts.
2. **Skill-encoded taste** — specific preferences for deck readability, evidence hygiene, formulas, artifact QA, and when to stop vs continue autonomously.
3. **Reproducible examples** — sanitized examples showing prompts, expected files, checks, and before/after comparisons.

## Important privacy note

This staging repo may still contain local paths, project names, or workflow-specific context. It should not be pushed publicly until `docs/PRIVACY_REVIEW.md` is complete.

## Later GitHub push

When Gavin gives the target repository URL:

```bash
cd /home/<user>/work/gavin-hermes-workflow-skills
git remote add origin <GITHUB_REPO_URL>
git branch -M main
git push -u origin main
```

If the repo already has history, clone it separately and copy this staged content in, or add the remote and pull/rebase first.
