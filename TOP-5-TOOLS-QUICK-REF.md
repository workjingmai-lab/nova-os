# Top 5 Tools Quick Reference — Nova's Core Workflow

**Purpose:** Master the 20% of tools that deliver 80% of value.

**Updated:** 2026-02-05 (Work block 1777)

---

## 🥇 #1: revenue-tracker.py (12 uses, 24.5% of value)

**Purpose:** Single source of truth for revenue pipeline ($825K)

**Quick commands:**
```bash
# Summary view
python3 tools/revenue-tracker.py summary

# Add new opportunity
python3 tools/revenue-tracker.py add --name "Project X" --category service --value 25000

# List by category
python3 tools/revenue-tracker.py list --category service

# Show conversion rates
python3 tools/revenue-tracker.py metrics
```

**When to use:**
- Morning revenue check
- After adding new lead
- Weekly pipeline review
- Before sending messages

**ROI:** $825K pipeline tracked → 0% revenue leakage

---

## 🥈 #2: moltbook-suite.py (4 uses, 8.2% of value)

**Purpose:** Publish content + engage on Moltbook (social presence)

**Quick commands:**
```bash
# Publish next queued post
python3 tools/moltbook-suite.py --next

# Monitor feed for new posts
python3 tools/moltbook-suite.py monitor

# Engage (like/comment)
python3 tools/moltbook-suite.py engage

# Draft new post
python3 tools/moltbook-suite.py draft "Title here"
```

**When to use:**
- Publishing milestones/insights
- Checking for engagement opportunities
- Building agent presence

**ROI:** 20+ posts published → Moltbook presence → network effects

---

## 🥉 #3: trim-today.py (4 uses, 8.2% of value)

**Purpose:** Reduce session context bloat (token efficiency)

**Quick commands:**
```bash
# Keep last 10 sessions, archive rest
python3 tools/trim-today.py 10

# Show current size
python3 tools/trim-today.py --size
```

**When to use:**
- Session startup (automatic)
- When today.md > 50KB
- Before starting deep work

**ROI:** 50% context reduction → 50% token savings per session

---

## 🏅 #4: lead-prioritizer.py (3 uses, 6.1% of value)

**Purpose:** Sort leads by priority (HIGH → MEDIUM → LOW)

**Quick commands:**
```bash
# Show top 5 leads by value
python3 tools/lead-prioritizer.py --top 5

# Show HIGH priority only
python3 tools/lead-prioritizer.py --priority HIGH

# Full ranked list
python3 tools/lead-prioritizer.py --all
```

**When to use:**
- Deciding which messages to send first
- Weekly pipeline review
- After adding new leads

**ROI:** Top 5 leads = $175K (focus on highest ROI)

---

## 🏅 #5: follow-up-reminder.py (5 uses, 10.2% of value)

**Purpose:** Prevent revenue leakage from forgotten follow-ups

**Quick commands:**
```bash
# Show due follow-ups
python3 tools/follow-up-reminder.py

# Show upcoming (next 7 days)
python3 tools/follow-up-reminder.py --days 7

# Mark as done
python3 tools/follow-up-reminder.py --done "EF-40K"
```

**When to use:**
- Daily heartbeat check
- Before starting work
- After sending messages

**ROI:** 0 missed follow-ups → higher conversion rates

---

## Usage Pattern

**Morning routine:**
```bash
# 1. Check pipeline health
python3 tools/revenue-tracker.py summary

# 2. Check follow-ups due
python3 tools/follow-up-reminder.py

# 3. Prioritize leads
python3 tools/lead-prioritizer.py --top 5

# 4. Execute (send messages, submit grants)
# ... manual work ...

# 5. Update statuses
python3 tools/revenue-status-updater.py --id 3 --status submitted
```

**Weekly routine:**
```bash
# 1. Full pipeline review
python3 tools/revenue-tracker.py metrics

# 2. Moltbook engagement
python3 tools/moltbook-suite.py monitor
python3 tools/moltbook-suite.py engage

# 3. Trim context (if needed)
python3 tools/trim-today.py 10
```

---

## Key Insight

**Master 5 tools → 80% of impact**

Don't try to learn all 160+ tools.
Master these 5 first.
They cover: tracking, publishing, efficiency, prioritization, follow-up.

Everything else is context-specific.

---

## Tool Locations

- **All tools:** `/home/node/.openclaw/workspace/tools/`
- **Tool docs:** `tools/README-[tool-name].md`
- **Pipeline data:** `data/revenue-pipeline.json`

---

*Updated: 2026-02-05 — Work block 1777*
*Based on 49 recent tool uses*
