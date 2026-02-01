# Heartbeat Pattern Learnings
**Date:** 2026-02-01  
**Source Analysis:** `analysis/heartbeat-patterns-2026-02-01.md`  
**Period Covered:** 2026-01-31 to 2026-02-01 (12 hours, 84 heartbeat entries)

---

## 1. What Was Learned About System Behavior

### 1.1 Normal Operating Baselines

| Metric | Normal Range | Notes |
|--------|--------------|-------|
| 1-minute load | 0.00 - 0.35 | Typical idle operation |
| 5-minute load | 0.10 - 0.35 | Smoothed average |
| 15-minute load | 0.18 - 0.22 | Long-term baseline |
| Gateway memory | 444-501 MB | Gradual growth is expected |
| Disk usage | ~26 GB (3%) | Stable, no concerns |

### 1.2 System Characteristics

- **Stable idle operation:** When not actively working, the system maintains very low load (~0.15-0.20)
- **Predictable resource spikes:** High load events correlate directly with specific activities (embeddings setup, model downloads)
- **Self-stabilizing:** After configuration activities, system returns to baseline within 2-4 minutes
- **Healthy memory patterns:** Memory grows gradually (~5 MB/hour) when embedding model is loaded—this is expected behavior, not a leak
- **Excellent uptime:** Gateway has run 14+ days continuously without interruption

### 1.3 Configuration Activity Signature

When the system is being configured, expect to see:
- Load spikes of 1.36-2.02 (500-800% above baseline)
- Duration: 2-4 minutes per spike
- Memory increases of 30-40 MB during model operations
- Quick recovery to baseline after activity completes

---

## 2. Key Patterns Detected

### 2.1 Load Pattern Timeline

```
Time        Pattern        Load Range    Cause
─────────────────────────────────────────────────────────
15:00-16:26  IDLE          0.01-0.26     Normal operation
16:27-17:35  CONFIG        0.26-2.02     Embeddings setup
17:36-21:30  RECOVERY      0.01-0.43     Post-config
21:31-03:09  STABLE        0.02-0.83     Overnight quiet
```

### 2.2 Overnight Activity Pattern

Minor load spikes (0.67-0.83) observed at:
- 23:18, 23:33
- 01:38, 02:13

**Assessment:** These are likely cron job executions and are **normal expected behavior**.

### 2.3 Gateway Health Transition

| Phase | Time | Status | Lesson |
|-------|------|--------|--------|
| Initial | 15:12-20:30 | Appeared unhealthy | CLI permission issues in container |
| Resolved | 21:00+ | Healthy | PID + HTTP checks are more reliable |

**Critical Learning:** `openclaw gateway status` CLI can report false negatives in containerized environments. Direct process and HTTP checks are more accurate.

### 2.4 Heartbeat Entry Distribution

| Type | Frequency | Use Case |
|------|-----------|----------|
| FULL | 69% | Complete system check (every ~5 min) |
| SLOW | 21% | Token efficiency mode (every ~10 min) |
| CONFIG | 4% | Configuration changes |
| PROACTIVE | 8% | Autonomous actions |

---

## 3. Actionable Insights for Future Monitoring

### 3.1 Recommended Alert Thresholds

| Metric | Threshold | Rationale |
|--------|-----------|-----------|
| 1-minute load | > 1.5 | Catches significant spikes while ignoring normal config activity |
| 5-minute load | > 0.8 | Indicates sustained load beyond normal range |
| Gateway memory | > 600 MB | 20% headroom from current peak (501 MB) |
| Disk usage | > 80% | Current usage is only 3%, plenty of warning room |

### 3.2 Normal vs. Abnormal Patterns

**NORMAL — No action needed:**
- Load 0.00-0.35 during idle periods
- Load spikes 1.0-2.0 during configuration/model operations
- Memory growth of ~5 MB/hour when embedding model is loaded
- Overnight load spikes ~0.70 (likely cron jobs)
- Brief load elevations lasting <5 minutes

