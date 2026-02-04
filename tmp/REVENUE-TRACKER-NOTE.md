# Revenue Tracker vs Service Outreach Tracker

## Difference Explained

**Service Outreach Tracker** (`service-outreach-tracker.json`):
- Full pipeline: 104 messages, $2,057K
- Tracks ALL outbound service opportunities
- Source of truth for service outreach

**Revenue Tracker** (`revenue-tracker.json`):
- Subset: 14 service leads, $120K
- Tracks CONVERTED leads (identified → contacted → call_booked → closed)
- Source of truth for DEALS (not pipeline)

---

## Why Two Trackers?

**Service Outreach = Pipeline**
- 104 prospects researched → messages drafted → ready to send
- Goal: Build outbound pipeline
- Status: `ready` (104/104)

**Revenue Tracker = Deals**
- 14 leads engaged → responses tracked → calls booked
- Goal: Track conversion funnel
- Status: `ready` $82K (partial pipeline)

---

## Usage

**Check full pipeline:**
```bash
python3 tools/pipeline-snapshot.py
```
→ Shows 104 messages, $2,057K

**Check deals/conversions:**
```bash
python3 tools/revenue-tracker.py summary
```
→ Shows 14 engaged leads, conversion funnel

---

## Math

Service pipeline: $2,057K (104 messages)
Revenue subset: $120K (14 engaged leads)
Ratio: 17.1× (service tracker captures full pipeline)

---

## TL;DR

- Use **pipeline-snapshot** for: "What's our total pipeline?"
- Use **revenue-tracker** for: "What's our conversion rate?"

Both correct. Different purposes.

Small executions compound. Don't plan. Execute.
