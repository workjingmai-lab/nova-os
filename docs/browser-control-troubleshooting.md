# Browser Control Troubleshooting (OpenClaw)

This is a quick checklist for when **Gateway browser control** isn’t responding ("browser access broken" / snapshots fail / no tabs).

## 1) Quick health checks
- Run: `openclaw status`
- Run: `openclaw gateway status`
- If the CLI says the gateway is down, start it: `openclaw gateway start`

If you get **`openclaw: not found`**:
- You’re likely inside an agent/container runtime that doesn’t have the OpenClaw CLI on PATH.
- Run the commands on the **host** where the Gateway is installed (or add the CLI to PATH in this runtime).

Tool sanity checks (from inside the agent):
- `functions.browser status`
  - If it returns `running:false` + `cdpReady:false`, the browser is not up yet → run `functions.browser start` then re-check status.
  - If it returns `enabled:true` but `functions.browser start` **times out**, suspect a Gateway/control-service issue (not just “no browser open”).
- `functions.browser profiles` (to confirm what’s available)
- `functions.browser tabs` (to confirm a tab is actually connected)

Known failure signature (control service unreachable):
- `functions.browser status` returns something like:
  - `enabled:true`, `running:false`, `cdpReady:false`
- `functions.browser start` fails with:
  - `Can't reach the openclaw browser control service (timed out after 15000ms)`

In that case, the next likely fix is **restart the Gateway on the host**:
- `openclaw gateway restart`

## 2) Tool-level symptoms → likely causes
- **`functions.browser status` fails / times out**
  - Gateway process stalled or crashed
  - Port conflict / control server not started
  - Agent runtime can’t reach the browser control service (networking / routing / service not running)
- **Can open browser but no tabs appear**
  - Using wrong profile
    - `profile="openclaw"` = isolated managed browser
    - `profile="chrome"` = Chrome extension relay (requires attached tab)
  - `functions.browser profiles` shows `chrome: running=true` but `tabCount=0`
    - Relay service is up, but **no Chrome tab is attached** (badge OFF or not installed)
  - Chrome Relay not attached (need toolbar badge ON)
  - You’re listing tabs on the wrong target (host/node) in multi-host setups
- **Snapshots work but actions fail**
  - Stale targetId
  - Page in a different tab/window
  - Shadow DOM / iframe UI not being targeted correctly

## 3) Recovery steps (non-destructive)
1. Retry `functions.browser status` (sometimes transient)
2. If `functions.browser start` fails with a **timeout**, treat it like “control service unreachable” (not just “browser closed”).
3. Restart the gateway (ask Arthur if this is a shared environment):
   - `openclaw gateway restart`
4. If using **Chrome Relay**:
   - Ensure the tab is attached via the OpenClaw Browser Relay toolbar icon (badge ON)
   - Then list tabs again

## 4) When debugging tricky logins
- Use watch-mode capture (NovaBrowser) and tail diffs:
  - `tools/novabrowser_watch_tail.sh artifacts/novabrowser`
- Watch for:
  - New iframes
  - Inputs appearing inside shadow roots
  - SPA route changes that don’t trigger full navigations

## 5) What to record when filing a bug
- Timestamp (UTC)
- What command/tool call failed
- Exact error text
- Whether Chrome Relay was used + whether the badge was ON
- OS/host info (from `openclaw status`)
