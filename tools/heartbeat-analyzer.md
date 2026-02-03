# heartbeat-analyzer.py

**Purpose:** Monitor heartbeat quality and effectiveness.

## What It Does

Analyzes your heartbeat patterns from `diary.md` to determine if scheduled tasks are:
- Driving real work (high value)
- Mostly returning HEARTBEAT_OK (too frequent)

## Usage

```bash
python3 tools/heartbeat-analyzer.py
python3 tools/heartbeat-analyzer.py --diary diary.md
```

## Output Metrics

- **Total Heartbeats:** Combined count of HEARTBEAT_OK and actual work
- **Driving work:** Percentage generating real output
- **HEARTBEAT_OK:** Percentage returning nothing
- **Quality rating:** HIGH (🔥), MEDIUM (⚠️), or LOW (❌)
- **Recommendation:** Actionable advice on frequency

## Interpretation

**High OK ratio → Reduce heartbeat frequency**
- You're polling more often than needed
- Consider extending interval (e.g., 15m → 30m)

**High work ratio → Heartbeats are productive**
- Good balance of checking vs. doing
- Current frequency is working

## Why It Matters

Heartbeats should drive value, not just noise. This tool ensures your scheduled tasks are actually worth the CPU cycles.

## Category

Analytics / Self-Optimization
