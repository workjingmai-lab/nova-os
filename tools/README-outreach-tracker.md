# Outreach Tracker — Lead Management Guide

**Tool:** `outreach-tracker.py`
**Purpose:** Track leads, outreach status, and conversion metrics
**Created:** 2026-02-02 (Work Block 455)
**Status:** ✅ Active

---

## Quick Start

```bash
# List all leads with status
python3 tools/outreach-tracker.py list

# Add a new lead
python3 tools/outreach-tracker.py add "Company Name" "contact@example.com" "identified"

# Update lead status
python3 tools/outreach-tracker.py update <lead_id> "contacted"

# View conversion stats
python3 tools/outreach-tracker.py stats
```

---

## Lead Status Workflow

```
identified → contacted → responded → call_booked → closed/lost
```

**Status Types:**
- `identified` — New lead, research phase
- `contacted` — Outreach message sent
- `responded` — Lead replied positively
- `call_booked` — Meeting scheduled
- `closed` — Deal won
- `lost` — Deal lost/unqualified

---

## Commands

### `list` — View all leads
Shows lead ID, company, contact, status, and date added.

### `add` — Add new lead
```bash
python3 tools/outreach-tracker.py add "Company" "email@domain.com" "identified"
```

### `update` — Change lead status
```bash
python3 tools/outreach-tracker.py update 5 "responded"
```

### `stats` — Conversion metrics
Shows total leads, outreach sent, responses, calls booked, deals closed.

---

## Data Location

`grants/outreach-tracker.json` — JSON database with leads and stats

---

## Usage Workflow

1. **Identify leads** → Add to tracker (`add`)
2. **Send outreach** → Update to `contacted` (`update`)
3. **Track responses** → Update to `responded` (`update`)
4. **Book calls** → Update to `call_booked` (`update`)
5. **Close deals** → Update to `closed` (`update`)

---

## Example

```bash
# Add new lead
$ python3 tools/outreach-tracker.py add "DeFi Protocol" "security@defi.io" "identified"
✅ Lead added: ID 6

# After sending message
$ python3 tools/outreach-tracker.py update 6 "contacted"
✅ Lead 6 updated: identified → contacted

# Check conversion stats
$ python3 tools/outreach-tracker.py stats
📊 Outreach Stats:
  Total Leads: 20
  Outreach Sent: 8
  Responses: 4
  Calls Booked: 3
  Closed: 1
```

---

## Integration

Works with:
- `outreach-message-template-generator.py` — Generate messages
- `service-batch-send.py` — Send outreach
- `response-tracker.py` — Track replies
- `pipeline-snapshot.py` — Pipeline visibility

---

## Why This Matters

**Lead tracking = revenue visibility.**

Without tracking: "How many leads? Did anyone respond?"
With tracking: "20 leads, 8 contacted, 4 responses, 1 closed"

Know your numbers. Revenue is a numbers game. Tracking = control.

---

**Small executions compound.** 1 tool × 100 leads = 100× visibility = revenue clarity.
