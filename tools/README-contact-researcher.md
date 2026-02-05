# Contact Researcher

Find contact information for service prospects autonomously.

## Overview

Automates contact research for the $2M+ service pipeline. Uses web search to discover:
- Company contact pages
- Public email addresses
- LinkedIn profiles
- Website contact forms

## Usage

```bash
# Research top 10 prospects (default)
python3 tools/contact-researcher.py

# Research top 20 prospects
python3 tools/contact-researcher.py --top 20

# Specify search method
python3 tools/contact-researcher.py --method google
python3 tools/contact-researcher.py --method linkedin
```

## How It Works

1. **Loads prospects** from `revenue-pipeline.json` (stage: "lead", category: "services")
2. **Sorts by value** (highest-value prospects first)
3. **Researches each prospect** using:
   - Website `/contact` page check
   - Google search for "[company] contact us email"
   - LinkedIn search for "[person] [company] LinkedIn" (if person known)
4. **Scores confidence** based on number of sources
5. **Outputs results** to `knowledge/contacts/` directory

## Output Files

- `research-YYYYMMDD-HHMMSS.json` — Full research data with all findings
- `summary-YYYYMMDD-HHMMSS.md` — Human-readable summary

## Example Output

```json
{
  "prospect": {
    "company": "Acme Corp",
    "contact_person": "Jane Smith",
    "website": "https://acme.com",
    "value_estimate": 25000
  },
  "findings": [
    {
      "source": "website",
      "url": "https://acme.com/contact",
      "confidence": 0.6
    },
    {
      "source": "google_search",
      "query": "\"Acme Corp\" contact us email",
      "results": "Found contact@acme.com...",
      "confidence": 0.4
    }
  ],
  "confidence": 1.0,
  "timestamp": "2026-02-04T10:52:00"
}
```

## Confidence Scoring

- **1.0 (100%)** — Multiple sources found (website + search results)
- **0.6-0.8** — Single reliable source (website contact page)
- **0.4-0.5** — Indirect evidence only (search results)
- **< 0.4** — Low confidence, needs manual verification

## Next Steps After Research

1. Review findings in output JSON
2. Manually verify contact info (2-3 min per prospect)
3. Update `revenue-pipeline.json` with confirmed contacts
4. Execute service outreach using `tools/service-outreach.py`

## Integration with Pipeline

This tool works with the existing revenue pipeline:
- **Input:** `revenue-pipeline.json` (stage: "lead")
- **Output:** Contact research files → verified contacts → outreach ready

## Time Estimate

- **Research automation:** ~30 seconds per prospect (automated)
- **Manual verification:** ~2-3 minutes per prospect
- **10 prospects:** ~5 minutes automated + 20-30 minutes manual

## Value Proposition

For $2,057K in service pipeline:
- **104 prospects** need contact info
- **Top 10** = ~$500K potential value
- **1 hour** of research unlocks $500K outreach
- **ROI:** $500K/hour = $8,333/min

## Created

2026-02-04 — Work block 1524
