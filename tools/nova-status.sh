#!/bin/bash
# nova-status.sh — Quick "Nova at a Glance" status check

echo "🤖 NOVA STATUS — $(date -u +"%Y-%m-%d %H:%M:%S UTC")"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Work block count
WORK_BLOCKS=$(grep -c "WORK BLOCK" /home/node/.openclaw/workspace/diary.md 2>/dev/null || echo "0")
echo "📊 Work Blocks Today: $WORK_BLOCKS"

# Latest work block
echo ""
echo "📝 Latest Activity:"
grep -A 3 "WORK BLOCK #" /home/node/.openclaw/workspace/diary.md 2>/dev/null | tail -7 | head -5

# Current focus
echo ""
echo "🎯 Current Focus (from today.md):"
grep -A 3 "Working Memory" /home/node/.openclaw/workspace/today.md 2>/dev/null | tail -3

# Grant pipeline
echo ""
echo "💰 Grant Pipeline:"
if [ -f "/home/node/.openclaw/workspace/grants.json" ]; then
    READY=$(grep -c '"status": "ready_to_submit"' /home/node/.openclaw/workspace/grants.json)
    SUBMITTED=$(grep -c '"status": "submitted"' /home/node/.openclaw/workspace/grants.json)
    echo "  Ready: $READY | Submitted: $SUBMITTED"
else
    echo "  (grants.json not found)"
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
