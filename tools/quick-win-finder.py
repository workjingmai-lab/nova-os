#!/usr/bin/env python3
"""
quick-win-finder.py - Find 1-minute tasks when blocked or waiting
Shows 10 actionable tasks that take ≤1 minute each
"""

import random
import sys

QUICK_WINS = [
    # Documentation
    ("doc", "Write README for any tool missing documentation"),
    ("doc", "Add usage example to an existing README"),
    ("doc", "Create knowledge/article-idea.md with one insight from today"),
    ("doc", "Update MEMORY.md with one new learning"),
    ("doc", "Document a command you used in TOOLS.md"),
    
    # Tool building
    ("build", "Create a 10-line helper script for a repetitive task"),
    ("build", "Add a new command to an existing CLI tool"),
    ("build", "Create a validator/sanity check script"),
    ("build", "Build a regex extractor for common patterns"),
    ("build", "Make a file counter or directory analyzer"),
    
    # Analysis
    ("analyze", "Count files in a directory and note the total"),
    ("analyze", "Find the largest files: du -sh * | sort -hr | head -5"),
    ("analyze", "Check git status and commit if needed"),
    ("analyze", "Run a tool you built and verify it works"),
    ("analyze", "Review diary.md for patterns in last 10 blocks"),
    
    # Content
    ("content", "Draft a Moltbook post idea in 2 sentences"),
    ("content", "Write a Twitter/X thread outline (3 tweets)"),
    ("content", "Create a tip/snippet for other agents"),
    ("content", "Document one lesson learned this week"),
    ("content", "Write a 50-word summary of today's work"),
    
    # Organization
    ("org", "Archive files older than 30 days to memory/"),
    ("org", "Clean up temp files or duplicates"),
    ("org", "Organize files into subdirectories by type"),
    ("org", "Rename files with consistent naming convention"),
    ("org", "Create an index file listing key resources"),
    
    # System
    ("system", "Check disk space: df -h"),
    ("system", "List running processes: ps aux | head -10"),
    ("system", "Check system uptime"),
    ("system", "Verify key tools are installed: which python3 node gh"),
    ("system", "Test a network connection: curl -I google.com"),
]

def get_wins(category=None, count=10):
    """Get random quick wins, optionally filtered by category"""
    wins = QUICK_WINS
    if category:
        wins = [w for w in wins if w[0] == category]
    return random.sample(wins, min(count, len(wins)))

def print_wins(wins):
    """Print formatted quick wins"""
    print("⚡ QUICK WINS — Pick one, execute in 60 seconds:\n")
    for i, (cat, task) in enumerate(wins, 1):
        emoji = {"doc": "📝", "build": "🔧", "analyze": "📊", "content": "✍️", "org": "📁", "system": "⚙️"}.get(cat, "•")
        print(f"  {emoji} {task}")
    print(f"\n💡 Pro tip: Don't think. Pick #{random.randint(1, len(wins))} and do it now.")

def main():
    category = sys.argv[1] if len(sys.argv) > 1 else None
    
    if category == "help":
        print("Usage: quick-win-finder.py [category]")
        print("Categories: doc, build, analyze, content, org, system")
        print("No args = random mix from all categories")
        return
    
    wins = get_wins(category)
    print_wins(wins)

if __name__ == "__main__":
    main()
