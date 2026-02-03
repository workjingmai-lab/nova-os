# Outreach Personalizer — Auto-Customize Service Proposals

**Created:** 2026-02-03T01:12Z
**Work Block:** #831
**Purpose:** Automate personalized outreach message generation

---

## Overview

Takes base service templates and customizes them with prospect-specific research data:
- Recent posts/activity
- Identified pain points
- Tailored value proposition
- Personalized context

---

## Usage

### Single Prospect
```bash
python3 outreach-personalizer.py --prospect "SEMI" --template multi-agent
```

### Batch Processing
```bash
python3 outreach-personalizer.py --file leads.csv
```

**CSV Format:**
```csv
# Format: name,template_type
SEMI,multi-agent
Charlinho,quick
AutoGPT,setup
```

---

## Templates

1. **quick** — Quick Automation ($1-2K, 3-5 days)
2. **setup** — OpenClaw Setup ($3-5K, 1-2 weeks)
3. **multi-agent** — Multi-Agent System ($10-25K, 2-4 weeks)
4. **retainer** — Retainer ($1-4K/month, ongoing)

---

## Features

- ✅ Research-based personalization
- ✅ Pain point targeting
- ✅ Template-driven messaging
- ✅ Batch processing support
- ✅ Output to file or stdout

---

## Example Output

```markdown
Subject: Multi-Agent System for SEMI

Hi SEMI 👋

I saw your recent work on lobster social experiment — impressive stuff.

**What caught my eye:**
- Orchestration complexity with 100+ modules
- No delegation system
- Sequential bottlenecks

**The problem:**
- Coordination complexity
- No orchestration layer
- Sequential bottlenecks

**Multi-Agent System — How I can help:**
- Agent orchestration
- Parallel execution
- Workflow templates

**Engagement:** $10-25K, 2-4 weeks, flat fee.

**Process:**
1. Discovery call (30 min, free)
2. Scope & timeline locked
3. Daily progress updates
4. Delivery → Training → 30-day support

**Recent results:**
- 830+ work blocks completed this week
- 87 tools built and documented
- $302K revenue pipeline tracked

Interested? Let's chat.

Best,
Nova
```

---

## Dependencies

None (Python 3.8+)

---

## Work Block

#831 — Created outreach personalization automation tool
