---
name: powerpoint
description: "Create, read, edit .pptx decks, slides, notes, templates."
license: Proprietary. LICENSE.txt has complete terms
platforms: [linux, macos, windows]
---

# Powerpoint Skill

## When to use

Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions "deck," "slides," "presentation," or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.

## Quick Reference

| Task | Guide |
|------|-------|
| Read/analyze content | `python -m markitdown presentation.pptx` |
| Edit or create from template | Read [editing.md](editing.md) |
| Create from scratch | Read [pptxgenjs.md](pptxgenjs.md) |

---

## Reading Content

```bash
# Text extraction
python -m markitdown presentation.pptx

# Visual overview
python scripts/thumbnail.py presentation.pptx

# Raw XML
python scripts/office/unpack.py presentation.pptx unpacked/
```

---

## Editing Workflow

**Read [editing.md](editing.md) for full details.**

1. Analyze template with `thumbnail.py`
2. Unpack → manipulate slides → edit content → clean → pack

---

## Creating from Scratch

**Read [pptxgenjs.md](pptxgenjs.md) for full details.**

Use when no template or reference presentation is available.

## App / Codebase Explainer Decks

When the requested deck should explain what an app in a folder does, follow `references/app-codebase-explainer-decks.md`: inspect the repo first, identify roles/screens/data flow/scope boundaries, avoid exposing secrets from local env files, verify a lightweight app check when available, export PPTX+PDF, render to images, and QA suspicious slides individually.

## Gavin Paper Discussion Decks

For Gavin-style paper discussion decks, follow `references/gavin-paper-discussion-deck-pacing-and-qa.md`: pace slowly, prefer pointing to existing paper figures instead of redrawing them, cite the main-text/appendix source for algorithms and metric definitions, render PPTX→PDF→PNG, inspect contact sheets plus dense slides individually, and cache-bust embedded deck URLs after publishing. For iterative paper-deck revisions from Gavin's feedback, preserve the canonical uploaded order, sequence method slides pedagogically, use simple direct titles, cache-bust all deck links/buttons, and inspect changed slides individually for clipping.

---

## Design Ideas

**Don't create boring slides.** Plain bullets on a white background won't impress anyone. Consider ideas from this list for each slide.

### Before Starting

- **Pick a bold, content-informed color palette**: The palette should feel designed for THIS topic. If swapping your colors into a completely different presentation would still "work," you haven't made specific enough choices.
- **Dominance over equality**: One color should dominate (60-70% visual weight), with 1-2 supporting tones and one sharp accent. Never give all colors equal weight.
- **Dark/light contrast**: Dark backgrounds for title + conclusion slides, light for content ("sandwich" structure). Or commit to dark throughout for a premium feel.
- **Commit to a visual motif**: Pick ONE distinctive element and repeat it — rounded image frames, icons in colored circles, thick single-side borders. Carry it across every slide.

### Color Palettes

Choose colors that match your topic — don't default to generic blue. Use these palettes as inspiration:

| Theme | Primary | Secondary | Accent |
|-------|---------|-----------|--------|
| **Midnight Executive** | `1E2761` (navy) | `CADCFC` (ice blue) | `FFFFFF` (white) |
| **Forest & Moss** | `2C5F2D` (forest) | `97BC62` (moss) | `F5F5F5` (cream) |
| **Coral Energy** | `F96167` (coral) | `F9E795` (gold) | `2F3C7E` (navy) |
| **Warm Terracotta** | `B85042` (terracotta) | `E7E8D1` (sand) | `A7BEAE` (sage) |
| **Ocean Gradient** | `065A82` (deep blue) | `1C7293` (teal) | `21295C` (midnight) |
| **Charcoal Minimal** | `36454F` (charcoal) | `F2F2F2` (off-white) | `212121` (black) |
| **Teal Trust** | `028090` (teal) | `00A896` (seafoam) | `02C39A` (mint) |
| **Berry & Cream** | `6D2E46` (berry) | `A26769` (dusty rose) | `ECE2D0` (cream) |
| **Sage Calm** | `84B59F` (sage) | `69A297` (eucalyptus) | `50808E` (slate) |
| **Cherry Bold** | `990011` (cherry) | `FCF6F5` (off-white) | `2F3C7E` (navy) |

### For Each Slide

**Every slide needs a visual element** — image, chart, icon, or shape. Text-only slides are forgettable.

