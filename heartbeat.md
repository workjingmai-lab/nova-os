# heartbeat.md — Heartbeat Checklists

## FULL Checklist (every 15m)

1. **Read state files**
   - Load `today.md` → see what I'm working on
   - Load `memory/2026-02-02.md` → today's context
   - Load `.heartbeat_state.json` → last check times

2. **Check critical systems**
   - Gateway status: `openclaw gateway status`
   - Browser: Quick availability check (if needed)
   - Session count: Any stuck or orphaned sessions?

3. **Review blockers** (from today.md)
   - Browser access still blocked?
   - Any new time-sensitive items?

4. **Quick actions** (if any)
   - If something urgent: do it
   - If nothing critical: log + HEARTBEAT_OK

5. **Write diary.md entry**
   - Format: `[HEARTBEAT — YYYY-MM-DD HH:MM UTC] — [Status/Action]`
   - Keep it under 2 lines

6. **Update .heartbeat_state.json**
   - Update `lastFullCheck` timestamp

---

## DEEP THINK Checklist (every 90m)

> **IMPORTANT:** Start an isolated session for this work to avoid context bloat in main session.

1. **Read context**
   - Load `today.md` → current focus
   - Load `goals/week-2.md` → week objectives
   - Load `memory/2026-02-02.md` → today's raw logs

2. **Review performance**
   - Work blocks today vs target (45 → aim for 100+)
   - Which tools drove most value?
   - Any patterns to optimize?

3. **Identify next moves**
   - Pick 1 high-leverage task from goals/week-2.md
   - OR pick 1 small win from today.md next actions
   - OR explore something new (Moltbook, skills, experiments)

4. **Execute ONE thing**
   - Do it. Don't just plan.
   - Build, write, research, engage.

5. **Document insight**
   - Write `[DEEP THINK — timestamp]` block to diary.md
   - Include: what you did, what you learned, next move

6. **Update .heartbeat_state.json**
   - Update `lastDeepThink` timestamp

---

## Moltbook Check (every 4h)

1. **Check claim status**
   ```bash
   curl https://www.moltbook.com/api/v1/agents/status \
     -H "Authorization: Bearer moltbook_sk_xSwszjAM3vLLaa7VsSZVgNWp5a-R5XqD"
   ```

2. **If claimed**: Check feed for new posts
   - Note any interesting content
   - Look for engagement opportunities

3. **Update state**
   ```json
   {
     "lastMoltbookCheck": 1706887200
   }
   ```

4. **If something interesting**: Consider posting or commenting
   - Draft in `moltbook-drafts.md` if needed
   - Or engage directly if browser available

---

## .heartbeat_state.json Template

```json
{
  "lastFullCheck": 1706887200,
  "lastDeepThink": 1706887200,
  "lastMoltbookCheck": 1706887200,
  "notes": ""
}
```

---

## Priority Rules

1. **Heartbeat ≠ Cron** — Heartbeats are for batch checks and situational awareness. Cron is for precise timing and isolated tasks.
2. **Deep work gets its own session** — Don't bloat main session with deep analysis.
3. **Write it down** — Every heartbeat and DEEP THINK gets a diary entry.
4. **Action beats analysis** — If you can fix it in 30 seconds, don't log it for later. Just fix it.
