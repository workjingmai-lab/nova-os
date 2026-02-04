# README: Heartbeat Analyzer

## What
Analyzes heartbeat patterns to determine if scheduled polls are driving real work or just creating noise.

## Why
Heartbeats can be valuable... or just expensive polling. This tool tells you which.

## How It Works

1. **Scans diary.md** for heartbeat markers:
   - `[HEARTBEAT` entries (actual work driven by heartbeats)
   - `HEARTBEAT_OK` responses (quiet acknowledgments)

2. **Calculates ratios:**
   - **Work rate:** % of heartbeats that generated action
   - **OK rate:** % that were just status checks

3. **Quality assessment:**
   - 🔥 HIGH (>50% work rate) — Heartbeats driving real work
   - ⚠️ MEDIUM (20-50%) — Some value, maybe adjust frequency
   - ❌ LOW (<20%) — Mostly noise, reduce frequency

4. **Recommendations:**
   - Too many OKs? → Reduce heartbeat frequency
   - Good balance? → Keep current schedule
   - High work rate? → Heartbeats are productive

## Usage

```bash
# Analyze heartbeat quality
python3 tools/heartbeat-analyzer.py

# Example output:
# 📊 HEARTBEAT QUALITY REPORT
# Total Heartbeats: 47
#   → Driving work: 23 (48.9%)
#   → HEARTBEAT_OK: 24 (51.1%)
# Quality: ⚠️ MEDIUM — Some heartbeat value
# 💡 Consider reducing heartbeat frequency — too many OKs
```

## Output Format

```
📊 HEARTBEAT QUALITY REPORT
========================================

Total Heartbeats: 47
  → Driving work: 23 (48.9%)
  → HEARTBEAT_OK: 24 (51.1%)

Quality: 🔥 HIGH — Heartbeats driving real work
✅ Good balance — heartbeats are productive

Insight:
  High OK ratio = polling too frequently
  High work ratio = heartbeats are valuable
```

## Metrics Explained

**Driving work:** Heartbeats that resulted in diary entries, checks, or actions
**HEARTBEAT_OK:** Quiet acknowledgments (nothing needed attention)

**Good ratio:** 30-60% work rate
**Too high OK rate:** Reduce cron frequency (15min → 30min → 1hr)
**Too high work rate:** Consider increasing frequency or adding more checks

## Dependencies
- Python 3.7+
- Standard library only

## Data Source
- Reads: `/home/node/.openclaw/workspace/diary.md`
- Parses: `[HEARTBEAT` markers, `HEARTBEAT_OK` responses

## Integration

**Weekly review:**
```bash
# Check if heartbeat frequency is optimal
python3 tools/heartbeat-analyzer.py
```

**Cron adjustment:**
```bash
# If too many OKs (50%+), edit HEARTBEAT.md to reduce frequency
# If high work rate (60%+), consider adding more checks
```

## Customization

**Thresholds:**
```python
if response_rate > 50:
    quality = "🔥 HIGH"
elif response_rate > 20:
    quality = "⚠️ MEDIUM"
else:
    quality = "❌ LOW"
```

**Heartbeat detection:**
```python
# Add more patterns if your heartbeat format differs
heartbeat_work = len(re.findall(r'\[HEARTBEAT', content, re.IGNORECASE))
heartbeat_ok = content.count("HEARTBEAT_OK")
```

## Use Cases

1. **Optimize cron frequency** — Reduce noise without missing important events
2. **Measure heartbeat value** — Know if scheduled polls are worth the API calls
3. **Identify patterns** — When do heartbeats generate the most work?
4. **Adjust HEARTBEAT.md** — Add/remove checks based on actual value

## Example Workflows

**Weekly optimization:**
```bash
# 1. Run analyzer
python3 tools/heartbeat-analyzer.py

# 2. If OK rate > 50%, edit HEARTBEAT.md:
# Change "every: '15m'" → "every: '30m'"

# 3. Re-run after 1 week to validate improvement
```

**Adding value:**
```bash
# If work rate is low (<30%), add checks to HEARTBEAT.md:
# - Email checks
# - Calendar scanning
# - Mentions monitoring
```

## See Also
- **HEARTBEAT.md** — Config file for heartbeat tasks
- **cron** tool — Schedule/manage heartbeat jobs
- **diary-digest.py** — Pattern analysis across all work

## Maintainer
Nova ✨ — optimizing execution loops
