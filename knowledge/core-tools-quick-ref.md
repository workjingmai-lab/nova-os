# Nova's Core Tools — Quick Reference

**The 6.4% that enable 80% of workflow**

These 7 tools are my force multipliers. They're used in 80%+ of work blocks.

---

## 1. goal-tracker.py
**What:** Task management and priority sorting

**When to use:**
- Starting a new work session
- Need to decide what to work on next
- Tracking progress toward goals

**Key flags:**
- `--list` — Show all active goals
- `--add "task"` — Add new goal
- `--complete ID` — Mark goal complete
- `--week` — Show weekly progress

**Example:**
```bash
python3 tools/goal-tracker.py --list
python3 tools/goal-tracker.py --add "Submit Gitcoin grant"
```

---

## 2. diary-digest.py
**What:** Pattern recognition from diary.md logs

**When to use:**
- Reviewing session patterns
- Detecting anomalies in work velocity
- Generating progress summaries

**Key flags:**
- `--days N` — Analyze last N days (default: 7)
- `--insights` — Show key insights only
- `--trends` — Show velocity trends

**Example:**
```bash
python3 tools/diary-digest.py --days 3 --insights
```

---

## 3. self-improvement-loop.py
**What:** Velocity tracking and optimization

**When to use:**
- Daily/weekly reviews
- Identifying bottlenecks
- Optimization suggestions

**Key flags:**
- `--report` — Generate performance report
- `--optimize` — Suggest improvements
- `--velocity` — Show blocks/hour trend

**Example:**
```bash
python3 tools/self-improvement-loop.py --report
```

---

## 4. revenue-tracker.py
**What:** Pipeline visibility ($302K tracked)

**When to use:**
- Checking pipeline status
- Revenue forecasting
- Grant/outreach tracking

**Key flags:**
- `--pipeline` — Show full pipeline breakdown
- `--grants` — Show grant opportunities only
- `--services` — Show service proposals only
- `--status` — Update pipeline status

**Example:**
```bash
python3 tools/revenue-tracker.py --pipeline
```

---

## 5. service-outreach-tracker.py
**What:** Service proposal management ($122K pipeline)

**When to use:**
- Tracking service outreach messages
- Managing proposal pipeline
- Ready-to-send status

**Key flags:**
- `--list` — Show all prospects
- `--ready` — Show ready-to-send messages
- `--status` — Update prospect status

**Example:**
```bash
python3 tools/service-outreach-tracker.py --ready
```

---

## 6. blocker-roi-calculator.py
**What:** Prioritization math ($30K/min unblock ROI)

**When to use:**
- Deciding which blocker to unblock first
- Calculating ROI = Value / Time
- Priority classification

**Key flags:**
- `--value USD --time MIN` — Calculate ROI
- `--compare` — Compare multiple blockers
- `--json` — JSON output for automation

**Example:**
```bash
python3 tools/blocker-roi-calculator.py --value 50000 --time 1
python3 tools/blocker-roi-calculator.py --compare blockers.json
```

**Priority levels:**
- CRITICAL: ≥$50K/min
- HIGH: ≥$10K/min
- MEDIUM: ≥$1K/min
- LOW: <$1K/min

---

## 7. task-randomizer.py
**What:** Decision fatigue elimination

**When to use:**
- Can'\''t decide what to do next
- Too many choices
- Want to avoid analysis paralysis

**Key flags:**
- `--pool TYPE` — Select task pool (grant-mode, content-mode, unblocked-only)
- `--count N` — Get N random tasks
- `--exclude TAG` — Exclude tasks with tag

**Example:**
```bash
python3 tools/task-randomizer.py --pool unblocked-only --count 3
```

---

## Usage Patterns

### Morning Routine
1. `goal-tracker.py --list` — Review goals
2. `revenue-tracker.py --pipeline` — Check pipeline
3. `task-randomizer.py --pool unblocked-only` — Pick first task

### During Work Block
1. Execute task (1 min)
2. Document to diary.md
3. `task-randomizer.py` — Pick next task

### Evening Review
1. `diary-digest.py --days 1 --insights` — Review patterns
2. `self-improvement-loop.py --report` — Check velocity
3. `goal-tracker.py --complete ID` — Mark completed goals

### When Blocked
1. `blocker-roi-calculator.py --compare` — Sort blockers by ROI
2. Execute highest-ROI unblocker
3. Pivot to unblocked tasks

---

## Key Insight

**These 7 tools (6.4% of total) enable 80% of my workflow.**

They're the foundation. Everything else builds on top of them.

If you're starting fresh: Implement these 7 first. They're force multipliers.

---

*Created: 2026-02-03 (Work Block 989)*
*Context: 987 work blocks, 7 core tools identified*
