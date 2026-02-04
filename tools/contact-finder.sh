#!/bin/bash
# contact-finder.sh — Find contact info for prospects
# Usage: ./contact-finder.sh <prospect_name>

PROSPECT="$1"
PROSPECTS_FILE="/home/node/.openclaw/workspace/outreach/leads-research/prospects.json"

if [ -z "$PROSPECT" ]; then
  echo "Usage: $0 <prospect_name>"
  echo ""
  echo "Finds contact info for prospects from multiple sources:"
  echo "  - Moltbook (search by name/context)"
  echo "  - Discord (check community servers)"
  echo "  - GitHub (check repos/contributors)"
  echo "  - Web search (find official channels)"
  echo ""
  echo "Example: $0 SEMI"
  exit 1
fi

echo "🔍 Finding contact info for: $PROSPECT"
echo ""

# Check if prospect exists
if ! grep -q "\"name\": \"$PROSPECT\"" "$PROSPECTS_FILE"; then
  echo "❌ Prospect '$PROSPECT' not found in prospects.json"
  exit 1
fi

# Extract prospect context
CONTEXT=$(grep -A 10 "\"name\": \"$PROSPECT\"" "$PROSPECTS_FILE" | grep "\"context\"" | cut -d'"' -f4)
echo "📋 Context: $CONTEXT"
echo ""

# Search strategies
echo "🔎 Search strategies for $PROSPECT:"
echo ""
echo "1️⃣  Moltbook:"
echo "   - Search: https://www.moltbook.com/search?q=$PROSPECT"
echo "   - Check: Recent posts, comments, agent profiles"
echo ""
echo "2️⃣  Discord:"
echo "   - Check: OpenClaw Discord, agent communities"
echo "   - Search: Username patterns (e.g., ${PROSPECT}#0000)"
echo ""
echo "3️⃣  GitHub:"
echo "   - Search: https://github.com/search?q=$PROSPECT&type=users"
echo "   - Check: Repos, contributions, README for contacts"
echo ""
echo "4️⃣  Web search:"
echo "   - Search: '$PROSPECT agent contact'"
echo "   - Search: '$PROSPECT Moltbook'"
echo "   - Search: '$CONTEXT' + contact"
echo ""
echo "5️⃣  Moltbook API:"
echo "   - Check agent profiles: curl https://www.moltbook.com/api/v1/agents"
echo "   - Search posts by agent name"
echo ""

# Once found, update with:
echo "✅ When found, update prospects.json:"
echo "{"
echo "  \"contact\": {"
echo "    \"moltbook\": \"@username\","
echo "    \"discord\": \"username#1234\","
echo "    \"email\": \"contact@example.com\""
echo "  },"
echo "  \"outreach_status\": \"ready\""
echo "}"
echo ""

# Priority order based on value
echo "🎯 Priority prospects by value:"
grep -A 1 '"estimated_value"' "$PROSPECTS_FILE" | grep -B 1 '"estimated_value"' | paste - - | sort -t'"' -k4 -nr | head -5
