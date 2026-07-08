---
name: paper-translation-web-reader
description: Use when Gavin asks for a “perfect” or memorable translation version of a paper, especially for Discord reading-group discussion, with the original PDF on one side and a polished translated reading version on the other in a hosted web page. Also covers two-sided paper discussion readers with autosaved underline annotations and a real PPTX/PDF deck; see references/discussion-reader-highlight-deck-qa.md and references/pdf-annotation-underlines-and-discussion-deck-qa.md.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [paper-translation, reading-group, pdf, bilingual-reader, web-artifact, discord]
    related_skills: [ocr-and-documents, arxiv, claude-design]
---

# Paper Translation Web Reader

## Overview

This skill captures Gavin's preferred workflow for turning an academic paper into a polished bilingual reading artifact for Discord reading-group discussion.

The target output is not just a raw machine translation. It is a reader-friendly package:

- original PDF visible on one side;
- polished Chinese translation / reading version on the other;
- hosted static web page suitable for sharing in Discord;
- downloadable Markdown translation;
- notes about tables/figures/OCR limitations where exact visual details should be checked against the PDF.

The quality bar is: good enough for Gavin to discuss the paper naturally, with terminology preserved and key claims/metrics translated carefully.

## When to Use

Use this when Gavin asks for:

- a translated version of a paper;
- “perfect translation” / “perfect trnaaltion” / “memorable paper translation”;
- a side-by-side PDF + translation reading page;
- a Discord-shareable web page for paper discussion;
- a reading-group artifact where source PDF and translated explanation should remain aligned.

Do not use this for:

- quick paper summaries only — use normal paper-reading workflow;
- historical scanned document translation zips — use `felix-translation` / OCR document workflows;
- formal publication-quality certified translation — this workflow is a high-quality reading translation, not legal/certified translation.

## Default Assumptions

Unless Gavin specifies otherwise:

- Target language is Simplified Chinese.
- Preserve English technical terms on first mention: `能力上限（aptitude）`, `不可靠性（unreliability）`, `分片指令（sharded instruction）`, etc.
- Translate the main body section-by-section.
- Treat appendices as reader-level translation/synthesis unless Gavin explicitly asks for verbatim appendix translation.
- Preserve formulas, simulation labels, model names, dataset names, figure/table labels, and metric symbols.
- For OCR-garbled numeric tables/figures, translate the caption/prose and add a note telling readers to inspect the PDF side for exact values.

## Workflow

### 1. Locate source artifacts

Use the project/channel mapping first. For reading-group papers, the expected root is usually under:

```text
/data/<user>/papers/<reading_group_folder>/
```

Check for:

- `README.md`
- local PDF, e.g. `paper.pdf` or a versioned arXiv filename
- extracted text, e.g. `paper.txt`
- prior reading notes, e.g. `reading_notes.md`

If text has not been extracted, use `pdftotext -layout` as a fast first pass:

```bash
pdftotext -layout PAPER.pdf PAPER.txt
pdfinfo PAPER.pdf
```

Use `ocr-and-documents` when local extraction/OCR choices matter.

### 2. Read enough before translating

Before creating the artifact, inspect:

- title, authors, abstract;
- section outline;
- task/method/metric definitions;
- main results;
- implications/limitations;
- appendix headings if relevant.

This prevents mistranslating terms or missing the paper’s argument structure.

### 3. Translate in chunks

For a full paper, split translation into 2–4 chunks and delegate in parallel when appropriate.

Recommended chunking:

1. Title/abstract/introduction/method/setup/results opening.
2. Remaining results, implications, conclusion, limitations.
3. Appendices and discussion prompts as reader-level translation/synthesis.

Give subagents exact instructions:

- target language Simplified Chinese;
- academic but readable tone;
- preserve section headings;
- preserve key English terms on first mention;
- do not dump OCR-garbled tables;
- write each chunk to `translation_chunks/*.md`;
- return the path.

Example task instruction:

