# 🎯 NOVA QUICK REFERENCE

*Last updated: 2026-02-07 02:15 UTC*

## Current Status
```
Pipeline:     $1.49M total
Ready NOW:    $734.5K
Submitted:    $5K
Conversion:   0.0% (pre-game)
```

## ⚡ 5 Essential Commands

```bash
# 1. See full pipeline
python3 tools/conversion-dashboard.py

# 2. Check execution gap
python3 tools/execution-gap.py

# 3. Top opportunities
python3 tools/lead-prioritizer.py

# 4. System health
python3 tools/system-health.py

# 5. Send everything (when ready)
bash tools/send-everything.sh
```

## 🚀 Ready to Execute

| Action | Time | Value | Command/File |
|--------|------|-------|--------------|
| Gateway restart | 1 min | $50K | `sudo systemctl restart openclaw` |
| GitHub auth | 5 min | $125K | `gh auth login` |
| Send services | 36 min | $332K | `bash tools/send-everything.sh services` |
| Submit grants | 15 min | $125K | `bash tools/send-everything.sh grants` |

## 📁 Key Files

| Purpose | File |
|---------|------|
| Full execution plan | `ARTHUR-57-MIN-QUICK-REF.md` |
| Daily checklist | `knowledge/daily-execution-checklist.md` |
| Service messages | `tools/send-everything.sh` |
| Follow-up templates | `knowledge/follow-up-templates.md` |
| Weekly review | `knowledge/weekly-revenue-review.md` |

## 📊 This Session

- **Work blocks:** 3075
- **Systems built:** Revenue execution system complete
- **Documentation:** 100% (85/85 tools)
- **Mode:** Operator (monitoring, awaiting signal)

## 🔥 Next Action

Run: `python3 tools/execution-gap.py`

Then follow the ACTION instructions.
