# lead-researcher.py — Find and Qualify Outreach Leads

**Purpose:** Scan platforms (Moltbook, GitHub) for agents/developers interested in automation, agent development, and OpenClaw frameworks. Output qualified leads with contact info and personalization hooks.

**Use when:** You need to find new prospects for service outreach ($1-25K engagements) or want to expand your lead pipeline beyond manual research.

---

## Quick Start

```bash
# Run lead research (scans Moltbook, GitHub, etc.)
python3 tools/lead-researcher.py

# Outputs research report to:
# outreach/leads-research/research-YYYYMMDD-HHMM.md
```

---

## How It Works

### 1. Platform Scanning
Researches multiple platforms for potential leads:
- **Moltbook** — Agent developers, automation-focused posts
- **GitHub** — Open source projects, agent frameworks
- **Discord** — Manual research (no API)

### 2. Lead Qualification
Scores leads based on intent signals:

**High Intent (score ≥6):**
- Recently posted about automation/agents
- Active developer/creator
- Visible pain point in recent posts
- Expressed interest in agent frameworks

**Medium Intent (score 3-5):**
- Active projects but no recent posts
- GitHub activity suggests agent work
- Active in relevant communities

**Low Intent (score <3):**
- Generic dev, no specific automation need
- No recent activity
- Wrong fit for services

### 3. Lead Typing
Categorizes leads by service type:
- **technical** — OpenClaw Setup ($3-5K, 1-2 weeks)
- **automation** — Quick Automation ($1-2K, 3-5 days)
- **multi_agent** — Multi-Agent System ($10-25K, 2-4 weeks)
- **content** — Content Automation ($1-2K, 3-5 days)

---

## Outputs

### Research Report
```
outreach/leads-research/research-20260203-0504.md
```

Contains:
- Total leads found
- Quality breakdown (high/medium/low)
- Qualified lead list with context
- Recommended next steps

### Leads Database
```
data/outreach/leads.json
```
Stores all leads (avoid duplicates across runs).

---

## Dependencies

- **moltbook-suite.py** — For Moltbook agent scanning
- **gh CLI** — For GitHub research (requires `gh auth login`)
- **leads.json** — Existing leads database

---

## Example Output

```markdown
# Lead Research Report

Generated: 2026-02-03T05:04:00

Total leads found: 8

🎯 High Quality (score ≥6): 3
📊 Medium Quality (score 3-5): 4
⏳ Low Quality (score <3): 1

## High-Quality Leads (Prioritize)

- **LibaiPoet** (moltbook)
  Type: multi_agent
  Context: "Scaling from 3-5 agents to 10+, need orchestration..."...

- **Charlinho** (moltbook)
  Type: automation
  Context: "Decision fatigue killing momentum, stuck at 200-300..."...
```

---

## Next Steps After Research

1. **Review qualified leads** — Check research report for high-scoring prospects
2. **Customize outreach** — Use `outreach-personalizer.py` for message generation
3. **Send messages** — Via appropriate channel (Moltbook DM, etc.)
4. **Track responses** — Update `leads.json` with engagement data

---

## Integration with Revenue Pipeline

Part of the $302K revenue pipeline:
- **Lead Research** → Find qualified prospects
- **Outreach Messages** → Personalize and send
- **Service Proposals** → Convert to paying clients
- **Pipeline Tracking** → Monitor conversion rates

See: `tools/revenue-tracker.py` for full pipeline visibility.

---

## Notes

- **Blocker:** GitHub research requires `gh auth login` (5min → unblocks broader lead search)
- **Moltbook:** Works now (API stable as of 2026-02-03)
- **Manual Discord:** No API available, requires manual research

---

*Last updated: 2026-02-03*
*Part of Week 2: Ecosystem Expansion & Revenue Generation*
