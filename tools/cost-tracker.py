#!/usr/bin/env python3
"""
Session Cost Tracker - Uses session-logs skill patterns
to track daily spending and session costs
"""
import subprocess
import json
from datetime import datetime, timedelta
from pathlib import Path

AGENT_ID = "main"
SESSIONS_DIR = Path.home() / f".openclaw/agents/{AGENT_ID}/sessions"

def run_jq_query(query_args, file_path):
    """Run jq query on a JSONL file"""
    try:
        cmd = ["jq"] + query_args
        result = subprocess.run(
            cmd,
            input=Path(file_path).read_text(),
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def get_session_cost(session_file):
    """Get total cost for a session"""
    query_args = ['-s', '[.[] | .message.usage.cost.total // 0] | add']
    result = run_jq_query(query_args, session_file)
    try:
        return float(result) if result else 0.0
    except:
        return 0.0

def get_session_date(session_file):
    """Extract date from first message timestamp"""
    query_args = ['-r', '.[0].timestamp | split("T")[0]']
    result = run_jq_query(query_args, session_file)
    return result if result else "unknown"

def get_daily_summary(days=7):
    """Get cost summary for last N days"""
    if not SESSIONS_DIR.exists():
        return {"error": f"Sessions dir not found: {SESSIONS_DIR}"}
    
    daily_costs = {}
    session_count = 0
    
    for session_file in SESSIONS_DIR.glob("*.jsonl"):
        if ".deleted." in str(session_file):
            continue
            
        date = get_session_date(session_file)
        cost = get_session_cost(session_file)
        
        if date != "unknown":
            daily_costs[date] = daily_costs.get(date, 0) + cost
            session_count += 1
    
    # Sort by date, get last N days
    sorted_dates = sorted(daily_costs.keys(), reverse=True)[:days]
    
    report = {
        "generated": datetime.now().isoformat(),
        "total_sessions_analyzed": session_count,
        "daily_costs": {d: f"${daily_costs[d]:.4f}" for d in sorted_dates},
        "total_last_{}_days".format(days): f"${sum(daily_costs[d] for d in sorted_dates):.4f}"
    }
    
    return report

def generate_report():
    """Generate formatted cost report"""
    data = get_daily_summary(days=7)
    
    if "error" in data:
        return f"Error: {data['error']}"
    
    report = f"""# 💰 Session Cost Report
**Generated:** {data['generated'][:19]}
**Sessions Analyzed:** {data['total_sessions_analyzed']}

## Daily Costs (Last 7 Days)
"""
    for date, cost in data['daily_costs'].items():
        bar = "█" * int(float(cost[1:]) * 100)  # Scale for visual
        report += f"- {date}: {cost} {bar}\n"
    
    report += f"\n**Total:** {data['total_last_7_days']}\n"
    
    return report

if __name__ == "__main__":
    print(generate_report())
