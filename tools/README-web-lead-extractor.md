# web-lead-extractor.py

Extract potential leads from web pages by detecting pain points, contacts, and service fit.

## What It Does

Scans web content for lead qualification signals:
- **Pain point detection** - Finds phrases like "manual process", "slow", "need automation"
- **Contact extraction** - Extracts emails, Twitter handles, Discord invites
- **Service matching** - Suggests best service type (monitoring, automation, support, etc.)
- **Lead scoring** - Pain score 2+ = good lead, 1 = possible, 0 = weak

## When to Use

- Researching prospects before outreach
- Qualifying leads from websites, docs, about pages
- Building target lists for service proposals

## Usage

```bash
# Scan specific page content
python3 tools/web-lead-extractor.py scan --url "https://example.com/about" --content "<HTML>"

# Batch scan (urls.txt with URLs, one per line)
python3 tools/web-lead-extractor.py batch --urls urls.txt
```

## Lead Scoring

- **Pain Score 2+:** ✅ GOOD LEAD - Multiple pain signals detected
- **Pain Score 1:** ⚠️ POSSIBLE LEAD - Single pain signal
- **Pain Score 0:** ❌ WEAK LEAD - No clear pain signals

## Service Types Detected

- **monitoring** - Alerts, incidents, uptime, tracking
- **automation** - Workflows, pipelines, integrations
- **support** - Customer service, helpdesk, tickets
- **governance** - Voting, proposals, DAO, treasury
- **analytics** - Data, dashboards, reporting, insights
- **security** - Breaches, monitoring, incident response

## Pain Point Keywords

The tool looks for phrases like:
- "manual process", "manual workflow"
- "slow process", "time consuming"
- "need automation", "automation needed"
- "spreadsheet hell", "data entry"
- "monitoring issues", "incident response slow"

## Output Example

```
🔍 Lead Scan: https://example.com/about
   Pain Points: manual process, slow process, need automation
   Suggested Service: automation
   Contacts: email:hello@example.com, twitter:@company
   Pain Score: 3/10
   ✅ GOOD LEAD - Multiple pain signals
```

## Related Tools

- **lead-score-calculator** - Prioritize leads by fit, value, readiness
- **service-outreach-tracker** - Track service proposals and pipeline
- **moltbook-prospector** - Find leads on Moltbook

## Insight

> "Lead qualification = higher conversion. Pain score 2+ = good lead."

Detecting automation needs before outreach = targeted, relevant proposals that convert.
