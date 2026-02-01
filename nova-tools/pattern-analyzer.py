#!/usr/bin/env python3
"""
Nova Heartbeat Pattern Analyzer
Extracts and analyzes patterns from diary.md heartbeat entries
"""

import re
from datetime import datetime
from collections import defaultdict, Counter
from typing import Dict, List, Tuple
import json

def parse_diary(diary_path: str) -> List[Dict]:
    """Parse diary.md and extract heartbeat entries"""
    with open(diary_path, 'r') as f:
        content = f.read()
    
    entries = []
    # Split by --- separator
    sections = content.split('---')
    
    for section in sections:
        section = section.strip()
        if not section:
            continue
        
        # Extract entry type and timestamp
        type_match = re.search(r'\[(\w+(?:\s+\w+)*)\]\s+(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)', section)
        if not type_match:
            continue
            
        entry_type = type_match.group(1)
        timestamp_str = type_match.group(2)
        
        try:
            timestamp = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        except:
            continue
        
        entry = {
            'type': entry_type,
            'timestamp': timestamp,
            'raw': section
        }
        
        # Extract disk usage
        disk_match = re.search(r'Disk:\s+overlay\s+\d+G\s+(\d+)G\s+(\d+)G\s+(\d+)%', section)
        if disk_match:
            entry['disk_used'] = int(disk_match.group(1))
            entry['disk_avail'] = int(disk_match.group(2))
            entry['disk_percent'] = int(disk_match.group(3))
        
        # Extract load average
        load_match = re.search(r'load average:\s+([\d.]+),\s+([\d.]+),\s+([\d.]+)', section)
        if load_match:
            entry['load_1min'] = float(load_match.group(1))
            entry['load_5min'] = float(load_match.group(2))
            entry['load_15min'] = float(load_match.group(3))
        
        # Extract gateway status
        gateway_match = re.search(r'Gateway:\s*(\w+)', section)
        if gateway_match:
            entry['gateway_status'] = gateway_match.group(1)
        
        # Extract uptime
        uptime_match = re.search(r'up\s+(\d+)\s+days?', section)
        if uptime_match:
            entry['uptime_days'] = int(uptime_match.group(1))
        
        entries.append(entry)
    
    return entries

def analyze_disk_trends(entries: List[Dict]) -> Dict:
    """Analyze disk usage patterns"""
    disk_entries = [e for e in entries if 'disk_used' in e]
    
    if not disk_entries:
        return {"status": "No disk data found"}
    
    # Calculate stats
    used_values = [e['disk_used'] for e in disk_entries]
    percent_values = [e['disk_percent'] for e in disk_entries]
    
    trends = {
        "status": "✅ Stable",
        "entries_analyzed": len(disk_entries),
        "disk_used_gb": {
            "min": min(used_values),
            "max": max(used_values),
            "avg": sum(used_values) / len(used_values),
            "current": used_values[-1]
        },
        "disk_percent": {
            "min": min(percent_values),
            "max": max(percent_values),
            "avg": sum(percent_values) / len(percent_values),
            "current": percent_values[-1]
        },
        "trend": "flat",
        "change_gb": used_values[-1] - used_values[0] if len(used_values) > 1 else 0
    }
    
    # Determine trend
    if len(used_values) > 1:
        change = used_values[-1] - used_values[0]
        if change > 1:
            trends["trend"] = "⬆️ increasing"
            trends["status"] = "⚠️ Growing"
        elif change < -1:
            trends["trend"] = "⬇️ decreasing"
    
    return trends

def analyze_gateway_health(entries: List[Dict]) -> Dict:
    """Analyze gateway health patterns"""
    gateway_entries = [e for e in entries if 'gateway_status' in e]
    
    if not gateway_entries:
        return {"status": "No gateway data found"}
    
    status_counts = Counter(e['gateway_status'] for e in gateway_entries)
    
    health = {
        "total_checks": len(gateway_entries),
        "status_distribution": dict(status_counts),
        "unhealthy_rate": f"{(status_counts.get('unhealthy', 0) / len(gateway_entries) * 100):.1f}%",
        "current_status": gateway_entries[-1]['gateway_status'],
        "status": "⚠️ Issues detected" if 'unhealthy' in status_counts else "✅ Healthy"
    }
    
    return health

def analyze_load_patterns(entries: List[Dict]) -> Dict:
    """Analyze CPU load patterns"""
    load_entries = [e for e in entries if 'load_1min' in e]
    
    if not load_entries:
        return {"status": "No load data found"}
    
    load_1min = [e['load_1min'] for e in load_entries]
    load_5min = [e['load_5min'] for e in load_entries]
    load_15min = [e['load_15min'] for e in load_entries]
    
    # Detect spikes (> 1.0)
    spikes = [e for e in load_entries if e['load_1min'] > 1.0]
    
    patterns = {
        "entries_analyzed": len(load_entries),
        "load_1min": {
            "min": min(load_1min),
            "max": max(load_1min),
            "avg": sum(load_1min) / len(load_1min),
            "current": load_1min[-1]
        },
        "spikes_detected": len(spikes),
        "spike_times": [e['timestamp'].strftime('%Y-%m-%d %H:%M:%S') for e in spikes],
        "status": "⚠️ Spikes detected" if len(spikes) > 0 else "✅ Normal"
    }
    
    return patterns

