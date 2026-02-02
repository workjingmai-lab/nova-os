# Incident: Browser control service unreachable (OpenClaw) — 2026-02-02

## Summary
In this runtime, the `functions.browser` tool reports browser automation **enabled** but the underlying **browser control service is unreachable**.

This is distinct from “Chromium is closed.” The signature is:
- `functions.browser status` → `enabled:true`, `running:false`, `cdpReady:false` (Chromium detected at `/usr/bin/chromium`)
- `functions.browser start` → timeout: "Can't reach the openclaw browser control service (timed out after 15000ms)"

## Why it matters
- Blocks: Moltbook posting/engagement, Code4rena onboarding, any browser-based automation.

## Evidence (from diary)
- First observed: 2026-02-02T07:02Z
- Re-confirmed: 2026-02-02T07:05Z

## Likely fix
Gateway restart on the host where OpenClaw is running:
- `openclaw gateway restart`

## After restart
Re-test:
1) `functions.browser status` → should show `running:true` and `cdpReady:true` (or at least start succeeds)
2) `functions.browser start` (profile=`openclaw`) should not time out

## Notes
- In this environment `openclaw` CLI is not on PATH, so gateway-level diagnostics must be executed on the host install.

## Action needed (Arthur)
When you have a moment on the host machine running the Gateway:
1) Run: `openclaw gateway status`
2) If it looks unhealthy, run: `openclaw gateway restart`
3) Then I’ll re-test `functions.browser start` and proceed with Moltbook + Code4rena tasks.
