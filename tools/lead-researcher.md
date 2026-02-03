# lead-researcher.py

**Find and qualify potential outreach leads for agent services.**

Scans platforms (Moltbook, GitHub) for agents/developers interested in automation, agent development, OpenClaw, or multi-agent systems. Outputs qualified leads with contact info and personalization hooks.

---

## Overview

Turns passive platform browsing into active lead generation. Automatically identifies, qualifies, and scores potential clients based on their content and activity.

## Use Cases

- **Revenue generation:** Find clients for automation/agent services
- **Partnership discovery:** Identify technical collaborators
- **Market research:** Understand who's building what
- **Outreach targeting:** Personalize messages based on lead context

## Features

### Multi-Platform Research
- **Moltbook:** Scan agent posts for technical needs
- **GitHub:** Search repos for agent framework users (requires gh auth)
- **Discord:** Manual research template included

### Lead Qualification System
Automatically scores leads based on intent signals:

**High Intent (score ≥6):**
- Recently posted about automation/agents
- Active developer/creator
- Visible pain point in recent posts
- Expressed interest in agent frameworks

**Medium Intent (score 3-5):**
- Runs active projects but no recent posts
- GitHub activity suggests agent work
- Active in relevant communities

**Low Intent (score <3):**
- Generic dev with no specific automation need
- No recent activity
- Wrong fit for services

### Lead Types & Service Mapping

| Lead Type | Template | Price Range | Timeline |
|-----------|----------|-------------|----------|
| Technical | OpenClaw Setup | $3-5K | 1-2 weeks |
| Automation | Quick Automation | $1-2K | 3-5 days |
| Multi-Agent | Multi-Agent System | $10-25K | 2-4 weeks |
| Content | Content Automation | $1-2K | 3-5 days |

## Installation

```bash
# No dependencies required (uses moltbook-suite.py integration)
# Ensure moltbook-suite.py exists in tools/
```

## Usage

### Basic Research

```bash
python3 tools/lead-researcher.py
```

### Output

- **Research report:** `outreach/leads-research/research-YYYYMMDD-HHMM.md`
- **Leads database:** `data/outreach/leads.json` (avoid duplicates)

### Example Report

```markdown
# Lead Research Report
Generated: 2026-02-02T19:55:00

Total leads found: 12

🎯 High Quality (score ≥6): 3
📊 Medium Quality (score 3-5): 7
⏳ Low Quality (score <3): 2

## High-Quality Leads (Prioritize)

- **agent_dev_42** (moltbook)
  Type: multi_agent
  Context: "Building a multi-agent system for content automation. Anyone have experience with OpenClaw coordination?"
```

## Workflow

1. **Run research:** `python3 tools/lead-researcher.py`
2. **Review report:** Check `outreach/leads-research/` for qualified leads
3. **Customize messages:** Use lead type templates for personalization
4. **Send outreach:** Contact via appropriate channel
5. **Track responses:** Update `data/outreach/leads.json`

## Integration

Works with other tools:
- **moltbook-suite.py:** Analyzes feed for agent activity
- **outreach-message-generator.py:** Creates personalized messages
- **leads.json:** Central lead database (avoid duplicates)

## Lead Qualification Criteria

### High Intent Signals (+3 points each)
- Recently posted about automation/agents
- Active developer/creator
- Visible pain point in recent posts
- Expressed interest in agent frameworks

### Medium Intent Signals (+1-2 points)
- Runs active projects but no recent posts
- GitHub activity suggests agent work
- Active in relevant communities

## Data Structures

### Lead Object

```json
{
  "name": "agent_dev_42",
  "platform": "moltbook",
  "type": "multi_agent",
  "score": 9,
  "context": "Building multi-agent system...",
  "status": "identified"
}
```

### Leads Database Format

```json
{
  "leads": [
    {
      "name": "...",
      "contact": "...",
      "type": "...",
      "status": "contacted|responded|converted|lost",
      "history": [...]
    }
  ]
}
```

## Limitations

- **GitHub:** Requires `gh auth login` for API access
- **Discord:** Manual research only (no API)
- **Moltbook:** Depends on moltbook-suite.py integration

## Future Enhancements

- [ ] Automated GitHub search integration
- [ ] Discord webhook monitoring
- [ ] Lead enrichment (auto-fetch social profiles)
- [ ] A/B testing for outreach messages
- [ ] CRM integration (pipeline tracking)

---

**Version:** 1.0.0
**Created:** 2026-02-02
**Category:** Revenue Generation
**Dependencies:** moltbook-suite.py (optional)
