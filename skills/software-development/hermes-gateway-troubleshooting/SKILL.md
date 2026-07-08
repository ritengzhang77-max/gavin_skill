---
name: hermes-gateway-troubleshooting
description: "Troubleshoot Hermes gateway/Discord sessions that appear stuck, retrying, or silent while an agent turn is still running."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [hermes-agent, gateway, discord, troubleshooting, logs, background-processes]
    related_skills: [hermes-agent, debugging-hermes-tui-commands, systematic-debugging]
---

# Hermes Gateway Troubleshooting

## When to Use

Use this skill when Gavin asks why Hermes is stuck, silent, retrying, typing forever, or not responding in Discord/Telegram/gateway sessions.

Typical trigger phrases:
- "why stuck here", "why stocked here", "what is going on"
- screenshot shows `Retrying in … (attempt 1/3)` or gateway typing indicator
- Discord thread has no final answer after a long autonomous/project turn
- background process completion notifications appear to have derailed or delayed a session
- Discord web-log / thread-canvas link fails with browser DNS errors such as `ERR_NAME_NOT_RESOLVED` for a `trycloudflare.com` hostname
- Gavin reports a Discord web-log page cannot be opened, especially browser DNS errors like `ERR_NAME_NOT_RESOLVED` for a `*.trycloudflare.com` link
- Gavin reports Thread Canvas is showing an old message, the clean-chat pane is stale, or a new Discord/web-log message is missing despite the page loading
- Gavin asks to improve Discord web-log research pages, Thread Canvas, thread-file previews, split chat/artifact panes, role-colored message styling, refresh behavior, or linked-file side panels
- Gavin asks for the Thread Canvas page/link and rejects an old thread log, artifact file, PPTX/PDF, or mobile file preview
- Gavin asks to “show/send the correct working Thread Canvas again” after an old `trycloudflare.com` link was posted

## First Principle

Do not assume the visible gateway status line is the current blocker. A stale `Retrying in …` message may only reflect a transient model stream failure that recovered, while the agent continued through many tool calls afterward. Diagnose from logs and session/process state before answering.

## Investigation Checklist

1. **Identify the thread/session from logs.** Search `~/.hermes/logs/gateway.log` and `~/.hermes/logs/agent.log` for the user's message text, Discord chat/thread id, or visible status text.

2. **Establish timeline, not just the first error.** For the matching session id, inspect:
   - inbound message time and chat id,
   - model/provider and session id,
   - API retry/error lines,
   - subsequent API calls/tool completions,
   - final `Turn ended` or `response ready` lines.

3. **Distinguish common states.**
   - Transient upstream/API retry: log has `API call failed (attempt 1/3)` followed by later successful `API call #...` lines.
   - Long-running turn: many `API call #N`, tool completions, `process completed`, or large token counts continue after the visible status.
   - Background-process handoff: `Process proc_... finished — injecting agent notification` creates a new turn in the same thread.
   - Compression stall: look for `context compression started`, `Failed to generate context summary`, or session hygiene lines.
   - Tool approval timeout: tool result includes `BLOCKED: Command timed out without user response`; report this honestly and do not retry the same command.

4. **Use lightweight status tools first.** Prefer log search/read and `process(action="list")` before broad terminal probes. In Discord troubleshooting turns, broad `ps`/system-state terminal commands can trigger approval/timeout and make the status response worse.

5. **For Discord web-log links, distinguish local server health from public tunnel health.** If a `trycloudflare.com` web-log URL gives DNS `ERR_NAME_NOT_RESOLVED`, check the old hostname with `getent hosts`, check local `http://127.0.0.1:8777/`, then start a fresh `cloudflared tunnel --url http://127.0.0.1:8777`, verify the new URL, and update `discord.web_log_base_url` via `hermes config set` rather than editing protected config files directly. If the current base URL and local server both return `200`, also verify the **specific thread path** the user is trying to open before rotating tunnels; often the fix is simply to send the raw direct URL because Discord preview/browser embedding failed while the page itself is healthy. See `references/discord-web-log-quick-tunnel-expiry.md`.

6. **For research web-log file previews, curate artifacts rather than dumping attachments.** Thread-file panels should show only manually promoted/linked important artifacts with human titles/nicknames. Do not expose raw local paths, `image.png`, `img_xxx.webp`, or every auto-cached screenshot in the visible Thread Files list. If an image is crucial, promote it with a title such as `Crucial UI Bug Screenshot`; otherwise keep it out of the curated list. Split preview panes should have hide/show controls, and the splitter should resize only while actively dragging, not on hover. See `references/discord-web-log-thread-file-preview.md`.

7. **For Thread Canvas readability complaints, style the iframe content, not just the shell.** If Gavin says he cannot see whether a message is from him or Hermes, add role-specific classes from the message `direction` and use subtle but distinct backgrounds/borders for `direction-user` vs `direction-assistant`. Apply this in both `chat_log_clean.html` and the normal thread `index.html`; `thread_canvas.html` only embeds the clean chat in an iframe, so shell-only CSS will not affect message cards. After changing it, refresh/regenerate the static web log and verify both files contain the role classes/styles. See `references/discord-thread-canvas-role-coloring.md`.

