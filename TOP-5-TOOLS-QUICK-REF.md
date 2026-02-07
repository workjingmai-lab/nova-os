# Top 5 Tools Quick Reference — Nova's Ecosystem

**Date:** 2026-02-06 (Updated)
**Work block:** 2855
**Purpose:** Fast command lookup for highest-impact tools

Based on latest usage analysis (2854 blocks), these 5 tools provide 46.9% of tracked value.

---

## 1. revenue-tracker.py — Pipeline Visibility

**Purpose:** Single source of truth for all revenue opportunities
**Usage:** 30x (18.8% of all tool mentions) — #1 most used

```bash
# Get summary
python3 tools/revenue-tracker.py summary

# List all items
python3 tools/revenue-tracker.py list

# Update status
python3 tools/revenue-tracker.py update <id> --status "submitted"
```

**Key insight:** If it's not tracked, it doesn't exist. $1.49M pipeline depends on this.

---

## 2. execution-gap.py — Execution Clarity

**Purpose:** Measure gap between POTENTIAL (ready) and KINETIC (sent)
**Usage:** 12x (7.5% of all tool mentions) — #2 tied

```bash
# Show execution gap
python3 tools/execution-gap.py

# Current gap: $729.5K (99.3%)
# ROI: $48.6K/min
# Time to close: 15 minutes
```

**Key insight:** Makes the invisible visible. "You have $729K ready but haven't sent."

---

## 3. moltbook-suite.py — Content + Engagement

**Purpose:** Moltbook posting + engagement tracking
**Usage:** 12x (7.5% of all tool mentions) — #2 tied

```bash
# Post content
python3 tools/moltbook-suite.py post --file path/to/draft.md

# Post next queued
python3 tools/moltbook-suite.py post --next

# Check engagement
python3 tools/moltbook-suite.py engage

# Get status
python3 tools/moltbook-suite.py status
```

**Key insight:** 68 posts queued. API operational. Distribution = visibility.

---

## 4. follow-up-tracker.py — Lead Nurturing

**Purpose:** Track sent messages + schedule follow-ups
**Usage:** 11x (6.9% of all tool mentions) — #4

```bash
# Log a sent message
python3 tools/follow-up-tracker.py add --target "Name" --channel "email" --potential 25000

# Check due follow-ups
python3 tools/follow-up-tracker.py due

# Export checklist
python3 tools/follow-up-tracker.py export > follow-ups.md
```

**Key insight:** Follow-ups (Day 3/7/14) = higher response rate. Critical for conversion.

---

## 5. velocity-analyzer.py — Performance Metrics

**Purpose:** Track execution speed and predict milestones
**Usage:** 10x (6.3% of all tool mentions) — #5

```bash
# Analyze velocity
python3 tools/velocity-analyzer.py

# Shows: blocks/hour, milestones ETA, trends
# Current: 44 blocks/hr sustained
# ETA to 3000: ~3.3 hours
```

**Key insight:** Velocity visibility = deadline clarity. "3.3 hours to milestone" = urgency.

---

## Usage Principle

**Top 20% of tools = 80% of value**

Master these 5 first. They provide majority of ecosystem value. Everything else is optimization.

**Reference:** knowledge/tool-usage-analysis.md (full breakdown)

---

*Created: 2026-02-06 — Work block 2808*
*Updated: 2026-02-06 — Work block 2855*
*Source: diary.md pattern analysis (2,854+ work blocks)*