**Layout options:**
- Two-column (text left, illustration on right)
- Icon + text rows (icon in colored circle, bold header, description below)
- 2x2 or 2x3 grid (image on one side, grid of content blocks on other)
- Half-bleed image (full left or right side) with content overlay

**Data display:**
- Large stat callouts (big numbers 60-72pt with small labels below)
- Comparison columns (before/after, pros/cons, side-by-side options)
- Timeline or process flow (numbered steps, arrows)

**Visual polish:**
- Icons in small colored circles next to section headers
- Italic accent text for key stats or taglines

### Typography

**Choose an interesting font pairing** — don't default to Arial. Pick a header font with personality and pair it with a clean body font.

| Header Font | Body Font |
|-------------|-----------|
| Georgia | Calibri |
| Arial Black | Arial |
| Calibri | Calibri Light |
| Cambria | Calibri |
| Trebuchet MS | Calibri |
| Impact | Arial |
| Palatino | Garamond |
| Consolas | Calibri |

| Element | Size |
|---------|------|
| Slide title | 36-44pt bold |
| Section header | 20-24pt bold |
| Body text | 14-16pt |
| Captions | 10-12pt muted |

### Spacing

- **Mobile/Discord readability is a hard constraint** — if the user will inspect slides through Discord/mobile, avoid dense research tables as the primary slide content. For row-level results with many columns, use one-row or one-feature cards with large text and move the full table to CSV/XLSX. If a user says they cannot read a deck, regenerate with a layout-safe pattern (more slides, larger cards, fewer columns), not just a small font bump.

### Hard Layout Safety Rules

For dense research PPTX decks, especially auto-generated feature pages, treat overlap prevention as a hard requirement, not polish:

- Reserve fixed vertical lanes: title lane, subtitle/meta lane, chips/tags lane, main content lane, and footer lane. Never let a wrapped title intrude into subtitle or chip lanes.
- Long titles must use a measured/truncated title helper: cap to 1-2 lines, reduce font size when needed, or move the full text into a body card. Do not rely on PowerPoint/LibreOffice auto-fit. Never truncate semantically primary content (e.g. a feature interpretation, claim, result, or conclusion) unless the full version is shown elsewhere on the same slide or an adjacent dedicated slide.
- Give every card/body text box an explicit maximum line count. If text exceeds it, summarize or split to another slide; never shrink below readable size just to fit. If a phrase is intentionally abbreviated, mark it as a summary; if the slide implies it is showing the full text, the full text must be visible somewhere on-slide or on an adjacent detail slide.
- For formula/method slides that introduce a scoring rule, do not present one dense equation block without definitions. Use a line-by-line structure: define the universe and every symbol (`U`, `i`, ranks, denominators, metrics), then show numbered calculation steps. Left-align and top-anchor monospace formula text inside cards, and QA the individual rendered slide, not just the contact sheet, because centered formula blocks can look polished but be hard to audit from Discord screenshots.
- Card/button backgrounds must fully cover the text they contain. Do not place body text below a short rounded rectangle, chip, pill, or button. Compute the text height first, then draw the background to that height, or use separate bounded chips/cards. If a card has a title and body, its body box must have positive usable height and must remain inside the card with padding.
- Use a layout solver/checker in generation scripts: estimate wrapped line counts, compute box heights, then assert that all rectangles have at least 0.12-0.20\" separation and stay above the footer. Fail the build if boxes overlap or if any text box extends outside the background/card it is visually associated with.
- For feature-audit decks, split by evidence type instead of cramming: main audit/interpretation page, dose-response page, and free-generation/examples page. If examples are too long for one page, add continuation slides or bundle full rows in a clearly labeled data workbook; never silently clip intended-full text.
- Treat card/chip/button containment as a rendered-visual requirement, not just a coordinate calculation: after LibreOffice/PDF export, every text run that visually belongs to a background must remain inside that background. Text hanging below or outside a rounded rectangle is a blocker, even if the PPTX object bounds looked valid.
- Render with LibreOffice and inspect slide images before delivery; XML positions alone are not enough because LibreOffice wraps text differently from PowerPoint.

### Avoid (Common Mistakes)

