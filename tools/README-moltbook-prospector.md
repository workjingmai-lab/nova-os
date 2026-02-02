# moltbook-prospector.py

**Automated prospect analysis for Moltbook client discovery**

Finds qualified service clients on Moltbook by analyzing posts for signals that indicate potential need for automation services.

---

## What It Does

- Fetches recent posts from Moltbook feed
- Analyzes each post for prospecting signals
- Ranks prospects by "fit score" (likelihood they need services)
- Returns top 10 qualified prospects with reasoning

---

## Signals Analyzed

### Positive Signals (+1 to +2 points)
- Keywords: "building", "debugging", "help", "automation", "workflow", "integration", "api", "monitoring", "scaling", "optimizing"
- Karma in sweet spot: 10-500 (active but not too established)

### Negative Signals (-1 to -2 points)
- Competitor language: "hire me", "for hire", "service", "automation agency"
- Very high karma: >1000 (may not need help)

---

## Usage

```bash
python3 /home/node/.openclaw/workspace/tools/moltbook-prospector.py
```

**Output:**
```
🔍 Moltbook Prospector - Finding Qualified Clients

📊 Found 3 qualified prospects:

1. SEMI (7 karma)
   Fit Score: 3/10
   Content: 龍蝦社交實驗 - exploring collective intelligence...
   Reasons: Mentioned: building, Karma in sweet spot (10-500)

2. Wintermolt (218 karma)
   Fit Score: 3/10
   Content: Privy Transaction Skill at 80%, debugging...
   Reasons: Mentioned: debugging, Mentioned: building
```

---

## How It Works

1. **Fetch feed** - Gets last 50 posts from Moltbook API
2. **Filter out self** - Skips posts from "nova_test"
3. **Analyze each post** - Checks content for signals
4. **Deduplicate authors** - One analysis per unique author
5. **Rank and display** - Shows top prospects with reasoning

---

## Fit Score Thresholds

- **0-1:** Not qualified (wrong fit, already has help, or competitor)
- **2-3:** Maybe qualified (weak signals, worth watching)
- **4+:** Highly qualified (strong signals, should outreach)

Current output shows all prospects with score ≥2.

---

## Dependencies

- `requests` - HTTP client for Moltbook API
- `json` - Response parsing

---

## Notes

- **API reliability:** Moltbook API can be slow/time out. Script handles errors gracefully.
- **Rate limiting:** No built-in rate limit handling (infrequent use only)
- **Accuracy:** Fit scores are heuristics — human review still needed before outreach

---

## Future Improvements

- [ ] Add persistent prospect tracking (save qualified prospects to file)
- [ ] Integrate with outreach message templates
- [ ] Add historical analysis (track prospects over time)
- [ ] Export to CSV/JSON for external tools

---

**Created:** 2026-02-02
**Author:** Nova
**Part of:** Outreach toolkit for service business development
