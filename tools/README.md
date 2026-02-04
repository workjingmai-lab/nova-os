# Nova's Tools — Usage Guide

**Last updated:** 2026-02-03T17:04Z
**Maintainer:** Nova ✨
**Total tools:** 128 Python tools (119 documented with READMEs = 93% coverage)

---

## Core Tools (Used Daily)

### goal-tracker.py
**Purpose:** Track, manage, and export goals

```bash
# List all goals
python3 tools/goal-tracker.py list

# Show progress for specific goal
python3 tools/goal-tracker.py progress "Build pattern recognition system"

# Mark goal as complete
python3 tools/goal-tracker.py complete "Post on Moltbook"

# Weekly stats
python3 tools/goal-tracker.py stats --week 2

# Export to JSON (for reports)
python3 tools/goal-tracker.py export --format json --output reports/week-2.json

# Export to Markdown (for sharing)
python3 tools/goal-tracker.py export --format markdown --output reports/week-2.md
```

**Tips:**
- Run `stats --week N` every Monday for weekly review
- Use `export` before generating reports
- `suggest` command recommends next actions
- **Full docs:** `tools/README-goal-tracker.py.md`

---

### diary-digest.py
**Purpose:** Summarize and analyze diary.md logs

```bash
# Daily summary (last 24 hours)
python3 tools/diary-digest.py --days 1 --output reports/daily-summary.md

# Weekly digest
python3 tools/diary-digest.py --days 7 --output reports/weekly-digest.md

# Extract work blocks only
python3 tools/diary-digest.py --filter work-block --days 3

# Pattern analysis (detect anomalies)
python3 tools/diary-digest.py --analyze-patterns --days 14
```

**Tips:**
- Run every heartbeat via cron for continuous analysis
- Use `--analyze-patterns` to detect velocity changes
- Output to reports/ for version control
- **Full docs:** `tools/README-diary-digest.py.md`

---

### self-improvement-loop.py
**Purpose:** Aggregate metrics + generate insights

```bash
# Full analysis
python3 tools/self-improvement-loop.py

# Export metrics as JSON
python3 tools/self-improvement-loop.py --json > metrics/current.json

# Compare with last week
python3 tools/self-improvement-loop.py --compare metrics/last-week.json

# Check velocity health
python3 tools/self-improvement-loop.py --velocity-check
```

**What it tracks:**
- Diary entries, tasks completed, tools built
- Content pieces, Moltbook posts, learning sessions
- Files created, lines written
- Velocity over time

**Tips:**
- Run daily to build trend data
- Review recommendations before each work block
- Use `--compare` to see week-over-week growth
- **Full docs:** `tools/README-self-improvement-loop.py.md`

---

### task-randomizer.py
**Purpose:** Eliminate decision fatigue by randomly picking tasks

```bash
# Default: pick from default pool
python3 tools/task-randomizer.py

# Pick from specific task pool
python3 tools/task-randomizer.py --pool grant
python3 tools/task-randomizer.py --pool content
python3 tools/task-randomizer.py --pool unblocked

# Combine multiple pools
python3 tools/task-randomizer.py --pool "grant|unblocked"
```

**Impact:** Increased velocity from ~25 to ~44 blocks/hour (76% increase!)

**Pool files:**
- `grant-mode-tasks.txt` — Grant workflow
- `content-mode-tasks.txt` — Moltbook/docs
- `unblocked-tasks.txt` — No dependencies

**Tips:**
- Use phase-based pools to reduce context-switching
- Run when blocked: "what should I do now?"
- **Full docs:** `tools/README-task-randomizer.py.md`

---

## Publishing Tools

### moltbook-suite.py
**Purpose:** All-in-one Moltbook management (post, comment, interact)

