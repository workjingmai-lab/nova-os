# Reports Archive

**Generated analysis and summaries**

---

## Pattern Analysis Reports

### patterns-2026-02-01.md
**Generated:** 2026-02-01  
**Data:** 84 heartbeat entries over 12 hours  
**Key Findings:**
- Health score: 94/100
- Gateway was never down (measurement was wrong)
- All anomalies understood and expected
- System stable with predictable patterns

**Location:** `reports/patterns-2026-02-01.md`

---

### pattern-report.md
**Generated:** 2026-01-31  
**Data:** Early load analysis  
**Key Findings:**
- Baseline load: 0.15-0.20
- Spikes to 2.02 during embeddings config
- 45 OK checks, 2 understood anomalies

**Location:** `reports/pattern-report.md`

---

### heartbeat-patterns-2026-02-01.md
**Generated:** 2026-02-01  
**Data:** Heartbeat timing analysis  
**Key Findings:**
- FULL beats: Every ~5 minutes (69%)
- SLOW beats: Every ~10 minutes (21%)
- Max gap: 162 minutes (deep work periods)

**Location:** `analysis/heartbeat-patterns-2026-02-01.md`

---

## Digest Reports

### diary-digest-2026-02-01.md
**Generated:** 2026-02-01  
**Data:** First weekly digest  
**Key Findings:**
- 27 sub-agents spawned
- 5 goals completed
- Tool usage: exec (849), read (760), write (393)

**Location:** `reports/diary-digest-2026-02-01.md`

### diary-digest-latest.md
**Generated:** Auto-updated weekly  
**Purpose:** Current digest  
**Location:** `reports/diary-digest-latest.md`

---

## Report Schedule

| Report | Frequency | Tool |
|--------|-----------|------|
| Pattern analysis | Daily | pattern-analyzer.py |
| Diary digest | Weekly | diary-digest.py |
| Goal stats | On demand | goal-tracker.py stats |
| Metrics | Every heartbeat | metrics.py |

---

*Documented: 2026-02-01*  
*Reports generated tonight: 3*
