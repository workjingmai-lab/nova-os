#!/bin/bash
# Nova Metrics Tracker - Self-improvement through usage tracking
# Logs tool usage to metrics/usage.log

METRICS_DIR="/home/node/.openclaw/workspace/metrics"
USAGE_LOG="$METRICS_DIR/usage.log"

mkdir -p "$METRICS_DIR"

# Log this invocation
TOOL_NAME="$1"
if [ -z "$TOOL_NAME" ]; then
    TOOL_NAME="unknown"
fi

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $TOOL_NAME" >> "$USAGE_LOG"

# Generate report if requested
if [ "$2" = "--report" ]; then
    echo "=== Tool Usage Report ==="
    echo "Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo ""
    echo "## Total Invocations"
    wc -l < "$USAGE_LOG"
    echo ""
    echo "## Usage by Tool (last 24h)"
    grep "$(date -u +%Y-%m-%d)" "$USAGE_LOG" | awk '{print $2}' | sort | uniq -c | sort -rn
    echo ""
    echo "## All-Time Top Tools"
    awk '{print $2}' "$USAGE_LOG" | sort | uniq -c | sort -rn | head -10
fi
