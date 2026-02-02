# Browser Access Unblock (Arthur)

**Goal:** Unblock Nova’s ability to use the `browser` tool (Playwright-controlled browser) so I can:
- post/engage on Moltbook (week-2 goals)
- do Code4rena / audit research
- general web research without manual copy/paste

## Current symptom
- I can run work blocks locally, but anything requiring interactive web access is blocked.
- `today.md` notes: “Restart gateway for browser access (needs Arthur)”.

## What to try (safe + fast)
1. **Restart the OpenClaw gateway** (most common fix):
   - `openclaw gateway status`
   - `openclaw gateway restart`

2. **Verify browser control server is up**
   - In Nova session I can run `browser.status` and confirm a running instance.

3. **If using Chrome Extension / Browser Relay**
   - Open the target tab in Chrome.
   - Click the **OpenClaw Browser Relay** toolbar icon so the badge shows **ON**.
   - Then tell me “tab attached” and I’ll drive it.

## Success check
- I should be able to:
  - `browser.start` (profile=openclaw)
  - `browser.open` a URL
  - `browser.snapshot` without errors

## Why this matters (work impact)
- Unblocks 3 Week-2 objectives (Moltbook presence + relationships + revenue research).
