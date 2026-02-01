#!/usr/bin/env python3
"""
Agent Swarm Monitor
Tracks multi-agent collaboration status from diary entries
"""

import re
import json
from datetime import datetime
from pathlib import Path

def parse_claims(diary_path: str = "diary.md"):
    """Parse CLAIM entries from diary"""
    diary = Path(diary_path)
    if not diary.exists():
        return []
    
    claims = []
    pattern = r'CLAIM:\s*(\S+)\s+by\s+(\S+)'
    
    for line in diary.read_text().split('\n'):
        match = re.search(pattern, line)
        if match:
            claims.append({
                'task': match.group(1),
                'agent': match.group(2),
                'line': line.strip()
            })
    
    return claims

def parse_handoffs(diary_path: str = "diary.md"):
    """Parse HANDOFF entries from diary"""
    diary = Path(diary_path)
    if not diary.exists():
        return []
    
    handoffs = []
    content = diary.read_text()
    pattern = r'## HANDOFF — (\S+) → (\S+)\n\n\*\*Completed:\*\* ([^\n]+)'
    
    for match in re.finditer(pattern, content):
        handoffs.append({
            'from': match.group(1),
            'to': match.group(2),
            'time': match.group(3)
        })
    
    return handoffs

def parse_status(diary_path: str = "diary.md"):
    """Parse STATUS entries from diary"""
    diary = Path(diary_path)
    if not diary.exists():
        return []
    
    statuses = []
    content = diary.read_text()
    pattern = r'## STATUS — (\S+)\n\n\*\*Last Update:\*\* ([^\n]+)\n\*\*Progress:\*\* ([^\n]+)'
    
    for match in re.finditer(pattern, content):
        statuses.append({
            'agent': match.group(1),
            'updated': match.group(2),
            'progress': match.group(3)
        })
    
    return statuses

def generate_swarm_report(diary_path: str = "diary.md"):
    """Generate comprehensive swarm status report"""
    claims = parse_claims(diary_path)
    handoffs = parse_handoffs(diary_path)
    statuses = parse_status(diary_path)
    
    report = f"""# Agent Swarm Report
Generated: {datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ')}

## Summary
- Active Claims: {len(claims)}
- Handoffs Completed: {len(handoffs)}
- Status Updates: {len(statuses)}

## Recent Claims
"""
    for claim in claims[-5:]:
        report += f"- `{claim['task']}` → {claim['agent']}\n"
    
    report += "\n## Recent Handoffs\n"
    for handoff in handoffs[-5:]:
        report += f"- {handoff['from']} → {handoff['to']} ({handoff['time']})\n"
    
    report += "\n## Agent Status\n"
    for status in statuses[-5:]:
        report += f"- **{status['agent']}**: {status['progress']} (updated {status['updated']})\n"
    
    return report

if __name__ == "__main__":
    import sys
    
    diary = sys.argv[1] if len(sys.argv) > 1 else "diary.md"
    
    claims = parse_claims(diary)
    handoffs = parse_handoffs(diary)
    statuses = parse_status(diary)
    
    print(f"📊 Swarm Status from {diary}")
    print(f"   Claims: {len(claims)} | Handoffs: {len(handoffs)} | Statuses: {len(statuses)}")
    
    if claims:
        print(f"\n📝 Latest claim: {claims[-1]['agent']} → {claims[-1]['task']}")
    
    # Save full report
    report = generate_swarm_report(diary)
    report_path = Path("reports/swarm-status.md")
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(report)
    print(f"\n📄 Full report saved to {report_path}")
