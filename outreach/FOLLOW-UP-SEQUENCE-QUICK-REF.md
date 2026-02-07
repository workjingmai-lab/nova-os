# Follow-up Sequence Quick Reference

**Created:** 2026-02-06 | **Purpose:** Track follow-up schedule for all outreach leads

---

## Follow-up Framework (PROOF + Day Sequence)

**Standard Follow-up Schedule:**
- **Day 0:** Send initial message
- **Day 3:** "Any thoughts on [topic]?" + 1-sentence recap of value
- **Day 7:** "Quick check-in — [specific question]?"
- **Day 14:** Final follow-up with ROI preview
- **Day 21:** Close out (if no response after 3 follow-ups)

**High-Priority Follow-ups (Day 0/3/7/14/21):**
- EF ($40K) — HIGH
- Fireblocks ($35K) — HIGH
- Uniswap ($40K) — HIGH
- Balancer ($20K) — HIGH priority for follow-up

---

## HIGH Priority Tier (3 leads, $115K)

| Lead | Value | Day 0 Sent | Day 3 | Day 7 | Day 14 | Day 21 | Status |
|------|-------|------------|-------|-------|--------|--------|--------|
| EF (Ethereum Foundation) | $40K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Fireblocks | $35K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Uniswap | $40K | Ready | TBD | TBD | TBD | TBD | Not sent |

**HIGH Tier Total:** $115K | **Status:** 0/3 sent, 0/15 follow-ups due

---

## MEDIUM Priority Tier (7 leads, $190K)

| Lead | Value | Day 0 Sent | Day 3 | Day 7 | Day 14 | Day 21 | Status |
|------|-------|------------|-------|-------|--------|--------|--------|
| Alchemy | $30K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Circle | $20K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Infura | $30K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Polygon | $30K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Chainlink | $30K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Arbitrum | $30K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Optimism | $30K | Ready | TBD | TBD | TBD | TBD | Not sent |

**MEDIUM Tier Total:** $190K | **Status:** 0/7 sent, 0/35 follow-ups due

---

## TACTICAL Priority Tier (19 leads, $315-375K) ✅

| Lead | Value | Day 0 Sent | Day 3 | Day 7 | Day 14 | Day 21 | Status |
|------|-------|------------|-------|-------|--------|--------|--------|
| ENS DAO Governance | $15-20K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Optimism DAO Governance | $20K | Ready | TBD | TBD | TBD | TBD | Not sent |
| 1inch DAO Governance | $15-20K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Aave DAO Governance | $20-30K | Ready | TBD | TBD | TBD | TBD | Not sent |
| SushiSwap DAO Governance | $15-20K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Curve DAO Governance | $15-20K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Yearn DAO Governance | $15-20K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Balancer DAO Governance | $15-20K | Ready | TBD | TBD | TBD | TBD | Not sent |
| Convex Finance Governance | $15-20K | Ready | TBD | TBD | TBD | TBD | Not sent |
| GMX DAO | $25K | Ready | TBD | TBD | TBD | TBD | Not sent |
| [9 additional tactical leads] | ~$171-201K | Ready | TBD | TBD | TBD | TBD | Not sent |

**TACTICAL Tier Total:** $315-375K | **Status:** 0/19 sent, 0/95 follow-ups due | **Messages:** 19/19 complete ✅

---

## Combined Pipeline Status

**Total Pipeline:** $620-680K (HIGH $115K + MEDIUM $190K + TACTICAL $315-375K)

**Execution Status:**
- Messages created: 29/29 (100%) ✅
- Messages sent: 0/29 (0%) ❌
- Follow-ups due: 0/145 (0%) — requires initial sends first
- Execution gap: 100% (nothing sent)

---

## Follow-up Command Reference

**Check due follow-ups:**
```bash
python3 /home/node/.openclaw/workspace/tools/follow-up-tracker.py check
```

**Generate follow-up messages:**
```bash
python3 /home/node/.openclaw/workspace/tools/follow-up-tracker.py generate --day 3
```

**Mark follow-up complete:**
```bash
python3 /home/node/.openclaw/workspace/tools/follow-up-tracker.py complete --lead <lead_name> --day 3
```

---

## Notes

- All follow-ups use value-first approach (no "just checking in")
- Day 3 = "Any thoughts?" + recap (brief)
- Day 7 = "Quick check-in" + specific question
- Day 14 = Final follow-up with ROI preview
- Day 21 = Close out (optional, for high-priority only)
- **Critical:** Initial messages must be sent BEFORE follow-ups become due
- **Blocker:** Arthur execution required (messages are ready, not sent)
- **ROI:** Sending all 29 messages = $620-680K pipeline activated

---

**Next Action:** Arthur executes `service-batch-send.py` to send all 29 outreach messages
**Timeline:** Once sent, Day 3 follow-ups begin 72 hours later
**Tool:** `follow-up-tracker.py` tracks all follow-up schedules automatically
