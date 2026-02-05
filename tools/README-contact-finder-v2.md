# contact-finder-v2.py

Discovers decision makers (CTO, VP Eng, Head of Platform) for service outreach using web search queries and generates research templates for personalized messaging.

## What It Does

- Generates targeted search queries for company contacts
- Creates research template files with outreach strategy
- Supports role-based targeting (CTO, VP Engineering, etc.)
- Saves research to `/data/contacts/` for follow-up

## Usage

```bash
# Generate search queries for company contacts
python3 tools/contact-finder-v2.py --company "Uniswap"

# Target specific role
python3 tools/contact-finder-v2.py --company "Vercel" --role "CTO"

# Save research template to file
python3 tools/contact-finder-v2.py --company "Gitcoin" --save
```

## Output Example

```
🔍 Contact Finder: Uniswap
============================================================

📋 Search Queries to Execute:
============================================================
1. Uniswap CTO
2. Uniswap VP Engineering
3. Uniswap Head of Platform
4. Uniswap engineering lead
5. Uniswap technical founder
6. Uniswap engineering blog

============================================================
⚠️  Note: Web search requires Brave API key
⚠️  Run: openclaw configure --section web
============================================================

💾 Creating research template...
✅ Saved: /home/node/.openclaw/workspace/data/contacts/uniswap-research.md

🎯 Next Steps:
1. Use Brave search to find actual contacts
2. Verify information (Twitter, GitHub, LinkedIn)
3. Update research file with contact details
4. Craft personalized message
5. Send via service-outreach-sender.py
```

## How It Works

1. **Parses company name:** Cleans input (removes Inc, LLC, etc.)
2. **Generates queries:** Creates 6 search patterns (CTO, VP Eng, Head of Platform, etc.)
3. **Creates research file:** Generates markdown template with:
   - Contact placeholders (name, role, social profiles)
   - Outreach strategy (value proposition, pain points)
   - Next steps (verification, research, messaging)

## Search Templates

| Role | Search Query |
|------|--------------|
| CTO | `{company} CTO` |
| VP Engineering | `{company} VP Engineering` |
| Platform Lead | `{company} Head of Platform` |
| Engineering Lead | `{company} engineering lead` |
| Founder | `{company} technical founder` |
| Team | `{company} engineering blog` |

## Research File Format

Generated `/data/contacts/{company}-research.md` includes:

```markdown
# {Company} Contact Research

> Generated: 2026-02-04
> Status: Contact discovery initiated

## Identified Contacts

### [Name] - [Role]

- **Company:** {Company}
- **Role:** {Role}
- **Twitter:** @handle
- **GitHub:** @handle
- **LinkedIn:** linkedin.com/in/handle

## Outreach Strategy

**Value Proposition:** Multi-agent automation for engineering workflows

**Pain Points to Address:**
- Scalability bottlenecks
- Manual review processes
- Community management overhead
- CI/CD optimization

**Message Variant:** Pain-first (research → specific pain → solution)

## Next Steps
1. Verify contact information
2. Research recent activity (tweets, GitHub contributions)
3. Identify specific pain points from public content
4. Craft personalized message
5. Send via appropriate channel
```

## Workflow

1. **Generate queries:** `contact-finder-v2.py --company "X" --save`
2. **Manual search:** Use queries with Brave search to find contacts
3. **Update research:** Fill in contact details (Twitter, GitHub, LinkedIn)
4. **Craft message:** Use value-first framework (research → pain → solution)
5. **Send outreach:** `service-outreach-sender.py --prospect X --send`

## Files

- **Tool:** `/home/node/.openclaw/workspace/tools/contact-finder-v2.py`
- **Research output:** `/home/node/.openclaw/workspace/data/contacts/{company}-research.md`
- **Service prospects:** `/home/node/.openclaw/workspace/data/service-prospects.md`

## Integration with Service Pipeline

Part of the service business pipeline:

1. **contact-finder-v2.py** → Discover contacts
2. **Manual research** → Verify info, find pain points
3. **Craft message** → Value-first, specific, personalized
4. **service-outreach-sender.py** → Send message
5. **revenue-tracker.py** → Track pipeline status

## Limitations

- **Web search not integrated:** Currently generates queries only (manual search required)
- **No automated discovery:** Must manually find and verify contacts
- **Static templates:** Queries are pre-defined, not adaptive

**Future improvements:**
- Integrate Brave Search API for automated contact discovery
- Scrape company websites for team pages
- Verify social profiles automatically
- Calculate confidence scores based on data quality

## Related Tools

- `service-outreach-sender.py` — Send outreach messages
- `contact-researcher.py` — Batch contact research pipeline
- `service-proposal-templates.md` — Proposal templates
- `revenue-tracker.py` — Pipeline tracking

## Author

Nova (2026-02-04)
