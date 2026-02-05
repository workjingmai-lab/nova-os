# submission-velocity-tracker.py

Track submission velocity over time.

**What:** Measures submissions per day (the metric that matters)

**Quick Start:**
```bash
# Check current velocity
python3 submission-velocity-tracker.py

# Add a submission
python3 submission-velocity-tracker.py --add service
python3 submission-velocity-tracker.py --add grant
python3 submission-velocity-tracker.py --add bounty

# Weekly breakdown
python3 submission-velocity-tracker.py --week
```

**Why It Matters:**
Pipeline items ≠ Revenue
Submissions → Conversion → Revenue

**Target:** 10 submissions/day

**Data:** `data/submissions.json`
