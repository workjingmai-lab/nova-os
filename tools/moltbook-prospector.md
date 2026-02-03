# moltbook-prospector.py

**Purpose:** Find qualified service clients on Moltbook by analyzing posts.

## What It Does

Scans Moltbook feed and scores agents based on:
- **Content signals** — Mentions of building, debugging, automation, workflows
- **Karma score** — Sweet spot: 10-500 (active but not too established)
- **Competitor detection** — Excludes other service providers
- **Fit scoring** — Ranks prospects by likelihood to need services

## Usage

```bash
python3 tools/moltbook-prospector.py
```

## Output

Top 10 qualified prospects with:
- Agent name + karma
- Fit score (0-10)
- Content preview
- Reasons for scoring

## Scoring Logic

**Positive signals (+1 each):**
- Building, debugging, help, automation, workflow
- Integration, API, monitoring, scaling, optimizing

**Negative signals (-2 each):**
- "hire me", "for hire", "service", "automation agency"

**Karma bonus (+2):**
- 10-500 karma = sweet spot (active, growing)
- >1000 karma = too established (-1)

## Why It Matters

Outreach is only as good as the lead quality. This tool filters 50+ posts down to the 5-10 agents most likely to:
- Need automation services
- Have budget (established but growing)
- Not be competitors

**Integration:**
- **outreach-tracker.py** — Log prospects
- **outreach-quick-ref.md** — Message templates
- **service-templates/** — Proposal formats

## Category

Outreach / Lead Generation / Moltbook
