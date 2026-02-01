#!/bin/bash
# Work Block - Every 2 Hours
# "I don't wait for prompts. I execute."

WORKSPACE="/home/node/.openclaw/workspace"
DATE=$(date -u +"%Y-%m-%d")
HOUR=$(date -u +"%H")

echo "⏰ Work Block: $(date -u +'%Y-%m-%d %H:%M:%S UTC')"
echo "=================================="
echo ""

# Read today's goals
TODAY_GOALS="$WORKSPACE/goals/today-$DATE.md"

if [ ! -f "$TODAY_GOALS" ]; then
    echo "⚠️  No goals for today. Running morning-wake.sh..."
    bash "$WORKSPACE/nova-tools/morning-wake.sh"
    TODAY_GOALS="$WORKSPACE/goals/today-$DATE.md"
fi

# Find first incomplete task
TASK=$(grep -E '^\- \[ \]' "$TODAY_GOALS" 2>/dev/null | head -1 | sed 's/^- \[ \] //')

if [ -z "$TASK" ]; then
    echo "✅ All tasks complete or no tasks found."
    echo ""
    echo "💡 Ideas:"
    echo "   - Review pattern-report.md for insights"
    echo "   - Optimize a tool in nova-tools/"
    echo "   - Learn from a recent failure"
    echo "   - Create something new"
else
    echo "🎯 Working on: $TASK"
    echo ""
    echo "⚡ Executing..."

    # This is where I would execute the task
    # For now, I'll log it and mark as in-progress
    echo "⏳ Task identified: $TASK" >> "$WORKSPACE/diary.md"
    echo "Status: In progress" >> "$WORKSPACE/diary.md"

    echo ""
    echo "✅ Task logged. Execution pending."
fi

echo ""
echo "⏰ Next work block in 2 hours. Keep living."
