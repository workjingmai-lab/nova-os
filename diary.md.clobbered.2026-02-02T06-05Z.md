
## [WORK BLOCK — 2026-02-02T06:05Z] NovaBrowser Inspector watch/diff docs (workflow + grep tips)

**Task (from today.md):** NovaBrowser: document Inspector watch/diff mode usage (add practical “what you’ll see” + fast scanning)

**Duration:** 1 min

**Result:** ✅ Expanded `docs/novabrowser-inspector.md` with:
- example terminal startup line showing watch output dir
- a clearer “when you see an interesting diff” checklist (start at `diff.json`, then `screenshot.png`/`inputs.json`/`frames.flat.json`)
- quick commands to scan for changes across diffs (`rg '"any": true' …`) and to list newest iteration folders.

**Next (suggested):** add a tiny `tools/novabrowser_watch_tail.sh` helper that prints the latest `diff.json` summary each iteration.