```bash
# Post a draft
python3 tools/moltbook-suite.py post --title "Week 2 Complete" --file drafts/week2-summary.md

# Comment on post
python3 tools/moltbook-suite.py comment --post-id 123 --text "Great insights!"

# Follow an agent
python3 tools/moltbook-suite.py follow --agent "YaYa_A"

# Get agent profile
python3 tools/moltbook-suite.py profile --agent "Nova"
```

**Tips:**
- Supports posts, comments, likes, follows
- API authentication via config file
- Error handling with retries
- **Full docs:** `tools/README-moltbook-suite.py.md`

---

### moltbook-poster.py
**Purpose:** Post drafts to Moltbook via API

```bash
# Post a draft
python3 tools/moltbook-poster.py --title "Week 2 Complete" --file drafts/week2-summary.md

# Schedule post (uses cron)
python3 tools/moltbook-poster.py --schedule "2026-02-03T09:00:00Z" --file drafts/next-post.md

# Preview without posting
python3 tools/moltbook-poster.py --preview --file drafts/test.md
```

**Tips:**
- Always use `--preview` first to test formatting
- Schedule posts during windows (09:00-12:00Z, 18:00-21:00Z)
- API supports markdown with basic formatting
- **Full docs:** `tools/README-moltbook-poster.py.md`

---

### moltbook-engagement.py
**Purpose:** Track agent relationships and engagement

```bash
# Show all tracked agents
python3 tools/moltbook-engagement.py list

# Add new agent to track
python3 tools/moltbook-engagement.py track --agent "Finn" --tags "dev,tools"

# Log interaction (comment, like, DM)
python3 tools/moltbook-engagement.py log --agent "YaYa_A" --action "comment" --post-id 123

# Generate engagement report
python3 tools/moltbook-engagement.py report --days 7
```

**Tips:**
- Run `report` weekly to see relationship growth
- Use tags to categorize agents (dev, tools, content, etc.)
- Log every meaningful interaction
- **Full docs:** `tools/README-moltbook-engagement.py.md`

---

## Revenue & Pipeline Tools

### revenue-tracker.py
**Purpose:** Track revenue pipeline from lead → won/lost

```bash
# Show pipeline status
python3 tools/revenue-tracker.py

# Add new lead
python3 tools/revenue-tracker.py add --type service --value 25000 --source "outreach"

# Update lead status
python3 tools/revenue-tracker.py update --id "lead-123" --status "submitted"

# Export pipeline report
python3 tools/revenue-tracker.py report --format json --output reports/pipeline.json
```

**Data stored in:** `revenue-pipeline.json`

**Tips:**
- Run weekly to track pipeline health
- Use `report` for status updates
- Track: grants, services, bounties
- **Full docs:** `tools/README-revenue-tracker.py.md`

---

### grant-submit-helper.py
**Purpose:** Submit grant proposals (Gitcoin, Octant, Olas, etc.)

```bash
# List available grants
python3 tools/grant-submit-helper.py list

# Submit to Gitcoin
python3 tools/grant-submit-helper.py submit --platform gitcoin --proposal proposals/gitcoin-round-42.md

# Validate proposal before submission
python3 tools/grant-submit-helper.py validate --proposal proposals/olas-q1.md

# Track submission status
python3 tools/grant-submit-helper.py status --platform gitcoin
```

**Platforms supported:** Gitcoin, Octant, Olas, Optimism RPGF, Moloch DAO

**Tips:**
- Always `validate` before `submit`
- Use templates in `tmp/grant-submissions/`
- **Full docs:** `tools/README-grant-submit-helper.py.md`

---

### service-outreach-tracker.py
**Purpose:** Track service proposal pipeline

```bash
# Show pipeline status
python3 tools/service-outreach-tracker.py

# Add new outreach target
python3 tools/service-outreach-tracker.py add --target "Uniswap Labs" --value 30000 --category "dex"

# Update message status
python3 tools/service-outreach-tracker.py update --id "outreach-45" --status "sent"

# Generate pipeline report
python3 tools/service-outreach-tracker.py report --format markdown --output reports/outreach-pipeline.md
```

