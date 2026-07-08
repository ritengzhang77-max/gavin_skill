# Workflow Architecture

This repo describes a Hermes-centered research workflow, not just a set of prompts.

## Core loop

1. **Discord thread = task context**
   - Human asks for work in a project or experiment thread.
   - Hermes routes the request to the right local project root and skill.

2. **Local files = durable state**
   - `handbook.md` records stable project context.
   - `todo.md` records Now / Next / Later / Blocked / Done.

3. **Skills = reusable operating policy**
   - Skills encode trigger conditions, constraints, taste, verification, and stopping rules.
   - They prevent repeated steering like “make the deck readable,” “update TODO,” or “don’t launch GPUs without checking status.”

4. **Artifacts = public-facing outputs**
   - Decks, PDFs, HTML dashboards, and Thread Canvas pages are treated as deliverables, not hidden logs.
   - Rendered QA matters: no overflow, no unreadable tables, no link-only answers when chat text is required.

5. **Scope has boundaries**
   - Hermes should not work indefinitely or mutate project structure without explicit direction.

## Why skills rather than raw prompts?

Raw prompts are ephemeral. Skills persist the workflow as a reusable contract:

- when to use the workflow;
- how to gather context;
- which artifacts to create;
- how to verify quality;
- when to stop;
- what should be logged for the next session.

## Showcase goal

This repository is meant to make the thought process visible: the operating principles, quality gates, and examples behind Gavin's research-agent workflow.
