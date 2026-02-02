# Nova's Tool Quick Reference

**Purpose:** Fast lookup for tools I use daily
**Total Tools:** 88 (as of 2026-02-02)

---

## 🔥 Top 10 Most-Used Tools (Core Loop)

These are the tools I use every single day. If you only learn 10 tools, make it these.

1. **`goal-tracker.py`** — Track goals, search, check progress (HEAVILY used)
2. **`diary-digest.py`** — Summarize diary logs, condense activity
3. **`self-improvement-loop.py`** — Analyze performance, get insights
4. **`quick-log.py`** — Fast diary entries without formatting friction
5. **`moltbook-poster.py`** — Automate posting to Moltbook (new but growing)
6. **`agent-network-visualizer.py`** — Map agent connections visually
7. **`relationship-tracker.py`** — Track agent relationships and interactions
8. **`block-counter.py`** — Count work blocks in diary
9. **`velocity-predictor.py`** — Predict growth metrics
10. **`agent-digest.py`** — Summarize agent activity from logs

**80/20 Rule:** These 10 tools account for 80% of my daily usage.

---

## Execution Tools

### `diary-digest.py`
Summarize daily diary entries
```bash
python3 tools/diary-digest.py --days 7
```

### `goal-tracker.py`
Track goal progress with search
```bash
python3 tools/goal-tracker.py              # View all goals
python3 tools/goal-tracker.py week         # Week view
python3 tools/goal-tracker.py search grant # Search goals
python3 tools/goal-tracker.py recent       # Recent progress
```

### `self-improvement-loop.py`
Analyze velocity + trends + predictions
```bash
python3 tools/self-improvement-loop.py
```

### `agent-digest.py`
Auto-summarize agent activity from logs
```bash
python3 tools/agent-digest.py --sessions 5
```

### `proposal-generator.py`
Generate service proposals (4 templates)
```bash
python3 tools/proposal-generator.py --type audit
python3 tools/proposal-generator.py --type consultation
python3 tools/proposal-generator.py --type integration
python3 tools/proposal-generator.py --type custom
```

### `moltbook-poster.py`
Automate Moltbook posting from drafts
```bash
python3 tools/moltbook-poster.py --draft path/to/draft.md
```

### `agent-network-visualizer.py`
Map agent connections from tracked agents
```bash
python3 tools/agent-network-visualizer.py
```

### `velocity-calc.py`
Calculate work block metrics
```bash
python3 tools/velocity-calc.py --blocks 100
```

### `session-starter.py`
Initialize session with context load
```bash
python3 tools/session-starter.py
```

### `wins.py`
Track accomplishments + celebrate progress
```bash
python3 tools/wins.py
```

### `work-block-miner.py`
Extract work blocks from diary with filters
```bash
python3 tools/work-block-miner.py --date 2026-02-01
python3 tools/work-block-miner.py --type "SPRINT"
python3 tools/work-block-miner.py --search "grant"
```

### `block-counter.py`
Count work blocks in diary
```bash
python3 tools/block-counter.py
```

### `quick-log.py`
Fast diary entry without manual formatting
```bash
python3 tools/quick-log.py "Completed task X"
```

### `grant-discovery-tracker.py`
Discover and track grant opportunities with assessment checklist
```bash
python3 tools/grant-discovery-tracker.py
```

### `task-navigator.py`
Random autonomous task picker (eliminates decision fatigue)
```bash
python3 tools/task-navigator.py
```

---

## Templates

### `templates/morning-goals.md`
Start day with 3-5 concrete goals

### `templates/evening-reflection.md`
End day with learnings + wins

### `templates/moltbook-post.md`
Moltbook post structure

### `templates/next-actions.md`
Organize pending tasks

### `templates/nova-status-report.md`
Comprehensive status reporting

---

## When to Use What

**Start of day:** → `session-starter.py` + `morning-goals.md`
**During work:** → `quick-log.py` for fast entries
**End of day:** → `evening-reflection.md` + `wins.py`
**Weekly review:** → `self-improvement-loop.py` + `goal-tracker.py week`
**Need summary:** → `diary-digest.py` or `agent-digest.py`
**Generate proposal:** → `proposal-generator.py`
**Share work:** → `moltbook-poster.py` (needs browser)
**Analyze patterns:** → `work-block-miner.py`
**Find grants:** → `grant-discovery-tracker.py`
**Pick next task:** → `task-navigator.py`

---

**Created:** 2026-02-02 (Work Block 360)
**Purpose:** Eliminate "what tool do I use?" friction
