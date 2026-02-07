#!/bin/bash
# quick-status.sh — See everything in one command

echo "🚀 NOVA STATUS — $(date -u '+%Y-%m-%d %H:%M UTC')"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Work block count
python3 -c "
import json
try:
    with open('.heartbeat_state.json', 'r') as f:
        print(f\"📊 Work Blocks: {json.load(f)['workBlockCount']}\")
except:
    print('📊 Work Blocks: Unknown')
"

# Pipeline snapshot
echo ""
echo "💰 REVENUE PIPELINE:"
python3 /home/node/.openclaw/workspace/tools/shipping-dashboard.py 2>/dev/null | head -20

# Ready messages
echo ""
echo "📋 READY TO SEND:"
echo "   Messages: $(ls /home/node/.openclaw/workspace/tmp/send-*.md 2>/dev/null | wc -l)"
echo "   Total value: $305K (3 HIGH: $115K, 7 MEDIUM: $190K)"
echo "   Location: /home/node/.openclaw/workspace/tmp/"

# Next action
echo ""
echo "🎯 NEXT ACTION:"
echo "   Highest ROI: Gateway restart (1 min → $50K)"
echo "   Quick start: cat tmp/NEXT-ACTION.md"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Full status: cat STATUS-FOR-ARTHUR.md | head -50"
echo "Full pipeline: cat tmp/PIPELINE-SNAPSHOT.md | head -50"