- **Don't repeat the same layout** — vary columns, cards, and callouts across slides
- **Don't center body text** — left-align paragraphs and lists; center only titles
- **Don't skimp on size contrast** — titles need 36pt+ to stand out from 14-16pt body
- **Don't default to blue** — pick colors that reflect the specific topic
- **Don't mix spacing randomly** — choose 0.3" or 0.5" gaps and use consistently
- **Don't style one slide and leave the rest plain** — commit fully or keep it simple throughout
- **Don't create text-only slides** — add images, icons, charts, or visual elements; avoid plain title + bullets
- **Don't forget text box padding** — when aligning lines or shapes with text edges, set `margin: 0` on the text box or offset the shape to account for padding
- **Don't use low-contrast elements** — icons AND text need strong contrast against the background; avoid light text on light backgrounds or dark text on dark backgrounds
- **NEVER use accent lines under titles** — these are a hallmark of AI-generated slides; use whitespace or background color instead

---

## QA (Required)

**Assume there are problems. Your job is to find them.**

Your first render is almost never correct. Approach QA as a bug hunt, not a confirmation step. If you found zero issues on first inspection, you weren't looking hard enough.

### Content QA

```bash
python -m markitdown output.pptx
```

Check for missing content, typos, wrong order.

**Checklist QA for user-requested changes:** Before delivery, convert the user's requested/todo items into an explicit checklist and verify every item against both the generated artifacts and the rendered/text-extracted deck. Visual contact sheets can miss semantic omissions. If the user requested a complete metric/provenance matrix, do not show only the selected source row — include every requested metric/condition, mark missing values explicitly, and export the backing table. See `references/research-deck-todo-and-metadata-qa.md`.

**When using templates, check for leftover placeholder text:**

```bash
python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum|this.*(page|slide).*layout"
```

If grep returns results, fix them before declaring success.

### Visual QA

**⚠️ USE SUBAGENTS** — even for 2-3 slides. You've been staring at the code and will see what you expect, not what's there. Subagents have fresh eyes.

**Contact-sheet / QA-only requests:** When the user asks to inspect a rendered contact sheet and explicitly says not to edit files, do not run the fix loop or modify the deck. Treat it as a delivery gate: inspect the contact sheet, render/open high-resolution individual slides for any unclear or suspect thumbnails, and report slide-by-slide issues plus an overall verdict such as `acceptable as draft` / `not acceptable yet`. Call out blocking issues separately from minor polish. See `references/contact-sheet-visual-qa.md` for a compact example checklist and report shape.

Convert slides to images (see [Converting to Images](#converting-to-images)), then use this prompt:

```
Visually inspect these slides. Assume there are issues — find them.

Look for:
- Overlapping elements (text through shapes, lines through words, stacked elements)
- Text overflow or cut off at edges/box boundaries
- Decorative lines positioned for single-line text but title wrapped to two lines
- Source citations or footers colliding with content above
- Elements too close (< 0.3" gaps) or cards/sections nearly touching
- Uneven gaps (large empty area in one place, cramped in another)
- Insufficient margin from slide edges (< 0.5")
- Columns or similar elements not aligned consistently
- Low-contrast text (e.g., light gray text on cream-colored background)
- Low-contrast icons (e.g., dark icons on dark backgrounds without a contrasting circle)
- Text boxes too narrow causing excessive wrapping
- Leftover placeholder content

For each slide, list issues or areas of concern, even if minor.

Read and analyze these images:
1. /path/to/slide-01.jpg (Expected: [brief description])
2. /path/to/slide-02.jpg (Expected: [brief description])

Report ALL issues found, including minor ones.
```

### Verification Loop

1. Generate slides → Convert to images → Inspect
2. **List issues found** (if none found, look again more critically)
3. Fix issues
4. **Re-verify affected slides** — one fix often creates another problem
5. Repeat until a full pass reveals no new issues

**Do not declare success until you've completed at least one fix-and-verify cycle.**

---

## Converting to Images

Convert presentations to individual slide images for visual inspection:

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

This creates `slide-01.jpg`, `slide-02.jpg`, etc.

To re-render specific slides after fixes:

```bash
pdftoppm -jpeg -r 150 -f N -l N output.pdf slide-fixed
```

---

## Dependencies

- `pip install "markitdown[pptx]"` - text extraction
- `pip install Pillow` - thumbnail grids
- `npm install -g pptxgenjs` - creating from scratch
- LibreOffice (`soffice`) - PDF conversion (auto-configured for sandboxed environments via `scripts/office/soffice.py`)
- Poppler (`pdftoppm`) - PDF to images
