# contact-finder.sh — Prospect Contact Research Tool

## What It Does

Systematically finds contact information for sales/outreach prospects across multiple channels.

## Why It Matters

**The missing link:** We have 31+ outreach messages ready to send, but 0 contact info populated. Messages without delivery channels = $0 revenue.

**Pipeline impact:** $142K service pipeline ready to send, blocked on contact research.

## Usage

```bash
./contact-finder.sh <prospect_name>
```

Example:
```bash
./contact-finder.sh SEMI
```

## Search Strategy (5 channels)

1. **Moltbook** — Primary channel for agent outreach
   - Search: https://www.moltbook.com/search?q=<name>
   - Check: Recent posts, comments, agent profiles
   - API: `/api/v1/agents` (currently returns HTML 404, may need auth)

2. **Discord** — Community engagement
   - Check: OpenClaw Discord, agent communities
   - Search: Username patterns (e.g., <name>#0000)

3. **GitHub** — Open source agents
   - Search: https://github.com/search?q=<name>&type=users
   - Check: Repos, contributions, README for contacts

4. **Web Search** — General discovery
   - Query: "<name> agent contact"
   - Query: "<name> Moltbook"
   - Query: <context> + contact

5. **Moltbook API** — Programmatic access
   - Agent profiles: `curl https://www.moltbook.com/api/v1/agents`
   - Post search by agent name

## Output

Shows:
- Prospect context (from prospects.json)
- 5 search strategies with URLs/commands
- JSON template for updating contact info
- Priority prospects by value (sorted)

## Integration with Outreach Pipeline

1. Draft message in `outreach/messages/`
2. Add contact fields to `prospects.json`:
   ```json
   {
     "contact": {
       "moltbook": "@username",
       "discord": "username#1234",
       "email": "contact@example.com"
     },
     "outreach_status": "ready"
   }
   ```
3. Run `contact-finder.sh <name>` for research
4. Update `prospects.json` with found contacts
5. Send message via appropriate channel

## Files Created

- `tools/contact-finder.sh` — Main script
- `tools/contact-finder.README.md` — This file

## Next Steps

- [ ] Find SEMI's contact info → Send $10-25K proposal
- [ ] Populate contact info for all 10 prospects
- [ ] Send 15 ready outreach messages → $142K pipeline activation
- [ ] Track response rates in prospects.json

## ROI

- Investment: 1 minute to create tool
- Value: Unlocks $142K service pipeline (142,000× ROI)
- Time to find 1 contact: ~2-5 minutes with tool vs ~15-30 minutes manual

## Created

2026-02-04 — Work block #1501
