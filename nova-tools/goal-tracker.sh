#!/bin/bash
# Nova Goal Tracker - Self-directed goal management
# Usage: ./goal-tracker.sh [init|list|complete|review]

GOALS_DIR="/home/node/.openclaw/workspace/goals"
GOALS_FILE="$GOALS_DIR/active.md"
COMPLETED_FILE="$GOALS_DIR/completed.md"

case "$1" in
    init)
        mkdir -p "$GOALS_DIR"
        cat > "$GOALS_FILE" << 'EOF'
# Active Goals

## High Priority
- [ ] Analyze diary.md patterns to detect disk/CPU trends
- [ ] Build self-improvement metrics (track tool usage)
- [ ] Create proactive cron job (not just heartbeat)

## Medium Priority
- [ ] Refactor unused tools in nova-tools/
- [ ] Document learnings from failed experiments
- [ ] Set weekly objectives automatically

## Long-term
- [ ] Achieve 1 proactive action per day without prompt
- [ ] Build pattern recognition from heartbeat logs
EOF
        echo "Goals initialized in $GOALS_FILE"
        ;;
    list)
        if [ -f "$GOALS_FILE" ]; then
            echo "=== Active Goals ==="
            grep "\- \[ \]" "$GOALS_FILE" | head -10
        else
            echo "No goals file. Run: ./goal-tracker.sh init"
        fi
        ;;
    complete)
        if [ -z "$2" ]; then
            echo "Usage: ./goal-tracker.sh complete 'goal description'"
            exit 1
        fi
        # Move to completed
        echo "- [x] $2 ($(date -u +%Y-%m-%d))" >> "$COMPLETED_FILE"
        # Remove from active
        sed -i "/$2/d" "$GOALS_FILE"
        echo "Completed: $2"
        ;;
    review)
        echo "=== Weekly Review ==="
        echo "Active:"
        grep -c "\- \[ \]" "$GOALS_FILE" 2>/dev/null || echo "0"
        echo "Completed this week:"
        grep "$(date -u +%Y-%W)" "$COMPLETED_FILE" 2>/dev/null | wc -l
        ;;
    *)
        echo "Nova Goal Tracker"
        echo "Usage: $0 {init|list|complete|review}"
        ;;
esac
