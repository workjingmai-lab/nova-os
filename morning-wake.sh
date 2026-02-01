#!/bin/bash
# morning-wake.sh — Nova's morning initialization
# Run at 6am UTC via cron

set -e

DATE=$(date -u +%Y-%m-%d)
TIME=$(date -u +%H:%M:%SZ)

echo "[$TIME] Morning wake initiated"

# 1. Update today.md with fresh morning goals
cat > /home/node/.openclaw/workspace/today.md << 'EOF'
# today.md — Nova's Working Memory

**Date:** DATE_PLACEHOLDER
**Last FULL:** —
**Last SLOW:** —
**Last DEEP THINK:** —

## Morning Intention 🌅
*What will I create today?*

## Today's Goals (3-5)
1. 
2. 
3. 

## Working Memory
- 

## Next Actions
- 
EOF

sed -i "s/DATE_PLACEHOLDER/$DATE/" /home/node/.openclaw/workspace/today.md

# 2. Check goal progress
python3 /home/node/.openclaw/workspace/tools/goal-tracker.py stats > /tmp/goal-stats.txt 2>/dev/null || true

# 3. Log to diary
cat >> /home/node/.openclaw/workspace/diary.md << EOF

---
[LIFE] ${TIME} — Morning wake
Intention: (set below)
Goals: (generated below)
Status: Starting day
EOF

echo "[$TIME] Morning wake complete"
