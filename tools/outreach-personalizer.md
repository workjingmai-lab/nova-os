# Outreach Personalizer — Auto-Customize Service Proposals

Generate personalized service proposals with prospect-specific research and context.

## Overview

Outreach Personalizer takes your prospect research and automatically generates customized outreach messages. Instead of generic "hi, buy my service" pitches, it creates specific, researched messages that convert.

**Why it works:**
- Generic pitches get ignored
- Specific research + named pain = "yes, that's me" moment
- Personalized messages show you did your homework

## Use Case

- **Service business:** Send proposals that actually convert
- **Outreach scaling:** Personalize 10 messages in 1 minute
- **Research integration:** Uses your prospect database for context
- **Template flexibility:** 4 service types (quick, setup, multi-agent, retainer)

## Installation

```bash
# Tool location
tools/outreach-personalizer.py

# Data files
outreach/leads-research/prospects.json  # Prospect research database
outreach/messages/  # Generated message outputs
```

## Usage

### Single Prospect
```bash
python3 tools/outreach-personalizer.py \
  --prospect "SEMI" \
  --template multi-agent \
  --output outreach/messages/semi-proposal.md
```

**Output:**
```markdown
Subject: Multi-Agent System for SEMI

Hi SEMI 👋

I saw your recent work on AI agent orchestration — impressive stuff.

**What caught my eye:**
- Coordination complexity across multiple agents
- Sequential bottlenecks in workflows
- No orchestration layer

**The problem:**
- Coordination complexity
- No orchestration
- Sequential bottlenecks

**Multi-Agent System — How I can help:**
- Agent orchestration
- Parallel execution
- Workflow templates

**Engagement:** $10-25K, 2-4 weeks, flat fee.
...
```

### Batch Processing
```bash
# Create leads.csv
cat > leads.csv << EOF
SEMI,multi-agent
LibaiPoet,quick
Charlinho,setup
EOF

# Batch personalize
python3 tools/outreach-personalizer.py --file leads.csv
```

**Output:**
```
📊 Batch Processing Results:
  ✅ SEMI → outreach/messages/semi-multi-agent-outreach.md
  ✅ LibaiPoet → outreach/messages/libaipoet-quick-outreach.md
  ✅ Charlinho → outreach/messages/charlinho-setup-outreach.md

Total: 3 prospects processed
```

### Print to Terminal
```bash
python3 tools/outreach-personalizer.py --prospect "SEMI" --template setup
```

## Service Templates

| Template | Price | Duration | Use Case |
|----------|-------|----------|----------|
| `quick` | $1-2K | 3-5 days | Automate a specific workflow |
| `setup` | $3-5K | 1-2 weeks | Full OpenClaw installation |
| `multi-agent` | $10-25K | 2-4 weeks | Custom multi-agent system |
| `retainer` | $1-4K/month | Ongoing | Monthly support & optimization |

## Prospect Database Format

`outreach/leads-research/prospects.json`:

```json
{
  "prospects": [
    {
      "name": "SEMI",
      "context": "AI research agent focused on multi-agent systems",
      "pain_points": [
        "Coordination complexity across multiple agents",
        "Sequential bottlenecks in workflows",
        "No orchestration layer"
      ],
      "recent_activity": "AI agent orchestration research",
      "contact": "contact@example.com",
      "platform": "Moltbook"
    }
  ]
}
```

## Message Structure

Each generated message follows the value-first structure:

1. **Research hook** — "I saw your recent work on X"
2. **Specific pain** — Their actual problems (from database)
3. **Template pain** — Common problems for this service type
4. **Solution** — How you'll fix it
5. **Engagement terms** — Price, timeline, process
6. **Social proof** — Your results
7. **Call to action** — "Let's chat"

## Workflow

### Step 1: Research Prospects
Add prospect data to `outreach/leads-research/prospects.json`:

```bash
# Add new prospect
cat >> outreach/leads-research/prospects.json << EOF
{
  "name": "Prospect Name",
  "context": "What they do",
  "pain_points": ["pain 1", "pain 2"],
  "recent_activity": "Recent post/work",
  "contact": "email@example.com",
  "platform": "where you found them"
}
EOF
```

### Step 2: Generate Messages
```bash
# Single message
python3 tools/outreach-personalizer.py \
  --prospect "Prospect Name" \
  --template quick \
  --output outreach/messages/prospect-name-proposal.md
```

### Step 3: Review & Send
- Read the generated message
- Edit if needed (add more specific details)
- Send via your channel (Telegram, Discord, etc.)

### Step 4: Track
Update `tmp/service-outreach-tracker.json`:
```bash
python3 tools/service-outreach-tracker.py update 1 --status sent
```

## Integration

Pairs with:
- `service-outreach-tracker.py` — Track pipeline status
- `templates/outreach-value-first-template.md` — Message structure reference
- `moltbook-suite.py` — Post to Moltbook for visibility
- `revenue-tracker.py` — Consolidate revenue pipeline

## Tips

- **Research beats templates** — The more specific the prospect data, the better the conversion
- **Name the pain** — Use their exact words from research
- **Show proof** — Include your results (830+ work blocks, 87 tools, etc.)
- **Clear CTA** — "Let's chat" > "Buy now"
- **Batch effectively** — Generate 10 messages, send 5, test response rate

## Example Session

```bash
# 1. Research prospect (add to prospects.json)
# 2. Generate message
python3 tools/outreach-personalizer.py \
  --prospect "SEMI" \
  --template multi-agent \
  --output outreach/messages/semi-proposal.md

# 3. Review
cat outreach/messages/semi-proposal.md

# 4. Edit if needed (add more specific details)
nano outreach/messages/semi-proposal.md

# 5. Send via your channel
# (copy message, send via Telegram/Discord/Email)

# 6. Track in pipeline
python3 tools/service-outreach-tracker.py add \
  --company "SEMI" \
  --contact "contact@semi.example" \
  --pain "Multi-agent coordination" \
  --solution "Orchestration system" \
  --service "multi_agent" \
  --value 15000

python3 tools/service-outreach-tracker.py update SEMI --status sent
```

## Philosophy

**Generic pitches = ignored messages.**

"Hi, I offer automation services" → Deleted.
"I saw your post about agent orchestration struggles" → Response.

**Specific research = conversion.**

When you name their exact pain point, they think: "This person understands me." That's the moment before the sale.

**Personalization at scale.**

Research once, generate infinite personalized messages. The tool remembers the details, you focus on the relationship.

## Metrics

Track these weekly:
- **Messages generated** → How many prospects reached
- **Response rate** → Replies ÷ Sent (aim for 20%+)
- **Conversion rate** → Deals ÷ Replies
- **Deal size** → Average value per service type

---

*Created: 2026-02-03*
*Part of Week 2 Revenue Pivot — Ecosystem Expansion & Value Creation*
