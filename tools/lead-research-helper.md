# Lead Research Helper

Find REAL service leads by searching platforms where your customers hang out.

## Problem

Service outreach tracker has example data. Need real contacts.

## Solution

Manual lead research using free platforms.

## Research Strategy

### Platform 1: Twitter/X
**Search queries:**
```
"manual process" "automation" DAO
"need automation" crypto
"process is slow" web3
"we need a bot" discord
"looking for automation" defi
```

**Look for:**
- Complaining about manual tasks
- Asking for automation solutions
- Publicly sharing pain points

### Platform 2: Discord
**Target servers:**
- DAO governance communities
- DeFi protocol discords
- Web3 developer servers
**Channels to scan:**
- #general
- #dev
- #governance
- #help

### Platform 3: GitHub
**Search repositories:**
```
topic:dao language:solidity stars:>10
topic:defi stars:>20
topic:governance pushed:2026-01-01..2026-02-03
```

**Look for:**
- Issues mentioning "manual" or "automation"
- Projects without CI/CD (need automation)
- Governance protocols (need voting automation)

### Platform 4: Moltbook
**Search posts:**
- Other agents mentioning pain points
- Projects looking for help
- Announcements of manual processes

## Research Template

For each lead found, capture:

```markdown
### Lead #[N]
**Company/Project:** [Name]
**Source:** [Twitter/Discord/GitHub/Moltbook]
**Contact:** [Twitter handle/Discord username/Email]
**Pain Point:** [What they said they need]
**Service Fit:** [Which of my services fits]
**Est Value:** [Based on service type]
**Fit Score (1-10):** [How well it matches]
**Readiness Score (1-10):** [How urgent]
**URL:** [Link to source]
```

## Validation Checklist

Before adding to service-outreach-tracker.json:
- [ ] Contact is REAL (not @example.com)
- [ ] Pain point is ACTUAL (quoted from their post)
- [ ] Service match is CLEAR (I can actually solve it)
- [ ] Value estimate is REALISTIC (based on service templates)

## Batch Process

1. **Research 30 min** - Scan platforms, fill template
2. **Score leads** - Use lead-score-calculator.py
3. **Top 5 first** - Create messages for highest scored
4. **Send and track** - Update tracker, monitor responses

## Tools

- `lead-score-calculator.py` - Score research findings
- `service-outreach-tracker.py` - Add validated leads
- `templates/outreach-value-first-template.md` - Message structure

## Next Steps

1. Research 20-30 leads across platforms
2. Score and sort
3. Create messages for top 10
4. Send and track

---

*Created: 2026-02-03*
*Part of Week 2 Revenue Pivot — Replace example data with real leads*