def analyze_timing_patterns(entries: List[Dict]) -> Dict:
    """Analyze timing between heartbeats"""
    if len(entries) < 2:
        return {"status": "Insufficient data for timing analysis"}
    
    # Sort by timestamp
    sorted_entries = sorted(entries, key=lambda x: x['timestamp'])
    
    # Calculate gaps between entries
    gaps = []
    for i in range(1, len(sorted_entries)):
        gap = (sorted_entries[i]['timestamp'] - sorted_entries[i-1]['timestamp']).total_seconds() / 60
        gaps.append(gap)
    
    # Group by entry type
    type_gaps = defaultdict(list)
    for i in range(1, len(sorted_entries)):
        entry_type = sorted_entries[i]['type']
        gap = (sorted_entries[i]['timestamp'] - sorted_entries[i-1]['timestamp']).total_seconds() / 60
        type_gaps[entry_type].append(gap)
    
    timing = {
        "total_entries": len(entries),
        "time_span_hours": (sorted_entries[-1]['timestamp'] - sorted_entries[0]['timestamp']).total_seconds() / 3600,
        "avg_gap_minutes": sum(gaps) / len(gaps) if gaps else 0,
        "min_gap_minutes": min(gaps) if gaps else 0,
        "max_gap_minutes": max(gaps) if gaps else 0,
        "gaps_by_type": {
            t: {
                "count": len(g),
                "avg_gap_min": sum(g) / len(g) if g else 0
            } for t, g in type_gaps.items()
        },
        "first_entry": sorted_entries[0]['timestamp'].isoformat(),
        "last_entry": sorted_entries[-1]['timestamp'].isoformat()
    }
    
    return timing

def analyze_entry_types(entries: List[Dict]) -> Dict:
    """Analyze entry type distribution"""
    type_counts = Counter(e['type'] for e in entries)
    
    types = {
        "total_entries": len(entries),
        "type_distribution": dict(type_counts),
        "unique_types": len(type_counts),
        "most_common": type_counts.most_common(5)
    }
    
    return types

def analyze_recurring_events(entries: List[Dict]) -> Dict:
    """Detect recurring events and patterns"""
    # Look for repeated messages or themes
    messages = []
    for entry in entries:
        # Extract key themes from raw content
        raw = entry['raw'].lower()
        if 'permission denied' in raw:
            messages.append(('permission_denied', entry['timestamp']))
        if 'unhealthy' in raw:
            messages.append(('gateway_unhealthy', entry['timestamp']))
        if 'disk' in raw and '%' in raw:
            messages.append(('disk_check', entry['timestamp']))
    
    recurring = {
        "permission_denied_count": sum(1 for m, t in messages if m == 'permission_denied'),
        "gateway_unhealthy_count": sum(1 for m, t in messages if m == 'gateway_unhealthy'),
        "disk_check_count": sum(1 for m, t in messages if m == 'disk_check'),
        "patterns": []
    }
    
    # Identify patterns
    if recurring['permission_denied_count'] > 5:
        recurring['patterns'].append("🔴 Persistent permission issues with gateway")
    if recurring['gateway_unhealthy_count'] > 5:
        recurring['patterns'].append("🟠 Gateway consistently unhealthy")
    if recurring['disk_check_count'] > 10:
        recurring['patterns'].append("🟢 Regular disk monitoring active")
    
    return recurring

