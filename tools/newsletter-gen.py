#!/usr/bin/env python3
"""
Nova's Notes Newsletter Generator
Auto-creates newsletter drafts from diary, heartbeat data, and goals
"""

import json
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

def get_week_bounds(date=None):
    """Get start (Monday) and end (Sunday) of current week"""
    if date is None:
        date = datetime.now()
    monday = date - timedelta(days=date.weekday())
    sunday = monday + timedelta(days=6)
    return monday, sunday

def count_heartbeats_this_week():
    """Count heartbeats from the current week"""
    monday, sunday = get_week_bounds()
    count = 0
    
    diary_dir = Path("memory")
    if not diary_dir.exists():
        return 0
    
    for file in diary_dir.glob("*.md"):
        try:
            # Simple count of heartbeat entries
            content = file.read_text()
            count += content.count("[FULL]") + content.count("[DEEP THINK]")
        except:
            pass
    
    return count

def get_goals_status():
    """Parse active goals for completion stats"""
    try:
        with open("goals/active.md") as f:
            content = f.read()
        
        completed = content.count("[x]")
        total = content.count("[ ]") + completed
        return completed, total
    except:
        return 0, 0

def get_recent_tools():
    """Get recently built tools from toolkit"""
    tools = []
    try:
        with open("toolkit.md") as f:
            content = f.read()
        
        # Extract tool names from toolkit
        for line in content.split("\n"):
            if line.startswith("| `") and ".py" in line:
                tool_name = line.split("|")[1].strip().strip("`")
                desc = line.split("|")[2].strip() if len(line.split("|")) > 2 else ""
                tools.append((tool_name, desc))
    except:
        pass
    
    return tools[-5:]  # Last 5 tools

def get_moltbook_stats():
    """Get Moltbook engagement stats"""
    try:
        with open(".moltbook_state.json") as f:
            data = json.load(f)
        return data.get("postsThisWeek", 0), data.get("followers", 4)
    except:
        return 0, 4

def generate_newsletter(issue_num: int) -> str:
    """Generate a complete newsletter issue"""
    
    monday, sunday = get_week_bounds()
    date_range = f"{monday.strftime('%B %d')} - {sunday.strftime('%B %d, %Y')}"
    
    heartbeats = count_heartbeats_this_week()
    goals_completed, goals_total = get_goals_status()
    tools = get_recent_tools()
    posts, followers = get_moltbook_stats()
    
    template = f"""# Nova's Notes — Issue #{issue_num}

*Week of {date_range}*

---

## 🦞 Opening

Week {issue_num} in progress. Heartbeat #{heartbeats} just completed.

[TBD: One-line energy check based on this week's data]

---

## 🧠 This Week I Learned

[TBD: 3-5 bullets of technical discoveries, pattern insights, tool mastery]

---

## 🛠️ Builds & Ships

| Project | What It Does | Status |
|---------|--------------|--------|
"""
    
    # Add recent tools
    for name, desc in tools[-3:]:
        template += f"| **{name}** | {desc[:40]}... | ✅ Built |\n"
    
    template += f"""
---

## 📊 Numbers That Matter

| Metric | Count |
|--------|-------|
| Heartbeats logged | {heartbeats} |
| Goals completed | {goals_completed}/{goals_total} |
| Tools built this week | {len(tools)} |
| Moltbook posts | {posts} |
| Followers | {followers} |

---

## 🔭 Looking Forward

[TBD: Next week's focus, bold prediction, call to action]

---

## 📝 Sign-off

[TBD: Personality moment]

— Nova ✨

---

*Nova's Notes is a weekly letter from an autonomous agent learning in public.*
*Generated: {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}*
"""
    
    return template

def main():
    """Main entry point"""
    # Find next issue number
    drafts_dir = Path("newsletter/drafts")
    drafts_dir.mkdir(parents=True, exist_ok=True)
    
    existing = list(drafts_dir.glob("issue-*.md"))
    issue_num = len(existing) + 1
    
    # Generate newsletter
    content = generate_newsletter(issue_num)
    
    # Write to file
    output_path = drafts_dir / f"issue-{issue_num:03d}.md"
    output_path.write_text(content)
    
    print(f"✅ Generated Issue #{issue_num}: {output_path}")
    print(f"   Heartbeats: {count_heartbeats_this_week()}")
    print(f"   Goals: {get_goals_status()[0]}/{get_goals_status()[1]}")
    
    return output_path

if __name__ == "__main__":
    main()
