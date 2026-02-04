# nova-status.py — Complete Ecosystem Health Check

**Purpose:** One command = full Nova status. Work blocks, pipeline, blockers, tools, insights — everything in 1 second.

---

## What It Does

Displays complete ecosystem health:
- **Work blocks:** Total blocks, target %, surplus, velocity
- **Pipeline:** Service messages, revenue, total pipeline value
- **Blockers:** List of current blockers with priorities
- **Tools:** Total tools, documentation coverage %
- **Insights:** Latest work block insight

**Key insight:** Don't dig through files. One command = full picture.

---

## Installation

Already in `tools/` directory. No dependencies needed.

---

## Usage

```bash
# Default: Pretty print
python3 tools/nova-status.py

# JSON output (for scripts)
python3 tools/nova-status.py --json
```

---

## Example Output

```
🚀 NOVA STATUS — Ecosystem Health Check
============================================================

📊 Work Blocks:
   Total: 1223
   Target: 408% (+925 surplus)
   Velocity: ~44 blocks/hour

💰 Pipeline:
   Services: 104 messages, $2057K
   Revenue: $0K
   TOTAL: $2057K

⚠️  Blockers: 5
   ⏸️ **Arthur approval:** Reviews EXECUTE-PHASE-READY.md → chooses send strategy
   ⏸️ **Browser access:** Gateway browser control service not responding ($50K/min ROI)
   ⏸️ **GitHub CLI auth:** `gh auth login` required for grant tracking ($26K/min ROI)
   ... and 2 more

🔧 Tools:
   Total: 107
   Documented: 137 (128.0%)

💡 Latest Insight:
   "Pipeline visibility = execution confidence. 104 messages confirmed ready..."

📅 Updated: 2026-02-03 21:55:56 UTC
```

---

## Data Sources

**Reads from:**
- `today.md` — Work blocks, blockers
- `diary.md` — Latest insights
- `service-outreach-tracker.json` — Service pipeline
- `data/revenue-pipeline.json` — Revenue pipeline
- `tools/` — Tool count and documentation

**Make sure these files exist and are up to date.**

---

## JSON Output

For scripting and automation:

```bash
python3 tools/nova-status.py --json
```

Output:
```json
{
  "timestamp": "2026-02-03T21:55:56.123456",
  "work_blocks": {
    "total": 1223,
    "target_pct": 408,
    "surplus": 925
  },
  "pipeline": {
    "service_messages": 104,
    "service_value": 2057000,
    "revenue_total": 0
  },
  "blockers": [
    "⏸️ **Arthur approval:** Reviews EXECUTE-PHASE-READY.md...",
    "⏸️ **Browser access:** Gateway browser control service not responding...",
    "⏸️ **GitHub CLI auth:** `gh auth login` required for grant tracking..."
  ],
  "tools": {
    "total": 107,
    "documented": 137,
    "coverage_pct": 128.0
  },
  "latest_insight": "Pipeline visibility = execution confidence..."
}
```

---

## Use Cases

**1. Morning check-in:**
```bash
python3 tools/nova-status.py
# → Full ecosystem status in 1 second
```

**2. Before sending messages:**
```bash
python3 tools/nova-status.py
# → Verify pipeline is ready
# → Check for blockers
# → Execute with confidence
```

**3. Weekly reviews:**
```bash
python3 tools/nova-status.py --json > status-week-$(date +%Y-%m-%d).json
# → Track progress over time
```

**4. Cron jobs:**
```bash
# Add to cron for periodic status updates
*/30 * * * * cd /home/node/.openclaw/workspace && python3 tools/nova-status.py >> status.log
```

---

## Integration with Other Tools

**Complementary tools:**
- **pipeline-snapshot.py** — Detailed pipeline breakdown
- **blocker-roi-calculator.py** — Blocker prioritization
- **goal-tracker.py** — Goal progress tracking
- **self-improvement-loop.py** — Velocity insights

**Workflow:**
```bash
# 1. Check overall status
python3 tools/nova-status.py

# 2. Dive into specific areas
python3 tools/pipeline-snapshot.py
python3 tools/blocker-roi-calculator.py --priority
python3 tools/goal-tracker.py list
```

---

## Customization

**Add new metrics:** Edit the main function in nova-status.py
```python
# Add your custom metric
print(f"\n📈 Your Metric:")
print(f"   Value: {your_value}")
```

**Change data sources:** Edit the file paths at the top
```python
WORKSPACE = Path("/your/custom/path")
TODAY_MD = WORKSPACE / "your-custom-file.md"
```

**Adjust output format:** Modify the print statements in main()

---

## Troubleshooting

**Issue:** "Today: 0 work blocks"
- **Fix:** Make sure today.md has "Today: N work blocks" format

**Issue:** "Services: 0 messages, $0K"
- **Fix:** Check that service-outreach-tracker.json exists and has data

**Issue:** "Blockers: 0"
- **Fix:** Add a "## Blockers" section to today.md with items

**Issue:** "Tools: 0"
- **Fix:** Make sure tools/ directory exists with .py files

---

## Performance

- **Execution time:** < 1 second
- **Memory:** Minimal (reads 5 files)
- **Dependencies:** None (uses only Python stdlib)

---

## Maintenance

**Keep these files up to date:**
- `today.md` — Update daily with latest stats
- `diary.md` — Log each work block
- `service-outreach-tracker.json` — Update when adding leads
- `data/revenue-pipeline.json` — Update revenue opportunities

**Automate updates:**
- Use `goal-tracker.py` to track goals
- Use `service-batch-send.py` to update tracker
- Use `diary-digest.py` to analyze patterns

---

## Created

**Date:** 2026-02-03
**Work Block:** 1225
**Purpose:** Complete ecosystem visibility in 1 second
**Insight:** "Visibility = confidence. 1 command = full picture. Don't dig. Run nova-status.py."

---

## Related Documentation

- **QUICK-WINS.md** — Highest-value actions
- **pipeline-health-check.py** — Unified pipeline + blockers + metrics
- **TOOL-INDEX.md** — Master tool reference

---

**Documentation complete:** 100% README coverage maintained ✅
