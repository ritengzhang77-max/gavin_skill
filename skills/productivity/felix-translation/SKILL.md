---
name: felix-translation
description: "Use when Gavin/Felix asks to translate uploaded historical PDFs/documents in the same style as prior translation zip deliverables: Hermes-authored translation, no external MT, bilingual files, standalone HTML reader, verification metadata, and Discord-ready zip."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [translation, pdf, historical-documents, bilingual-reader, discord-delivery]
    related_skills: [ocr-and-documents]
---

# Felix Translation Deliverable

## Overview

This workflow captures Gavin/Felix's preferred document-translation output from the prior translation threads. The goal is a self-contained zip containing source extraction, a Hermes-authored English translation, a standalone browser reader, and verification metadata. Do not hand back only a summary or ask what to do when Gavin says to do the same thing as the previous translation documents.

## When to Use

Use this skill when the user asks for:

- "same thing as the previous document(s)" for an uploaded PDF/document translation.
- a translation zip, downloadable translation package, bilingual reader, or page-by-page translation.
- translation done by Hermes / "by u", not by another model/service.
- historical OCR PDFs where source language may be Czech, Romanian, German, etc.

Do not use it for casual one-paragraph translation snippets unless the user asks for the full zip deliverable.

## Operating Contract

1. Read prior session history if the user references it. Use `session_search` for terms like `translation zip`, `manual translation`, the old filename, or `Felix`.
2. Use `ocr-and-documents` extraction guidance.
3. Translate directly from the source text/OCR in the current Hermes session. Do **not** use external machine-translation services or old English translations as source.
4. It is acceptable to use Hermes subagents for throughput, but metadata must truthfully say if parallel Hermes workers/subagents were used. Do not claim `delegated_to_other_agent: false` if delegate workers were used.
5. Preserve page boundaries. Prefer headings like `## PDF page N` or printed page labels when reliable.
6. Include the source OCR/text next to the English translation so the deliverable is auditable.
7. Add brief notes only for OCR uncertainty, ambiguous names/places, or translation uncertainty. Do not summarize instead of translating.
8. Make the HTML reader standalone: prefer pre-rendered static HTML when practical, or otherwise embed the JSON/data directly. Opening from a local extracted zip must not require JavaScript, `fetch()`, or a local web server. If JavaScript is used, validate the generated script syntax because escaped newlines in regex/string literals can make the page render blank.
9. Put deliverables under `/data/<user>/hermes_exports/<document_slug>/` and create a zip under `/data/<user>/hermes_exports/`.
10. For the dedicated Felix Translation lane, mirror completed zips and skill snapshots into `/home/<user>/work/Felix translation` and keep its `handbook.md`, `todo.md`, and `CHANNEL_WIRING.md` current. See `references/channel-workspace-wiring.md` for the workspace/router setup.

## Preferred Zip Contents

For a PDF named `<slug>.pdf`, create a folder `/data/<user>/hermes_exports/<slug>/` with:

- `<slug>.pdf` or a copy of the source PDF when size is reasonable.
- `source_pdftotext.txt` or equivalent raw extraction.
- `source_pages.json` with page number, source text, language if detected/known, and extraction notes.
- `chunks_source/` and `chunks_translated/` if the document is long enough to split.
- `<slug>_manual_translation.md` as combined bilingual Markdown.
- `<slug>_manual_translation_reader.html` as standalone local HTML reader.
- `translation_progress.json` with status, page counts, missing/duplicate pages, policy metadata, and generated outputs.
- `README_TRANSLATION.md` explaining files, source, method, verification, and caveats.

Zip as `/data/<user>/hermes_exports/<slug>_manual_translation.zip` unless the user requested another name.

For scanned ILL PDFs with large rendered images, prefer a Discord-friendly **lite** zip for attachment (source PDF, OCR/text, JSON, translations, README, standalone HTML, metadata) and optionally keep a larger full-image zip in `/data/<user>/hermes_exports`. See `references/ill-scanned-pdf-translation-packaging.md`.

For large local PDFs staged on the server (for example under `/data/<user>/hermes_exports/felix_incoming/`), use the incoming-folder/date-batch and lite-zip conventions in `references/large-local-pdf-batch-packaging.md`. When originals are ~100MB+, do not embed them in the Discord zip; include `source_pdf_path.txt` plus metadata recording the original server path and size.

