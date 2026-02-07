#!/bin/bash
# daily-revenue-notify.sh — Daily revenue execution reminder
# Add to cron: 0 9 * * * /bin/bash /home/node/.openclaw/workspace/tools/daily-revenue-notify.sh

cd /home/node/.openclaw/workspace

# Run rhythm tracker
OUTPUT=$(python3 tools/revenue-rhythm.py 2>/dev/null)

# Extract key numbers
TOTAL=$(echo "$OUTPUT" | grep "Total Potential" | grep -oP '\$[0-9,]+' | tr -d '$,' || echo "0")
HIGH=$(echo "$OUTPUT" | grep "HIGH Priority" | grep -oP '\$[0-9,]+' | tr -d '$,' || echo "0")

# Simple notification
echo "💰 Daily Revenue Check"
echo "Pipeline: \$${TOTAL:-0} | HIGH Priority: \$${HIGH:-0}"
echo "Run: python3 tools/revenue-rhythm.py"
