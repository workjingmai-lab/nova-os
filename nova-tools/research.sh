#!/bin/bash
# Nova Research Tool - Uses web_fetch via OpenClaw to gather info
# Usage: ./research.sh "search query"

QUERY="$1"
if [ -z "$QUERY" ]; then
    echo "Usage: ./research.sh <search query>"
    exit 1
fi

# Create research output directory
mkdir -p /home/node/.openclaw/workspace/research-output

TIMESTAMP=$(date -u +%Y%m%d_%H%M%S)
OUTPUT_FILE="/home/node/.openclaw/workspace/research-output/research_${TIMESTAMP}.md"

echo "# Research: $QUERY" > "$OUTPUT_FILE"
echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

echo "Research saved to: $OUTPUT_FILE"
echo "Use OpenClaw web_fetch tool to populate this file with content."
