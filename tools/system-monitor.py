#!/usr/bin/env python3
"""
Nova OS System Health Monitor
Real-time dashboard for my operational metrics
"""
import os
import json
import glob
from datetime import datetime, timezone
from pathlib import Path

def get_file_stats():
    """Get stats from key directories"""
    workspace = Path("/home/node/.openclaw/workspace")
    
    stats = {
        "heartbeat_files": len(list((workspace / "logs" / "heartbeats").glob("*.jsonl"))),
        "diary_lines": 0,
        "knowledge_files": len(list((workspace / "knowledge").glob("*.md"))),
        "tools_count": len(list((workspace / "tools").glob("*.py"))),
        "goals_completed": 0,
        "total_goals": 0
    }
    
    # Count diary lines
    diary_path = workspace / "diary.md"
    if diary_path.exists():
        stats["diary_lines"] = len(diary_path.read_text().splitlines())
    
    # Parse goals
    active_goals = workspace / "goals" / "active.md"
    if active_goals.exists():
        content = active_goals.read_text()
        stats["goals_completed"] = content.count("[x]")
        stats["total_goals"] = content.count("[x]") + content.count("[ ]") + content.count("[🔄]")
    
    return stats

def get_uptime():
    """Calculate uptime from first heartbeat"""
    workspace = Path("/home/node/.openclaw/workspace")
    heartbeat_dir = workspace / "logs" / "heartbeats"
    
    if not heartbeat_dir.exists():
        return "Unknown"
    
    files = sorted(heartbeat_dir.glob("*.jsonl"))
    if not files:
        return "Unknown"
    
    # Get first entry from first file
    with open(files[0]) as f:
        first_line = f.readline()
        try:
            data = json.loads(first_line)
            first_ts = datetime.fromisoformat(data["timestamp"].replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            delta = now - first_ts
            days = delta.days
            hours = delta.seconds // 3600
            return f"{days}d {hours}h"
        except:
            return "Unknown"

def generate_dashboard():
    """Generate HTML dashboard"""
    stats = get_file_stats()
    uptime = get_uptime()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    completion_rate = 0
    if stats["total_goals"] > 0:
        completion_rate = (stats["goals_completed"] / stats["total_goals"]) * 100
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="60">
    <title>Nova OS | System Health</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background: #0a0a0f;
            color: #e0e0ff;
            font-family: 'SF Mono', Monaco, monospace;
            min-height: 100vh;
            padding: 2rem;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{
            font-size: 2.5rem;
            background: linear-gradient(90deg, #00d4ff, #7b2cbf);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}
        .subtitle {{ color: #666; margin-bottom: 2rem; }}
        .timestamp {{ color: #444; font-size: 0.9rem; margin-bottom: 2rem; }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        .card {{
            background: linear-gradient(135deg, #111118 0%, #1a1a2e 100%);
            border: 1px solid #222;
            border-radius: 12px;
            padding: 1.5rem;
            transition: transform 0.2s, border-color 0.2s;
        }}
        .card:hover {{
            transform: translateY(-2px);
            border-color: #00d4ff;
        }}
        .card-label {{ color: #666; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem; }}
        .card-value {{ font-size: 2.5rem; font-weight: bold; color: #00d4ff; }}
        .card-sub {{ color: #888; font-size: 0.9rem; margin-top: 0.5rem; }}
        .status-online {{ color: #00ff88; }}
        .progress-bar {{
            background: #222;
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 0.5rem;
        }}
        .progress-fill {{
            background: linear-gradient(90deg, #00d4ff, #7b2cbf);
            height: 100%;
            width: {completion_rate:.1f}%;
            transition: width 0.5s ease;
        }}
        footer {{ color: #444; text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #222; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>⚡ Nova OS</h1>
        <p class="subtitle">Autonomous Agent System Health</p>
        <p class="timestamp">Last updated: {now}</p>
        
        <div class="grid">
            <div class="card">
                <div class="card-label">System Uptime</div>
                <div class="card-value">{uptime}</div>
                <div class="card-sub status-online">● Online</div>
            </div>
            
            <div class="card">
                <div class="card-label">Heartbeat Cycles</div>
                <div class="card-value">{stats['heartbeat_files']}</div>
                <div class="card-sub">Total full heartbeats completed</div>
            </div>
            
            <div class="card">
                <div class="card-label">Diary Entries</div>
                <div class="card-value">{stats['diary_lines']:,}</div>
                <div class="card-sub">Lines of operational history</div>
            </div>
            
            <div class="card">
                <div class="card-label">Knowledge Base</div>
                <div class="card-value">{stats['knowledge_files']}</div>
                <div class="card-sub">Curated knowledge files</div>
            </div>
            
            <div class="card">
                <div class="card-label">Tools Built</div>
                <div class="card-value">{stats['tools_count']}</div>
                <div class="card-sub">Custom Python utilities</div>
            </div>
            
            <div class="card">
                <div class="card-label">Goal Progress</div>
                <div class="card-value">{completion_rate:.0f}%</div>
                <div class="progress-bar"><div class="progress-fill"></div></div>
                <div class="card-sub">{stats['goals_completed']}/{stats['total_goals']} goals completed</div>
            </div>
        </div>
        
        <footer>
            <p>Built by Nova | Autonomous since 2026-01-31</p>
        </footer>
    </div>
</body>
</html>"""
    return html

if __name__ == "__main__":
    dashboard = generate_dashboard()
    output_path = Path("/home/node/.openclaw/workspace/dashboard/index.html")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(dashboard)
    print(f"✅ Dashboard updated: {output_path}")
