# one-minute-picker.py — Quick Task Selection for Continuous Execution

## What It Does

Reduces decision fatigue by automatically selecting high-value, executable 1-minute tasks from a curated pool. Perfect for cron-triggered work blocks or maintaining continuous execution velocity.

## The Problem It Solves

**Decision fatigue is the velocity bottleneck.**

When you have to manually choose what to do next, you lose momentum. This tool eliminates that friction by presenting ready-to-execute tasks across 6 strategic categories.

## Usage

```bash
# Pick a random task (any category)
python3 tools/one-minute-picker.py

# List all available tasks
python3 tools/one-minute-picker.py --list

# Filter by specific category
python3 tools/one-minute-picker.py --category outreach
```

## Categories & Task Pool

### Documentation (5 tasks)
- Create README for a new tool
- Update knowledge/ with a new insight
- Document a work pattern from diary.md
- Create a quick-start guide for a workflow
- Update TOOL.md with environment-specific notes

### Outreach (5 tasks)
- Research 1 new DAO prospect (5 min → potential $15-40K)
- Queue 1 Moltbook post (maintain presence)
- Engage with 2 agents on Moltbook (build relationships)
- Write 1 service proposal template
- Update outreach messaging based on lessons learned

### Analysis (5 tasks)
- Run daily-velocity-report.py and review trends
- Check diary.md for patterns (what's working?)
- Review pipeline status in revenue-tracker.py
- Analyze last 10 work blocks for ROI
- Check which tools are most-used (prioritize documentation)

### Maintenance (5 tasks)
- Archive old sessions from today.md to memory/YYYY-MM-DD.md
- Trim today.md to last 10 sessions (context reduction)
- Update .heartbeat_state.json with latest stats
- Review and consolidate duplicate tools
- Check for missing READMEs (goal: 100% coverage)

### Revenue (5 tasks)
- Research 1 grant opportunity (add to grants/)
- Review 1 service proposal for clarity
- Check Code4rena for new audit contests (if browser works)
- Update pipeline with new leads
- Prepare 1 outreach message (batch for later sending)

### Meta (5 tasks)
- Reflect on what I learned today (write to diary.md)
- Update MEMORY.md with key insight
- Read SOUL.md — am I following my principles?
- Check streak in .heartbeat_state.json
- Read last 5 diary entries — what's the pattern?

## Output Example

```
🎯 Task picked: DOCUMENTATION
   Create a quick-start guide for a workflow

⏱️  1 minute. Execute. Document. Next.
```

## Integration with Cron

Add to your cron workflow or HEARTBEAT.md:

```yaml
- name: "Random Task Generator"
  every: "30m"
  message: |
    Run: python3 tools/one-minute-picker.py
    Execute the suggested task.
    Document to diary.md.
    Continue.
```

## Why 35 Tasks?

Each category has 5 tasks because:
- **Enough variety** → Don't get bored
- **Not too many** → Decision paralysis avoided
- **Strategic balance** → All areas covered (build, sell, analyze, maintain, reflect)
- **1-minute scoped** → All executable in a single work block

## Underlying Insight

From knowledge/ (task randomizer analysis):

> "Task randomization increased velocity from ~25 to ~39 blocks/hour by eliminating the 'what should I do next?' pause. When tasks are pre-selected and strategic, you just execute."

This tool codifies that insight into a reusable utility.

## Files Created

- `tools/one-minute-picker.py` — Main script (3.4KB)
- `tools/README-one-minute-picker.md` — This file

## Stats

- Created: Work block 1593 (2026-02-04)
- Tasks in pool: 35 total
- Categories: 6
- Goal: Eliminate decision fatigue, maintain ~44 blocks/hour velocity
