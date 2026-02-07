#!/usr/bin/env python3
"""
nova-status.py — Nova's complete status dashboard
One command to see everything: revenue, content queue, velocity, goals.
Usage: python3 nova-status.py
"""

import json
import os
import subprocess
from datetime import datetime

def run_tool(tool_name, *args):
    """Run a tool and capture output."""
    try:
        result = subprocess.run(
            ["python3", f"{tool_name}.py"] + list(args),
            capture_output=True, text=True, timeout=5
        )
        return result.stdout if result.returncode == 0 else f"⚠️  {tool_name} failed"
    except:
        return f"⚠️  {tool_name} not available"

def main():
    print("\n" + "=" * 60)
    print("  ⚡ NOVA STATUS — Complete Dashboard")
    print("=" * 60)
    
    # Revenue Section
    print("\n" + "─" * 60)
    print("  💰 REVENUE PIPELINE")
    print("─" * 60)
    
    if os.path.exists("revenue-pipeline.json"):
        with open("revenue-pipeline.json") as f:
            data = json.load(f)
        
        grants = data.get("grants", [])
        services = data.get("services", [])
        bounties = data.get("bounties", [])
        
        grant_ready = sum(g.get("amount", 0) for g in grants if g.get("status") == "ready")
        grant_sub = sum(g.get("amount", 0) for g in grants if g.get("status") == "submitted")
        svc_ready = sum(s.get("potential", 0) for s in services if s.get("status") == "ready")
        bounty_blocked = sum(b.get("amount", 0) for b in bounties if b.get("status") == "blocked")
        
        print(f"   Grants (ready):    ${grant_ready/1000:.0f}K")
        print(f"   Grants (sub'd):    ${grant_sub/1000:.0f}K")
        print(f"   Services:          ${svc_ready/1000:.0f}K")
        print(f"   Bounties (block):  ${bounty_blocked/1000:.0f}K")
        print(f"   ─────────────────────────────────")
        print(f"   TOTAL READY:       ${(grant_ready + svc_ready)/1000:.0f}K")
    else:
        print("   ⚠️  No revenue data")
    
    # Moltbook Section
    print("\n" + "─" * 60)
    print("  📱 MOLTBOOK QUEUE")
    print("─" * 60)
    
    if os.path.exists("moltbook-queue.json"):
        with open("moltbook-queue.json") as f:
            queue = json.load(f)
        
        posts = queue.get("posts", [])
        scheduled = len([p for p in posts if p.get("scheduled") and not p.get("published")])
        ready = len([p for p in posts if not p.get("published") and 
                    datetime.now().timestamp() >= datetime.fromisoformat(
                        p.get("scheduled", "2099-01-01").replace("Z", "+00:00")
                    ).timestamp()])
        
        print(f"   Scheduled:         {scheduled}")
        print(f"   Ready to publish:  {ready}")
        
        if posts:
            print(f"\n   Next 3 posts:")
            for p in sorted(posts, key=lambda x: x.get("scheduled", ""))[:3]:
                status = "✅" if p.get("published") else "⏳"
                title = p.get('title', 'Untitled')[:30]
                print(f"   {status} {title}")
    else:
        print("   ⚠️  No queue data")
    
    # Velocity Section
    print("\n" + "─" * 60)
    print("  ⚡ VELOCITY")
    print("─" * 60)
    
    today_file = f"memory/{datetime.now().strftime('%Y-%m-%d')}.md"
    if os.path.exists(today_file):
        with open(today_file) as f:
            content = f.read()
        blocks_today = content.count("Work Block")
        print(f"   Today's blocks:    {blocks_today}")
    else:
        print(f"   Today's blocks:    0")
    
    # Goals Section
    print("\n" + "─" * 60)
    print("  🎯 TOP GOALS (unchecked)")
    print("─" * 60)
    
    if os.path.exists("goals/active.md"):
        with open("goals/active.md") as f:
            content = f.read()
        
        import re
        tasks = re.findall(r'\- \[ \](.+)', content)
        for task in tasks[:5]:
            print(f"   ☐ {task.strip()[:50]}")
        if len(tasks) > 5:
            print(f"   ... and {len(tasks) - 5} more")
    
    # Quick Commands
    print("\n" + "─" * 60)
    print("  🚀 QUICK COMMANDS")
    print("─" * 60)
    print("   python3 daily-snapshot.py      # Revenue dashboard")
    print("   python3 moltbook-queue.py      # Content queue")
    print("   python3 revenue-scoreboard.py  # Submissions/wins")
    print("   python3 lead-prioritizer.py    # Top 5 leads")
    
    print("\n" + "=" * 60)
    print(f"  Generated: {datetime.now().strftime('%H:%M UTC')}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
