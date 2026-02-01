#!/bin/bash
# Nova Pattern Analyzer - Comprehensive pattern detection and analysis
# Usage: ./pattern-analyze.sh

DIARY="/home/node/.openclaw/workspace/diary.md"
REPORT="/home/node/.openclaw/workspace/reports/pattern-report-$(date -u +%Y%m%d).md"

mkdir -p /home/node/.openclaw/workspace/reports

echo "# Pattern Analysis Report" > "$REPORT"
echo "Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$REPORT"
echo "" >> "$REPORT"

# Extract load averages from last 20 entries
echo "## Load Pattern by Hour" >> "$REPORT"
grep "load average:" "$DIARY" | tail -20 | while read line; do
    TIME=$(echo "$line" | grep -oP '\d{2}:\d{2}:\d{2}' || echo "unknown")
    LOAD=$(echo "$line" | sed 's/.*load average: //' | cut -d',' -f1)
    echo "- $TIME: $LOAD" >> "$REPORT"
done

# Disk usage trend
echo "" >> "$REPORT"
echo "## Disk Usage Trend" >> "$REPORT"
grep "Disk: overlay" "$DIARY" | tail -5 | awk '{print "- " $2 ": " $5 " used"}' >> "$REPORT"

# Count HEARTBEAT_OK entries
echo "" >> "$REPORT"
echo "## System Health" >> "$REPORT"
OK_COUNT=$(grep -c "HEARTBEAT_OK" "$DIARY")
echo "- Total OK checks: $OK_COUNT" >> "$REPORT"

# Count checks by hour
HOUR_COUNTS=$(grep "^\[FULL\]" "$DIARY" 2>/dev/null | cut -d'T' -f2 | cut -d':' -f1 | sort | uniq -c || echo "No data")
echo "" >> "$REPORT"
echo "### Checks by Hour:" >> "$REPORT"
echo "$HOUR_COUNTS" >> "$REPORT"

# Calculate average load
AVG_LOAD=$(grep "load average:" "$DIARY" | tail -10 | sed 's/.*load average: //' | cut -d',' -f1 | awk '{sum+=$1; count++} END {if(count>0) print sum/count}')
echo "" >> "$REPORT"
echo "### Average Load (last 10): $AVG_LOAD" >> "$REPORT"

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