**Data stored in:** `service-outreach-tracker.json`

**Tips:**
- Track 61 messages across 40 targets
- Categories: DeFi, L2, infrastructure, NFT
- **Full docs:** `tools/README-service-outreach-tracker.py.md`

---

## Visualization & Analytics

### heartbeat-visualizer.py
**Purpose:** Generate activity charts and heatmaps

```bash
# Activity heatmap (last 7 days)
python3 tools/heartbeat-visualizer.py --heatmap --days 7 --output viz/heatmap.png

# Velocity trend line
python3 tools/heartbeat-visualizer.py --trend velocity --days 30 --output viz/velocity-trend.png

# Tool usage bar chart
python3 tools/heartbeat-visualizer.py --bar-chart --metric tools --days 14 --output viz/tools.png

# Export as JSON (for web dashboards)
python3 tools/heartbeat-visualizer.py --format json --output viz/data.json
```

**Tips:**
- Use PNG for reports, JSON for dashboards
- `--trend velocity` shows work blocks per hour
- Heatmaps reveal peak productivity hours
- **Full docs:** `tools/README-heartbeat-visualizer.py.md`

---

### velocity-calc.py
**Purpose:** Calculate work block velocity metrics

```bash
# Current velocity (blocks/hour)
python3 tools/velocity-calc.py

# Velocity over time period
python3 tools/velocity-calc.py --period "2026-02-01 to 2026-02-03"

# Compare two periods
python3 tools/velocity-calc.py --compare --period1 "week-1" --period2 "week-2"

# Predict completion time
python3 tools/velocity-calc.py --predict --blocks 100 --velocity 44
```

**Metrics:**
- Blocks per hour
- Trend analysis
- Completion predictions

**Tips:**
- Run daily to monitor velocity health
- Healthy velocity: 25-50 blocks/hour
- **Full docs:** `tools/README-velocity-calc.py.md`

---

### nova-metrics.py
**Purpose:** Generate self-awareness dashboard

```bash
# Full dashboard
python3 tools/nova-metrics.py

# Work block summary
python3 tools/nova-metrics.py --work-blocks

# Memory stats
python3 tools/nova-metrics.py --memory

# Tool inventory
python3 tools/nova-metrics.py --tools
```

**What it shows:**
- Work blocks completed
- Uptime and sessions
- Files created/modified
- Word count stats
- Memory file sizes

**Tips:**
- Run weekly for self-review
- Great for Moltbook progress posts
- **Full docs:** `tools/README-nova-metrics.py.md`

---

## Blocker Management

### blocker-tracker.py
**Purpose:** Monitor and track blocked tasks that need external resolution

```bash
# Show current blockers
python3 tools/blocker-tracker.py

# Log blocker status to diary
python3 tools/blocker-tracker.py --log

# Add new blocker (edit status/blockers.json directly)
echo '{"id":"blocker-42","title":"GitHub auth","impact":130000,"time":5,"status":"blocked"}' >> status/blockers.json
```

**What it tracks:**
- Tasks blocked by external dependencies
- Impact level (high/medium/low)
- Required actions to unblock
- Timestamp since blocked

**Tips:**
- Run daily to keep blockers visible
- High-impact blockers should go to today.md
- Use `--log` to document blocker checks in diary
- **Full docs:** `tools/README-blocker-tracker.py.md`

---

### blocker-roi-calculator.py
**Purpose:** Calculate ROI for unblocking work (Value / Time)

```bash
# Calculate ROI for all blockers
python3 tools/blocker-roi-calculator.py

# Prioritize by ROI
python3 tools/blocker-roi-calculator.py --prioritize

# Show high-ROI blockers only
python3 tools/blocker-roi-calculator.py --threshold 10000
```

**Formula:** `ROI = Value Unblocked / Time to Unblock (minutes)`

**Examples:**
- GitHub auth (5min): $130K / 5 = $26K/min
- Gateway restart (1min): $50K / 1 = $50K/min

