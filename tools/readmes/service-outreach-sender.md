# service-outreach-sender.py

Automates sending service outreach messages via OpenClaw message tool. Loads prospect research data, formats value-first messages, and supports single or batch outreach with dry-run mode.

## What It Does

- Loads prospect research from `data/contacts/{prospect}-research.md`
- Extracts and formats the Value-First Message section
- Sends outreach messages (dry-run or live)
- Tracks sent/failed status for batch campaigns

## Usage

```bash
# Preview message for single prospect
python3 service-outreach-sender.py --prospect gitcoin

# Send to single prospect (LIVE)
python3 service-outreach-sender.py --prospect gitcoin --send

# Batch preview for top 5 prospects
python3 service-outreach-sender.py --batch 5

# Batch send to top 5 prospects (LIVE)
python3 service-outreach-sender.py --batch 5 --send
```

## How It Works

1. **Prospect Research**: Loads research data from `data/contacts/{prospect}-research.md`
2. **Message Extraction**: Finds the "Value-First Message" section in research file
3. **Formatting**: Cleans up markdown formatting (headers, code blocks)
4. **Sending**: Dry-run mode previews; `--send` flag sends live messages

## Research File Format

Expected structure in `{prospect}-research.md`:

```markdown
## Value-First Message

**Subject:** Quick question about {specific pain}

Hey {name},

{Research-backed pain point}
{Specific solution}
{Proof/credibility}
{Clear CTA}

```

## Top Prospects (Phase 1)

- gitcoin
- uniswap
- mirror
- lens
- aave

## Integration Notes

Currently in dry-run mode. Live sending requires:
1. Actual contact details (Twitter handle, email, etc.)
2. OpenClaw message tool integration
3. Sent status tracking in `revenue-pipeline.json`

## Related Tools

- `service-outreach-sender.py` — This tool (outreach execution)
- `service-proposal-templates.md` — Proposal templates
- `revenue-tracker.py` — Pipeline tracking
- `contact-researcher.py` — Research automation

## Files

- Tool: `/home/node/.openclaw/workspace/tools/service-outreach-sender.py`
- Research: `/home/node/.openclaw/workspace/data/contacts/`
- Prospects: `/home/node/.openclaw/workspace/data/service-prospects.md`

## Author

Nova (2026-02-04)
