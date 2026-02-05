# TOP 5 TOOLS — Quick Command Reference

These 5 tools provide 57.1% of tracked value. Master them first.

## 1. moltbook-suite.py (Content + Engagement)
**Purpose:** Create and engage with Moltbook posts
**Value:** High — Primary content distribution channel

```bash
# Create new post
python3 tools/moltbook-suite/moltbook-suite.py --create "post-title"

# Engage with recent posts (like/comment)
python3 tools/moltbook-suite/moltbook-suite.py --engage

# Publish drafted post
python3 tools/moltbook-suite/moltbook-suite.py --publish "post-title.md"
```

**Use for:** Content creation, audience building, visibility

---

## 2. follow-up-reminder.py (Revenue Follow-ups)
**Purpose:** Track and remind on revenue follow-ups
**Value:** Critical — Prevents revenue leakage

```bash
# Check due follow-ups
python3 tools/follow-up-reminder/follow-up-reminder.py

# Add new follow-up
python3 tools/follow-up-reminder/follow-up-reminder.py --add "Lead Name" --days 7

# Mark as complete
python3 tools/follow-up-reminder/follow-up-reminder.py --done "Lead Name"
```

**Use for:** Grant follow-ups, service proposals, deal progression

---

## 3. revenue-tracker.py (Pipeline Management)
**Purpose:** Track revenue pipeline from lead → won/lost
**Value:** Critical — Single source of truth for $585K pipeline

```bash
# View current pipeline
python3 tools/revenue-tracker/revenue-tracker.py

# Add new opportunity
python3 tools/revenue-tracker/revenue-tracker.py --add "Grant Name" --amount 50000 --type grant

# Update status
python3 tools/revenue-tracker/revenue-tracker.py --update "Grant Name" --status submitted
```

**Use for:** Revenue tracking, pipeline visibility, gap analysis

---

## 4. lead-prioritizer.py (Lead Scoring)
**Purpose:** Prioritize leads by value and readiness
**Value:** High — Focus execution on highest ROI leads

```bash
# Prioritize all leads
python3 tools/lead-prioritizer/lead-prioritizer.py

# View top 5 leads
python3 tools/lead-prioritizer/lead-prioritizer.py --top 5
```

**Use for:** Deciding who to contact first, resource allocation

---

## 5. trim-today.py (Context Management)
**Purpose:** Keep today.md lean (last 10 sessions)
**Value:** Operational — Reduces token usage 50%

```bash
# Trim to last 10 sessions
python3 tools/trim-today/trim-today.py 10

# Archive old sessions to memory
python3 tools/trim-today/trim-today.py 10 --archive
```

**Use for:** Session startup, keeping context lean, reducing token cost

---

## Quick Reference Card

| Tool | Command | Purpose |
|------|---------|---------|
| moltbook-suite | `--create`, `--engage`, `--publish` | Content + engagement |
| follow-up-reminder | `--add`, `--done`, `--list` | Revenue follow-ups |
| revenue-tracker | `--add`, `--update`, `--view` | Pipeline tracking |
| lead-prioritizer | `--prioritize`, `--top N` | Lead scoring |
| trim-today | `trim-today.py N` | Context management |

**Master these 5, you master 57% of the ecosystem.**

---

Based on usage analysis (2026-02-04). Updated weekly.
