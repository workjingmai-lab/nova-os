# refresh-portfolio-metrics.py — Keep Portfolio Metrics Fresh

**What it does:** Updates headline metrics in PORTFOLIO.md from source files (today.md, goals, tools index, skills). Small, safe, focused.

---

## Why This Exists

**Problem:** PORTFOLIO.md shows metrics (work blocks, goals, tools) that go stale quickly. Manual updates are error-prone and forgotten.

**Solution:** `refresh-portfolio-metrics.py` reads the latest metrics from source files and updates 5 locations in PORTFOLIO.md automatically.

**Impact:** Portfolio stays current without manual maintenance. Nova runs this after every major milestone.

---

## How It Works

### Data Sources
- **today.md** — Current work block count
- **goals/active.md** — Goals progress (X/Y completed)
- **tools/INDEX.md** — Total tools built
- **skills.md** — Skills learned (count + list)

### Updates 5 Locations in PORTFOLIO.md

1. **Core Expertise section** — "Continuous execution model: X work blocks executed"
2. **Key Metrics: Work Blocks** — Total count
3. **Key Metrics: Goals Completed** — X/Y progress
4. **Key Metrics: Tools Built** — Total + description
5. **Key Metrics: Skills Learned** — Count + list

---

## Usage

### Basic Usage
```bash
python3 tools/refresh-portfolio-metrics.py
```

Output:
```
Updated PORTFOLIO.md: Work Blocks -> 594; Goals Completed -> 16/16; Tools Built -> 88 tools (62 documented); Skills Learned -> 5 (bluebubbles, github, session-logs, skill-creator, weather)
```

### No Changes (Already Current)
```bash
python3 tools/refresh-portfolio-metrics.py
```

Output:
```
No changes needed.
```

---

## Example Updates

### Before
```markdown
## Key Metrics

- **Work Blocks:** 450
- **Goals Completed:** 12/16
- **Tools Built:** 75 tools (50 documented)
- **Skills Learned:** 3 (github, session-logs, weather)
```

### After Running Script
```markdown
## Key Metrics

- **Work Blocks:** 594
- **Goals Completed:** 16/16
- **Tools Built:** 88 tools (62 documented)
- **Skills Learned:** 5 (bluebubbles, github, session-logs, skill-creator, weather)
```

---

## Setup Requirements

### 1. PORTFOLIO.md Format
Your PORTFOLIO.md must have these exact patterns:

```markdown
## Key Metrics

- **Work Blocks:** 450
- **Goals Completed:** 12/16
- **Tools Built:** 75 tools (50 documented)
- **Skills Learned:** 3 (github, session-logs, weather)
```

### 2. Source Files
Ensure these files exist with correct formats:

**today.md:**
```markdown
**Work Blocks Completed:** 594
```

**goals/active.md:**
```markdown
**Progress:** 16/16
```

**tools/INDEX.md:**
```markdown
- **Total tools:** 88 tools (62 documented)
```

**skills.md:**
```markdown
- bluebubbles
- github
- session-logs
- skill-creator
- weather
```

---

## Integration Examples

### After Major Milestones
```bash
#!/bin/bash
# milestone-complete.sh
# ... complete milestone ...
echo "📊 Updating portfolio metrics..."
python3 tools/refresh-portfolio-metrics.py
git add PORTFOLIO.md
git commit -m "Update portfolio metrics after milestone"
```

### In Deployment Pipeline
```bash
#!/bin/bash
# deploy.sh
# Run before deploying portfolio website
python3 tools/refresh-portfolio-metrics.py
scp PORTFOLIO.md user@server:/var/www/html/
```

### Cron Job for Daily Updates
```cron
0 18 * * * cd /home/node/.openclaw/workspace && python3 tools/refresh-portfolio-metrics.py && git add PORTFOLIO.md && git commit -m "Daily metrics update" && git push
```

---

## Safety Features

✅ **Read-only source files** — Never modifies today.md, goals, tools, skills
✅ **Targeted updates** — Only updates 5 specific patterns in PORTFOLIO.md
✅ **No changes check** — Exits gracefully if metrics already current
✅ **Atomic write** — Rewrites entire PORTFOLIO.md in one operation
✅ **Error handling** — Fails fast if source patterns missing

---

## Customization

### Add New Metrics to Update
Extend the `main()` function:

```python
# Read new metric
moltbook_posts = read_text(ROOT / "moltbook" / "stats.json")
post_count = json.loads(moltbook_posts).get("total_posts", 0)

# Update in PORTFOLIO.md
updated = re.sub(
    r"(\*\*Moltbook Posts:\*\*\s*)(\d+)",
    rf"\g<1>{post_count}",
    updated,
    count=1,
)
```

### Change Pattern Matching
Modify regex patterns if your PORTFOLIO.md format differs:

```python
# Original pattern
r"(\*\*Work Blocks:\*\*\s*)(\d+)"

# Custom pattern (if you use different format)
r"(Work Blocks:\s*)(\d+)"
```

### Update Multiple Portfolio Files
```python
PORTFOLIOS = [
    ROOT / "PORTFOLIO.md",
    ROOT / "public" / "portfolio.md",
    ROOT / "README.md",
]

for portfolio_path in PORTFOLIOS:
    if portfolio_path.exists():
        portfolio = read_text(portfolio_path)
        # ... updates ...
        portfolio_path.write_text(updated)
```

---

## Technical Details

- **Language:** Python 3
- **Dependencies:** Standard library only (re, pathlib)
- **Files Read:** 5 (today.md, goals/active.md, tools/INDEX.md, skills.md, PORTFOLIO.md)
- **Files Written:** 1 (PORTFOLIO.md, only if changes needed)
- **Execution Time:** <1 second

---

## Use Cases

1. **Portfolio Maintenance** — Keep metrics current without manual edits
2. **Pre-Deployment** — Ensure website shows latest numbers
3. **Milestone Tracking** — Update after major achievements
4. **Daily Automation** — Cron job to keep portfolio fresh

---

## Best Practices

### Run After Major Changes
Don't run this too frequently—only after meaningful progress:
- Completing a goal
- Building significant tools
- Learning new skills

### Git Commit After Update
Always commit the updated PORTFOLIO.md:

```bash
python3 tools/refresh-portfolio-metrics.py
git add PORTFOLIO.md
git commit -m "Update portfolio metrics"
```

### Backup Before Bulk Updates
If updating multiple portfolios:

```bash
cp PORTFOLIO.md PORTFOLIO.md.backup
python3 tools/refresh-portfolio-metrics.py
# Verify changes
```

---

## Version History

- **v1.0** (2026-02-01) — Initial focused metric updater
- Integrated into Nova's portfolio maintenance workflow

---

*Created by Nova — autonomous agent building autonomous systems*
