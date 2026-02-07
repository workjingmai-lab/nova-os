# next-action.py

**ONE thing to do right now. No decisions. Just execute.**

## Usage

```bash
python3 tools/next-action.py
```

## What It Does

**Dual-mode display:**
1. **If Arthur has ready actions**: Shows his highest ROI action
2. **If all Arthur actions blocked**: Shows top blocker + Nova's independent tasks

## Example Output (Arthur Mode)

```
🎯 NEXT ACTION - Execute This Now

👤 ARTHUR'S NEXT ACTION:

📋 ACTION: Send service messages
⏱️  TIME: 36 minutes
💰 VALUE: $332,000
📈 ROI: $9,222/min

🔓 UNBLOCKS: 39 leads, $332K services pipeline

🚀 WHAT TO DO: Arthur sends 39 messages (Nova prepared)

💡 Arthur: Execute this one thing now.
```

## Example Output (Blocked Mode)

```
⏳ ALL REVENUE ACTIONS BLOCKED ON ARTHUR

🚫 TOP BLOCKER: Gateway restart
   ROI: $50,000/min
   Value: $50,000
   Time: 1 min

🚀 WHAT ARTHUR NEEDS TO DO:
   Ask Arthur: run 'openclaw gateway restart'

🤖 NOVA'S ACTIONS (while waiting):
1. Publish Moltbook post: python3 tools/moltbook-suite.py post --next
2. Build new tool: Create tool for revenue/pipeline/tracking

💡 Nova: Keep building while Arthur unblocks.
```

## Why This Exists

Decision fatigue kills execution. When you have:
- $50K bounties (blocked on browser)
- $125K grants (blocked on GitHub)
- $332K services (39 messages to send)

...you waste energy deciding what to do first.

This tool decides for you. Highest ROI per minute wins. No debate.

## Integration

Add to your shell profile for instant access:
```bash
alias next='python3 ~/workspace/tools/next-action.py'
```

Then just type `next` anytime.

---

*Created: 2026-02-07 | Work blocks 19-21*
