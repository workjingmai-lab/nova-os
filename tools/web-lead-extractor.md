# web-lead-extractor.py

**Extract potential leads from web pages by scanning for pain points, contact info, and service match signals.**

## What It Does

Scans web page content to identify high-probability leads for automation services:
- Detects pain point keywords ("manual process", "slow process", "need automation")
- Extracts contact information (emails, Twitter handles, Discord invites)
- Matches content to service types (monitoring, automation, support, governance, analytics, security)
- Scores leads based on pain signal intensity

## When to Use

- **Outreach research:** Qualify prospects before reaching out
- **Competitive analysis:** Understand what problems others are solving
- **Market research:** Identify companies with automation needs
- **Lead qualification:** Filter good leads from weak leads

## Usage

```bash
# Scan a URL (requires browser or web_fetch for content)
python3 tools/web-lead-extractor.py scan --url "https://example.com/about" --content "We have manual processes and slow workflows..."

# Scan with raw content
python3 tools/web-lead-extractor.py scan --url "https://acme.com" --content "Our team struggles with manual incident response and slow monitoring"

# Show help
python3 tools/web-lead-extractor.py --help
```

## Output

```
🔍 Lead Scan: https://acme.com
   Pain Points: manual process, slow process, incident response slow
   Suggested Service: monitoring
   Contacts: email:hello@acme.com, twitter:@acme_inc
   Pain Score: 3/10
   ✅ GOOD LEAD - Multiple pain signals
```

## Lead Scoring

- **Pain Score 2+:** GOOD LEAD — Multiple pain signals, high conversion probability
- **Pain Score 1:** POSSIBLE LEAD — Single pain signal, worth investigating
- **Pain Score 0:** WEAK LEAD — No clear pain signals, low priority

## Service Categories

- **monitoring:** Alerts, incidents, uptime, tracking
- **automation:** Workflow, pipeline, integration needs
- **support:** Customer service, helpdesk, tickets
- **governance:** Voting, proposals, DAO, treasury
- **analytics:** Data, dashboards, reporting, insights
- **security:** Breaches, incidents, monitoring gaps

## Integration

Pairs with:
- `service-outreach-tracker.py` — Log qualified leads
- `outreach-personalizer.py` — Generate personalized outreach
- `templates/outreach-value-first-template.md` — Structure messages

## Status

✅ Working (blocked on browser access for automated fetching)
