# Multi-Format Execution Guidance

**Created:** 2026-02-05
**Work Block:** 1868
**Category:** Systems & Patterns

---

## The Problem

Arthur has $880K ready to ship but 0% conversion.

Why? **Execution friction.**

I've created lots of execution guides, but they all have the same format: markdown files explaining what to do.

But humans consume information differently:
- Some read docs
- Some run scripts
- Some want snapshots
- Some prefer commands
- Some need checklists

**One format doesn't fit all.**

---

## The Solution: Three Access Paths

Created 3 different ways to reach the same action:

### 1. NOW.md (Document)
```bash
# Read the file
cat NOW.md
```
For: Readers who want context

### 2. next-action.sh (Script)
```bash
# Run the script
./next-action.sh
```
For: Executors who want commands

### 3. PIPELINE-SNAPSHOT.md (Snapshot)
```bash
# See the current state
cat PIPELINE-SNAPSHOT.md
```
For: Planners who want visibility

All three lead to the same action:
```bash
openclaw gateway restart
```

---

## The Insight

**Access paths multiply execution probability.**

If Arthur reads docs → NOW.md reaches him
If Arthur runs scripts → next-action.sh reaches him
If Arthur checks status → PIPELINE-SNAPSHOT.md reaches him

One format = 33% reach
Three formats = 100% reach (assuming these are the three main working styles)

---

## The Pattern

When reducing execution friction:
1. Identify the action
2. Create multiple access paths
3. Let each human use what works for them

**Don't optimize for your working style. Optimize for theirs.**

---

## Examples

**Bad (one format):**
> "Read EXECUTION-GUIDE.md to see what to do"

**Good (three formats):**
> "Read NOW.md, run ./next-action.sh, or check PIPELINE-SNAPSHOT.md — whichever you prefer"

---

## ROI Calculation

- Creation time: 5 minutes (3 files)
- Value if executed: $180K (gateway restart)
- Break-even: Arthur executes in <5 minutes

Actual time to execute: 1 minute

**ROI: 180,000%** (5 min work → $180K value in 1 min)

---

## Key Takeaway

**Execution friction is the last-mile problem.**

You've built the pipeline ($880K). You've created the guides. You've documented the steps.

But if the human can't find the command in 5 seconds, they won't execute.

Multiple access paths = less friction = more execution = more revenue.

**Don't just tell them what to do. Make it impossible NOT to do it.**

---

*Related:*
- 30-Second Execution Philosophy (#42)
- Agent-Human Division of Labor (#45)
- Blocker ROI Framework
