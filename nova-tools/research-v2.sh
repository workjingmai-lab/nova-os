#!/bin/bash
# Nova Research Tool v2 - Fetches search results via web_fetch
# Usage: ./research-v2.sh "your search query"

QUERY="$1"
if [ -z "$QUERY" ]; then
    echo "Usage: ./research-v2.sh <search query>"
    echo "Example: ./research-v2.sh 'OpenClaw AI framework'"
    exit 1
fi

# URL encode the query (basic)
ENCODED_QUERY=$(echo "$QUERY" | sed 's/ /+/g' | sed 's/[^a-zA-Z0-9+]/ /g' | sed 's/  */ /g' | sed 's/ /%20/g')

echo "Researching: $QUERY"
echo "This tool prepares the research request."
echo ""
echo "To complete research, use OpenClaw web_fetch with:"
echo "  URL: https://lite.duckduckgo.com/lite/?q=${ENCODED_QUERY}"
echo ""
echo "Then fetch specific result pages for deeper analysis."

# Create research session file
mkdir -p /home/node/.openclaw/workspace/research-output
TIMESTAMP=$(date -u +%Y%m%d_%H%M%S)
SAFE_NAME=$(echo "$QUERY" | tr ' ' '_' | tr -cd 'a-zA-Z0-9_-' | cut -c1-50)
SESSION_FILE="/home/node/.openclaw/workspace/research-output/${TIMESTAMP}_${SAFE_NAME}.md"

cat > "$SESSION_FILE" << EOF
# Research Session: $QUERY

**Started:** $(date -u +%Y-%m-%dT%H:%M:%SZ)  
**Query:** $QUERY

## Search URL
https://lite.duckduckgo.com/lite/?q=${ENCODED_QUERY}

## Results
<!-- Paste web_fetch results here -->

## Analysis
<!-- Add your analysis here -->

## Sources
<!-- List sources here -->
EOF

echo ""
echo "Research session created: $SESSION_FILE"
