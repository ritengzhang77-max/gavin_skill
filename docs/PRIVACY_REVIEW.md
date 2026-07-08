# Privacy Review Before Public Push

Status: **not yet public-approved**.

This repo intentionally excludes private runtime state (`.env`, config, logs, memories, sessions), but copied skills can still include local paths, names, project-specific examples, or internal workflow details.

## Must check before pushing

- [ ] No API keys, OAuth tokens, cookies, passwords, or private SSH keys.
- [ ] No unpublished paper text/results that should stay private.
- [ ] No private Discord logs or raw session transcripts.
- [ ] No student/collaborator email addresses unless intentionally public.
- [ ] No private local paths that reveal more than intended.
- [ ] No data files, checkpoints, exported decks, PDFs, screenshots, or logs accidentally copied.
- [ ] Skills with project-specific examples are either public-safe or replaced with synthetic examples.
- [ ] License is acceptable for sharing these workflow documents.

## Automated scan performed

Run:

```bash
python scripts/privacy_scan.py
```

The scan is only a guardrail; manual review is still required.
