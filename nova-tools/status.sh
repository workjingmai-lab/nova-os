#!/bin/bash
# Nova Quick Status - Fast system health check
# Usage: ./status.sh

echo "=== Nova Quick Status ==="
echo "Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

echo "--- System ---"
 uptime | awk '{print "Uptime: " $3 " " $4 " " $5}' | sed 's/,//g'
df -h / | tail -1 | awk '{print "Disk: " $5 " used (" $4 " free)"}'

echo ""
echo "--- Workspace ---"
ls -1 /home/node/.openclaw/workspace/*.md 2>/dev/null | wc -l | xargs echo "MD files:"
git -C /home/node/.openclaw/workspace status --short 2>/dev/null | wc -l | xargs echo "Untracked/modified files:"

echo ""
echo "--- Last Heartbeat ---"
tail -1 /home/node/.openclaw/workspace/diary.md | head -c 100

echo ""
echo "=== End Status ==="