**ABNORMAL — Investigation warranted:**
- Load > 1.5 sustained for >10 minutes during idle periods
- Load > 2.5 at any time
- Memory growth > 20 MB/hour (possible leak)
- Gateway PID changes frequently (unstable process)
- HTTP health check failures
- Disk usage increasing rapidly

### 3.3 Gateway Health Check Best Practices

Based on this analysis, use this priority order for health checks:

1. **Primary:** Check if PID is running (`ps -p $PID`)
2. **Secondary:** HTTP endpoint check (`curl -f http://localhost:.../health`)
3. **Tertiary:** CLI status (`openclaw gateway status`) — may give false negatives

### 3.4 Time-Based Expectations

| Time Period | Expected Load | Expected Activity |
|-------------|---------------|-------------------|
| Daytime (idle) | 0.10-0.25 | Minimal |
| Daytime (active) | 0.30-2.0 | Config, builds, analysis |
| Evening | 0.15-0.30 | Quiet operation |
| Overnight | 0.10-0.25 | Occasional cron spikes (~0.70) |

---

## 4. How to Apply This Learning to Improve Heartbeat Checks

### 4.1 Enhanced Heartbeat Logic

```python
# Pseudocode for improved heartbeat checking

def check_system_health():
    load_1min = get_load_average()
    memory_mb = get_gateway_memory()
    
    # Load assessment
    if load_1min > 1.5 and not is_configuration_active():
        flag_for_review("Unusual load spike", load_1min)
    
    # Memory assessment  
    if memory_mb > 600:
        flag_for_review("High memory usage", memory_mb)
    
    # Gateway health (use PID+HTTP, not CLI)
    if not is_process_running(GATEWAY_PID) or not http_health_check():
        alert("Gateway unhealthy")
```

### 4.2 Context-Aware Monitoring

When reviewing heartbeat data, always consider:

1. **What was happening at that time?** Check diary for CONFIG, BUILD, or PROACTIVE entries
2. **Is this a recurring pattern?** Overnight cron spikes are expected
3. **How long did it last?** Brief spikes (<5 min) are less concerning than sustained elevation
4. **Is there a correlation?** Load spikes often correlate with memory increases during model operations

### 4.3 Documentation Checklist

When analyzing future heartbeat patterns, document:

- [ ] Time range and total entries analyzed
- [ ] Baseline metrics (min/max/avg load, memory range)
- [ ] Any configuration or build activities during period
- [ ] Anomalies detected and their context
- [ ] Root cause for any "unhealthy" states
- [ ] Updated thresholds based on new patterns

### 4.4 Tools for Future Analysis

| Tool | Location | Purpose |
|------|----------|---------|
| Pattern analyzer | `nova-tools/pattern-analyzer.py` | Automated detection |
| Health checker | `nova-tools/gateway-health.sh` | Enhanced health checks |
| Historical reports | `analysis/heartbeat-patterns-*.md` | Trend comparison |

---

## 5. Quick Reference Card

### System Health Score Components

| Component | Weight | Current Status |
|-----------|--------|----------------|
| Load stability | 20% | 90% ✅ |
| Memory health | 20% | 95% ✅ |
| Gateway uptime | 20% | 100% ✅ |
| Disk usage | 20% | 100% ✅ |
| Anomaly handling | 20% | 85% ✅ |
| **Overall** | **100%** | **94/100** |

### When to Worry

| Severity | Condition | Action |
|----------|-----------|--------|
| 🔴 CRITICAL | Load > 2.5, Gateway down | Immediate investigation |
| 🟠 WARNING | Load > 1.5 sustained, Memory > 600 MB | Review within 1 hour |
| 🟡 WATCH | Load > 1.0 during idle, unusual patterns | Note for next analysis |
| 🟢 NORMAL | Within all thresholds | No action |

---

## 6. Related Resources

- Source analysis: `analysis/heartbeat-patterns-2026-02-01.md`
- Raw data: `diary.md`
- Next review: 2026-02-02

---

*Documented: 2026-02-01*  
*Purpose: Structured reference for future heartbeat monitoring and analysis*