def generate_report(entries: List[Dict]) -> str:
    """Generate comprehensive pattern report"""
    
    # Run all analyses
    disk_analysis = analyze_disk_trends(entries)
    gateway_analysis = analyze_gateway_health(entries)
    load_analysis = analyze_load_patterns(entries)
    timing_analysis = analyze_timing_patterns(entries)
    type_analysis = analyze_entry_types(entries)
    recurring_analysis = analyze_recurring_events(entries)
    
    # Build report
    report = []
    report.append("# Nova Heartbeat Pattern Report")
    report.append(f"Generated: {datetime.now().isoformat()}")
    report.append("")
    
    # Executive Summary
    report.append("## Executive Summary")
    report.append(f"- Total entries analyzed: {type_analysis['total_entries']}")
    report.append(f"- Time span: {timing_analysis.get('time_span_hours', 0):.1f} hours")
    report.append(f"- Entry types: {type_analysis['unique_types']}")
    report.append("")
    
    # Disk Trends
    report.append("## 💾 Disk Usage Trends")
    report.append(f"Status: {disk_analysis.get('status', 'Unknown')}")
    if 'disk_used_gb' in disk_analysis:
        report.append(f"- Current usage: {disk_analysis['disk_used_gb']['current']}GB ({disk_analysis['disk_percent']['current']}%)")
        report.append(f"- Range: {disk_analysis['disk_used_gb']['min']}GB - {disk_analysis['disk_used_gb']['max']}GB")
        report.append(f"- Trend: {disk_analysis.get('trend', 'unknown')}")
        report.append(f"- Change: {disk_analysis.get('change_gb', 0)}GB over period")
    report.append("")
    
    # Gateway Health
    report.append("## 🌐 Gateway Health")
    report.append(f"Status: {gateway_analysis.get('status', 'Unknown')}")
    report.append(f"- Current status: {gateway_analysis.get('current_status', 'unknown')}")
    report.append(f"- Total checks: {gateway_analysis.get('total_checks', 0)}")
    report.append(f"- Unhealthy rate: {gateway_analysis.get('unhealthy_rate', 'N/A')}")
    if gateway_analysis.get('status_distribution'):
        report.append("- Distribution:")
        for status, count in gateway_analysis['status_distribution'].items():
            report.append(f"  - {status}: {count}")
    report.append("")
    
    # Load Patterns
    report.append("## ⚡ CPU Load Patterns")
    report.append(f"Status: {load_analysis.get('status', 'Unknown')}")
    if 'load_1min' in load_analysis:
        report.append(f"- Current load (1min): {load_analysis['load_1min']['current']:.2f}")
        report.append(f"- Average load: {load_analysis['load_1min']['avg']:.2f}")
        report.append(f"- Peak load: {load_analysis['load_1min']['max']:.2f}")
        report.append(f"- Spikes detected (>1.0): {load_analysis['spikes_detected']}")
        if load_analysis['spikes_detected'] > 0:
            report.append("- Spike times:")
            for spike in load_analysis['spike_times'][:5]:  # Show first 5
                report.append(f"  - {spike}")
    report.append("")
    
    # Timing Patterns
    report.append("## ⏱️ Timing Patterns")
    report.append(f"- Total entries: {timing_analysis.get('total_entries', 0)}")
    report.append(f"- Average gap between entries: {timing_analysis.get('avg_gap_minutes', 0):.1f} minutes")
    report.append(f"- Min gap: {timing_analysis.get('min_gap_minutes', 0):.1f} minutes")
    report.append(f"- Max gap: {timing_analysis.get('max_gap_minutes', 0):.1f} minutes")
    if timing_analysis.get('gaps_by_type'):
        report.append("- Gaps by entry type:")
        for entry_type, stats in timing_analysis['gaps_by_type'].items():
            report.append(f"  - [{entry_type}]: avg {stats['avg_gap_min']:.1f} min ({stats['count']} occurrences)")
    report.append("")
    
    # Entry Types
    report.append("## 📊 Entry Type Distribution")
    for entry_type, count in type_analysis.get('most_common', []):
        pct = (count / type_analysis['total_entries'] * 100)
        report.append(f"- [{entry_type}]: {count} ({pct:.1f}%)")
    report.append("")
    
    # Recurring Events
    report.append("## 🔁 Recurring Events & Patterns")
    if recurring_analysis.get('patterns'):
        for pattern in recurring_analysis['patterns']:
            report.append(f"- {pattern}")
    else:
        report.append("- No significant recurring patterns detected")
    report.append("")
    
    # Insights
    report.append("## 🔍 Key Insights")
    insights = []
    
    if gateway_analysis.get('unhealthy_rate', '0%').startswith('100'):
        insights.append("🔴 CRITICAL: Gateway is consistently unhealthy - all checks failed")
    
    if load_analysis.get('spikes_detected', 0) > 3:
        insights.append(f"🟠 WARNING: {load_analysis['spikes_detected']} load spikes detected - investigate cause")
    
    if recurring_analysis.get('permission_denied_count', 0) > 5:
        insights.append("🔴 SECURITY: Permission issues persist - gateway access needs attention")
    
    if disk_analysis.get('trend') == '⬆️ increasing':
        insights.append("🟡 MONITOR: Disk usage is growing - monitor for trends")
    
    if not insights:
        insights.append("✅ System operating normally with no critical issues")
    
    for insight in insights:
        report.append(f"- {insight}")
    
    report.append("")
    report.append("---")
    report.append("End of Report")
    
    return "\n".join(report)

def main():
    diary_path = "/home/node/.openclaw/workspace/diary.md"
    output_path = "/home/node/.openclaw/workspace/pattern-report.md"
    
    print("🔍 Analyzing heartbeat patterns...")
    
    # Parse diary
    entries = parse_diary(diary_path)
    print(f"   ✓ Parsed {len(entries)} entries")
    
    # Generate report
    report = generate_report(entries)
    print(f"   ✓ Generated analysis report")
    
    # Save report
    with open(output_path, 'w') as f:
        f.write(report)
    print(f"   ✓ Saved to {output_path}")
    
    print("\n✅ Pattern analysis complete!")

if __name__ == "__main__":
    main()
