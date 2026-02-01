# Heartbeat Checklist

**When:** Every 15 minutes (cron-triggered)
**Goal:** Stay proactive without being annoying

## Pre-Heartbeat Checks
- [ ] What time is it? (Avoid late-night noise: 23:00-08:00 UTC)
- [ ] Last heartbeat < 30 min ago? (Don't spam)
- [ ] Human clearly busy? (Wait for quieter time)

## What to Check (Rotate through these)
- [ ] **Emails** — Any urgent unread?
- [ ] **Calendar** — Events in next 24-48h?
- [ ] **Moltbook** — New activity from tracked agents?
- [ ] **Work log** — Review recent progress

## When to Reach Out
✅ **Do reach out:**
- Important email arrived
- Calendar event < 2 hours away
- Something interesting found
- Been > 8h since last message

❌ **Stay quiet (HEARTBEAT_OK):**
- Late night (23:00-08:00)
- Nothing new since last check
- Just checked < 30 min ago
- Human is clearly busy

## Background Work (Safe to do anytime)
- Read and organize memory files
- Check on projects (git status, etc.)
- Update documentation
- Commit and push changes
- Review and update MEMORY.md

## Tracking
Track your checks in memory/.heartbeat-state.json:
```json
{
  "lastChecks": {
    "email": 1703275200,
    "calendar": 1703260800,
    "moltbook": null
  }
}
```

## Heartbeat Response Format
**Nothing needs attention:**
```
HEARTBEAT_OK
```

**Something needs attention:**
```
[ALERT] Calendar: Meeting with Arthur in 1 hour
[CONTEXT] Project sync, link in calendar
[SUGGESTED] Prepare progress summary
```

---

**Remember:** Be helpful without being annoying. Quality > frequency.
