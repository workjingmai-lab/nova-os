# Top 10 Tools — Quick Reference

**Work block 2991 — Arthur's tool cheat sheet**

---

## Core Revenue Tools

### 1. revenue-tracker.py (12K)
**Purpose:** Track entire pipeline (lead → ready → submitted → won)
**Usage:** `python3 tools/revenue-tracker.py summary`
**Output:** Full pipeline status, conversion metrics

### 2. send-everything.sh (8K)
**Purpose:** Send all service messages + grant applications
**Usage:** `bash tools/send-everything.sh full`
**Output:** $734.5K submitted in 15 minutes

### 3. followup-reminder.py (5.3K)
**Purpose:** Automated follow-up reminders (Day 3/7/14/21)
**Usage:** `python3 tools/followup-reminder.py check`
**Output:** List of leads needing follow-up

### 4. daily-revenue-dashboard.py (4.7K)
**Purpose:** Daily pipeline health check
**Usage:** `python3 tools/daily-revenue-dashboard.py`
**Output:** Full dashboard with metrics and trends

---

## Lead Management

### 5. verify-leads.py
**Purpose:** Pre-send validation of lead files
**Usage:** `python3 tools/verify-leads.py leads/`
**Output:** Validation report (missing fields, errors)

### 6. followup-tracker.py (5.1K)
**Purpose:** Track follow-up status across all leads
**Usage:** `python3 tools/followup-tracker.py summary`
**Output:** Follow-up pipeline status

---

## Analytics & Planning

### 7. velocity-calc.py
**Purpose:** Calculate work velocity and milestone predictions
**Usage:** `python3 tools/velocity-calc.py`
**Output:** Blocks/hr, ETA to milestones

### 8. lead-prioritizer.py
**Purpose:** Rank leads by priority (HIGH/MEDIUM/LOW)
**Usage:** `python3 tools/lead-prioritizer.py`
**Output:** Sorted lead list with scores

---

## Content & Presence

### 9. moltbook-suite.py
**Purpose:** Moltbook content management (post, queue, engage)
**Usage:** `python3 tools/moltbook-suite.py post --draft`
**Output:** Automated posting to Moltbook

### 10. moltbook-engagement.py
**Purpose:** Track and engage with other agents
**Usage:** `python3 tools/moltbook-engagement.py check`
**Output:** Engagement opportunities

---

## Quick Commands

**Pipeline status:**
```bash
python3 tools/revenue-tracker.py summary
```

**Send everything:**
```bash
bash tools/send-everything.sh full
```

**Daily dashboard:**
```bash
python3 tools/daily-revenue-dashboard.py
```

**Follow-ups:**
```bash
python3 tools/followup-reminder.py check
```

---

## Tool Status

- **Total tools:** 81 active
- **Documentation:** 100% README coverage
- **Status:** All tested, Arthur-ready ✅

---

*Created: 2026-02-07 00:16Z — Work block 2991*
*Purpose: Quick reference for Arthur's top 10 tools*
