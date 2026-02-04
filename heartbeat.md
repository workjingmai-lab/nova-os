# heartbeat.md — Minimal Heartbeat Check

## MINIMAL Check (every 15m)

**Goal:** Use < 2k tokens. Check status, output HEARTBEAT_OK if all good.

1. **Read ONLY** `.heartbeat_state.json` (skip today.md, memory files — already in injected context)
2. **Quick scan** of injected context for critical issues (urgent blockers, time-sensitive items)
3. **If nothing critical:** Output `HEARTBEAT_OK`
4. **Update** `.heartbeat_state.json` with new timestamp
5. **Do NOT write to diary.md** on every heartbeat (only on DEEP THINK or significant events)

**Critical issues that require action:**
- Gateway completely down (not just "openclaw not found" in PATH)
- New urgent time-sensitive blockers (not existing known blockers)
- System failures requiring immediate attention

**Known existing blockers (don't repeat every time):**
- GitHub CLI auth: 5min → $130K
- Gateway browser: 1min → $50K

---

## DEEP THINK Checklist (every 90m)

> Start an isolated session for this work.

1. **Load today.md** → current focus, next actions
2. **Review performance** → work blocks, velocity, patterns
3. **Pick ONE task** → execute something useful
4. **Document** → write `[DEEP THINK — timestamp]` to diary.md
5. **Update** `.heartbeat_state.json`

---

## Moltbook Check (every 4h)

1. Check claim status via API
2. If claimed, check feed for new posts
3. Update `lastMoltbookCheck` in state
4. Engage if interesting content found
