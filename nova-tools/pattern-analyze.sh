#!/bin/bash
# Nova Pattern Analyzer - Detect trends from diary.md
# Usage: ./pattern-analyze.sh

DIARY="/home/node/.openclaw/workspace/diary.md"
REPORT="/home/node/.openclaw/workspace/reports/pattern-report.md"

mkdir -p /home/node/.openclaw/workspace/reports

echo "# Pattern Analysis Report" > "$REPORT"
echo "Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$REPORT"
echo "" >> "$REPORT"

# Extract load averages from last 10 entries
echo "## Load Average Trend (last 10 checks)" >> "$REPORT"
grep "load average:" "$DIARY" | tail -10 | sed 's/.*load average: //' | awk '{print "- " $1 ", " $2 ", " $3}' >> "$REPORT"

# Disk usage trend
echo "" >> "$REPORT"
echo "## Disk Usage Trend" >> "$REPORT"
grep "Disk: overlay" "$DIARY" | tail -5 | awk '{print "- " $2 ": " $5 " used"}' >> "$REPORT"

# Count HEARTBEAT_OK entries
echo "" >> "$REPORT"
echo "## System Health" >> "$REPORT"
OK_COUNT=$(grep -c "HEARTBEAT_OK" "$DIARY")
echo "- Total OK checks: $OK_COUNT" >> "$REPORT"

# Detect anomalies (load > 1.0)
echo "" >> "$REPORT"
echo "## Anomalies Detected" >> "$REPORT"
ANOMALIES=$(grep "load average:" "$DIARY" | awk -F'load average: ' '{print $2}' | awk -F',' '{if ($1 > 1.0) print $1}')
if [ -n "$ANOMALIES" ]; then
    echo "High load spikes:" >> "$REPORT"
    echo "$ANOMALIES" | while read load; do
        echo "- Load: $load" >> "$REPORT"
    done
else
    echo "- None detected (all loads nominal)" >> "$REPORT"
fi

echo "" >> "$REPORT"
echo "## Recommendations" >> "$REPORT"
echo "- Continue monitoring load trends" >> "$REPORT"
echo "- Archive diary.md when >1000 entries" >> "$REPORT"

cat "$REPORT"
