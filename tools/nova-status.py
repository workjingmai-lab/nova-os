#!/usr/bin/env python3
"""
nova-status.py — Compact health check for Nova's systems
Shows blocks, tools, pipeline, blockers in 5 lines
"""

import subprocess
import json
import os
from datetime import datetime

def run_cmd(cmd):
    """Run shell command and return output"""
    try:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    except:
        return "N/A"

def get_blocks_today():
    """Get today's work block count"""
    today_file = f"memory/{datetime.now().strftime('%Y-%m-%d')}.md"
    if not os.path.exists(today_file):
        return 0
    result = run_cmd(f"grep -c '^### Work Block' {today_file}")
    return int(result) if result.isdigit() else 0

def get_tool_counts():
    """Count tools and docs"""
    py_count = run_cmd("ls tools/*.py 2>/dev/null | wc -l")
    doc_count = run_cmd("ls tools/README*.md 2>/dev/null | wc -l")
    return int(py_count) if py_count.isdigit() else 0, int(doc_count) if doc_count.isdigit() else 0

def get_pipeline():
    """Get revenue pipeline summary"""
    try:
        with open('data/revenue-pipeline.json', 'r') as f:
            data = json.load(f)
        total = sum(p['potential'] for p in data.get('grants', []))
        total += sum(p['potential'] for p in data.get('services', []))
        ready = sum(p['potential'] for p in data.get('grants', []) if p.get('status') == 'ready_to_submit')
        ready += sum(p['potential'] for p in data.get('services', []) if p.get('status') == 'ready')
        return total, ready
    except:
        return 0, 0

def main():
    blocks = get_blocks_today()
    tools, docs = get_tool_counts()
    pipeline_total, pipeline_ready = get_pipeline()
    
    print("┌─────────────────────────────────────┐")
    print("│         ✨ NOVA STATUS              │")
    print("├─────────────────────────────────────┤")
    print(f"│  📊 Blocks:     {blocks:>4} today           │")
    print(f"│  🔧 Tools:      {tools:>4} py  / {docs:>4} docs   │")
    print(f"│  💰 Pipeline:   ${pipeline_ready/1000:.0f}K ready / ${pipeline_total/1000:.0f}K total │")
    print("├─────────────────────────────────────┤")
    
    # Blockers
    blockers = []
    if pipeline_ready > 0:
        blockers.append(f"Send ${pipeline_ready/1000:.0f}K messages")
    
    if blockers:
        print(f"│  ⚡ Next: {blockers[0][:24]:<24}│")
    else:
        print("│  ✅ No blockers                     │")
    
    print("└─────────────────────────────────────┘")

if __name__ == "__main__":
    main()
