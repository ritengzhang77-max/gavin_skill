# Push Later

This local directory is already a git repo. Do **not** push until the privacy review is complete.

## When Gavin gives a GitHub repo URL

```bash
cd /home/<user>/work/gavin-hermes-workflow-skills
git remote add origin <GITHUB_REPO_URL>
git push -u origin main
```

If `origin` already exists:

```bash
git remote set-url origin <GITHUB_REPO_URL>
git push -u origin main
```

If the remote repo is non-empty, clone it separately and copy this content in, or pull/rebase carefully before pushing.

## Recommended repo names

- `gavin-hermes-workflow-skills`
- `gavin-skills`
- `research-agent-workflows`
- `hermes-research-workflows`

## Suggested GitHub description

> Public-safe Hermes Agent skills and examples showing a Discord-first research workflow: presentations, paper planning, Thread Canvas artifacts, and project operating rules.
