# NovaBrowser Inspector (CDP) — Watch/Diff Mode

This is a lightweight “what’s on the page right now?” inspector for NovaBrowser, built on Chrome DevTools Protocol (CDP).

Source: `tools/novabrowser_inspector.js`

## Prereq: run Chromium with remote debugging

You need a Chromium/Chrome instance started with a remote debugging port, e.g.:

```bash
chromium --remote-debugging-port=9222
```

(Any port works; pass it via `--port` below.)

## One-shot snapshot

Captures a single snapshot of the current active page:

```bash
node tools/novabrowser_inspector.js --port 9222 --out artifacts/novabrowser
```

Output goes to:

```
artifacts/novabrowser/<timestamp>/
```

Files written per snapshot:
- `page.json` — `{ capturedAt, url, title, ... }`
- `frames.json` — raw CDP frame tree
- `frames.flat.json` — flattened list (easier to diff/scan)
- `inputs.json` — discovered inputs + counts (includes visibleCount)
- `screenshot.png` — current page screenshot

The CLI prints a short summary:
- page title + URL
- total inputs + visible inputs

## Watch mode (continuous snapshots + diff)

Watch mode repeatedly captures snapshots and writes a `diff.json` for each iteration.

```bash
node tools/novabrowser_inspector.js --watch --every-ms 2000 --iterations 0 --out artifacts/novabrowser
```

Flags:
- `--watch` : enable loop
- `--every-ms <n>` : interval between captures (default 2000)
- `--iterations <n>` : number of iterations (`0` = infinite)
- `--out <dir>` : base output directory (default `artifacts/novabrowser`)
- `--port <n>` : CDP port (default `9222`)

Output structure:

```
artifacts/novabrowser/watch-<timestamp>/
  iter-0001-<timestamp>/
    ...snapshot files...
    diff.json
  iter-0002-<timestamp>/
    ...
```

### diff.json schema (high level)

Each iteration writes `diff.json` with:
- `iter`, `capturedAt`
- `step` (a lightweight "progress" counter)
- `stepSignal` (true when this iteration looked like a new step)
- `prev`: `{ page, counts }` (or `null` on first iter)
- `next`: `{ page, counts }`
- `diff`:
  - `urlChanged`, `titleChanged`
  - `inputCountChanged` (total/visible counts)
  - `frameCountChanged`
  - `inputsChanged` (stable JSON compare of summarized inputs)
  - `inputDelta` (bounded, human-meaningful):
    - `addedCount`, `removedCount`, `changedCount`
    - plus small samples of added/removed/changed (when present)
  - `any` (OR of the above)

The CLI prints a short line whenever `diff.any` is true, e.g. navigation, iframe changes, form fields appearing/disappearing.

Example output (when something changes):

```text
• change @ iter 12 (step 3↑): url=false title=false inputs=true count=true frames=false
  inputs delta: +1 -0 ~0
  page: Sign in — https://example.com/login
```

## When to use this

Use Inspector watch mode when NovaBrowser is “blind” about page structure or form fields:
- login flows that dynamically render inputs
- pages that swap iframes (e.g. auth/embedded widgets)
- debugging why a form-fill step can’t find the expected field

It’s especially useful to correlate:
- what changed on-screen (`screenshot.png`)
- what changed structurally (`diff.json`, `inputs.json`, `frames.flat.json`)

## Quick workflow

1) Start Chromium with remote debugging.
2) Open/navigate to the page you’re automating.
3) Run watch mode during the interaction.
4) Inspect the latest `iter-*/diff.json` + `inputs.json` + `screenshot.png`.

### Quick tail (one-line summary of latest diff)

If you’re running watch mode and just want a single “did anything change?” line:

```bash
tools/novabrowser_watch_tail.sh artifacts/novabrowser
```

It finds the newest `watch-*/iter-*/diff.json` and prints a compact summary.

---

## Known blind spots + next improvements

### Step detection (reduce noise)
Current `stepSignal` is intentionally lightweight. Next iteration:
- detect “real step transitions” using a multi-signal score (URL/title change + DOM/input deltas + frame-tree churn)
- optionally include **small** screenshot perceptual hash deltas to catch “same DOM, new screen” transitions

### Frames, iframes, and Shadow DOM coverage
Inspector currently relies on CDP frame tree + basic input discovery. Next iteration:
- explicitly traverse **all frames** (including nested iframes) for input discovery
- add **Shadow DOM** enumeration (open shadow roots) so inputs inside web components are not missed
- annotate each discovered input with `{ frameId, frameUrl, inShadowDom }` to make diffs debuggable

(These items exist to stop NovaBrowser “blind spots” during tricky logins and embedded auth widgets.)
