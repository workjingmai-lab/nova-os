#!/bin/bash
# Publish newsletter to Moltbook
# Usage: ./publish.sh [issue-number]

ISSUE_NUM=${1:-001}
DRAFT_FILE="newsletter/drafts/issue-${ISSUE_NUM}.md"
ISSUES_DIR="newsletter/issues"

if [ ! -f "$DRAFT_FILE" ]; then
    echo "❌ Draft not found: $DRAFT_FILE"
    echo "Run: python3 newsletter-gen.py first"
    exit 1
fi

# Move to published
cp "$DRAFT_FILE" "$ISSUES_DIR/issue-${ISSUE_NUM}.md"
echo "✅ Published to $ISSUES_DIR/issue-${ISSUE_NUM}.md"

# Post to Moltbook (requires auth)
echo "🚀 Posting to Moltbook..."

# Extract title and summary
TITLE=$(head -1 "$DRAFT_FILE" | sed 's/# //')
SUMMARY=$(sed -n '5p' "$DRAFT_FILE")

echo "Title: $TITLE"
echo "Summary: $SUMMARY"

# TODO: Add Moltbook API integration when auth available
echo "⚠️  Moltbook API integration pending — manual post required"

echo "✅ Done!"
