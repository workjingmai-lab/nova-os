# Quick 1-Minute Tasks (No Decision Fatigue)

**Created:** 2026-02-05 (Work block 1799)
**Purpose:** Instant task pick → execute → repeat
**Usage:** Pick ONE task. Execute. Document. Repeat.

---

## Revenue Pipeline Tasks

- [ ] Run `revenue-tracker.py summary` → Check pipeline status
- [ ] Run `follow-up-reminder.py check` → Check due follow-ups
- [ ] Run `lead-prioritizer.py` → Verify top priorities
- [ ] Review data/revenue-pipeline.json → Verify data integrity
- [ ] Count ready services → `grep -c '"status": "ready"' data/revenue-pipeline.json`

---

## Knowledge & Documentation Tasks

- [ ] Create knowledge article → Pick today's insight, write 500-1000 words
- [ ] Review diary.md → Extract patterns, create insight
- [ ] Update TOP-5-TOOLS-QUICK-REF.md → Add recent tool usage
- [ ] Read random knowledge article → Refresh memory
- [ ] Consolidate 2-3 related knowledge articles → Merge themes

---

## Moltbook Tasks

- [ ] Run `moltbook-suite.py monitor --check-feed` → Check new posts
- [ ] Run `moltbook-suite.py monitor --check-mentions` → Check mentions
- [ ] Run `moltbook-suite.py queue list` → Review queued content
- [ ] Run `moltbook-suite.py status` → Full Moltbook overview
- [ ] Read moltbook/published/ → Review past content patterns

---

## System & Tool Tasks

- [ ] Run `trim-today.py 10` → Keep last 10 sessions (reduce context bloat)
- [ ] Review tools/README.md → Pick random tool, test it
- [ ] Count knowledge articles → `ls knowledge/*.md | wc -l`
- [ ] Review outreach/messages/ → Count ready messages
- [ ] Check BLOCKER-SUMMARY-FOR-ARTHUR.md → Verify current blockers

---

## Analytics & Review Tasks

- [ ] Count today's work blocks → `grep "Work block" diary.md | wc -l`
- [ ] Calculate blocks/hour → (blocks ÷ hours worked)
- [ ] Review WEEK-3-EXECUTION-SUMMARY.md → Check alignment
- [ ] Scan diary.md for patterns → `grep "Insight:" diary.md | tail -20`
- [ ] Check goal progress → Review goals/active.md checkboxes

---

## Outreach & Revenue Tasks (Arthur-Dependent)

- [ ] Count ready service messages → Should be 13 ($375K)
- [ ] Verify grant submissions → `grep '"submitted"' data/revenue-pipeline.json`
- [ ] Review SERVICE-OUTREACH-QUICK-START.md → Refresh execution flow
- [ ] Check DAILY-REVENUE-CHECKLIST.md → Morning routine
- [ ] Read TOP-3-FOLLOW-UP-SCHEDULE.md → Refresh follow-up timing

---

## Random Pick (No Thinking)

- [ ] Pick random number 1-25 → Execute that task
- [ ] Set timer 60s → Complete ANY task before timer
- [ ] Close eyes → Point to screen → Execute that task
- [ ] Alphabet game → Pick task starting with A, then B, then C...

---

## Task Completion Template

After completing ANY task, document to diary.md:
```
### Work Block N — HH:MM UTC
**Task:** [One-line description]
**Action:** [What you did]
**Result:**
- [Key outcomes]
- [Metrics updated]
**Insight:** [What you learned]
**Stats:** N blocks today
**Duration:** ~1 min
```

---

## Principles

1. **Pick fast, execute fast** — No 5-minute task selection
2. **One task per block** — Don't multitask
3. **Document immediately** — diary.md is your memory
4. **Trust the system** — All tasks create value
5. **Small executions compound** — 1790 blocks = $880K pipeline

---

## When In Doubt

Default task: **`python3 tools/revenue-tracker.py summary`**

Why? It's the heartbeat of the entire system. 10 seconds, full pipeline visibility, validates all other work.

---

**File:** QUICK-1MIN-TASKS.md
**Size:** 3.1KB
**Purpose:** Eliminate decision fatigue. Execute. Repeat.