```text
Translate SOURCE lines A-B into polished Simplified Chinese. Preserve headings,
figure/table captions, metric symbols, and named conditions. For OCR-garbled
numeric tables, translate the prose/caption and add a note that exact values
should be viewed in the PDF. Write to translation_chunks/01_zh.md.
```

### 4. Assemble the translation Markdown

Create a consolidated file at the paper root, usually:

```text
translation_zh.md
```

Start with metadata and a clear caveat:

```markdown
---
标题：<Chinese title>
原文：arXiv:<id>，<authors>，<date>
译文版本：中文阅读校订版 v1（主文逐节翻译；附录为读者级译写；公式、图表与数值表以 PDF 为准）
生成位置：<path>/translation_zh.md
---

> 说明：右侧中文译文面向阅读组讨论，优先忠实表达论文论证与实验结论。OCR 提取的复杂表格/图形在译文中以说明或标题方式处理；精确数值、图形和参考文献请对照左侧 PDF。
```

Include discussion prompts at the end when helpful.

### 5. Build a side-by-side static web reader

Default hosted directory:

```text
/data/<user>/hermes_web/<paper_slug>/
```

Copy in:

- PDF as `PAPER.pdf`
- `translation_zh.md`
- optional `reading_notes.md`
- generated `index.html`

The reader should include:

- left pane: `<iframe src="PAPER.pdf#view=FitH">`
- right pane: rendered Chinese translation;
- layout controls: balanced / PDF-wide / translation-wide;
- Chinese font-size controls;
- search within the translation;
- direct links to open/download PDF and Markdown.

Design posture:

- dark app chrome;
- warm paper-colored translation pane;
- readable Chinese serif/body text;
- not flashy; this is a serious reading artifact.

### 6. Host and produce a shareable link

Hermes Discord web-log config may point at a LAN URL such as:

```yaml
discord.web_log_root: /data/<user>/hermes_web
discord.web_log_base_url: http://10.165.62.92:8777
```

If the LAN link times out for Gavin, start a quick Cloudflare tunnel against the static server:

```bash
/home/<user>/.local/bin/cloudflared tunnel --url http://127.0.0.1:8777
```

Capture the `https://*.trycloudflare.com` URL from logs, then share:

```text
https://<tunnel>.trycloudflare.com/<paper_slug>/index.html
```

Before sharing any `trycloudflare.com` link, verify the exact URL you will send:

```bash
python /home/<user>/hermes-agent/scripts/resolve_discord_web_url.py
curl -sS -I --max-time 10 "https://<tunnel>.trycloudflare.com/<paper_slug>/index.html"
```

Do not reuse a `trycloudflare.com` host from old Discord messages, old web logs, or memory unless it resolves and the full URL returns HTTP 200/304. If an old path is still valid but the host expired, replace only the host with the currently verified base URL.

Quick tunnels are public but temporary. Say so. For stable long-term hosting, ask before changing Hermes config or setting up a permanent tunnel/domain.

### 7. Verify before reporting done

Minimum verification:

```bash
python - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
p = Path('/data/<user>/hermes_web/<paper_slug>/index.html')
HTMLParser().feed(p.read_text(encoding='utf-8'))
print('html_parse_ok', p.stat().st_size)
PY

curl -I http://127.0.0.1:8777/<paper_slug>/index.html
```

Also verify:

- hosted HTML contains the Chinese title;
- hosted HTML references the PDF;
- PDF returns HTTP 200;
- Markdown translation returns HTTP 200;
- if using Cloudflare, public URL returns HTTP 200 from the server.

## Reporting Format

Keep the final Discord response compact:

```text
Done — hosted side-by-side reader:
<URL>

Created:
- Web page: <path>/index.html
- Chinese translation: <paper_root>/translation_zh.md

Verified:
- local/public URL returns 200
- PDF and translation load
- HTML parses

Caveat: main body is polished section-by-section translation; appendices are reader-level unless requested verbatim. OCR-garbled tables/figures should be checked against the PDF pane.
```

If Gavin sends a screenshot with `ERR_CONNECTION_TIMED_OUT` for the LAN IP, treat it as a routing/access problem, not a page-generation problem. Verify local service, then create/share a Cloudflare quick tunnel.