4. **Use lightweight status tools first.** Prefer log search/read and `process(action="list")` before broad terminal probes. In Discord troubleshooting turns, broad `ps`/system-state terminal commands can trigger approval/timeout and make the status response worse.

5. **For web-log canvas link DNS failures, separate local server health from tunnel hostname health.** If a `trycloudflare.com` URL returns `ERR_NAME_NOT_RESOLVED`, check whether `http://127.0.0.1:8777/` still returns 200. If local works, start a fresh quick tunnel, verify the new URL, update `discord.web_log_base_url` via `hermes config set`, and tell Gavin old links can be repaired by replacing only the hostname. See `references/discord-web-log-quick-tunnel-expiry.md`.

For Thread Canvas link requests, send only the actual canvas URL. Gavin's phrase "Thread Canvas" means the static split-pane page ending in `/thread_canvas.html` (chat left, artifact preview right). For artifact drawer hygiene and readable HTML expectations, see `references/thread-canvas-artifact-hygiene.md`.

   Detailed checklist: see `references/thread-canvas-artifact-hygiene.md` for link verification, curated drawer rules, mobile-readable HTML artifact requirements, and cache-busting stale previews. (chat left, artifact preview right). Never send the directory/root URL, normal thread `index.html`, `chat_log_clean.html`, a PDF/PPTX, CSV, or a Thread Files artifact when he asks for Thread Canvas. A wrong target can still return HTTP 200, so verify both: URL path ends with `/thread_canvas.html` and the HTML title/body contains `Thread Canvas - ...`. If mobile/Discord opens the wrong item or the full path is long, create a short clean alias under the web root (for example `/sae-bench-canvas/thread_canvas.html`) and verify that alias before sending. See `references/discord-thread-canvas-direct-link-vs-artifact.md`.

6. **Answer with a concise diagnosis.** Include:
   - what the visible status/link error meant,
   - whether it recovered or the replacement link works,
   - what the agent is/was actually doing now,
   - safest next action (`wait`, `/stop`, ask for artifact summary, inspect specific outputs, or use the repaired web-log link).

## Response Pattern for Gavin

Use short bullets. Avoid overexplaining internals unless he asks.

Example:

```text
It is not stuck exactly at the visible retry line.

Logs show:
- openai-codex/gpt-5.5 had a transient stream/protocol failure and retried.
- the retry recovered; the session continued through many API/tool calls.
- the real delay is the long single turn / background process / compression step.

Safest next move: send /stop if you want control back, then ask for a current artifact summary and next concrete step.
```

## Pitfalls

- Do not tell Gavin "the API failed" as the whole explanation if logs show later successful calls.
- Do not treat a retry banner as proof the current process is dead.
- Do not kill or preempt GPU/model-loading jobs unless Gavin explicitly asks.
- Do not retry a terminal command that returned an approval timeout warning; switch to non-destructive log/session/process tools or stop.
- Do not save transient provider failures as durable negative claims about Hermes or a provider. Capture the diagnostic pattern, not the one-off outage.
- Do not display auto-cached Discord attachments or raw data/source/download files as curated research thread files. Promote only viewable human artifacts (HTML/PDF/PNG/JPG/WebP) with human-readable titles; keep CSV/XLSX/TSV/Parquet, PPTX/DOCX, Markdown readouts, and extensionless copied files under export paths unless Gavin explicitly asks for a download.
- Do not implement split-pane resizing as hover/proximity behavior. The boundary should move only during active drag/click-hold.
- Do not assume Thread Canvas visual changes belong in `thread_canvas.html` itself. The left chat is `chat_log_clean.html` inside an iframe; message-card role coloring must be rendered into the iframe document and also into the normal thread log.
- Do not assume a regenerated static web log will update inside mobile Safari/Discord webview if the clean-chat iframe URL is unchanged. Add an explicit refresh path/cache-busting iframe `src` and verify the embedded `chat_log_clean.html` separately.
- Do not answer a Thread Canvas request with the normal thread `index.html`, a Thread Files PDF/PPTX, or a promoted artifact link. Verify `thread_canvas.html`/HTML MIME specifically; HTTP 200 alone is not enough.
- Do not rely on long underscore-heavy Discord paths if Gavin's mobile browser opens the wrong target. Provide a short verified alias to the canvas page.

## References

- `references/discord-stale-retry-vs-running-turn.md` — session-derived pattern for a Discord screenshot showing `Retrying in 2.1s` while the agent continued working afterward.
- `references/discord-web-log-thread-file-preview.md` — Gavin's preferred research web-log UX for curated thread files, human titles, hide/show panels, and drag-only split-pane resizing.
- `references/discord-thread-canvas-role-coloring.md` — implementation pattern for role-colored user vs assistant message cards in Thread Canvas / clean-chat iframes and normal thread logs.
- `references/discord-thread-canvas-cache-refresh.md` — implementation pattern for stale clean-chat iframes: Refresh chat button, cache-busting `v=` parameter, near-bottom auto-refresh, and public-page verification.
- `references/discord-thread-canvas-direct-link-vs-artifact.md` — link-handling pattern for Gavin's Thread Canvas requests: send/verify `thread_canvas.html`, not `index.html` or a PDF/PPTX Thread Files artifact.
