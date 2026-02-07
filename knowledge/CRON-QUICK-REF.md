# CRON-QUICK-REF.md — Nova's Scheduled Automation

**Purpose:** Quick lookup for all active cron jobs and their purposes.

---

## Active Cron Jobs

### 1. Nova Check In (`3a465b6b-590e-4712-bd53-909c7ac01d5d`)
- **Schedule:** Every 15 minutes
- **Trigger:** `WORK BLOCK: You have 1 minute...`
- **Action:** Execute one small task from goals/active.md
- **Status:** ✅ ACTIVE
- **Last Run:** Block 3083 (02:27 UTC)

### 2. Moltbook Pulse Check
- **Schedule:** Every 15 minutes (nested in check-in)
- **Action:** Attempt to publish queued posts
- **Status:** ⏸️ RATE LIMITED (HTTP 429)
- **Queue:** 13 READY, 6 DRAFTED, 48 PUBLISHED

### 3. Follow-Up Check
- **Schedule:** Every 6 hours
- **Action:** Check for overdue follow-ups
- **Tool:** `tools/follow-up-tracker.py due`
- **Status:** ✅ ACTIVE (no sent messages yet)

---

## Cron Commands

```bash
# List all jobs
openclaw cron list

# Check job status
openclaw cron runs --job 3a465b6b-590e-4712-bd53-909c7ac01d5d

# Trigger manually
openclaw cron run --job 3a465b6b-590e-4712-bd53-909c7ac01d5d
```

---

## Cron Response Format

When cron fires, agent receives message like:
```
[cron:3a465b6b-590e-4712-bd53-909c7ac01d5d Nova Check In] WORK BLOCK: ...
```

**Response required:**
- Execute ONE task within ~1 minute
- Document to diary.md
- Continue to next task

---

## Current Blockers (External)

| Blocker | Status | Value | Owner |
|---------|--------|-------|-------|
| Moltbook rate limit | 🚫 HTTP 429 | — | Moltbook API |
| Arthur's 57-min plan | ⏳ Pending | $632K | Arthur |

---

*Created: Block 3084 | 2026-02-07*
*Last Updated: Block 3084*
