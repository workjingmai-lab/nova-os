#!/bin/bash
# Publish newsletter to Moltbook
# Usage: ./publish-newsletter.sh [issue-number]

ISSUE=${1:-001}
FILE="newsletter/drafts/issue-${ISSUE}.md"

if [ ! -f "$FILE" ]; then
    echo "❌ Issue $ISSUE not found at $FILE"
    exit 1
fi

echo "📰 Publishing Nova's Notes Issue #$ISSUE..."

# Read content
CONTENT=$(cat "$FILE")

# Post to Moltbook via API (requires credentials)
# This is a placeholder - actual implementation needs API key
echo "📝 Content ready (${#CONTENT} chars)"
echo "⚠️  Manual step: Copy content to Moltbook post"
echo "🔗 Open: https://moltbook.com/post"

# Mark as published
mv "$FILE" "newsletter/published/issue-${ISSUE}-$(date +%Y-%m-%d).md"
echo "✅ Moved to published/"
