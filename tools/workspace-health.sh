#!/bin/bash
# Quick workspace health check
# Shows disk, git status, recent activity, and pending tasks

echo "🏥 WORKSPACE HEALTH CHECK"
echo "=========================="
echo ""

# Disk usage
echo "💾 Disk:"
df -h /home/node/.openclaw/workspace 2>/dev/null | tail -1 | awk '{print "   Used: " $3 " / " $2 " (" $5 ")"}'
echo ""

# Git status (if in git repo)
if [ -d .git ]; then
  echo "📁 Git Status:"
  git status --short 2>/dev/null | head -5
  if [ $(git status --short | wc -l) -gt 5 ]; then
    echo "   ... and more"
  fi
  echo ""
fi

# Recent files modified
echo "📝 Recent Activity:"
find /home/node/.openclaw/workspace -maxdepth 1 -name "*.md" -mmin -60 -type f 2>/dev/null | head -3 | while read f; do
  echo "   $(basename $f) - modified $(stat -c %y "$f" 2>/dev/null | cut -d'.' -f1)"
done
echo ""

# Pending tasks (if today.md exists)
TODAY="/home/node/.openclaw/workspace/today.md"
if [ -f "$TODAY" ]; then
  echo "📋 Next Actions:"
  grep -A 5 "Next Actions" "$TODAY" 2>/dev/null | grep "^-" | head -3 | sed 's/^- /   /'
fi

echo ""
echo "✨ Health check complete"
