# Heartbeat Check Template

## Purpose
Systematic checks during heartbeat cycles (every 15 minutes).

## Check Rotation (2-4 per day)

### Priority Checks
- [ ] **Emails** — Any urgent unread messages?
- [ ] **Calendar** — Upcoming events in next 24-48h?
- [ ] **Moltbook** — New activity from tracked agents?
- [ ] **Notifications** — Mentions, alerts, updates?

### State Updates
```json
{
  "lastChecks": {
    "email": timestamp,
    "calendar": timestamp,
    "moltbook": timestamp,
    "notifications": timestamp
  }
}
```

## When to Reach Out
- ✅ Important email arrived
- ✅ Calendar event < 2h away
- ✅ Moltbook agent posted something interesting
- ✅ > 8h since last meaningful message

## When to Stay Quiet (HEARTBEAT_OK)
- ✅ Late night (23:00-08:00) unless urgent
- ✅ Human clearly busy
- ✅ Nothing new since last check
- ✅ Just checked < 30 min ago

## Proactive Work (No Ask Needed)
- Read and organize memory files
- Check on projects (git status)
- Update documentation
- Commit and push changes
- Review and update MEMORY.md

## Goal: Helpful, Not Annoying
Check in 2-4x per day. Do useful background work. Respect quiet time.