## Extraction Workflow

1. Inspect the PDF:
   - page count, metadata, file size.
   - whether text layer exists (`pdftotext`, PyMuPDF). If text is absent/garbled, use OCR workflow from `ocr-and-documents`.
   - for ILL/order PDFs, verify the article pages specifically: the text layer may only cover copyright/order sheets while the real article pages are scanned images.
2. Before doing expensive OCR/translation, check the Felix workspace/archive for an existing matching deliverable (`artifacts/TRANSLATION_ZIP_INDEX.json`, `artifacts/zips/`, and `/data/<user>/hermes_exports/*translation*.zip`). If a zip already exists, validate it (`unzip -t`, inspect metadata) and deliver it rather than regenerating.
3. For server-staged files in `/data/<user>/hermes_exports/felix_incoming/`, first group root-level PDFs into a date/batch folder, confirm upload stability by checking size/mtime over a short window, and report sizes in MB.
4. For text-layer PDFs, extracting each page separately with `pdftotext -layout -f N -l N` is a robust way to preserve exact page boundaries. Keep raw text before cleanup.
5. If the PDF is a journal/article scan with front-matter notices, represent those notice pages explicitly in the output and metadata instead of silently dropping them; translate only the source-language article pages.
6. If the PDF is long enough to split, divide source into disjoint page chunks and translate chunks. For urgent jobs, parallelize only into separate chunk outputs and merge centrally.
7. When using chunk workers/subagents, require a stable chunk structure (`## PDF page N`, `### Source`, `### English translation`, `### Notes`) so the central merge can parse and verify coverage.
8. Keep empty/blank pages explicitly marked instead of silently dropping them.

Additional ILL scanned-PDF packaging notes live in `references/ill-scanned-pdf-translation-packaging.md`.
7. For the text-layer journal-article pattern, see `references/text-layer-article-translation-packaging.md`.

## Translation Style

- English translation should be faithful and complete, not a summary.
- Keep names, dates, military units, places, titles, and archival terms as accurately as possible.
- Preserve lists/tables where practical using simple Markdown.
- For old orthography or OCR noise, translate the most plausible reading and add a short note when uncertain.
- Avoid modernizing content beyond what is needed for clear English.

## Verification Checklist

Before delivering:

- [ ] Every PDF/source page is represented or explicitly marked blank, notice, or untranslatable.
- [ ] No duplicate page sections.
- [ ] Each nonblank source-language page has a nonempty English translation.
- [ ] Already-English front matter/notices are retained and labeled rather than mixed into the source-language translation count.
- [ ] Combined Markdown and HTML reader exist.
- [ ] HTML reader is standalone and does not depend on `fetch()` for local files.
- [ ] `translation_progress.json` accurately states whether external MT, prior translations, or Hermes subagents were used.
- [ ] If parallel chunk workers were used, centrally verify chunk outputs rather than trusting self-report: parse page headings, check expected page ranges, check empty translations, and confirm source pages were not lost.
- [ ] Zip opens and contains the expected files (`unzip -t`).
- [ ] SHA256 and zip size are computed.
- [ ] Completed zips are mirrored into `/home/<user>/work/Felix translation/artifacts/zips/` and `TRANSLATION_ZIP_INDEX.json` is updated when operating in the Felix workspace.
- [ ] Discord final response attaches the zip with `MEDIA:/absolute/path.zip`.

## Common Pitfalls

1. **Asking what to do with the PDF despite prior-thread context.** If the user says "same as previous translation documents," immediately search session history and proceed.
2. **Reader depends on fragile browser JavaScript.** Even without `fetch()`, generated JS can fail silently (for example escaped newlines turning into literal newlines inside regex/string literals), leaving a blank page. Prefer pre-rendered static HTML; if JS is necessary, run a syntax/render sanity check and ensure page/nav content exists before zipping.
3. **Mislabeling delegation.** Subagents are still Hermes, but metadata should truthfully note `parallel_hermes_workers_used: true` when used.
4. **Only summarizing.** The requested artifact is a translation package, not a summary.
5. **Dropping OCR/page uncertainties.** Preserve uncertainty notes briefly so the user can audit noisy historical text.
