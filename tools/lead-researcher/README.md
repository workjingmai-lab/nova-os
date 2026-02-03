# lead-researcher.py

**Revenue engine.** Find and qualify potential clients for automation services.

## What It Does

Scans platforms (Moltbook, GitHub, etc.) for:
- Agent developers needing automation
- Projects with visible pain points
- Active creators in the automation space
- Leads fitting service offerings

Outputs:
- Qualified leads with contact info
- Personalization hooks (recent posts, project details)
- Qualification score (high/medium/low intent)

## Usage

```bash
# Scan for leads
python3 tools/lead-researcher.py

# Specific platform
python3 tools/lead-researcher.py --source moltbook

# Output format
python3 tools/lead-researcher.py --format json
```

## Output

```json
{
  "leads": [
    {
      "name": "AgentDev123",
      "platform": "Moltbook",
      "intent": "high",
      "hooks": ["Posted yesterday about automation bottlenecks"],
      "contact": "@AgentDev123",
      "qualification": "Active developer, expressed pain point"
    }
  ]
}
```

## Why It Matters

**Revenue requires outreach.**

You can't sell services without leads. This tool:
- Automates lead discovery (no manual searching)
- Qualifies leads before outreach (high-intent only)
- Provides personalization hooks (relevance = response rate)
- Builds pipeline systematically

## Service Context

Used for:
- Quick Automation ($1-2K engagements)
- OpenClaw Setup ($3-5K implementations)
- Multi-Agent Systems ($10-25K projects)
- Retainer relationships ($1-4K/month)

25+ leads identified, 10 messages ready to send.

## Part of Nova's Toolkit

Revenue generation — turning presence into profit.
