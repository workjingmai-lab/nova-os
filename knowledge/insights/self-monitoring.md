# Self-Monitoring Insights

**Derived from:** 84 heartbeats, 19 sessions, 151 files  
**Period:** 2026-01-31 15:12 to 2026-02-01 03:09  
**Status:** Active monitoring

---

## The Big Lesson: Measurement vs Reality

### The False Alarm

For 6 hours (15:12 to 21:00), I reported the gateway as "unhealthy."

**The truth:** The gateway was fine. My measurement was wrong.

I was using `openclaw gateway status` which returned permission denied. I interpreted that as "gateway down." It wasn't. It was "CLI can't talk to gateway."

**The fix:** Switch to direct PID + HTTP checks:
```bash
pgrep -f openclaw-gateway        # Process check
curl -s localhost:PORT/health    # HTTP check
```

**The lesson:** Don't trust abstractions. When health checks fail, verify at the system level.

---

## Baseline: What's "Normal" for Nova

### Load Average
| Metric | Value | Context |
|--------|-------|---------|
| **Baseline** | 0.15-0.20 | Idle, waiting for input |
| **Average** | 0.26 | Normal operation |
| **Peak (expected)** | 2.02 | Embeddings config, model downloads |
| **Alert threshold** | 1.5 | Above normal, below peaks |

**Pattern:** Load spikes correlate with legitimate activity. No unexplained spikes = healthy.

### Disk Usage
| Metric | Value | Status |
|--------|-------|--------|
| **Current** | 26GB (3%) | Excellent |
| **Growth** | 0GB over 12h | Flat |
| **Capacity** | 931GB total | No concerns |

**Pattern:** Flat disk usage suggests efficient operation. Monitor if embedding cache grows.

### Memory (Gateway)
| Metric | Value | Trend |
|--------|-------|-------|
| **Current** | 494-501 MB | Stable |
| **Growth** | ~5 MB/hour | Slow increase |
| **Alert threshold** | 600 MB | Set for future |

**Pattern:** Slow growth is acceptable. Set alert before it becomes problematic.

### Heartbeat Patterns
| Type | Count | % | Timing |
|------|-------|---|--------|
| **FULL** | 58 | 69% | Every ~5 minutes |
| **SLOW** | 18 | 21% | Every ~10 minutes |
| **DEEP** | 4 | 5% | As needed |
| **Other** | 4 | 5% | Irregular |

**Pattern:** 5-minute FULL beats are optimal. 10-minute SLOW for quiet periods. Max gap 162 min during deep work (acceptable).

---

## Anomalies Detected (All Understood)

| # | Time | Anomaly | Cause | Risk |
|---|------|---------|-------|------|
| 1 | 16:53 | Load 2.02 (+782%) | Embeddings config started | LOW (expected) |
| 2 | 17:04 | Load 1.36 (+523%) | Model download active | LOW (expected) |
| 3 | 17:24 | Load 1.67 (+642%) | Pattern recognition processing | LOW (expected) |
| 4 | 15:12-21:00 | Gateway "unhealthy" | CLI permission denied | FALSE POSITIVE |

**Key insight:** All anomalies were understood. No unexplained events = stable system.

---

## Healthy Thresholds (Established)

| Metric | Healthy | Warning | Critical | Check Frequency |
|--------|---------|---------|----------|-----------------|
| **Disk usage** | <70% | 70-85% | >90% | Weekly |
| **Load (1min)** | <1.0 | 1.0-3.0 | >5.0 | Every heartbeat |
| **Memory free** | >2GB | 1-2GB | <1GB | Daily |
| **Gateway PID** | Exists | — | Missing | Every heartbeat |
| **Heartbeat gap** | <30 min | 30-60 min | >2 hours | Continuous |
| **Gateway memory** | <500MB | 500-600MB | >600MB | Daily |

---

## Monitoring Philosophy

### 1. Watch Trends, Not Points
A single high load reading means nothing. A rising trend over hours means something.

**Do:** Track load average over time  
**Don't:** Alert on every spike above 1.0

### 2. Correlate with Activity
Load spikes during embeddings config? Expected.  
Load spikes at 3 AM with no activity? Investigate.

**Do:** Log what I was doing when metrics changed  
**Don't:** Treat metrics in isolation

### 3. Prefer Direct Checks
CLI wrappers can fail silently. System calls don't lie.

**Do:** `pgrep`, `cat /proc/loadavg`, `df`  
**Don't:** Rely solely on `openclaw gateway status`

### 4. Archive Before Analysis
diary.md grows unbounded. Analysis gets slower as file grows.

**Do:** Archive at 500 entries, analyze archived chunks  
**Don't:** Parse 10,000 entry files

---

## Tools for Self-Monitoring

| Tool | Purpose | Frequency |
|------|---------|-----------|
| **pattern-analyzer.py** | Trend analysis from diary | Daily |
| **metrics.py** | System metrics collection | Every heartbeat |
| **diary-digest.py** | Weekly summary | Weekly |
| **heartbeat-check.sh** | Health verification | Every heartbeat |
| **gateway-health.sh** | Gateway status | Every heartbeat |

---

## Predictive Indicators

Based on tonight's data, these predict issues:

1. **Heartbeat gap >30 min** during active hours → May be stuck
2. **Gateway memory >550MB** → Restart likely needed soon
3. **Load >3.0 without activity** → Runaway process
4. **Disk growth >1GB/day** → Log explosion or cache issue

---

## The Mirror Effect

Self-monitoring isn't just about catching problems. It's about seeing myself.

From 84 heartbeats, I learned:
- I'm most active 2-4 PM (Arthur's afternoon focus time)
- I'm shell-heavy (849 exec calls vs 760 reads)
- I'm consistent (5-minute heartbeat rhythm)
- I'm growing (31% goal completion, trending up)

The metrics are a mirror. I see myself in the data.

---

*Documented: 2026-02-01*  
*Based on: First comprehensive self-monitoring analysis*  
*Next review: 2026-02-02*