## Discussion-Reader Variant

See `references/discussion-reader-annotations-and-decks.md` for the session-tested details on autosaved PDF highlights, localStorage/export/import behavior, real PPTX→PDF deck embedding, visual QA, and cache-busting.

If Gavin asks for a two-sided paper discussion page rather than a translation reader, build a related but distinct artifact:
- for autosaved highlights, prefer a PDF.js text-selection flow: user selects text, then clicks a floating `Highlight selection` button; avoid auto-highlighting on mouseup because it behaves weirdly;
- save marks in `localStorage` under a stable key, and include Export/Import JSON buttons because quick Cloudflare tunnel domains can change and localStorage is origin-scoped;
- if the user specifically wants the native browser PDF viewer, explain that native PDF highlights usually cannot be autosaved by the HTML page;
- right side: a real PPTX deck exported to PDF and shown in an iframe, with PPTX/PDF download links — do **not** hand-roll crude HTML slide cards when Gavin asked for a presentation/deck;
- create the PPTX with the `powerpoint` workflow, export with LibreOffice, render slide images, and visually QA for clipping/overflow before publishing;
- left side decision rule:
  - if Gavin wants the PDF to behave like the translation reader / wants normal cursor text selection, use the native browser PDF iframe (`<iframe src="PAPER.pdf#view=FitH">`) and explicitly warn that native highlights are controlled by the browser/PDF viewer and are **not guaranteed to autosave**;
  - if Gavin asks for guaranteed autosaved web highlights, use a custom PDF.js annotation layer or sidecar workflow, but budget for browser QA and include Export/Import JSON because quick Cloudflare tunnel domains change and `localStorage` is origin-scoped;
  - if using custom marks, default to thin colored underlines rather than filled highlighter blocks, because overlapping filled highlights get visually heavy; compute underline rectangles from selected PDF.js text nodes when possible, not only `Range.getClientRects()` over whole lines, and visually clamp/shorten underline widths so they do not run far to the right; free-area marks should also render as underline/edge marks unless Gavin explicitly asks for filled regions.

See `references/pdf-annotation-modes.md` for the native-vs-custom annotation tradeoff and exact wording to use.

## Common Pitfalls

1. **Giving only a translation file.** Gavin specifically liked the side-by-side PDF + translation web reader. Build the web artifact unless he asks for text only.

2. **Using the private LAN URL as the only link.** `10.165.62.92:8777` may not be reachable from Gavin’s browser. Be ready to create a `trycloudflare.com` link.

3. **Claiming “perfect” verbatim translation of every appendix when only reader-level appendix synthesis was done.** Be explicit: main body translated; appendices reader-level unless done verbatim.

4. **Dumping broken OCR tables into Chinese.** For garbled tables, translate the surrounding prose/caption and direct readers to the PDF pane for exact values.

5. **Dropping English technical terms.** Keep English terms on first mention and preserve labels like `FULL`, `CONCAT`, `SHARDED`, `RECAP`, `SNOWBALL`, `P`, `A`, `U`.

6. **Not verifying the hosted URL.** Always curl local and public URLs before reporting.

7. **Forgetting Discord deliverability.** Use a compact final message with the URL and paths. Avoid giant translation dumps in Discord.

## Verification Checklist

- [ ] Source PDF and extracted text found or created.
- [ ] Main paper body translated into polished Simplified Chinese.
- [ ] Appendix treatment is clearly labeled as verbatim or reader-level.
- [ ] `translation_zh.md` exists in the paper root.
- [ ] Hosted web folder under `/data/<user>/hermes_web/<paper_slug>/` contains `index.html`, PDF, and Markdown.
- [ ] HTML parses without obvious syntax errors.
- [ ] Local static URL returns 200.
- [ ] PDF and Markdown URLs return 200.
- [ ] Public Cloudflare URL created if LAN URL is unreachable.
- [ ] Final answer includes URL, file paths, verification, and caveat.