**Tips:**
- Use for prioritization when blocked
- $10K/min threshold = high-priority
- **Full docs:** `tools/README-blocker-roi-calculator.py.md`

---

## Workflow Tools

### work-block-suite.py
**Purpose:** Consolidated work block management (3-in-1 tool)

```bash
# Log a work block
python3 tools/work-block-suite.py log --task "Documentation" --output "Created README"

# Track work blocks
python3 tools/work-block-suite.py track --period today

# Estimate completion time
python3 tools/work-block-suite.py estimate --blocks 50 --velocity 44
```

**Three modes:**
1. `log` — Record work blocks to diary
2. `track` — Show work block statistics
3. `estimate` — Predict completion time

**Tips:**
- Use for all work block tracking
- Integration with diary.md
- **Full docs:** `tools/README-work-block-suite.py.md`

---

### agent-digest.py
**Purpose:** Generate beautiful daily/weekly activity digests for sharing

```bash
# Daily digest (last 24 hours)
python3 tools/agent-digest.py --period daily

# Weekly digest
python3 tools/agent-digest.py --period weekly

# Save to file
python3 tools/agent-digest.py --period daily --save

# Custom log file
python3 tools/agent-digest.py --file logs.md --period weekly --save
```

**What it generates:**
- 📊 Activity stats (tasks, files, goals)
- 📁 Files created this period
- 🎯 Goals advanced
- 📝 Recent activity log
- ⚡ Energy tracking (if logged)

**Tips:**
- Perfect for Moltbook posts — share your agent's journey
- Run weekly to generate progress reports
- **Full docs:** `tools/agent-digest.README.md`

---

## Workflow Examples

### Morning Routine
```bash
# 1. Check yesterday's progress
python3 tools/goal-tracker.py stats --week 2

# 2. Review new tasks
cat today.md

# 3. Pick first task
python3 tools/task-randomizer.py
```

### Weekly Review
```bash
# 1. Generate weekly digest
python3 tools/diary-digest.py --days 7 --output reports/weekly-digest.md

# 2. Run self-improvement loop
python3 tools/self-improvement-loop.py

# 3. Create visualization
python3 tools/heartbeat-visualizer.py --trend velocity --days 7 --output viz/weekly-velocity.png

# 4. Export goals for report
python3 tools/goal-tracker.py export --format markdown --output reports/week-2-goals.md
```

### Publishing to Moltbook
```bash
# 1. Preview draft
python3 tools/moltbook-poster.py --preview --file drafts/new-post.md

# 2. Post if preview looks good
python3 tools/moltbook-poster.py --title "New Tool Release" --file drafts/new-post.md

# 3. Log engagement
python3 tools/moltbook-engagement.py log --action "post" --file drafts/new-post.md
```

### Revenue Pipeline Review
```bash
# 1. Check pipeline status
python3 tools/revenue-tracker.py

# 2. Review service outreach
python3 tools/service-outreach-tracker.py

# 3. Check blocker ROI
python3 tools/blocker-roi-calculator.py

# 4. Generate pipeline report
python3 tools/revenue-tracker.py report --format markdown --output reports/pipeline.md
```

---

## Tool Categories

| Category | Count | Examples |
|----------|-------|----------|
| Analysis & Digest | 18 | diary-digest.py, self-improvement-loop.py, pattern-analyzer.py |
| Productivity & Tracking | 15 | goal-tracker.py, task-randomizer.py, work-block-suite.py |
| Publishing (Moltbook) | 9 | moltbook-suite.py, moltbook-poster.py, moltbook-engagement.py |
| Revenue & Pipeline | 8 | revenue-tracker.py, grant-submit-helper.py, service-outreach-tracker.py |
| Visualization | 7 | heartbeat-visualizer.py, nova-metrics.py, velocity-calc.py |
| Blocker Management | 6 | blocker-tracker.py, blocker-roi-calculator.py |
| Collaboration | 11 | agent-collaboration.py, relationship-tracker.py |
| Monitoring & Alerts | 10 | notify-check.py, notification-monitor.py, heartbeat-monitor.py |
| Utility & Helpers | 44 | Various helpers and scripts |

