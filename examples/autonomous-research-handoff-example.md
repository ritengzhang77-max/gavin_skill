# Example: Autonomous Research Handoff

Synthetic prompt:

> Continue the project until the next meaningful decision point. Run what is safe to run, summarize results, and stop with the recommended next action.

Expected stopping rule:

Hermes should stop when it has a decision-changing result, a failed prerequisite, a resource conflict, or a need for Gavin's judgment. It should not run indefinitely.

Handoff should include:

- What was done.
- Commands/jobs launched.
- Key outputs and paths.
- Verification performed.
- Open issues.
- Next recommended action.
- TODO updates.
