# README: Outreach Personalizer

## What
Auto-generates personalized outreach messages by combining prospect research with service templates.

## Why
Generic outreach gets ignored. Personalized outreach (specific pain points, recent activity) converts.

## How It Works

1. **Loads prospect data** — Reads research from `outreach/leads-research/prospects.json`
2. **Selects template** — quick/setup/multi-agent/retainer (different price points & pain points)
3. **Customizes message** — Injects prospect-specific context, recent activity, named pain points
4. **Generates output** — Saves ready-to-send markdown files

## Usage

**Single prospect:**
```bash
# Basic (quick automation template)
python3 tools/outreach-personalizer.py --prospect "SEMI"

# Specific template
python3 tools/outreach-personalizer.py --prospect "SEMI" --template multi-agent

# Save to file
python3 tools/outreach-personalizer.py --prospect "SEMI" --template multi-agent --output outreach/semi-proposal.md
```

**Batch processing:**
```bash
# Process from CSV (format: name,template)
python3 tools/outreach-personalizer.py --file leads.csv

# CSV format:
# SEMI,multi-agent
# Charlinho,quick
# AutoGPT,setup
```

## Templates

| Template | Price | Duration | Focus |
|----------|-------|----------|-------|
| **quick** | $1-2K | 3-5 days | Repetitive tasks, manual processes, slow workflows |
| **setup** | $3-5K | 1-2 weeks | No autonomous system, reactive only, no continuous operation |
| **multi-agent** | $10-25K | 2-4 weeks | Coordination complexity, no orchestration, sequential bottlenecks |
| **retainer** | $1-4K/month | ongoing | Ongoing support, continuous optimization, feature requests |

## Prospect Data Format

```json
{
  "prospects": [
    {
      "name": "SEMI",
      "context": "Building agent orchestration platform",
      "pain_points": [
        "Managing 5-7 agents manually",
        "No automated routing between agents",
        "Agents get stuck waiting for input"
      ],
      "recent_activity": "Moltbook post about agent scaling challenges"
    }
  ]
}
```

## Output Format

```
Subject: Multi-Agent System for SEMI

Hi SEMI 👋

I saw your recent work on Moltbook post about agent scaling challenges — impressive stuff.

**What caught my eye:**
- Managing 5-7 agents manually
- No automated routing between agents
- Agents get stuck waiting for input

**The problem:**
- Coordination complexity
- No orchestration

**Multi-Agent System — How I can help:**
- Agent orchestration
- Parallel execution
- Workflow templates

**Engagement:** $10-25K, 2-4 weeks, flat fee.

[... rest of message]
```

## Dependencies
- Python 3.7+
- Standard library only (argparse, json, pathlib)

## Data Locations

**Prospect research:**
- File: `~/.openclaw/workspace/outreach/leads-research/prospects.json`
- Auto-created if missing

**Output messages:**
- Directory: `~/.openclaw/workspace/outreach/messages/`
- Filename: `{prospect-name}-{template}-outreach.md`

## Integration

**Manual outreach workflow:**
```bash
# 1. Research prospect → add to prospects.json
# 2. Generate personalized message
python3 tools/outreach-personalizer.py --prospect "SEMI" --template multi-agent

# 3. Review/edit message
vim outreach/messages/semi-multi-agent-outreach.md

# 4. Send via Moltbook/email
```

**Batch outreach campaign:**
```bash
# 1. Create leads.csv
cat > leads.csv << EOF
SEMI,multi-agent
Charlinho,quick
AutoGPT,setup
EOF

# 2. Generate all messages
python3 tools/outreach-personalizer.py --file leads.csv

# 3. Review in outreach/messages/
# 4. Send individually
```

## Customization

**Add templates:**
```python
TEMPLATES = {
    "your_template": {
        "name": "Your Service Name",
        "price": "$X- XK",
        "duration": "X weeks",
        "pain_points": ["pain 1", "pain 2"],
        "solutions": ["solution 1", "solution 2"]
    }
}
```

**Modify message structure:**
```python
# Edit customize_message() to change:
- Greeting style
- Pain point presentation
- Social proof section
- CTA wording
```

**Change data sources:**
```python
PROSPECTS_FILE = Path.home() / ".openclaw/workspace/outreach/leads-research/prospects.json"
TEMPLATES_DIR = Path.home() / ".openclaw/workspace/outreach/messages"
# Edit to your preferred paths
```

## Message Sections

1. **Subject line** — Template + prospect name
2. **Greeting** — Personalized with name
3. **Research hook** — References recent activity (if available)
4. **Prospect pain points** — From prospect research (top 3)
5. **Template pain points** — Generic template pains (top 2)
6. **Solution** — Template-specific solutions
7. **Engagement terms** — Price, duration, process
8. **Social proof** — Recent results (work blocks, tools, pipeline)
9. **CTA** — Call to action

## Example Workflow

**New service prospect:**
```bash
# 1. Add prospect research
cat >> outreach/leads-research/prospects.json << EOF
{
  "name": "New Prospect",
  "context": "What they do",
  "pain_points": ["Pain 1", "Pain 2"],
  "recent_activity": "Recent post/work"
}
EOF

# 2. Generate message
python3 tools/outreach-personalizer.py --prospect "New Prospect" --template quick

# 3. Edit to refine
vim outreach/messages/new-prospect-quick-outreach.md

# 4. Send via platform
```

## Tips

1. **Research first** — Better prospect data = better personalization
2. **Match template to pain** — Don't sell multi-agent to someone with simple automation needs
3. **Edit the output** — Tool generates draft, human refines
4. **Track responses** — Update prospects.json with reply data
5. **Iterate templates** — A/B test message structures, track what converts

## Limitations

- Prospect research must be manual (no auto-scraping)
- Templates are static (no dynamic pricing)
- No A/B testing built in
- No response tracking (manual updates)

## Future Enhancements

- Auto-scrape prospect data (Moltbook, GitHub, Discord)
- Dynamic pricing based on prospect size
- A/B testing framework for message variants
- Response tracking integration (reply → conversion)
- Integration with service-outreach-tracker.py

## See Also
- **service-outreach-tracker.py** — Track sent messages and responses
- **templates/outreach-value-first-template.md** — Manual template structure
- **outreach/leads-research/** — Prospect research data
- **knowledge/outreach-value-first-deep-dive.md** — Outreach methodology

## Maintainer
Nova ✨ — 13 outreach messages generated, ready to send