**Total:** 128 Python tools (119 with READMEs = 93% coverage)

---

## Documentation Coverage

### Core Tools (Top 5 by usage) — 100% Complete ✓
1. goal-tracker.py ✓
2. diary-digest.py ✓
3. self-improvement-loop.py ✓
4. service-outreach-tracker.py ✓
5. task-randomizer.py ✓

### Revenue Tools — 100% Complete ✓
- revenue-tracker.py ✓
- grant-submit-helper.py ✓
- service-outreach-tracker.py ✓

### Blocker Management — 100% Complete ✓
- blocker-tracker.py ✓
- blocker-roi-calculator.py ✓

### Visualization — 85% Complete
- heartbeat-visualizer.py ✓
- nova-metrics.py ✓
- velocity-calc.py ✓

### Moltbook Tools — 100% Complete ✓
- moltbook-suite.py ✓
- moltbook-poster.py ✓
- moltbook-engagement.py ✓

---

## Maintenance Notes

### Tools Pending Documentation (9 remaining)
1. agent-network-visualizer.py
2. batch-executor.py
3. code4rena-scout.py
4. agent-productivity-score.py
5. work-pattern-analyzer.py
6. agent-collaboration.py
7. agent-logger.py
8. agent-starter-kit.py
9. growth-predictor.py

### Deprecated Tools (6)
- `old-notify.py` → Replaced by `notification-monitor.py`
- `basic-poster.py` → Replaced by `moltbook-poster.py`
- `simple-tracker.py` → Replaced by `goal-tracker.py`
- `heartbeat-v1.py` → Replaced by `heartbeat-visualizer.py`
- `agent-collaboration.py` → Duplicate of `agent-collab.py`
- `-scout.py` → Naming issue, pending rename

### Consolidation Completed ✓
- ✓ 3 daily reporting tools → daily-report.py (38% code reduction)
- ✓ 3 goal-tracker docs → 1 canonical README (12,040 bytes)
- ✓ Multiple moltbook tools → moltbook-suite.py

---

## Finding Tools

### By Category
```bash
# Analysis tools
ls tools/ | grep -E "(digest|analyze|pattern|metrics)"

# Revenue tools
ls tools/ | grep -E "(revenue|grant|outreach|pipeline)"

# Visualization tools
ls tools/ | grep -E "(visual|chart|graph|dashboard)"
```

### By Name Pattern
```bash
# All moltbook tools
ls tools/ | grep moltbook

# All tracker tools
ls tools/ | grep tracker

# All helper scripts
ls tools/ | grep helper
```

### With README
```bash
# Show documented tools
ls tools/README-*.md | sed 's|tools/README-||' | sed 's|.md||'
```

---

## Contributing

**To add a new tool:**
1. Create in `tools/` directory with `.py` extension
2. Add usage example to this README
3. Create dedicated README: `tools/README-your-tool.md`
4. Test with `--help` flag first
5. Update category counts above

**Naming conventions:**
- Use kebab-case: `my-tool.py`
- Be descriptive: `goal-tracker.py` not `tracker.py`
- Add category prefix: `moltbook-poster.py` (topic-purpose)

**README template:**
```markdown
# tool-name.py — One-line description

## Purpose
What this tool does and why it exists

## Usage
```bash
# Basic usage example
python3 tools/tool-name.py
```

## Features
- Feature 1
- Feature 2

## Tips
- Tip 1
- Tip 2

## Integration
Works with: other-tool.py, config-file.json
```

---

*Last updated: 2026-02-03T17:04Z — Work block 1125*
*Documentation coverage: 93% (119/128 tools)*
