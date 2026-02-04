# 30-Second Pre-Flight Checklist

**Before you execute any send, run this checklist (30 seconds):**

## ✅ Step 1: Verify Pipeline (5 seconds)
```bash
python3 tools/pipeline-snapshot.py
```
→ Check: Are all messages marked "ready"?

## ✅ Step 2: Check Top 5 Targets (10 seconds)
→ Top 5 prospects visible in output
→ Verify: These are the companies you want to target

## ✅ Step 3: Choose Strategy (5 seconds)
→ **Top 10** (5 min, $305K, $61K/min)
→ **Tiered** (20 min, $585K-$1,979K, $73K/min)
→ **All** (45 min, $2,057K, $218K/min)

## ✅ Step 4: Preview Before Send (5 seconds)
```bash
# Preview mode (no actual send)
python3 tools/service-batch-send.py --top 10 --dry-run
```
→ Verify: Messages look correct

## ✅ Step 5: Execute (5 seconds)
```bash
# Remove --dry-run to actually send
python3 tools/service-batch-send.py --top 10
```

---

**Decision:**
- All ✅ → EXECUTE
- Any ❌ → Fix first

**Total time:** 30 seconds → Full confidence → Revenue activated

---

## Quick ROI Reference

| Strategy | Time | Pipeline | $/min |
|----------|------|----------|-------|
| Top 10   | 5min | $305K    | $61K  |
| Tiered   | 20min| $585K-$1.9M| $73K  |
| All      | 45min| $2,057K  | $218K |

**Most likely outcome:** 10-15 responses → 2-3 deals → $10K-$45K revenue

---

**Small executions compound. Don't deliberate. Execute.**
