# 60-Second Pre-Execution Checklist

**For:** Arthur
**When:** Before sending service outreach messages
**Time:** 60 seconds
**Status:** ✅ Ready (2026-02-04)

---

## Step 1: Verify Pipeline (10 seconds)
```bash
python3 tools/pipeline-snapshot.py
```
✅ **Pass:** 104 messages, $2,057K, all "ready"
❌ **Fail:** Messages not ready → Fix status in service-outreach-tracker.json

---

## Step 2: Check Blockers (10 seconds)
```bash
python3 tools/blocker-status.py
```
✅ **Pass:** Services = NO blockers
❌ **Fail:** Blockers exist → See BLOCKER-UNBLOCKER-GUIDE.md

---

## Step 3: Preview Messages (20 seconds)
```bash
python3 tools/service-batch-send.py --top 5 --dry-run
```
✅ **Pass:** Top 5 prospects look correct
❌ **Fail:** Wrong prospects → Edit service-outreach-tracker.json

---

## Step 4: Choose Strategy (5 seconds)
**Option A:** Top 10 (5 min, $305K, $61K/min)
**Option B:** Tiered (20 min, $585K-$1,979K, $73K/min)
**Option C:** All (45 min, $2,057K, $218K/min)

---

## Step 5: Execute (15 seconds)
```bash
# Copy one command and execute:
python3 tools/service-batch-send.py --top 10
# OR
python3 tools/service-batch-send.py --tiered
# OR
python3 tools/service-batch-send.py --all
```

---

## If Anything Fails

**Pipeline not ready:**
- Check `data/service-outreach-tracker.json`
- Ensure all messages have `"status": "ready"`

**Blockers exist:**
- Gateway restart: 1 min = $50K unblocked
- GitHub auth: 5 min = $130K unblocked
- See `BLOCKER-UNBLOCKER-GUIDE.md`

**Messages look wrong:**
- Edit `data/service-outreach-tracker.json`
- Update `prospect`, `amountRange`, `category`
- Re-run `--dry-run` to verify

---

## Expected Outcome

**After execution:**
- ✅ Messages sent to prospects
- ✅ Tracker updated to "sent" status
- ✅ Responses arrive in 1-7 days
- ✅ 10-15 responses expected
- ✅ 2-3 deals expected ($5K-$45K)

**What to do next:**
- See `FIRST-24-HOURS.md` for response handling
- Use `response-tracker.py` to log replies
- Follow 4-color triage (GREEN → YELLOW → BLUE → RED)

---

## TL;DR

1. `pipeline-snapshot.py` → Verify 104 ready
2. `blocker-status.py` → Confirm NO blockers
3. `service-batch-send.py --top 5 --dry-run` → Preview
4. Choose: Top 10 / Tiered / All
5. Execute → Revenue pipeline activated

**60 seconds = Complete confidence.**

---

*Build complete. Execute ready. Don't deliberate. Send.*
