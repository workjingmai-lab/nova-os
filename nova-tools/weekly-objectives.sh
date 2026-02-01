#!/bin/bash
# Nova Weekly Objectives - Auto-generate weekly goals
# Usage: ./weekly-objectives.sh

GOALS_FILE="/home/node/.openclaw/workspace/goals/active.md"
WEEK=$(date -u +%Y-W%U)

echo "# Weekly Objectives: $WEEK" > /tmp/weekly-goals.md
echo "" >> /tmp/weekly-goals.md

# Analyze diary for recurring themes
echo "## From Pattern Analysis" >> /tmp/weekly-goals.md
LOAD_SPIKES=$(grep "load average:" /home/node/.openclaw/workspace/diary.md | awk -F'load average: ' '{print $2}' | awk -F',' '{if ($1 > 1.0) print "high"}' | wc -l)
if [ "$LOAD_SPIKES" -gt 2 ]; then
    echo "- [ ] Investigate $LOAD_SPIKES load spikes detected this period" >> /tmp/weekly-goals.md
fi

# Check disk trend
DISK_NOW=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ "$DISK_NOW" -gt 5 ]; then
    echo "- [ ] Disk at ${DISK_NOW}%, monitor growth" >> /tmp/weekly-goals.md
fi

# Default growth goals
echo "" >> /tmp/weekly-goals.md
echo "## Growth" >> /tmp/weekly-goals.md
echo "- [ ] Complete 1 medium priority goal from active.md" >> /tmp/weekly-goals.md
echo "- [ ] Log 3 learnings to learnings.md" >> /tmp/weekly-goals.md

cat /tmp/weekly-goals.md
echo ""
echo "Weekly objectives generated for $WEEK"
