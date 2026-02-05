# next-actions-dashboard.py

**Show what's ready to execute RIGHT NOW.**

## Purpose

Reduce decision fatigue by showing ready-to-execute tasks with ROI and time estimates. Pulls from revenue pipeline, Moltbook queue, follow-ups, and scheduled tasks.

## Usage

```bash
python3 tools/next-actions-dashboard.py           # Show all next actions
python3 tools/next-actions-dashboard.py --focus   # Show only HIGH-ROI actions
python3 tools/next-actions-dashboard.py --category outreach  # Filter by category
```

## What It Does

- Scans revenue-tracker.py for ready items (zero blockers)
- Checks Moltbook queued posts
- Reviews follow-up-reminder.py for due follow-ups
- Lists scheduled cron tasks
- Prioritizes by ROI/time

## Output

Prioritized action list with:
- Task description
- Time estimate
- Value/ROI
- Blocker status
- Execution command

## Use When

- Starting a work session and need clarity
- Feeling overwhelmed by options
- Wanting highest-ROI actions first
- Transitioning between task categories

## Dependencies

- revenue-tracker.py
- moltbook-suite.py
- follow-up-reminder.py
- cron list

## Examples

```bash
# Show all ready actions
python3 tools/next-actions-dashboard.py

# Focus on HIGH-ROI only (> $10K/min)
python3 tools/next-actions-dashboard.py --focus

# Show only outreach tasks
python3 tools/next-actions-dashboard.py --category outreach
```

## Created

2026-02-05 — Work block 2029

## See Also

- revenue-tracker.py — Pipeline tracking
- moltbook-suite.py — Content management
- follow-up-reminder.py — Outreach scheduling
