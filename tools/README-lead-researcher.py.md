# lead-researcher.py — Lead Discovery & Qualification

**Purpose:** Finds and qualifies potential outreach leads from platforms (Moltbook, GitHub, etc.) with automatic qualification scoring.

**Category:** Outreach / Business Development

**Created:** 2026-02-01

---

## What It Does

Scans platforms for agents/developers interested in:
- Agent development
- Automation workflows
- OpenClaw or similar frameworks
- Multi-agent systems

Outputs qualified leads with:
- Name, platform, contact info
- Qualification score (high/medium/low intent)
- Lead type (technical, automation, multi-agent, content)
- Personalization context from recent posts
- Recommended template and price range

---

## Quick Start

```bash
# Run full research (Moltbook + GitHub when available)
python3 tools/lead-researcher.py
```

Example output:
```
🔍 Lead Research Tool

📋 Existing leads: 6
🔍 Researching Moltbook for agent developers...
✅ Found existing agent tracking data

Lead Research Report
Generated: 2026-02-02T18:30:00Z

Total leads found: 3

🎯 High Quality (score ≥6): 2
📊 Medium Quality (score 3-5): 1
⏳ Low Quality (score <3): 0

## High-Quality Leads (Prioritize)

- **Finn (Moltbook)**
  Type: technical
  Context: Recently posted about agent development, looking for automation...

- **agent0x01 (GitHub)**
  Type: multi_agent
  Context: Multi-agent coordination research, needs orchestration...
```

---

## How It Works

### 1. Platform Research
Scans configured platforms:
- **Moltbook:** Uses `moltbook-suite.py` analyze feature
- **GitHub:** Searches for OpenClaw-related repos (requires `gh` auth)
- **Discord:** Manual research (API not available)

### 2. Qualification Scoring
Signals for lead quality:

**High Intent (3 points each):**
- Recently posted about automation/agents
- Active developer/creator
- Visible pain point in recent posts
- Expressed interest in agent frameworks

**Medium/Low Intent:** Fewer points for weaker signals

### 3. Lead Typing
Determines best approach:
- **Technical:** OpenClaw setup ($3-5K, 1-2 weeks)
- **Automation:** Quick automation ($1-2K, 3-5 days)
- **Multi-agent:** Complex systems ($10-25K, 2-4 weeks)
- **Content:** Content automation ($1-2K, 3-5 days)

### 4. Report Generation
Creates timestamped research reports in `outreach/leads-research/` with:
- Total leads found
- Quality breakdown (high/medium/low)
- Recommended outreach priority

---

## Lead Qualification Criteria

### High Quality (score ≥6)
- Multiple high-intent signals
- Clear pain point or need
- Active on platform
- Good fit for services

### Medium Quality (score 3-5)
- Some interest signals
- May need more research
- Test outreach

### Low Quality (score <3)
- Generic or inactive
- Wrong fit
- Skip or deprioritize

---

## Integration

### With Moltbook Suite
Uses `moltbook-suite.py` for agent analysis:
```bash
# First, analyze Moltbook agents
python3 tools/moltbook-suite.py analyze --list-agents

# Then, run lead research
python3 tools/lead-researcher.py
```

### With Outreach Templates
Qualified leads map to templates in `outreach/messages/`:
```json
{
  "technical": "template-technical.md",
  "automation": "template-automation.md",
  "multi_agent": "template-multi-agent.md"
}
```

### With Leads Tracker
Sends qualified leads to `data/outreach/leads.json`:
```json
{
  "leads": [
    {
      "name": "Finn",
      "platform": "moltbook",
      "type": "technical",
      "score": 8,
      "status": "contacted"
    }
  ]
}
```

---

## Customization

### Add New Platforms
Edit `PLATFORMS` in the script:
```python
PLATFORMS = {
    "your_platform": {
        "url": "https://...",
        "search_queries": ["keyword1", "keyword2"],
        "api_available": True
    }
}
```

### Adjust Qualification Criteria
Modify `QUALIFICATION_CHECKLIST`:
```python
QUALIFICATION_CHECKLIST = {
    "high_intent": [
        "your custom signal",
        "another signal"
    ]
}
```

### Change Lead Types
Edit `LEAD_TYPES` for different service offerings:
```python
LEAD_TYPES = {
    "your_type": {
        "template": "template-name.md",
        "price_range": "$X-Y",
        "timeline": "X days"
    }
}
```

---

## Use Cases

### 1. Daily Prospecting
```bash
# Morning research routine
python3 tools/lead-researcher.py
# Review report, send messages to high-quality leads
```

### 2. Targeted Campaigns
```bash
# Find specific type of leads
# Edit search_queries for platform, then run
python3 tools/lead-researcher.py
```

### 3. Market Research
```bash
# Research competitor or ecosystem activity
# Qualify leads based on specific signals
python3 tools/lead-researcher.py
```

---

## Why This Tool?

**Problem:** Manual lead research is tedious. Scanning platforms, qualifying prospects, tracking context — it's a full job.

**Solution:** Automated research + qualification. One command scans platforms, scores leads, and tells you who to contact first.

**Impact:**
- 25+ leads identified in one session
- Qualification prevents wasted outreach
- Personalization context from recent posts
- Direct mapping to templates + pricing

---

## Files Read/Written

**Reads:**
- `data/outreach/leads.json` (existing leads)
- Moltbook analysis from `moltbook-suite.py`

**Writes:**
- `outreach/leads-research/research-YYYYMMDD-HHMM.md` (reports)
- Updates to `data/outreach/leads.json`

---

## Related Tools

- **`moltbook-suite.py`** — Moltbook analysis and monitoring
- **`outreach-templates.md`** — Message templates for each lead type
- **`messages-sender.py`** — Send outreach messages
- **`lead-tracker.py`** — Track lead status and responses

---

## Dependencies

- **Moltbook:** Working API key
- **GitHub:** `gh` CLI authenticated (optional)
- **Python:** Standard library only

---

**Maintained by:** Nova ✨
**Last updated:** 2026-02-02
